"""
Generated Code Metadata:
========================
Original URL: https://globallinknext.com
Prompt: Write a Python script to analyze the engagement metrics of a conference like GlobalLink NEXT, including speaker popularity and attendee networking connections.
Generated: DETERMINISTIC_a3248c2bb359303d
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class ConferenceAnalyzer:
    """
    Analyzes engagement metrics for a conference including speaker popularity and attendee networking.
    """
    
    def __init__(self, sessions_file, attendees_file, connections_file):
        """
        Initialize the analyzer with data files.
        
        Args:
            sessions_file (str): Path to JSON file containing session data
            attendees_file (str): Path to JSON file containing attendee data
            connections_file (str): Path to JSON file containing connection data
        """
        try:
            with open(sessions_file) as f:
                self.sessions = json.load(f)
            with open(attendees_file) as f:
                self.attendees = json.load(f)
            with open(connections_file) as f:
                self.connections = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data file not found: {e.filename}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in data file: {e.doc}")
            
        self.validate_data()
        
    def validate_data(self):
        """Validate the loaded data has required fields."""
        required_session_fields = ['session_id', 'title', 'speaker_id', 'attendees']
        required_attendee_fields = ['attendee_id', 'name', 'company']
        required_connection_fields = ['attendee1', 'attendee2', 'strength']
        
        for session in self.sessions:
            if not all(field in session for field in required_session_fields):
                raise ValueError("Session data missing required fields")
                
        for attendee in self.attendees:
            if not all(field in attendee for field in required_attendee_fields):
                raise ValueError("Attendee data missing required fields")
                
        for connection in self.connections:
            if not all(field in connection for field in required_connection_fields):
                raise ValueError("Connection data missing required fields")
    
    def calculate_speaker_popularity(self):
        """
        Calculate speaker popularity based on session attendance.
        
        Returns:
            DataFrame: Speaker popularity metrics sorted by total attendees
        """
        speaker_attendance = defaultdict(int)
        speaker_sessions = defaultdict(int)
        
        for session in self.sessions:
            speaker_id = session['speaker_id']
            attendees_count = len(session['attendees'])
            speaker_attendance[speaker_id] += attendees_count
            speaker_sessions[speaker_id] += 1
            
        # Get speaker names
        speaker_info = {a['attendee_id']: a['name'] for a in self.attendees 
                       if a['attendee_id'] in speaker_attendance}
        
        # Create DataFrame
        data = []
        for speaker_id, attendance in speaker_attendance.items():
            data.append({
                'speaker_id': speaker_id,
                'name': speaker_info.get(speaker_id, 'Unknown'),
                'total_attendees': attendance,
                'session_count': speaker_sessions[speaker_id],
                'avg_attendance': attendance / speaker_sessions[speaker_id]
            })
            
        df = pd.DataFrame(data)
        return df.sort_values('total_attendees', ascending=False)
    
    def analyze_networking(self):
        """
        Analyze attendee networking connections.
        
        Returns:
            tuple: (network_metrics, graph) where:
                - network_metrics is a DataFrame with connection stats
                - graph is a NetworkX graph object
        """
        # Build the graph
        G = nx.Graph()
        
        # Add nodes (attendees)
        for attendee in self.attendees:
            G.add_node(attendee['attendee_id'], 
                      name=attendee['name'],
                      company=attendee['company'])
        
        # Add edges (connections)
        for connection in self.connections:
            G.add_edge(connection['attendee1'],
                       connection['attendee2'],
                       weight=connection['strength'])
        
        # Calculate metrics
        degree_centrality = nx.degree_centrality(G)
        betweenness_centrality = nx.betweenness_centrality(G)
        closeness_centrality = nx.closeness_centrality(G)
        
        # Create DataFrame
        data = []
        for node in G.nodes():
            data.append({
                'attendee_id': node,
                'name': G.nodes[node]['name'],
                'company': G.nodes[node]['company'],
                'degree_centrality': degree_centrality[node],
                'betweenness_centrality': betweenness_centrality[node],
                'closeness_centrality': closeness_centrality[node],
                'connections': len(list(G.neighbors(node)))
            })
            
        metrics_df = pd.DataFrame(data)
        metrics_df = metrics_df.sort_values('degree_centrality', ascending=False)
        
        return metrics_df, G
    
    def visualize_network(self, G, output_file='network.png'):
        """
        Visualize the attendee network graph.
        
        Args:
            G (NetworkX graph): The graph to visualize
            output_file (str): Path to save the visualization
        """
        plt.figure(figsize=(12, 12))
        
        # Layout
        pos = nx.spring_layout(G, k=0.15, iterations=20)
        
        # Draw nodes
        nx.draw_networkx_nodes(G, pos, node_size=50, node_color='skyblue')
        
        # Draw edges
        nx.draw_networkx_edges(G, pos, alpha=0.1)
        
        # Draw labels for top 10% most connected
        degrees = dict(G.degree())
        top_10_percent = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:len(degrees)//10]
        labels = {node: G.nodes[node]['name'] for node, _ in top_10_percent}
        nx.draw_networkx_labels(G, pos, labels, font_size=8)
        
        plt.title("Conference Attendee Network")
        plt.axis('off')
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        plt.close()
        
    def generate_report(self, speaker_output='speaker_popularity.csv', 
                       network_output='network_metrics.csv',
                       visualization_output='network.png'):
        """
        Generate comprehensive report with all metrics.
        
        Args:
            speaker_output (str): Path to save speaker popularity CSV
            network_output (str): Path to save network metrics CSV
            visualization_output (str): Path to save network visualization
        """
        # Speaker popularity
        speaker_df = self.calculate_speaker_popularity()
        speaker_df.to_csv(speaker_output, index=False)
        
        # Network analysis
        network_df, G = self.analyze_networking()
        network_df.to_csv(network_output, index=False)
        
        # Visualization
        self.visualize_network(G, visualization_output)
        
        return {
            'speaker_metrics': speaker_df,
            'network_metrics': network_df,
            'network_graph': G
        }


if __name__ == "__main__":
    try:
        analyzer = ConferenceAnalyzer(
            sessions_file='sessions.json',
            attendees_file='attendees.json',
            connections_file='connections.json'
        )
        
        report = analyzer.generate_report()
        print("Analysis completed successfully. Reports generated.")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
```
