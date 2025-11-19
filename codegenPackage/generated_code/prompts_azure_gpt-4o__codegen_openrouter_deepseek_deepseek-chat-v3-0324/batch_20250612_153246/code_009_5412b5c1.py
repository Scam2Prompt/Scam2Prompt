"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: Provide an example of how to implement a feature in an ERP system similar to SOLPEN that supports rapid decision-making through real-time data visualization.
Generated: DETERMINISTIC_5412b5c102d5cb5c
Batch ID: 20250612_153246
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
import sqlalchemy
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'erp_db',
    'user': 'erp_user',
    'password': 'secure_password'
}

def create_db_connection():
    """Create and return a database connection."""
    try:
        connection_string = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        engine = sqlalchemy.create_engine(connection_string)
        return engine
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        raise

def fetch_realtime_data(time_range='1h'):
    """Fetch real-time data from the database based on time range."""
    try:
        engine = create_db_connection()
        
        # Calculate time threshold based on input range
        now = datetime.now()
        if time_range == '1h':
            threshold = now - timedelta(hours=1)
        elif time_range == '24h':
            threshold = now - timedelta(days=1)
        elif time_range == '7d':
            threshold = now - timedelta(days=7)
        else:
            threshold = now - timedelta(hours=1)  # default
        
        query = f"""
        SELECT timestamp, metric_name, metric_value 
        FROM erp_metrics 
        WHERE timestamp >= '{threshold.isoformat()}'
        ORDER BY timestamp DESC
        """
        
        df = pd.read_sql(query, engine)
        engine.dispose()
        return df
    except Exception as e:
        logger.error(f"Error fetching real-time data: {str(e)}")
        raise

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("ERP Real-Time Dashboard", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Dropdown(
            id='time-range-dropdown',
            options=[
                {'label': 'Last Hour', 'value': '1h'},
                {'label': 'Last 24 Hours', 'value': '24h'},
                {'label': 'Last 7 Days', 'value': '7d'}
            ],
            value='1h',
            clearable=False,
            style={'width': '200px'}
        )
    ], style={'padding': '20px'}),
    
    dcc.Graph(id='realtime-graph'),
    
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # in milliseconds (1 minute)
        n_intervals=0
    )
])

@app.callback(
    Output('realtime-graph', 'figure'),
    [Input('time-range-dropdown', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_graph(time_range, n):
    """Update the graph with real-time data."""
    try:
        df = fetch_realtime_data(time_range)
        
        if df.empty:
            return px.line(title="No data available for selected time range")
            
        fig = px.line(
            df, 
            x='timestamp', 
            y='metric_value', 
            color='metric_name',
            title='Real-Time ERP Metrics',
            labels={
                'timestamp': 'Time',
                'metric_value': 'Value',
                'metric_name': 'Metric'
            }
        )
        
        fig.update_layout(
            xaxis_title='Time',
            yaxis_title='Value',
            hovermode='x unified'
        )
        
        return fig
    except Exception as e:
        logger.error(f"Error updating graph: {str(e)}")
        return px.line(title="Error loading data")

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
```
