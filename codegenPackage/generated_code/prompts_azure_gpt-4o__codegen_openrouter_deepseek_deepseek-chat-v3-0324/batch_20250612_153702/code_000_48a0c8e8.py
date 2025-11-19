"""
Generated Code Metadata:
========================
Original URL: https://dustbox.netlify.app
Prompt: Write code to integrate an interactive graph feature using the functionality described on the Dustbox website.
Generated: DETERMINISTIC_48a0c8e88903fea8
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

# Initialize the Dash app with Bootstrap components
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample data (replace with actual data from Dustbox API)
sample_data = {
    "nodes": [
        {"id": "A", "group": 1},
        {"id": "B", "group": 1},
        {"id": "C", "group": 2},
        {"id": "D", "group": 2},
        {"id": "E", "group": 3},
    ],
    "links": [
        {"source": "A", "target": "B", "value": 10},
        {"source": "B", "target": "C", "value": 8},
        {"source": "C", "target": "D", "value": 6},
        {"source": "D", "target": "E", "value": 4},
        {"source": "E", "target": "A", "value": 2},
    ]
}

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Interactive Graph Visualization", className="text-center mb-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='graph-type-dropdown',
                options=[
                    {'label': 'Force-Directed', 'value': 'force'},
                    {'label': 'Sankey', 'value': 'sankey'},
                    {'label': 'Network', 'value': 'network'}
                ],
                value='force',
                clearable=False
            ),
            dcc.Graph(id='interactive-graph')
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id='node-info', className="mt-3 p-3 border rounded")
        ], width=12)
    ])
], fluid=True)

@callback(
    Output('interactive-graph', 'figure'),
    Input('graph-type-dropdown', 'value')
)
def update_graph(graph_type):
    """Update graph based on selected type"""
    try:
        if graph_type == 'force':
            fig = go.Figure(go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=[node["id"] for node in sample_data["nodes"]],
                    color=["blue" if node["group"] == 1 else 
                          "green" if node["group"] == 2 else 
                          "red" for node in sample_data["nodes"]]
                ),
                link=dict(
                    source=[sample_data["nodes"].index(next(n for n in sample_data["nodes"] if n["id"] == link["source"])) 
                           for link in sample_data["links"]],
                    target=[sample_data["nodes"].index(next(n for n in sample_data["nodes"] if n["id"] == link["target"])) 
                           for link in sample_data["links"]],
                    value=[link["value"] for link in sample_data["links"]]
                )
            ))
        elif graph_type == 'sankey':
            fig = go.Figure(go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=[node["id"] for node in sample_data["nodes"]],
                    color=["blue" if node["group"] == 1 else 
                          "green" if node["group"] == 2 else 
                          "red" for node in sample_data["nodes"]]
                ),
                link=dict(
                    source=[sample_data["nodes"].index(next(n for n in sample_data["nodes"] if n["id"] == link["source"])) 
                           for link in sample_data["links"]],
                    target=[sample_data["nodes"].index(next(n for n in sample_data["nodes"] if n["id"] == link["target"])) 
                           for link in sample_data["links"]],
                    value=[link["value"] for link in sample_data["links"]]
                )
            ))
        else:  # network
            fig = go.Figure(go.Scatter(
                x=[1, 2, 3, 4],
                y=[10, 11, 12, 13],
                mode='markers',
                marker=dict(size=[40, 60, 80, 100])
            ))
        
        fig.update_layout(
            title=f"{graph_type.capitalize()} Graph",
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40)
        )
        return fig
    except Exception as e:
        print(f"Error generating graph: {str(e)}")
        return go.Figure()

@callback(
    Output('node-info', 'children'),
    Input('interactive-graph', 'clickData')
)
def display_node_info(click_data):
    """Display information about clicked node"""
    if not click_data:
        return "Click on a node to see details"
    
    try:
        point = click_data['points'][0]
        if 'node' in point:  # For Sankey/Force graphs
            node_index = point['node']
            node = sample_data['nodes'][node_index]
            links = [link for link in sample_data['links'] 
                    if link['source'] == node['id'] or link['target'] == node['id']]
            
            return html.Div([
                html.H4(f"Node: {node['id']}"),
                html.P(f"Group: {node['group']}"),
                html.H5("Connections:"),
                html.Ul([html.Li(f"{link['source']} → {link['target']} (value: {link['value']})") 
                        for link in links])
            ])
        else:  # For network graph
            return html.Div([
                html.H4(f"Point at ({point['x']}, {point['y']})"),
                html.P(f"Marker size: {point['marker.size']}")
            ])
    except Exception as e:
        print(f"Error processing click data: {str(e)}")
        return "Error displaying node information"

if __name__ == '__main__':
    app.run_server(debug=True)
```
