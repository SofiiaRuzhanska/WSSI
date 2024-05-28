import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class Neuron:  
    def __init__(self, n_inputs, bias=0., weights=None):  
        self.b = bias
        if weights: 
            self.ws = np.array(weights)
        else: 
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):  # activation function (here: leaky_relu)
        return max(x * 0.1, x)   

    def __call__(self, xs):  # calculate the neuron's output
             return self._f(xs @ self.ws + self.b) 

class NeuralNetwork:
    def __init__(self, input_size, hidden_layers, output_size):
        self.input_size = input_size
        self.hidden_layers = hidden_layers
        self.output_size = output_size
        self.layers = self.build_network()

    def build_network(self):
        layers = []
        # Input layer
        layers.append([Neuron(n_inputs=1) for _ in range(self.input_size)])
        # Hidden layers
        prev_layer_size = self.input_size
        for layer_size in self.hidden_layers:
            layers.append([Neuron(n_inputs=prev_layer_size) for _ in range(layer_size)])
            prev_layer_size = layer_size
        # Output layer
        layers.append([Neuron(n_inputs=prev_layer_size) for _ in range(self.output_size)])
        return layers

    def visualize(self):
        G = nx.DiGraph()

    
        layer_idx = 0
        for layer in self.layers:
            for neuron_idx in range(len(layer)):
                node_color = "red" if layer_idx == 0 else ("skyblue" if layer_idx < len(self.layers) - 1 else "green")
                G.add_node(f"L{layer_idx}N{neuron_idx}", layer=layer_idx, color=node_color)
            layer_idx += 1

       
        for layer_idx in range(len(self.layers) - 1):
            for src_idx in range(len(self.layers[layer_idx])):
                for dst_idx in range(len(self.layers[layer_idx + 1])):
                    G.add_edge(f"L{layer_idx}N{src_idx}", f"L{layer_idx + 1}N{dst_idx}")

        pos = nx.multipartite_layout(G, subset_key="layer")
        nx.draw(G, pos, with_labels=True, node_size=3000, font_size=10, font_weight="bold", arrowsize=20,
                node_color=[node[1]["color"] for node in G.nodes(data=True)])
        plt.show()


nn = NeuralNetwork(input_size=3, hidden_layers=[4, 4], output_size=1)
nn.visualize()
