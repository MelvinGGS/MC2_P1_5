# Buscar grafo a lo ancho y largo
## Descripción General
Este programa es una aplicación gráfica que permite visualizar un grafo y realizar búsquedas a lo ancho y a lo largo utilizando la librería networkx. Los usuarios pueden ingresar vértices y aristas para construir un grafo, y la interfaz gráfica mostrará el grafo original junto con el resultado del mismo grafo destacando la busqueda a lo largo y a lo ancho.
### Esta es la interfaz para el usuario
![vista general](https://github.com/user-attachments/assets/0359e0a4-adfa-4296-8a94-e590af1d4eb5)

## Uso del Programa:
- Verificar que las librerias necesarias esten instaladas, si no, ejecutar el siguiente comando desde la consola:
```bash
pip install networkx matplotlib
```
- Ingrese los vértices separados por comas (ejemplo: "A,B,C,D")
- Ingrese las aristas con formato v1--v2 (ejemplo: "A--B, B--C, C--D") como el formato que se muestra en la imagen:
  ![verticesAristas](https://github.com/user-attachments/assets/2e0a1b7c-3e44-4295-aab2-beda2b8c3574)
- Presione "Agregar Grafo" para  para generar y visualizar el grafo en la ventana. Los vértices y aristas ingresados también aparecerán en la tabla bajo el título "Vértices y Aristas".
- Los tres grafos se actualizarán mostrando:
    - Grafo original
    - Recorrido a lo ancho
    - Recorrido a lo largo
   
El resultado será como el que se muestra en la imagen:
  ![VistaConGrafos](https://github.com/user-attachments/assets/e07cd093-1627-4d4d-a8b1-0b51441e5fe5)

## Requisitos del Sistema
### Librerías necesarias:
Este programa utiliza las siguientes librerías que deben estar instaladas:

- Tkinter: Librería estándar de Python para construir interfaces gráficas.
- networkx: Librería para la creación, manipulación y estudio de grafos y redes complejas.
- matplotlib: Utilizada para generar gráficos y visualizaciones de los grafos.
- matplotlib.backends.backend_tkagg: Se utiliza para incrustar gráficos de matplotlib en una ventana de Tkinter.

## Estructura del Programa
### Atributos principales:
- original_graph: Almacena el grafo principal
- vertices: Lista de vértices ingresados
- edges: Lista de aristas ingresadas
- pos: Posiciones de los nodos para visualización

### Componentes de la Interfaz:

#### Panel de Entrada:
- Campo para ingresar vértices separados por comas
- Campo para ingresar aristas en formato v1--v2
- Botón "Agregar" para actualizar el grafo

#### Métodos Principales:
- add_graph(): Procesa los vértices y aristas ingresados
- update_bfs_graph(): Visualiza la búsqueda en anchura
- update_dfs_graph(): Visualiza la búsqueda en profundidad
- update_graph(): Actualiza la visualización del grafo principal
- update_table(): Actualiza la tabla de vértices y aristas

#### Visualización:
- Grafo Original: Muestra todos los vértices y aristas
- Ancho: Resalta en azul el recorrido a lo ancho
- Largo: Resalta en rojo el recorrido a lo largo
