"""
Generated Code Metadata:
========================
Original URL: https://socialimpactheroes.com
Prompt: Create a data visualization dashboard to showcase the distribution of social impact heroes across different categories (e.g., "Stars Making A Social Impact," "Unstoppable!") and their geographic locations.
Generated: DETERMINISTIC_a73f505156592291
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load dataset (replace with your actual data source)
def load_data():
    # Sample data - replace with your actual data loading logic
    data = {
        "Name": ["Hero1", "Hero2", "Hero3", "Hero4", "Hero5"],
        "Category": ["Stars Making A Social Impact", "Unstoppable!", 
                    "Stars Making A Social Impact", "Community Builders", 
                    "Unstoppable!"],
        "Country": ["USA", "UK", "Canada", "Australia", "India"],
        "City": ["New York", "London", "Toronto", "Sydney", "Mumbai"],
        "Impact_Score": [85, 92, 78, 88, 95]
    }
    return pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Load the data
df = load_data()

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Social Impact Heroes Dashboard", style={'text-align': 'center'}),
    
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='category-dropdown',
                options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
                value=df['Category'].unique()[0],
                clearable=False,
                placeholder="Select a category"
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df['Country'].unique()],
                value=None,
                clearable=True,
                placeholder="Select a country (optional)"
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    
    html.Div([
        dcc.Graph(id='category-distribution')
    ]),
    
    html.Div([
        dcc.Graph(id='geo-distribution')
    ]),
    
    html.Div([
        dcc.Graph(id='impact-score-distribution')
    ])
])

# Callback for updating graphs based on dropdown selections
@app.callback(
    [Output('category-distribution', 'figure'),
     Output('geo-distribution', 'figure'),
     Output('impact-score-distribution', 'figure')],
    [Input('category-dropdown', 'value'),
     Input('country-dropdown', 'value')]
)
def update_graphs(selected_category, selected_country):
    # Filter data based on selections
    filtered_df = df.copy()
    if selected_category:
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]
    if selected_country:
        filtered_df = filtered_df[filtered_df['Country'] == selected_country]
    
    # Create category distribution pie chart
    category_counts = df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']
    pie_fig = px.pie(
        category_counts,
        names='Category',
        values='Count',
        title='Distribution Across Categories'
    )
    
    # Create geographic distribution map
    geo_fig = px.scatter_geo(
        filtered_df,
        locations='Country',
        locationmode='country names',
        color='Category',
        hover_name='Name',
        hover_data=['City', 'Impact_Score'],
        title='Geographic Distribution of Heroes'
    )
    geo_fig.update_geos(showcountries=True)
    
    # Create impact score histogram
    hist_fig = px.histogram(
        filtered_df,
        x='Impact_Score',
        nbins=10,
        color='Category',
        title='Impact Score Distribution',
        labels={'Impact_Score': 'Impact Score'}
    )
    
    return pie_fig, geo_fig, hist_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
