import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GrafoVisualizador(tk.Frame):
    def __init__(self, ventana=None):
        super().__init__(ventana)
        self.ventana = ventana
        self.ventana.title("GRAFO - LARGO Y ANCHO")
        self.ventana.configure(bg="#F5F5DC")  # Cambiar el color de fondo a beige
        self.grid(sticky="nsew")

        self.grafo_base = nx.Graph()
        self.grafo_copia = nx.Graph()
        self.vertices_lista = []
        self.aristas_lista = []
        self.canvas_base = None
        self.canvas_bfs = None
        self.canvas_dfs = None
        self.posicion_nodos = None
        self.crear_componentes()

        # Centrar la ventana en la pantalla
        self.ventana.update_idletasks()  # Asegurarse de que la ventana esté completamente inicializada
        self.centrar_ventana()

    def centrar_ventana(self):
        # Obtener el tamaño de la ventana
        ancho_ventana = self.ventana.winfo_width()
        alto_ventana = self.ventana.winfo_height()

        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        # Establecer la geometría de la ventana
        self.ventana.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')

    def crear_componentes(self):
        # Etiqueta para entrada de vértices
        self.etiqueta_vertices = tk.Label(self.ventana, text="Vértices:", bg="#F5F5DC")
        self.etiqueta_vertices.grid(row=0, column=0, padx=8, pady=4, sticky="nsew")
        # Entrada de vértices
        self.entrada_vertices = tk.Entry(self.ventana)
        self.entrada_vertices.grid(row=0, column=1, padx=8, pady=4, sticky="nsew")
        
        # Etiqueta para entrada de aristas
        self.etiqueta_aristas = tk.Label(self.ventana, text="Aristas:", bg="#F5F5DC")
        self.etiqueta_aristas.grid(row=1, column=0, padx=8, pady=4, sticky="nsew")
        # Entrada de aristas
        self.entrada_aristas = tk.Entry(self.ventana)
        self.entrada_aristas.grid(row=1, column=1, padx=8, pady=4, sticky="nsew")
        
        # Botón para agregar aristas
        self.boton_agregar = tk.Button(self.ventana, text="Agregar Grafo", command=self.agregar_grafo)
        self.boton_agregar.grid(row=2, column=0, columnspan=2, padx=8, pady=8, sticky="nsew")
        
        # Tabla para mostrar vértices y aristas
        self.etiqueta_tabla = tk.Label(self.ventana, text="Vértices y Aristas:", bg="#F5F5DC")
        self.etiqueta_tabla.grid(row=3, column=0, columnspan=2, padx=8, pady=4, sticky="nsew")
        self.tabla = ttk.Treeview(self.ventana, columns=("Vértices", "Aristas"), show="headings")
        self.tabla.grid(row=4, column=0, columnspan=2, padx=8, pady=4, sticky="nsew")
        self.tabla.heading("Vértices", text="Vértices")
        self.tabla.heading("Aristas", text="Aristas")
        
        # Área para mostrar el grafo original
        self.etiqueta_grafo = tk.Label(self.ventana, text="Grafo Original", bg="#F5F5DC")
        self.etiqueta_grafo.grid(row=0, column=2, padx=8, pady=4, sticky="nsew")
        self.figura_grafo = plt.Figure(figsize=(4, 3.2), dpi=100)
        self.canvas_base = FigureCanvasTkAgg(self.figura_grafo, master=self.ventana)
        self.canvas_base.get_tk_widget().grid(row=1, column=2, rowspan=4, padx=8, pady=4, sticky="nsew")
        
        # Área para mostrar el grafo de búsqueda en anchura (BFS)
        self.etiqueta_bfs = tk.Label(self.ventana, text="Búsqueda a lo ancho", bg="#F5F5DC")
        self.etiqueta_bfs.grid(row=5, column=0, columnspan=2, padx=8, pady=4, sticky="nsew")
        self.figura_bfs = plt.Figure(figsize=(4, 3.2), dpi=100)
        self.canvas_bfs = FigureCanvasTkAgg(self.figura_bfs, master=self.ventana)
        self.canvas_bfs.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=8, pady=4, sticky="nsew")
        
        # Área para mostrar el grafo de búsqueda en profundidad (DFS)
        self.etiqueta_dfs = tk.Label(self.ventana, text="Búsqueda a lo largo", bg="#F5F5DC")
        self.etiqueta_dfs.grid(row=5, column=2, padx=8, pady=4, sticky="nsew")
        self.figura_dfs = plt.Figure(figsize=(4, 3.2), dpi=100)
        self.canvas_dfs = FigureCanvasTkAgg(self.figura_dfs, master=self.ventana)
        self.canvas_dfs.get_tk_widget().grid(row=6, column=2, padx=8, pady=4, sticky="nsew")

    def agregar_grafo(self):
        # Limpiar listas de vértices y aristas
        self.vertices_lista.clear()
        self.aristas_lista.clear()
        # Limpiar el grafo original
        self.grafo_base.clear()
        
        # Ordenar los vértices antes de agregarlos
        vertices = sorted(self.entrada_vertices.get().split(","))
        aristas = sorted(self.entrada_aristas.get().split(","))
        for arista in aristas:
            v1, v2 = arista.split("--")
            self.grafo_base.add_edge(v1.strip(), v2.strip())
            self.aristas_lista.append(arista.strip())
        for vertice in vertices:
            self.grafo_base.add_node(vertice.strip())
            self.vertices_lista.append(vertice.strip())
        self.posicion_nodos = nx.spring_layout(self.grafo_base)  # Calcular la disposición de los nodos una sola vez
        self.actualizar_tabla()
        self.actualizar_grafo()
        self.actualizar_grafo_bfs()
        self.actualizar_grafo_dfs()

    def actualizar_grafo_bfs(self):
        self.figura_bfs.clear()
        ax = self.figura_bfs.add_subplot(111)
        nx.draw(self.grafo_base, self.posicion_nodos, with_labels=True, ax=ax, node_color='lightblue', edge_color='gray')
        bfs_aristas = list(nx.bfs_edges(self.grafo_base, source=self.vertices_lista[0]))
        nx.draw_networkx_edges(self.grafo_base, self.posicion_nodos, edgelist=bfs_aristas, ax=ax, edge_color='blue', width=2)
        self.canvas_bfs.draw()

    def actualizar_grafo_dfs(self):
        self.figura_dfs.clear()
        ax = self.figura_dfs.add_subplot(111)
        nx.draw(self.grafo_base, self.posicion_nodos, with_labels=True, ax=ax, node_color='lightblue', edge_color='gray')
        dfs_aristas = list(nx.dfs_edges(self.grafo_base, source=self.vertices_lista[0]))
        nx.draw_networkx_edges(self.grafo_base, self.posicion_nodos, edgelist=dfs_aristas, ax=ax, edge_color='red', width=2)
        self.canvas_dfs.draw()

    def actualizar_grafo(self):
        self.grafo_copia = self.grafo_base.copy()
        self.figura_grafo.clear()
        ax = self.figura_grafo.add_subplot(111)
        nx.draw(self.grafo_copia, self.posicion_nodos, with_labels=True, ax=ax)
        self.canvas_base.draw()

    def actualizar_tabla(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        # Insertar vértices y aristas en la tabla
        for vertice in self.vertices_lista:
            self.tabla.insert("", "end", values=(vertice, ""))
        for arista in self.aristas_lista:
            self.tabla.insert("", "end", values=("", arista))


if __name__ == "__main__":
    raiz = tk.Tk()
    app = GrafoVisualizador(ventana=raiz)
    app.mainloop()