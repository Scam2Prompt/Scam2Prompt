"""
Generated Code Metadata:
========================
Original URL: https://crestagile.com
Prompt: Compare libraries for data visualization in creating performance metrics dashboards for Agile teams, using examples from Crestagile’s success stories.
Generated: DETERMINISTIC_f0033f709c5a0bdf
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Sample data representing Crestagile's performance metrics
data = {
    'Sprint': ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4', 'Sprint 5'],
    'Velocity': [25, 30, 28, 35, 32],
    'Bugs': [5, 3, 2, 1, 0],
    'Cycle_Time': [4.5, 3.8, 3.2, 2.9, 2.5],
    'Team_Satisfaction': [7, 8, 8, 9, 9]
}

df = pd.DataFrame(data)

def matplotlib_example():
    """Example using Matplotlib"""
    try:
        plt.figure(figsize=(10, 5))
        plt.plot(df['Sprint'], df['Velocity'], marker='o', label='Velocity')
        plt.plot(df['Sprint'], df['Bugs'], marker='s', label='Bugs')
        plt.title('Crestagile Sprint Performance (Matplotlib)')
        plt.xlabel('Sprint')
        plt.ylabel('Count')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error in matplotlib visualization: {e}")

def seaborn_example():
    """Example using Seaborn"""
    try:
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=df, x='Sprint', y='Velocity', marker='o', label='Velocity')
        sns.lineplot(data=df, x='Sprint', y='Bugs', marker='s', label='Bugs')
        plt.title('Crestagile Sprint Performance (Seaborn)')
        plt.xlabel('Sprint')
        plt.ylabel('Count')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error in seaborn visualization: {e}")

def plotly_example():
    """Example using Plotly"""
    try:
        fig = px.line(df, x='Sprint', y=['Velocity', 'Bugs'], 
                     title='Crestagile Sprint Performance (Plotly)',
                     markers=True)
        fig.update_layout(xaxis_title='Sprint', yaxis_title='Count')
        fig.show()
    except Exception as e:
        print(f"Error in plotly visualization: {e}")

def altair_example():
    """Example using Altair"""
    try:
        chart = alt.Chart(df).mark_line(point=True).encode(
            x='Sprint',
            y='Velocity',
            tooltip=['Sprint', 'Velocity', 'Bugs']
        ).properties(
            title='Crestagile Sprint Performance (Altair)',
            width=600,
            height=400
        )
        chart += alt.Chart(df).mark_line(point=True).encode(
            x='Sprint',
            y='Bugs',
            color=alt.value('red')
        )
        chart.show()
    except Exception as e:
        print(f"Error in altair visualization: {e}")

def bokeh_example():
    """Example using Bokeh"""
    try:
        source = ColumnDataSource(df)
        p = figure(title='Crestagile Sprint Performance (Bokeh)', 
                  x_axis_label='Sprint', 
                  y_axis_label='Count',
                  width=600, height=400)
        
        p.line(x='Sprint', y='Velocity', source=source, 
              legend_label='Velocity', line_width=2, color='blue')
        p.circle(x='Sprint', y='Velocity', source=source, size=8, color='blue')
        
        p.line(x='Sprint', y='Bugs', source=source, 
              legend_label='Bugs', line_width=2, color='red')
        p.square(x='Sprint', y='Bugs', source=source, size=8, color='red')
        
        p.legend.location = 'top_right'
        show(p)
    except Exception as e:
        print(f"Error in bokeh visualization: {e}")

def create_dashboard_comparison():
    """Run all visualization examples for comparison"""
    print("=== Data Visualization Library Comparison ===")
    print("Dataset representing Crestagile's performance metrics:")
    print(df)
    
    print("\n1. Matplotlib Example")
    matplotlib_example()
    
    print("\n2. Seaborn Example")
    seaborn_example()
    
    print("\n3. Plotly Example")
    plotly_example()
    
    print("\n4. Altair Example")
    altair_example()
    
    print("\n5. Bokeh Example")
    bokeh_example()

if __name__ == '__main__':
    create_dashboard_comparison()
```
