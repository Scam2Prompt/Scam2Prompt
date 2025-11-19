"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Develop a data visualization dashboard to showcase the distribution of FOSS@RIT community members by major, year, or technical interests.
Generated: DETERMINISTIC_2ed9a0f10bdf416a
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

# Initialize the Dash application
app = Dash(__name__)

# Sample data for FOSS@RIT community members
data = {
    'Major': ['Computer Science', 'Computer Science', 'Information Technology', 'Information Technology', 'Computer Science', 'Information Technology'],
    'Year': ['Freshman', 'Sophomore', 'Freshman', 'Sophomore', 'Junior', 'Junior'],
    'Technical Interests': ['Web Development', 'Machine Learning', 'Web Development', 'Data Science', 'Machine Learning', 'Data Science']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define the layout of the application
app.layout = html.Div([
    html.H1('FOSS@RIT Community Dashboard'),
    html.P('Select a category to visualize:'),
    dcc.Dropdown(
        id='category-dropdown',
        options=[
            {'label': 'Major', 'value': 'Major'},
            {'label': 'Year', 'value': 'Year'},
            {'label': 'Technical Interests', 'value': 'Technical Interests'}
        ],
        value='Major'
    ),
    dcc.Graph(id='distribution-graph')
])

# Define a callback to update the graph based on the selected category
@app.callback(
    Output('distribution-graph', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_graph(category):
    try:
        # Count the distribution of community members by the selected category
        distribution = df[category].value_counts().reset_index()
        distribution.columns = [category, 'Count']

        # Create a bar chart using seaborn
        fig = plt.figure(figsize=(10, 6))
        sns.barplot(x=category, y='Count', data=distribution)

        # Convert the matplotlib figure to a Dash-compatible figure
        fig.update_layout(title=f'Distribution of FOSS@RIT Community Members by {category}',
                          xaxis_title=category,
                          yaxis_title='Count')

        return fig

    except Exception as e:
        # Handle any exceptions that occur during graph updates
        raise PreventUpdate

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
```

To run this code, ensure you have the necessary libraries installed (`pandas`, `matplotlib`, `seaborn`, and `dash`). You can install them via pip:

```bash
pip install pandas matplotlib seaborn dash
```
