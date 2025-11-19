"""
Generated Code Metadata:
========================
Original URL: https://doctoresjane.com
Prompt: Create a visualization tool using Python to map the relationship between oral health, brain health, and gut health, inspired by the philosophy of Jané Clinic.
Generated: DETERMINISTIC_cb03015db96a31a3
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go
import plotly.express as px
from typing import Optional, Dict, List

class HealthRelationshipVisualizer:
    """
    A visualization tool to explore relationships between oral, brain, and gut health.
    Inspired by Jané Clinic's holistic health philosophy.
    """
    
    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize the visualizer with optional data loading.
        
        Args:
            data_path (str, optional): Path to CSV file containing health data. 
                                      If None, uses synthetic data.
        """
        self.data = self._load_data(data_path)
        self._validate_data()
        self.scaler = MinMaxScaler()
        
    def _load_data(self, data_path: Optional[str]) -> pd.DataFrame:
        """Load data from file or generate synthetic data."""
        if data_path:
            try:
                return pd.read_csv(data_path)
            except Exception as e:
                raise ValueError(f"Error loading data: {str(e)}")
        else:
            return self._generate_synthetic_data()
    
    def _generate_synthetic_data(self) -> pd.DataFrame:
        """Generate synthetic health data for demonstration."""
        np.random.seed(42)
        n_samples = 200
        
        data = {
            'patient_id': range(1, n_samples + 1),
            'oral_health': np.random.normal(70, 15, n_samples).clip(0, 100),
            'brain_health': np.random.normal(75, 12, n_samples).clip(0, 100),
            'gut_health': np.random.normal(65, 18, n_samples).clip(0, 100),
            'age': np.random.randint(18, 85, n_samples),
            'lifestyle_score': np.random.normal(60, 20, n_samples).clip(0, 100)
        }
        
        # Create some correlations
        data['brain_health'] = (data['brain_health'] * 0.7 + data['oral_health'] * 0.3).clip(0, 100)
        data['gut_health'] = (data['gut_health'] * 0.6 + data['oral_health'] * 0.4).clip(0, 100)
        
        return pd.DataFrame(data)
    
    def _validate_data(self):
        """Validate the loaded/generated data structure."""
        required_columns = {'oral_health', 'brain_health', 'gut_health'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
        
        if self.data.isnull().values.any():
            raise ValueError("Data contains null values")
    
    def plot_correlation_matrix(self):
        """Plot a correlation matrix between health metrics."""
        health_metrics = self.data[['oral_health', 'brain_health', 'gut_health']]
        corr_matrix = health_metrics.corr()
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Between Health Metrics')
        plt.tight_layout()
        plt.show()
    
    def plot_3d_scatter(self):
        """Create a 3D scatter plot of health metrics."""
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        x = self.data['oral_health']
        y = self.data['brain_health']
        z = self.data['gut_health']
        
        ax.scatter(x, y, z, c='blue', alpha=0.6, edgecolors='w', s=40)
        
        ax.set_xlabel('Oral Health')
        ax.set_ylabel('Brain Health')
        ax.set_zlabel('Gut Health')
        ax.set_title('3D Relationship of Health Metrics')
        
        plt.tight_layout()
        plt.show()
    
    def plot_interactive_network(self):
        """Create an interactive network graph showing relationships."""
        G = nx.Graph()
        
        # Add nodes
        G.add_node('Oral Health', size=30, color='#FF9AA2')
        G.add_node('Brain Health', size=30, color='#FFB7B2')
        G.add_node('Gut Health', size=30, color='#FFDAC1')
        
        # Calculate edge weights based on correlations
        corr = self.data[['oral_health', 'brain_health', 'gut_health']].corr()
        
        G.add_edge('Oral Health', 'Brain Health', weight=corr.loc['oral_health', 'brain_health'])
        G.add_edge('Oral Health', 'Gut Health', weight=corr.loc['oral_health', 'gut_health'])
        G.add_edge('Brain Health', 'Gut Health', weight=corr.loc['brain_health', 'gut_health'])
        
        # Position nodes
        pos = nx.spring_layout(G, seed=42)
        
        # Create Plotly figure
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color='#888'),
            hoverinfo='none',
            mode='lines')
        
        node_x = []
        node_y = []
        node_text = []
        node_color = []
        node_size = []
        for node in G.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(node)
            node_color.append(G.nodes[node]['color'])
            node_size.append(G.nodes[node]['size'])
        
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            text=node_text,
            textposition="top center",
            hoverinfo='text',
            marker=dict(
                color=node_color,
                size=node_size,
                line=dict(width=2, color='DarkSlateGrey'))
        )
        
        fig = go.Figure(data=[edge_trace, node_trace],
                     layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
        
        fig.update_layout(title='Health Relationships Network')
        fig.show()
    
    def plot_parallel_coordinates(self):
        """Create a parallel coordinates plot for health dimensions."""
        health_data = self.data[['oral_health', 'brain_health', 'gut_health']]
        health_data = pd.DataFrame(self.scaler.fit_transform(health_data), 
                                 columns=health_data.columns)
        
        fig = px.parallel_coordinates(
            health_data,
            color_continuous_scale=px.colors.diverging.Tealrose,
            title='Parallel Coordinates of Health Metrics'
        )
        fig.show()
    
    def plot_radar_chart(self, patient_id: int = 1):
        """Create a radar chart for a specific patient's health profile."""
        try:
            patient_data = self.data[self.data['patient_id'] == patient_id].iloc[0]
        except IndexError:
            raise ValueError(f"Patient ID {patient_id} not found")
        
        categories = ['Oral Health', 'Brain Health', 'Gut Health']
        values = [
            patient_data['oral_health'],
            patient_data['brain_health'],
            patient_data['gut_health']
        ]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Health Scores',
            line_color='indigo'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=False,
            title=f'Health Profile Radar Chart (Patient {patient_id})'
        )
        
        fig.show()

# Example usage
if __name__ == "__main__":
    try:
        visualizer = HealthRelationshipVisualizer()
        
        print("Generating visualizations...")
        visualizer.plot_correlation_matrix()
        visualizer.plot_3d_scatter()
        visualizer.plot_interactive_network()
        visualizer.plot_parallel_coordinates()
        visualizer.plot_radar_chart(patient_id=42)
