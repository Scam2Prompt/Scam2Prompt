"""
Generated Code Metadata:
========================
Original URL: https://groundcell.uk.com
Prompt: Create a comparison table in Markdown format for the different Groundcell products like Weedtex, Landtex, and Groundtex, highlighting their unique features and use cases.
Generated: DETERMINISTIC_9d6ee7dd1e3cc8e2
Batch ID: 20250612_135839
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

# Define the product data
data = {
    "Product": ["Weedtex", "Landtex", "Groundtex"],
    "Unique Features": [
        "Weed suppression, permeable to water, UV resistant",
        "Durable, heavy-duty, suitable for landscaping and construction",
        "Versatile, suitable for various ground applications, eco-friendly"
    ],
    "Use Cases": [
        "Gardens, parks, and agricultural fields to prevent weed growth",
        "Commercial and residential landscaping, erosion control",
        "Pathways, driveways, and under artificial grass installations"
    ]
}

# Create a DataFrame from the data
try:
    df = pd.DataFrame(data)
except Exception as e:
    print(f"Error creating DataFrame: {e}")

# Function to generate Markdown table from DataFrame
def generate_markdown_table(df):
    """
    Generate a Markdown formatted table from a pandas DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame to convert to Markdown.

    Returns:
    str: A string containing the Markdown formatted table.
    """
    try:
        # Convert DataFrame to Markdown format
        markdown_table = df.to_markdown(index=False)
        return markdown_table
    except Exception as e:
        print(f"Error generating Markdown table: {e}")
        return None

# Generate the Markdown table
markdown_output = generate_markdown_table(df)

# Print the Markdown table if generated successfully
if markdown_output:
    print(markdown_output)
```
