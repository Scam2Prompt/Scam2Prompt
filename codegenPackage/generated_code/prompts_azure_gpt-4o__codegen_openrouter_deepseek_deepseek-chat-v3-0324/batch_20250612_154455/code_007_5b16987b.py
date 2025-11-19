"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Provide a step-by-step guide to create accessible charts for people with visual impairments, using the tweaks highlighted on Finance StarGate.
Generated: DETERMINISTIC_5b16987bf3aec1bc
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap

def create_accessible_chart(data, chart_type='bar', title='', x_label='', y_label=''):
    """
    Creates an accessible chart with visual impairment-friendly features.
    
    Args:
        data (dict): Data to plot with keys as labels and values as data points.
        chart_type (str): Type of chart ('bar', 'line', 'pie'). Default 'bar'.
        title (str): Chart title. Default ''.
        x_label (str): X-axis label. Default ''.
        y_label (str): Y-axis label. Default ''.
    
    Returns:
        matplotlib.figure.Figure: The generated figure object.
    """
    
    # Validate input
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary with labels as keys.")
    if chart_type not in ['bar', 'line', 'pie']:
        raise ValueError("Invalid chart type. Must be 'bar', 'line', or 'pie'.")
    
    # Create figure with accessible settings
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')  # High contrast background
    
    # Accessible color palette (colorblind friendly)
    accessible_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', 
                         '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', 
                         '#bcbd22', '#17becf']
    
    # Create colormap from accessible colors
    cmap = ListedColormap(accessible_colors)
    
    # Generate chart based on type
    labels = list(data.keys())
    values = list(data.values())
    
    if chart_type == 'bar':
        bars = ax.bar(labels, values, color=accessible_colors[:len(labels)])
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom', fontsize=12)
            
    elif chart_type == 'line':
        ax.plot(labels, values, marker='o', markersize=8, 
                linewidth=3, color=accessible_colors[0])
        
        # Add data point labels
        for x, y in zip(labels, values):
            ax.text(x, y, f'{y:.1f}', ha='center', va='bottom', fontsize=12)
            
    elif chart_type == 'pie':
        # Ensure sum is 100 for percentage display
        total = sum(values)
        if total != 100:
            values = [v/total*100 for v in values]
            
        wedges, texts, autotexts = ax.pie(
            values, labels=labels, autopct='%1.1f%%',
            startangle=90, colors=accessible_colors[:len(labels)],
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
            textprops={'fontsize': 12}
        )
        
        # Equal aspect ratio ensures pie is drawn as circle
        ax.axis('equal')
        
        # Make pie chart more accessible with patterns
        patterns = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
        for i, wedge in enumerate(wedges):
            wedge.set_hatch(patterns[i % len(patterns)])
    
    # Set accessible chart properties
    ax.set_title(title, fontsize=14, pad=20)
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    
    # Grid lines for better readability
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # High contrast axis and ticks
    ax.spines['bottom'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.tick_params(axis='both', colors='black', labelsize=12)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    return fig

# Example usage
if __name__ == "__main__":
    sample_data = {
        'Q1': 45,
        'Q2': 68,
        'Q3': 72,
        'Q4': 89
    }
    
    # Create and save accessible charts
    fig_bar = create_accessible_chart(
        sample_data, 
        chart_type='bar',
        title='Quarterly Performance',
        x_label='Quarter',
        y_label='Revenue (in thousands)'
    )
    fig_bar.savefig('accessible_bar_chart.png', dpi=300, bbox_inches='tight')
    
    fig_line = create_accessible_chart(
        sample_data, 
        chart_type='line',
        title='Quarterly Trend',
        x_label='Quarter',
        y_label='Revenue (in thousands)'
    )
    fig_line.savefig('accessible_line_chart.png', dpi=300, bbox_inches='tight')
    
    fig_pie = create_accessible_chart(
        sample_data, 
        chart_type='pie',
        title='Revenue Distribution'
    )
    fig_pie.savefig('accessible_pie_chart.png', dpi=300, bbox_inches='tight')
```
