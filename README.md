GraphVisualization - Visualización de Grafos con Búsqueda en Anchura y Profundidad
Descripción
Este programa es una interfaz gráfica desarrollada en Python utilizando Tkinter que permite visualizar un grafo, así como realizar y mostrar las búsquedas en anchura (BFS) y en profundidad (DFS) en dicho grafo. Los usuarios pueden ingresar los vértices y aristas del grafo mediante campos de texto y luego visualizar el grafo junto con sus representaciones BFS y DFS.

Requisitos del Sistema
Dependencias
El programa utiliza varias bibliotecas de Python para la interfaz gráfica y la manipulación de grafos. Asegúrate de tener las siguientes bibliotecas instaladas:

Tkinter: Biblioteca estándar de Python para la creación de interfaces gráficas.
Matplotlib: Biblioteca para la creación de gráficos en Python.
NetworkX: Biblioteca para la creación, manipulación y estudio de la estructura, dinámica y funciones de redes complejas.
Puedes instalar las bibliotecas necesarias usando pip:

bash
Copiar código
pip install matplotlib networkx
Software Requerido
Python 3.x: El programa está escrito en Python 3.x, por lo que necesitas tener instalada esta versión de Python.
Tkinter: Viene preinstalado con Python en la mayoría de las distribuciones, pero si no lo tienes instalado, sigue las instrucciones según tu sistema operativo.
Librerías Importadas
tkinter: Biblioteca estándar para crear interfaces gráficas en Python.
tkinter.ttk: Parte de Tkinter, proporciona estilos y widgets adicionales.
networkx: Biblioteca para la creación y manipulación de grafos.
matplotlib.pyplot: Biblioteca utilizada para generar gráficos y visualizaciones.
matplotlib.backends.backend_tkagg: Módulo que permite incrustar gráficos de Matplotlib en una interfaz de Tkinter.
Funcionalidades
Entrada de Vértices y Aristas: El usuario puede ingresar los vértices y aristas del grafo.
Visualización del Grafo: El grafo original, el grafo resultante de la búsqueda en anchura (BFS) y el grafo resultante de la búsqueda en profundidad (DFS) se muestran en la interfaz.
Tabla de Vértices y Aristas: Los vértices y aristas se muestran en una tabla interactiva en la interfaz gráfica.
Instrucciones de Uso
Ejecutar el Programa: Para ejecutar el programa, simplemente corre el archivo Python.

bash
Copiar código
python nombre_del_archivo.py
Entrada de Datos:

Entrada de Vértices: Ingresa los vértices separados por comas en el campo de texto "Entrada de Vértices".
Entrada de Aristas: Ingresa las aristas en formato vértice1--vértice2, separadas por comas, en el campo de texto "Entrada de Aristas".
Agregar Grafo: Haz clic en el botón "Agregar" para generar el grafo basado en los vértices y aristas ingresados.

Visualización:

Grafo Original: Se muestra el grafo con las aristas y vértices tal como se ingresaron.
Búsqueda en Anchura (BFS): Se realiza y visualiza la búsqueda en anchura a partir del primer vértice.
Búsqueda en Profundidad (DFS): Se realiza y visualiza la búsqueda en profundidad a partir del primer vértice.
Tabla: Los vértices y aristas se visualizan en la tabla situada debajo de las áreas gráficas.

Estructura del Código
GraphVisualization (Clase Principal): Hereda de tk.Frame y maneja la creación de la interfaz, la captura de los datos de vértices y aristas, y la actualización de las visualizaciones.

Métodos Principales:
__init__: Inicializa la ventana y los elementos de la interfaz gráfica.
create_widgets: Crea y organiza los widgets de la interfaz (entradas de texto, tabla, botones, etc.).
add_graph: Recoge los vértices y aristas ingresados, actualiza el grafo y las visualizaciones.
update_bfs_graph: Actualiza y visualiza el grafo generado mediante la búsqueda en anchura (BFS).
update_dfs_graph: Actualiza y visualiza el grafo generado mediante la búsqueda en profundidad (DFS).
update_graph: Actualiza y visualiza el grafo original.
update_table: Actualiza la tabla de vértices y aristas con los datos ingresados.
Ejemplo de Entrada
Vértices: A,B,C,D
Aristas: A--B,B--C,C--D,A--D
Después de agregar el grafo, se generarán tres visualizaciones:

Grafo Original: Mostrará los vértices conectados según las aristas proporcionadas.
Búsqueda en Anchura (BFS): Mostrará el recorrido en anchura comenzando desde el primer vértice (en este caso, A).
Búsqueda en Profundidad (DFS): Mostrará el recorrido en profundidad comenzando desde el primer vértice.
