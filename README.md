<h1 align="center">TFM-Gibbs-States</h1>

In this repository you can find part of the code developed to carry out the work presented as Final Project (TFE). In the repository you can find the data used for the generation of the figures presented in the document. Specifically, the data are divided into the following folders:

🔵 **logger_data_qaoa_performance_gibbs_states_borders_hadamard_state**: The data necessary to make a comparison between the Gibbs and Hadamard states are available.

🔵 **logger_data_qaoa_performance_gibbs_states_borders_one_state**: data necessary to make a comparison between Gibbs states and states resulting from the computational basis are found.

🔵 **logger_data_qaoa_performance_gibbs_states_heat_map**: data necessary to compose the figure of the heat map, which shows the performance of the different states of the diagram, can be found.

🔵 **logger_data_qaoa_performance_gibbs_states_border_pseudoGibbs_state**: data necessary to compare Gibbs states with pseudoGibbs states are found.

🔵 **logger_data_pretraining**: data necessary to represent the behavior of the two types of existing pre-optimization protocols are found.

On the other hand, we find the jupyter **qaoa_gibbs_tests** in which the code necessary to compose the images presented in the paper related to the performance of Gibbs states from the corresponding raw data can be found. In the jupyter **qaoa_gibbs_pretraining** can be found the code necessary to compose the images presented in the paper related to the DMRG-VQE and ITEVO-QAOA pre-optimization protocol. On the other hand, the files named as **qaoa_max_cut_border_hadamard_state**, **qaoa_max_cut_border_one_state**, **qaoaoa_max_cut_heat_map** and **qaoa_max_cut_border_pseudoGibbs_state** are the ones used to simulate the comparisons between Gibbs states and any other type of state. In the **qaoa_utils** file you can find the auxiliary functions developed to carry out the corresponding simulations.
