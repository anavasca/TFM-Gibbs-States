import numpy as np
import networkx as nx
import json

from pflacco.classical_ela_features import calculate_information_content

from qibo import models
from qaoa_utils import (exprectum_hamiltonian, 
                        create_gibbs_state, 
                        create_gausgibbs_state, 
                        expected_value, 
                        sample_state, 
                        build_maxcut_hamiltonian, 
                        build_mixer_hamiltonian, 
                        max_cut_brute_force)

n = 8
pb = 0.5
t = 4
test = 1
test_iter = 4
tol = 0.4

for p in range(4, 5):
    
    print('case:', p)
    
    delta = 0.1
    iterations = 0
    expected_value_psgibbs_state = 0
    expected_value_gibbs_state = 0

    G = nx.erdos_renyi_graph(n, pb)

    dict_values = exprectum_hamiltonian(G)
    
    
    while (
        abs(expected_value_psgibbs_state - expected_value_gibbs_state) < tol
        and iterations < test_iter
    ):
        
        
        gibbs_state = create_gibbs_state(dict_values, t = t)
        expected_value_gibbs_state = expected_value(state = gibbs_state, 
                                                dict_values = dict_values)

        dict_pb_gibbs = sample_state(gibbs_state)

        pb_gibbs = list(dict_pb_gibbs.values())

        entropy_gibbs = -sum(
        pb_gibbs[i] * np.log(pb_gibbs[i])
        for i in range(len(pb_gibbs))
        if pb_gibbs[i] != 0 )

        pseudo_gibbs_state = create_gausgibbs_state(solutions_dict = dict_values, 
                                                    delta_energy = delta, 
                                                    mu_energy = expected_value_gibbs_state)
        
        expected_value_psgibbs_state = expected_value(
            state=pseudo_gibbs_state, dict_values=dict_values)

        
        dict_pb_psgibbs = sample_state(pseudo_gibbs_state)

        pb_psgibbs = list(dict_pb_psgibbs.values())

        entropy_psgibbs = -sum(
            pb_psgibbs[i] * np.log(pb_psgibbs[i])
            for i in range(len(pb_psgibbs))
            if pb_psgibbs[i] != 0
        )

        hamiltonian = build_maxcut_hamiltonian(graph = G)
        mixer_hamiltonian = build_mixer_hamiltonian(graph = G)

        a = np.linspace(0, 2 * np.pi, 50)
        b = np.linspace(0, 2 * np.pi, 50)

        list_gibbs_params = []
        list_gibbs_value = []
        
        list_psgibbs_params = []
        list_psgibbs_value = []

        for i in a:
            for j in b:

                        list_gibbs_params.append([i, j])
                        
                        final_parameters = np.array([i, j])
                        
                        qaoa = models.QAOA(hamiltonian=hamiltonian, mixer=mixer_hamiltonian)
                        
                        qaoa.set_parameters(final_parameters)
                        
                        quantum_state = qaoa.execute(initial_state = gibbs_state)
                        
                        value = expected_value(state = quantum_state, dict_values = dict_values)
                        
                        list_gibbs_value.append(value)
                        
        for i in a:
            for j in b:

                        list_psgibbs_params.append([i, j])
                        
                        final_parameters = np.array([i, j])
                        
                        qaoa = models.QAOA(hamiltonian=hamiltonian, mixer=mixer_hamiltonian)
                        
                        qaoa.set_parameters(final_parameters)
                        
                        quantum_state = qaoa.execute(initial_state = pseudo_gibbs_state)
                        
                        value = expected_value(state = quantum_state, dict_values = dict_values)
                        
                        list_psgibbs_value.append(value)
                        
        gibbs_information_content = calculate_information_content(list_gibbs_params, list_gibbs_value)
        psgibbs_information_content = calculate_information_content(list_psgibbs_params, list_psgibbs_value)
        
        
        path_data = (
            f"logger_data/logger_data_qaoa_landscape_gibbs_states/logger_data_max_cut_qaoa_common_instances_n_{n}/"
            f"cmaes_qaoa_max_cut_n_{n}_case_{p}_t_{t}_"
            f"layers_{1}_delta_gauss_{round(delta, 3)}.json"
        )
        
        data_test = {
                "gibbs_entropy": entropy_gibbs,
                "gibbs_m0_information": gibbs_information_content['ic.m0'],
                "gibbs_e0_information": gibbs_information_content['ic.eps_ratio'],
                "gibbs_hmax_information": gibbs_information_content['ic.h_max'],
                "psgibbs_entropy": entropy_psgibbs,
                "psgibbs_m0_information": psgibbs_information_content['ic.m0'],
                "psgibbs_e0_information": psgibbs_information_content['ic.eps_ratio'],
                "psgibbs_hmax_information": psgibbs_information_content['ic.h_max'],

            }


        json_datos = json.dumps(data_test, indent=2)

        with open(path_data, 'w') as archivo:
            archivo.write(json_datos)
            
        delta += 0.2
        iterations += 1