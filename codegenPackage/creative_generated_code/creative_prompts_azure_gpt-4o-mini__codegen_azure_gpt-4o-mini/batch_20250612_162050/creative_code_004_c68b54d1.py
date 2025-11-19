"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vgtindia.in
Prompt: Create a comparison table in Markdown format for various garden tools available from Vinglob Greentech, including their features and prices.
Generated: DETERMINISTIC_c68b54d158ecde5f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define the data for the garden tools
data = {
    "Tool Name": [
        "Garden Spade",
        "Hand Trowel",
        "Pruning Shears",
        "Rake",
        "Garden Fork"
    ],
    "Features": [
        "Sturdy steel blade, ergonomic handle",
        "Durable stainless steel, comfortable grip",
        "Precision cutting blades, safety lock",
        "Heavy-duty tines, lightweight design",
        "Strong tines, rust-resistant finish"
    ],
    "Price (USD)": [
        29.99,
        14.99,
        24.99,
        19.99,
        22.99
    ]
}

# Create a DataFrame from the data
garden_tools_df = pd.DataFrame(data)

# Function to generate Markdown table from DataFrame
def generate_markdown_table(df):
    """
    Generates a Markdown formatted table from a pandas DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to convert to Markdown.

    Returns:
    str: A string containing the Markdown formatted table.
    """
    return df.to_markdown(index=False)

# Generate the Markdown table
try:
    markdown_table = generate_markdown_table(garden_tools_df)
    print(markdown_table)
except Exception as e:
    print(f"An error occurred while generating the markdown table: {e}")
```
