import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class GraphVisualization(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Búsqueda en Anchura y Profundidad")
        self.master.configure(bg="#FFEEEE")  # Cambiar el color de fondo de la ventana

        self.original_graph = nx.Graph()
        self.graph = nx.Graph()
        self.vertices = []
        self.edges = []
        self.canvas = None
        self.bfs_canvas = None
        self.dfs_canvas = None
        self.pos = None
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para entrada de vértices
        self.vertex_label = tk.Label(self.master, text="Entrada de Vértices:")
        self.vertex_label.grid(row=0, column=0, padx=5, pady=5)
        # Entrada de vértices
        self.vertex_entry = tk.Entry(self.master)
        self.vertex_entry.grid(row=1, column=0, padx=5, pady=5)
        # Etiqueta para entrada de aristas
        self.edge_label = tk.Label(self.master, text="Entrada de Aristas:")
        self.edge_label.grid(row=0, column=1, padx=5, pady=5)
        # Entrada de aristas
        self.edge_entry = tk.Entry(self.master)
        self.edge_entry.grid(row=1, column=1, padx=5, pady=5)
        # Botón para agregar aristas
        self.add_button = tk.Button(self.master, text="Agregar", command=self.add_graph)
        self.add_button.grid(row=1, column=2, padx=5, pady=5)
        # Tabla para mostrar vértices y aristas
        self.table_label = tk.Label(self.master, text="Vértices y Aristas:")
        self.table_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        self.treeview = ttk.Treeview(self.master, columns=("Vértices", "Aristas"), show="headings")
        self.treeview.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
        self.treeview.heading("Vértices", text="Vértices")
        self.treeview.heading("Aristas", text="Aristas")
        # Centrar la tabla en el eje x
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        
        # Título para el grafo original
        self.graph_label = tk.Label(self.master, text="Grafo Original")
        self.graph_label.grid(row=4, column=0, padx=5, pady=5)
        # Área para mostrar el grafo original
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().grid(row=5, column=0, padx=5, pady=5)

        # Título para el grafo de búsqueda en anchura
        self.bfs_label = tk.Label(self.master, text="Búsqueda en Anchura")
        self.bfs_label.grid(row=4, column=1, padx=5, pady=5)
        # Área para mostrar el grafo de búsqueda en anchura
        self.bfs_figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.bfs_canvas = FigureCanvasTkAgg(self.bfs_figure, master=self.master)
        self.bfs_canvas.get_tk_widget().grid(row=5, column=1, padx=5, pady=5)

        # Título para el grafo de búsqueda en profundidad
        self.dfs_label = tk.Label(self.master, text="Búsqueda en Profundidad")
        self.dfs_label.grid(row=4, column=2, padx=5, pady=5)
        # Área para mostrar el grafo de búsqueda en profundidad
        self.dfs_figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.dfs_canvas = FigureCanvasTkAgg(self.dfs_figure, master=self.master)
        self.dfs_canvas.get_tk_widget().grid(row=5, column=2, padx=5, pady=5)

    def add_graph(self):
        # Limpiar listas de vértices y aristas
        self.vertices.clear()
        self.edges.clear()
        # Limpiar el grafo original
        self.original_graph.clear()
        
        vertices = self.vertex_entry.get().split(",")
        edges = self.edge_entry.get().split(",")
        for edge in edges:
            v1, v2 = edge.split("--")
            self.original_graph.add_edge(v1.strip(), v2.strip())
            self.edges.append(edge.strip())
        for vertex in vertices:
            self.original_graph.add_node(vertex.strip())
            self.vertices.append(vertex.strip())
        self.pos = nx.spring_layout(self.original_graph)  # Calcular la disposición de los nodos una sola vez
        self.update_table()
        self.update_graph()
        self.update_bfs_graph()
        self.update_dfs_graph()

    def update_bfs_graph(self):
        self.bfs_figure.clear()
        ax = self.bfs_figure.add_subplot(111)
        nx.draw(self.original_graph, self.pos, with_labels=True, ax=ax, node_color='lightblue', edge_color='gray')
        bfs_edges = list(nx.bfs_edges(self.original_graph, source=self.vertices[0]))
        nx.draw_networkx_edges(self.original_graph, self.pos, edgelist=bfs_edges, ax=ax, edge_color='blue', width=2)
        self.bfs_canvas.draw()

    def update_dfs_graph(self):
        self.dfs_figure.clear()
        ax = self.dfs_figure.add_subplot(111)
        nx.draw(self.original_graph, self.pos, with_labels=True, ax=ax, node_color='lightblue', edge_color='gray')
        dfs_edges = list(nx.dfs_edges(self.original_graph, source=self.vertices[0]))
        nx.draw_networkx_edges(self.original_graph, self.pos, edgelist=dfs_edges, ax=ax, edge_color='red', width=2)
        self.dfs_canvas.draw()

    def update_graph(self):
        self.graph = self.original_graph.copy()
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        nx.draw(self.graph, self.pos, with_labels=True, ax=ax)
        self.canvas.draw()

    def update_table(self):
        # Limpiar tabla
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        # Insertar vértices y aristas en la tabla
        for vertex in self.vertices:
            self.treeview.insert("", "end", values=(vertex, ""))
        for edge in self.edges:
            self.treeview.insert("", "end", values=("", edge))


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphVisualization(master=root)
    app.mainloop()