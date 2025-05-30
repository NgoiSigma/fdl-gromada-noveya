# 🕸️ FDL Graph Engine
# Visualizes semantic structure of FDL logic blocks

import networkx as nx
import matplotlib.pyplot as plt
from fdl_compiler import FDLCompiler

class FDLGraphEngine:
    def __init__(self):
        self.G = nx.DiGraph()

    def build_graph(self, fdl_ast):
        for block in fdl_ast:
            block_name = block['name']
            self.G.add_node(block_name, type='block')
            for phase, entries in block['phases'].items():
                phase_node = f"{block_name}::{phase}"
                self.G.add_node(phase_node, type='phase')
                self.G.add_edge(block_name, phase_node)
                for line in entries:
                    content_node = f"{phase_node}::{line}"
                    self.G.add_node(content_node, type='content')
                    self.G.add_edge(phase_node, content_node)

    def visualize(self):
        plt.figure(figsize=(14, 8))
        pos = nx.spring_layout(self.G, seed=42)
        node_colors = ["skyblue" if d["type"] == "block" else "lightgreen" if d["type"] == "phase" else "lightgrey" for n, d in self.G.nodes(data=True)]
        nx.draw(self.G, pos, with_labels=True, node_color=node_colors, font_size=8, node_size=2000, edge_color="gray")
        plt.title("FDL Semantic Structure")
        plt.show()

# Example usage
if __name__ == "__main__":
    source_code = """
    @block "VisualExample::Demo"
    init:
      intent: "demo graph"
    expand:
      variable: x = 10
    synthesize:
      output: x
    """
    compiler = FDLCompiler()
    result = compiler.compile(source_code)
    if result['status'] == 'success':
        engine = FDLGraphEngine()
        engine.build_graph([result['ast']])
        engine.visualize()
