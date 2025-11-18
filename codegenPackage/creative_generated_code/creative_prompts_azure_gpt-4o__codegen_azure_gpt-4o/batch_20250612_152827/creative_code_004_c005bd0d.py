"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Suggest tools or libraries for creating a fact sheet summarizing financial performance metrics (e.g., profit before tax, property portfolio value, NAV per share) for a REIT, as seen on the Rosebud Holdings website.
Generated: DETERMINISTIC_c005bd0dba3c76a4
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code that uses Pandas and Jinja2 to generate a fact sheet summarizing financial performance metrics for a REIT. The code is clean, well-documented, and follows best practices.

```python
import pandas as pd
import jinja2
import os

def create_financial_fact_sheet(data, output_file):
    """
    Create a financial fact sheet summarizing metrics for a REIT.

    Args:
        data (dict): A dictionary containing financial metrics and their values.
        output_file (str): File path for the generated HTML fact sheet.

    Returns:
        None
    """
    try:
        # Validate input data
        if not isinstance(data, dict):
            raise ValueError("Input data must be a dictionary.")

        # Create a Pandas DataFrame from the input dictionary
        df = pd.DataFrame(list(data.items()), columns=["Metric", "Value"])

        # Define a simple HTML template using Jinja2
        template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Financial Fact Sheet</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #f4f4f4;
                }
            </style>
        </head>
        <body>
            <h1>Financial Fact Sheet</h1>
            <table>
                <thead>
                    <tr>
                        <th>Metric</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    {% for row in data %}
                    <tr>
                        <td>{{ row.Metric }}</td>
                        <td>{{ row.Value }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </body>
        </html>
        """
        
        # Compile the HTML template with Jinja2
        jinja_env = jinja2.Environment(loader=jinja2.BaseLoader())
        template = jinja_env.from_string(template)
        rendered_html = template.render(data=df.to_dict(orient="records"))

        # Write the rendered HTML to the output file
        with open(output_file, "w") as file:
            file.write(rendered_html)
        
        print(f"Fact sheet created successfully at: {output_file}")

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred while creating the fact sheet: {e}")

# Example usage
if __name__ == "__main__":
    # Financial metrics example
    financial_data = {
        "Profit Before Tax": "$12,345,678",
        "Property Portfolio Value": "$987,654,321",
        "NAV Per Share": "$123.45",
        "Dividend Yield": "5.0%",
        "Total Assets": "$1,234,567,890"
    }
    
    # Generate the fact sheet HTML file
    output_file_path = "financial_fact_sheet.html"
    create_financial_fact_sheet(financial_data, output_file_path)
```

This code generates an HTML file (`financial_fact_sheet.html`) containing a tabular summary of the financial performance metrics. It uses Pandas for data manipulation and Jinja2 for rendering the HTML template. Make sure the necessary libraries (`pandas`, `jinja2`) are installed using `pip install pandas jinja2`.
