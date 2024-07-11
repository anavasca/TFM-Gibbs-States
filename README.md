<h1 align="center">TFM-Gibbs-States</h1>

En este repositorio se encuentra parte del código desarrollado para llevar a cabo el trabajo presentado como Trabajo de Fin de Estudios (TFE). En el repositorio puede encontrarse los datos utilizados para la generación de las figuras presentadas dentro del documento. Concretamente, los datos están divididos en las siguientes carpetas:

🔵 **logger_data_qaoa_performance_gibbs_states_borders_hadamard_state**: se encuentran los datos necesarios para realizar una comparativa entre los estados de Gibbs y estados Hadamard.

🔵 **logger_data_qaoa_performance_gibbs_states_borders_one_state**: se encuentran los datos necesarios para realizar una comparativa entre los estados de Gibbs y estados producto de la base computacional.

🔵 **logger_data_qaoa_performance_gibbs_states_heat_map**: se encuentran los datos necesarios para componer la figura del mapa de calor, en el cual se muestra el rendimiento de los distintos estados del diagrama.

🔵 **logger_data_qaoa_performance_gibbs_states_border_pseudoGibbs_state**: se encuentran los datos necesarios para comparar los estados de Gibbs con estados de pseudoGibbs.

🔵 **logger_data_pretraining**: se encuentran los datos necesarios para representar el comportamiento de los dos tipos de protocolos de pre-optimización existentes.

Por otro lado, encontramos el jupyter **qaoa_gibbs_tests** en el cual se puede encontrar el código necesario para componer las imágenes presentadas en el documento relacionadas con el rendimiento de los estados de Gibbs a partir de los datos en bruto correspondientes. En el jupyter **qaoa_gibbs_pretraining** se encuentra el código necesario para componer las imágenes presentadas en el documento relacionadas con el protocolo de pre-optimización DMRG-VQE e ITEVO-QAOA. Por otro lado, los archivos denominados como **qaoa_max_cut_border_hadamard_state**, **qaoa_max_cut_border_one_state**, **qaoa_max_cut_heat_map** y **qaoa_max_cut_border_pseudoGibbs_state** son los utilizados para simular las comparativas entre los estados de Gibbs y cualquier otro tipo de estado. En el fichero **qaoa_utils** se encuentran las funciones auxiliares desarrolladas para poder llevar a cabo las simulaciones correspondientes.
