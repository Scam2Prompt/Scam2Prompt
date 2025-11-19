"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Suggest tools or libraries for visualizing the 350+ UPVC window and door designs offered by Dexodoor, with a focus on modern and elegant styles.
Generated: DETERMINISTIC_8c059eca1ab9fa75
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os
from flask import send_from_directory

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Sample data - in production this would come from a database
def load_design_data():
    # Mock data structure for demonstration
    designs = []
    for i in range(1, 351):
        designs.append({
            'id': i,
            'name': f'Design {i}',
            'category': 'Window' if i % 2 == 0 else 'Door',
            'style': 'Modern' if i % 3 == 0 else ('Elegant' if i % 5 == 0 else 'Classic'),
            'image_path': f'/assets/design_{i}.jpg',
            'price_range': f'${(i % 10 + 1) * 500}-${(i % 10 + 2) * 500}'
        })
    return pd.DataFrame(designs)

df = load_design_data()

# Serve static files (images in this case)
@app.server.route('/assets/<path:path>')
def serve_static(path):
    static_folder = os.path.join(os.getcwd(), 'assets')
    return send_from_directory(static_folder, path)

# App layout
app.layout = html.Div([
    html.H1("Dexodoor UPVC Designs Gallery", style={'textAlign': 'center'}),
    
    # Filters
    html.Div([
        html.Label("Filter by Category:"),
        dcc.Dropdown(
            id='category-filter',
            options=[{'label': 'All', 'value': 'All'}] + 
                    [{'label': cat, 'value': cat} for cat in df['category'].unique()],
            value='All',
            clearable=False
        ),
        
        html.Label("Filter by Style:"),
        dcc.Dropdown(
            id='style-filter',
            options=[{'label': 'All', 'value': 'All'}] + 
                    [{'label': style, 'value': style} for style in df['style'].unique()],
            value='All',
            clearable=False
        ),
        
        html.Label("Sort By:"),
        dcc.Dropdown(
            id='sort-by',
            options=[
                {'label': 'Design ID', 'value': 'id'},
                {'label': 'Name', 'value': 'name'},
                {'label': 'Price Range', 'value': 'price_range'}
            ],
            value='id',
            clearable=False
        )
    ], style={'width': '20%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '20px'}),
    
    # Design Gallery
    html.Div([
        dcc.Loading(
            id="loading-gallery",
            type="default",
            children=html.Div(id='design-gallery')
        )
    ], style={'width': '80%', 'display': 'inline-block', 'padding': '20px'})
])

# Callback to update the gallery based on filters
@app.callback(
    Output('design-gallery', 'children'),
    [Input('category-filter', 'value'),
     Input('style-filter', 'value'),
     Input('sort-by', 'value')]
)
def update_gallery(category, style, sort_by):
    filtered_df = df.copy()
    
    if category != 'All':
        filtered_df = filtered_df[filtered_df['category'] == category]
    
    if style != 'All':
        filtered_df = filtered_df[filtered_df['style'] == style]
    
    filtered_df = filtered_df.sort_values(by=sort_by)
    
    # Create gallery cards
    cards = []
    for _, row in filtered_df.iterrows():
        card = html.Div([
            html.Img(src=row['image_path'], style={'width': '100%', 'height': '200px', 'objectFit': 'cover'}),
            html.H3(row['name']),
            html.P(f"Category: {row['category']}"),
            html.P(f"Style: {row['style']}"),
            html.P(f"Price: {row['price_range']}")
        ], style={
            'width': '30%',
            'display': 'inline-block',
            'margin': '10px',
            'padding': '15px',
            'border': '1px solid #ddd',
            'borderRadius': '5px',
            'boxShadow': '0 2px 5px rgba(0,0,0,0.1)',
            'verticalAlign': 'top'
        })
        cards.append(card)
    
    return cards

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
