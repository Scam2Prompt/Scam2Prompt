"""
Generated Code Metadata:
========================
Original URL: https://www.sgeek-seo.com
Prompt: Write a Python script to generate HTML5 or SVG diagrams using one of the free tools mentioned on the SGeek SEO website.
Generated: DETERMINISTIC_e672b8abf4367c36
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Generate HTML5/SVG diagrams using Pygal library.

This script creates various types of charts (line, bar, pie) and saves them as SVG/HTML files.
"""

import pygal
from pygal.style import Style
import os
import argparse

def create_chart(chart_type, data, title, output_file, style=None):
    """
    Create a chart based on the specified type and save it to a file.
    
    Args:
        chart_type (str): Type of chart ('line', 'bar', 'pie')
        data (dict): Data to plot {label: value}
        title (str): Chart title
        output_file (str): Output filename
        style (pygal.style.Style): Custom style for the chart
    """
    try:
        if chart_type == 'line':
            chart = pygal.Line(style=style)
        elif chart_type == 'bar':
            chart = pygal.Bar(style=style)
        elif chart_type == 'pie':
            chart = pygal.Pie(style=style)
        else:
            raise ValueError(f"Unsupported chart type: {chart_type}")
        
        chart.title = title
        for label, value in data.items():
            chart.add(label, value)
        
        if output_file.endswith('.svg'):
            chart.render_to_file(output_file)
        elif output_file.endswith('.html'):
            chart.render_to_file(output_file)
        else:
            raise ValueError("Output file must have .svg or .html extension")
            
    except Exception as e:
        print(f"Error creating chart: {e}")
        raise

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Generate SVG/HTML charts using Pygal')
    parser.add_argument('--type', choices=['line', 'bar', 'pie'], required=True,
                       help='Type of chart to generate')
    parser.add_argument('--title', required=True, help='Title of the chart')
    parser.add_argument('--output', required=True, 
                       help='Output filename (must end with .svg or .html)')
    parser.add_argument('--data', nargs='+', required=True,
                       help='Data in format label1:value1 label2:value2 ...')
    return parser.parse_args()

def main():
    """Main function to generate the chart."""
    try:
        args = parse_args()
        
        # Parse data
        data = {}
        for item in args.data:
            label, value = item.split(':')
            data[label] = float(value)
        
        # Custom style
        custom_style = Style(
            background='white',
            plot_background='#f0f0f0',
            foreground='black',
            foreground_strong='black',
            foreground_subtle='#555',
            opacity='.6',
            opacity_hover='.9',
            transition='400ms ease-in',
            colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53')
        )
        
        create_chart(
            chart_type=args.type,
            data=data,
            title=args.title,
            output_file=args.output,
            style=custom_style
        )
        
        print(f"Chart successfully saved to {args.output}")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
```
