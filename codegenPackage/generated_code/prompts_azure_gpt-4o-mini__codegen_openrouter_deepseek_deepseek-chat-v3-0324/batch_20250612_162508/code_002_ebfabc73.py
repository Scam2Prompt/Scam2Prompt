"""
Generated Code Metadata:
========================
Original URL: https://metamass.de
Prompt: Create a prototype for a brand concept that incorporates data visualization techniques highlighted in the portfolio section of metamass.de.
Generated: DETERMINISTIC_ebfabc73c1882f09
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
from dash.exceptions import PreventUpdate

# Initialize the Dash app
app = Dash(__name__)

# Sample data generation function
def generate_sample_data():
    """Generate sample data for visualization"""
    np.random.seed(42)
    categories = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Energy']
    data = {
        'Category': categories,
        'Value': np.random.randint(100, 1000, size=len(categories)),
        'Growth': np.random.uniform(-0.2, 0.5, size=len(categories)),
        'MarketShare': np.random.uniform(0.1, 0.3, size=len(categories))
    }
    return pd.DataFrame(data)

# Load or generate data
df = generate_sample_data()

# Create interactive bubble chart
def create_bubble_chart(data):
    """Create an interactive bubble chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=data['Growth'],
        y=data['MarketShare'],
        text=data['Category'],
        mode='markers',
        marker=dict(
            size=data['Value']/20,
            color=data['Value'],
            colorscale='Viridis',
            showscale=True
        ),
        hovertemplate="<b>%{text}</b><br>" +
                      "Growth: %{x:.2%}<br>" +
                      "Market Share: %{y:.2%}<br>" +
                      "Value: %{marker.size:,}<extra></extra>"
    ))
    
    fig.update_layout(
        title='Industry Market Overview',
        xaxis_title='Growth Rate',
        yaxis_title='Market Share',
        hovermode='closest',
        template='plotly_dark'
    )
    
    return fig

# Create treemap visualization
def create_treemap(data):
    """Create a hierarchical treemap"""
    fig = go.Figure(go.Treemap(
        labels=data['Category'],
        parents=[''] * len(data),
        values=data['Value'],
        marker=dict(colors=data['Value'], colorscale='Blues'),
        textinfo="label+value+percent parent",
        hovertemplate="<b>%{label}</b><br>Value: %{value:,}<extra></extra>"
    ))
    
    fig.update_layout(
        title='Market Value Distribution',
        template='plotly_dark'
    )
    
    return fig

# App layout
app.layout = html.Div([
    html.H1("Metamass Data Visualization Prototype", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            dcc.Graph(
                id='bubble-chart',
                figure=create_bubble_chart(df)
            )
        ], className='six columns'),
        html.Div([
            dcc.Graph(
                id='treemap',
                figure=create_treemap(df)
            )
        ], className='six columns')
    ], className='row'),
    html.Div([
        dcc.Dropdown(
            id='data-selector',
            options=[
                {'label': 'Sample Data', 'value': 'sample'},
                {'label': 'Randomized Data', 'value': 'random'}
            ],
            value='sample',
            clearable=False
        )
    ], style={'width': '50%', 'margin': '0 auto'}),
    html.Div(id='data-info', style={'marginTop': 20})
])

# Callback for data updates
@app.callback(
    [Output('bubble-chart', 'figure'),
     Output('treemap', 'figure'),
     Output('data-info', 'children')],
    [Input('data-selector', 'value')]
)
def update_data(selected_data):
    """Update visualizations based on data selection"""
    try:
        if selected_data == 'random':
            new_df = generate_sample_data()
            random.seed()
            new_df['Value'] = np.random.randint(50, 1500, size=len(new_df))
            new_df['Growth'] = np.random.uniform(-0.3, 0.6, size=len(new_df))
            new_df['MarketShare'] = np.random.uniform(0.05, 0.35, size=len(new_df))
        else:
            new_df = generate_sample_data()
        
        bubble = create_bubble_chart(new_df)
        treemap = create_treemap(new_df)
        info = f"Displaying {selected_data} data with {len(new_df)} categories"
        
        return bubble, treemap, info
    except Exception as e:
        raise PreventUpdate(f"Error updating data: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
```
