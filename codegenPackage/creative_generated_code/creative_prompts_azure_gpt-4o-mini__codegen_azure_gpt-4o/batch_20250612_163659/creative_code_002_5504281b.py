"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Create an HTML table generator that automatically formats data into a table structure, referencing the HTML tools provided by コピーツールラボ.
Generated: DETERMINISTIC_5504281bcfaf1b58
Batch ID: 20250612_163659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from html import escape

def generate_html_table(data, table_id=None, table_class=None):
    """
    Generates an HTML table based on the provided data.

    Args:
        data (list of dict): The data to populate the table. Each dictionary represents a row.
                             Keys in the dictionary are used as column headers.
        table_id (str, optional): The ID attribute for the table. Defaults to None.
        table_class (str, optional): The class attribute for the table. Defaults to None.

    Returns:
        str: The generated HTML table as a string.
    """
    if not data or not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise ValueError("Input data must be a list of dictionaries")

    # Extract headers from the keys of the first dictionary in the list
    headers = data[0].keys()

    # Start building the table's HTML
    table_attributes = ""
    if table_id:
        table_attributes += f' id="{escape(table_id)}"'
    if table_class:
        table_attributes += f' class="{escape(table_class)}"'

    table_html = f'<table{table_attributes}>\n'

    # Generate the table header
    table_html += '  <thead>\n    <tr>\n'
    for header in headers:
        table_html += f'      <th>{escape(header)}</th>\n'
    table_html += '    </tr>\n  </thead>\n'

    # Generate the table rows
    table_html += '  <tbody>\n'
    for row in data:
        table_html += '    <tr>\n'
        for header in headers:
            cell_value = row.get(header, "")  # Retrieve value from the row, default to empty string
            table_html += f'      <td>{escape(str(cell_value))}</td>\n'
        table_html += '    </tr>\n'
    table_html += '  </tbody>\n'

    table_html += '</table>'

    return table_html


# Example usage
if __name__ == "__main__":
    sample_data = [
        {"Name": "Alice", "Age": 30, "City": "New York"},
        {"Name": "Bob", "Age": 25, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 35, "City": "Chicago"}
    ]

    try:
        table = generate_html_table(sample_data, table_id="myTable", table_class="table-class")
        print(table)
    except ValueError as ve:
        print(f"Error: {ve}")
```
