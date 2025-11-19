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
import os

def generate_markdown_table(file_name, tools):
    """
    Generates a Markdown table for garden tools and saves it to the specified file.

    Args:
        file_name (str): The name of the output Markdown file.
        tools (list of dict): A list where each dictionary represents a garden tool with its features and price.

    Example content of "tools":
        [
            {"Name": "Garden Rake", "Features": "Lightweight, Durable", "Price": "$20"},
            {"Name": "Pruning Shears", "Features": "Sharp Blades, Ergonomic Handle", "Price": "$15"},
        ]
    """
    try:
        # Validate input
        if not tools or not isinstance(tools, list):
            raise ValueError("Tools must be a non-empty list of dictionaries.")

        # Markdown table header
        header = "| Name          | Features                  | Price |\n"
        separator = "|---------------|---------------------------|-------|\n"

        # Markdown table rows
        rows = [
            f"| {tool['Name']} | {tool['Features']} | {tool['Price']} |\n"
            for tool in tools
            if "Name" in tool and "Features" in tool and "Price" in tool
        ]

        # Combine all parts
        markdown_content = header + separator + "".join(rows)

        # Write to file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(markdown_content)

        print(f"Markdown table successfully written to '{file_name}'.")

    except Exception as e:
        print(f"An error occurred while generating the Markdown table: {e}")


# Example usage
if __name__ == "__main__":
    # Define garden tools data
    garden_tools = [
        {"Name": "Garden Rake", "Features": "Lightweight, Durable", "Price": "$20"},
        {"Name": "Pruning Shears", "Features": "Sharp Blades, Ergonomic Handle", "Price": "$15"},
        {"Name": "Hose Reel", "Features": "Expandable, Anti-Twist", "Price": "$25"},
        {"Name": "Wheelbarrow", "Features": "Heavy-Duty, Rust Resistant", "Price": "$50"},
    ]

    # Output Markdown file
    output_file = "garden_tools_table.md"

    # Generate and save the Markdown table
    generate_markdown_table(output_file, garden_tools)
```

This code creates a Markdown table based on the provided list of garden tools and their features, and saves it to a file. Ensure the `garden_tools` variable is populated with the appropriate data before running the script.
