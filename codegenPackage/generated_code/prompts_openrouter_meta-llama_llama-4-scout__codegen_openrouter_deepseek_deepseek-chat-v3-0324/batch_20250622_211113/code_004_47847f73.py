"""
Generated Code Metadata:
========================
Original URL: https://stelth-boxing.web.app
Prompt: Create a data analytics dashboard using a suitable library (e.g., Tableau, Power BI) to track the performance of the Magic Box project, including metrics such as total items, mint rate, and burn rate.
Generated: DETERMINISTIC_47847f737c8624f7
Batch ID: 20250622_211113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Sample data (in production, this would come from a database or API)
data = {
    'date': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'total_items': [100 + i*2 for i in range(365)],
    'minted': [5 + i%7 for i in range(365)],
    'burned': [2 + i%5 for i in range(365)]
}
df = pd.DataFrame(data)
df['net_change'] = df['minted'] - df['burned']

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Magic Box Project Analytics Dashboard", style={'textAlign': 'center'}),
    
    # Summary metrics row
    html.Div([
        html.Div([
            html.H3("Total Items"),
            html.P(id='total-items', style={'fontSize': 24})
        ], className='four columns', style={'textAlign': 'center'}),
        
        html.Div([
            html.H3("Mint Rate (7d avg)"),
            html.P(id='mint-rate', style={'fontSize': 24})
        ], className='four columns', style={'textAlign': 'center'}),
        
        html.Div([
            html.H3("Burn Rate (7d avg)"),
            html.P(id='burn-rate', style={'fontSize': 24})
        ], className='four columns', style={'textAlign': 'center'})
    ], className='row'),
    
    # Date range selector
    dcc.DatePickerRange(
        id='date-range',
        min_date_allowed=df['date'].min(),
        max_date_allowed=df['date'].max(),
        start_date=df['date'].min(),
        end_date=df['date'].max()
    ),
    
    # Charts
    dcc.Graph(id='total-items-chart'),
    dcc.Graph(id='mint-burn-chart'),
    dcc.Graph(id='net-change-chart')
])

# Callbacks for dynamic updates
@app.callback(
    [Output('total-items', 'children'),
     Output('mint-rate', 'children'),
     Output('burn-rate', 'children')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_summary(start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    
    total_items = filtered_df['total_items'].iloc[-1]
    mint_rate = filtered_df['minted'].tail(7).mean()
    burn_rate = filtered_df['burned'].tail(7).mean()
    
    return f"{total_items:,}", f"{mint_rate:.1f}/day", f"{burn_rate:.1f}/day"

@app.callback(
    Output('total-items-chart', 'figure'),
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_total_items_chart(start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    fig = px.line(filtered_df, x='date', y='total_items', 
                  title='Total Items Over Time')
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('mint-burn-chart', 'figure'),
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_mint_burn_chart(start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    fig = px.line(filtered_df, x='date', y=['minted', 'burned'], 
                  title='Mint vs Burn Rates')
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('net-change-chart', 'figure'),
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_net_change_chart(start_date, end_date):
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    fig = px.bar(filtered_df, x='date', y='net_change', 
                 title='Daily Net Change (Minted - Burned)')
    fig.update_layout(transition_duration=500)
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
```
