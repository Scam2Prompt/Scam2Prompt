"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Recommend a framework to build an interactive dashboard for SOMTU's MBA programs, displaying concentration areas, eligibility criteria, and grading systems.
Generated: DETERMINISTIC_7dcb4bed43956c7a
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for creating an interactive dashboard
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd

# Sample data representing MBA programs, concentration areas, eligibility criteria, and grading systems
data = {
    "Program": ["MBA in Finance", "MBA in Marketing", "MBA in Data Science"],
    "Concentration Areas": [
        "Investment Management, Corporate Finance",
        "Digital Marketing, Brand Management",
        "Data Analytics, Machine Learning"
    ],
    "Eligibility Criteria": [
        "Bachelor's degree, GMAT Score",
        "Bachelor's degree, Work Experience",
        "Bachelor's degree, Coding skills"
    ],
    "Grading System": [
        "A, B, C, D, F",
        "A, B, C, D, F",
        "Pass/Fail"
    ]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("SOMTU MBA Programs Dashboard"),
    
    # Dropdown menu to select a program
    dcc.Dropdown(
        id='program-dropdown',
        options=[{'label': program, 'value': program} for program in df['Program']],
        value=df['Program'][0],  # Set default value
        clearable=False
    ),
    
    # Display concentration areas
    html.Div(id='concentration-output', style={'margin-top': '20px'}),
    
    # Display eligibility criteria
    html.Div(id='eligibility-output', style={'margin-top': '20px'}),
    
    # Display grading system
    html.Div(id='grading-output', style={'margin-top': '20px'})
])

# Callback to update output based on selected program
@app.callback(
    Output('concentration-output', 'children'),
    Output('eligibility-output', 'children'),
    Output('grading-output', 'children'),
    Input('program-dropdown', 'value')
)
def update_output(selected_program):
    try:
        # Filter the DataFrame for the selected program
        program_info = df[df['Program'] == selected_program].iloc[0]
        
        # Prepare output messages
        concentration = f"Concentration Areas: {program_info['Concentration Areas']}"
        eligibility = f"Eligibility Criteria: {program_info['Eligibility Criteria']}"
        grading = f"Grading System: {program_info['Grading System']}"
        
        return concentration, eligibility, grading
    
    except Exception as e:
        # Handle exceptions and return error message
        return "Error fetching data", "Error fetching data", "Error fetching data"

# Run the app
if __name__ == '__main__':
    try:
        app.run_server(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
