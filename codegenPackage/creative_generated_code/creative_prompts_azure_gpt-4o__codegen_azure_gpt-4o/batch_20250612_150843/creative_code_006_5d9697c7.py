"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.immediateapexai.org
Prompt: Write a Python function to personalize chart colors and styles using Immediate Apex AI's customization options for enhanced data visualization.
Generated: DETERMINISTIC_5d9697c7009cfaeb
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def personalize_chart(data, chart_type, title, x_label, y_label, color_scheme='default', style='default', save_path=None):
    """
    Personalizes chart colors and styles using Immediate Apex AI's customization options.

    Parameters:
        data (dict): Dictionary containing data for the chart. 
                     Keys should be labels/categories and values should be numeric data.
        chart_type (str): Type of chart ('bar', 'line', 'pie').
        title (str): Title of the chart.
        x_label (str): Label for the x-axis (ignored for pie charts).
        y_label (str): Label for the y-axis (ignored for pie charts).
        color_scheme (str): Name of the color scheme ('default', 'pastel', 'vibrant').
        style (str): Matplotlib style ('default', 'ggplot', 'seaborn', etc.).
        save_path (str): Optional file path to save the chart image.

    Returns:
        None: Displays the chart and optionally saves it to the specified path.
    """
    # Error handling for invalid inputs
    if not isinstance(data, dict) or not all(isinstance(v, (int, float)) for v in data.values()):
        raise ValueError("Data must be a dictionary with numeric values.")
    if chart_type not in ['bar', 'line', 'pie']:
        raise ValueError("Invalid chart type. Supported types are 'bar', 'line', 'pie'.")
    if color_scheme not in ['default', 'pastel', 'vibrant']:
        raise ValueError("Invalid color scheme. Supported schemes are 'default', 'pastel', 'vibrant'.")

    # Set style for the chart
    plt.style.use(style if style != 'default' else 'classic')

    # Customize color schemes
    color_palettes = {
        'default': mcolors.TABLEAU_COLORS,
        'pastel': mcolors.CSS4_COLORS,
        'vibrant': mcolors.XKCD_COLORS
    }
    colors = list(color_palettes[color_scheme].values())

    # Create the chart based on the type
    if chart_type == 'bar':
        plt.bar(data.keys(), data.values(), color=colors[:len(data)])
    elif chart_type == 'line':
        plt.plot(data.keys(), data.values(), marker='o', color=colors[0])
    elif chart_type == 'pie':
        plt.pie(data.values(), labels=data.keys(), colors=colors[:len(data)], autopct='%1.1f%%')

    # Add chart details
    plt.title(title)
    if chart_type in ['bar', 'line']:
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    # Save or display chart
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

# Example Usage
if __name__ == "__main__":
    sample_data = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
    personalize_chart(sample_data, chart_type='bar', title='Sample Chart', x_label='Categories', y_label='Values', 
                      color_scheme='pastel', style='ggplot')
```
