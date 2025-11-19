"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Create a Python script to model "Resonance" in societal systems, inspired by the discussions on ScienceArtThinking.de. Use network analysis libraries to simulate interconnectedness.
Generated: DETERMINISTIC_ec6e34d6dc572903
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import Dict, List, Tuple, Optional
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ResonanceModel:
    """
    A model to simulate resonance effects in societal systems using network analysis.
    """
    
    def __init__(self, num_nodes: int = 50, initial_connection_prob: float = 0.1):
        """
        Initialize the resonance model with a random network.
        
        Args:
            num_nodes: Number of nodes in the network
            initial_connection_prob: Probability of initial connections between nodes
        """
        self.graph = nx.erdos_renyi_graph(num_nodes, initial_connection_prob)
        self.num_nodes = num_nodes
        self.initialize_node_attributes()
        
    def initialize_node_attributes(self) -> None:
        """
        Initialize node attributes with random values for:
        - Influence (how much a node affects others)
        - Susceptibility (how much a node is affected by others)
        - State (current resonance state)
        """
        for node in self.graph.nodes():
            self.graph.nodes[node]['influence'] = random.uniform(0.1, 1.0)
            self.graph.nodes[node]['susceptibility'] = random.uniform(0.1, 1.0)
            self.graph.nodes[node]['state'] = random.uniform(-1.0, 1.0)
            self.graph.nodes[node]['color'] = self._state_to_color(self.graph.nodes[node]['state'])
    
    def _state_to_color(self, state: float) -> Tuple[float, float, float]:
        """
        Convert node state to RGB color for visualization.
        
        Args:
            state: Node state value between -1 and 1
            
        Returns:
            RGB tuple representing the state
        """
        if state < 0:
            return (0.5 + state/2, 0.5 + state/2, 0.5 - state/2)  # Blueish for negative
        else:
            return (0.5 + state/2, 0.5 - state/2, 0.5 - state/2)  # Reddish for positive
    
    def update_resonance(self, damping_factor: float = 0.1) -> None:
        """
        Update node states based on resonance effects with neighbors.
        
        Args:
            damping_factor: Controls how quickly resonance effects decay
        """
        new_states = {}
        
        for node in self.graph.nodes():
            total_influence = 0.0
            weighted_sum = 0.0
            
            for neighbor in self.graph.neighbors(node):
                # Calculate resonance effect from neighbor
                edge_weight = self.graph[node][neighbor].get('weight', 1.0)
                neighbor_influence = self.graph.nodes[neighbor]['influence']
                neighbor_state = self.graph.nodes[neighbor]['state']
                
                weighted_sum += neighbor_state * neighbor_influence * edge_weight
                total_influence += neighbor_influence * edge_weight
            
            if total_influence > 0:
                # Update state based on neighbors' influence
                susceptibility = self.graph.nodes[node]['susceptibility']
                current_state = self.graph.nodes[node]['state']
                new_state = current_state * (1 - damping_factor) + (weighted_sum / total_influence) * susceptibility * damping_factor
                new_states[node] = np.clip(new_state, -1.0, 1.0)
            else:
                new_states[node] = self.graph.nodes[node]['state']
        
        # Apply the new states and update colors
        for node, state in new_states.items():
            self.graph.nodes[node]['state'] = state
            self.graph.nodes[node]['color'] = self._state_to_color(state)
    
    def add_external_influence(self, node: int, influence: float) -> None:
        """
        Apply external influence to a specific node.
        
        Args:
            node: Node ID to influence
            influence: Amount of influence to apply (-1 to 1)
        """
        if node not in self.graph.nodes():
            logger.warning(f"Node {node} not found in graph")
            return
            
        current_state = self.graph.nodes[node]['state']
        new_state = np.clip(current_state + influence, -1.0, 1.0)
        self.graph.nodes[node]['state'] = new_state
        self.graph.nodes[node]['color'] = self._state_to_color(new_state)
    
    def visualize(self, title: str = "Resonance in Societal Systems") -> None:
        """
        Visualize the current state of the network.
        
        Args:
            title: Title for the visualization
        """
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(self.graph, seed=42)
        
        colors = [self.graph.nodes[node]['color'] for node in self.graph.nodes()]
        sizes = [300 * self.graph.nodes[node]['influence'] for node in self.graph.nodes()]
        
        nx.draw(
            self.graph,
            pos,
            node_color=colors,
            node_size=sizes,
            edge_color='gray',
            width=0.5,
            with_labels=False,
            alpha=0.8
        )
        
        plt.title(title)
        plt.show()
    
    def animate_evolution(self, frames: int = 50, interval: int = 200) -> FuncAnimation:
        """
        Create an animation of the resonance evolution.
        
        Args:
            frames: Number of animation frames
            interval: Time between frames in milliseconds
            
        Returns:
            matplotlib.animation.FuncAnimation object
        """
        fig, ax = plt.subplots(figsize=(10, 8))
        pos = nx.spring_layout(self.graph, seed=42)
        
        def update(frame):
            ax.clear()
            self.update_resonance()
            
            colors = [self.graph.nodes[node]['color'] for node in self.graph.nodes()]
            sizes = [300 * self.graph.nodes[node]['influence'] for node in self.graph.nodes()]
            
            nx.draw(
                self.graph,
                pos,
                node_color=colors,
                node_size=sizes,
                edge_color='gray',
                width=0.5,
                with_labels=False,
                alpha=0.8,
                ax=ax
            )
            
            ax.set_title(f"Resonance Evolution - Frame {frame + 1}/{frames}")
        
        return FuncAnimation(fig, update, frames=frames, interval=interval, repeat=False)

def main():
    """Main function to demonstrate the ResonanceModel."""
    try:
        # Initialize model
        model = ResonanceModel(num_nodes=30, initial_connection_prob=0.15)
        
        # Add some initial influences
        for _ in range(5):
            node = random.choice(list(model.graph.nodes()))
            model.add_external_influence(node, random.uniform(-0.5, 0.5))
        
        # Visualize initial state
        model.visualize("Initial State of Societal Resonance")
        
        # Create and show animation
        logger.info("Creating resonance evolution animation...")
        animation = model.animate_evolution(frames=30)
        plt.show()
        
        # Visualize final state
        model.visualize("Final State After Resonance Effects")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    main()
```
