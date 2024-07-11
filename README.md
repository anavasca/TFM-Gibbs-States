\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{xcolor}
\usepackage{graphicx}

\title{\textbf{TFM-Gibbs-States}}
\date{}

\begin{document}

\maketitle
\begin{center}
    \large
    \textbf{TFM-Gibbs-States}
\end{center}

En este repositorio se encuentra parte del código desarrollado para llevar a cabo el trabajo presentado como Trabajo de Fin de Estudios (TFE). En el repositorio puede encontrarse los datos utilizados para la generación de las figuras presentadas dentro del documento. Concretamente, los datos están divididos en las siguientes carpetas:

\begin{itemize}
    \item \textcolor{blue}{\textbf{logger_data_qaoa_performance_gibbs_states_borders_hadamard_state}}: se encuentran los datos necesarios para realizar una comparativa entre los estados de Gibbs y estados Hadamard.

    \item \textcolor{blue}{\textbf{logger_data_qaoa_performance_gibbs_states_borders_one_state}}: se encuentran los datos necesarios para realizar una comparativa entre los estados de Gibbs y estados producto de la base computacional.

    \item \textcolor{blue}{\textbf{logger_data_qaoa_performance_gibbs_states_heat_map}}: se encuentran los datos necesarios para componer la figura del mapa de calor, en el cual se muestra el rendimiento de los distintos estados del diagrama.

    \item \textcolor{blue}{\textbf{logger_data_qaoa_performance_gibbs_states_temperature}}: se encuentran los datos necesarios para comparar los estados de Gibbs con estados de pseudoGibbs.

    \item \textcolor{blue}{\textbf{logger_data_pretraining}}: se encuentran los datos necesarios para representar el comportamiento de los dos tipos de protocolos de pre-optimización existentes.
\end{itemize}

Por otro lado, encontramos el jupyter \textbf{qaoa_gibbs_tests} en el cual se puede encontrar el código necesario para componer las imágenes presentadas en el documento relacionadas con el rendimiento de los estados de Gibbs a partir de los datos en bruto correspondientes. Por otro lado, los archivos denominados como \textbf{qaoa_max_cut_border_hadamard_state}, \textbf{qaoa_max_cut_border_one_state}, \textbf{qaoa_max_cut_heat_map} y \textbf{qaoa_max_cut_temperature} son los utilizados para simular las comparativas entre los estados de Gibbs y cualquier otro tipo de estado. En el fichero \textbf{qaoa_utils} se encuentran las funciones auxiliares desarrolladas para poder llevar a cabo las simulaciones correspondientes.

\end{document}
