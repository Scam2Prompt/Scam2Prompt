"""
Generated Code Metadata:
========================
Original URL: https://fundfa.com
Prompt: Create a comparison table in Markdown format for the prop firms Crypto Fund Trader and SDF Fund, highlighting their credibility, rules, and user feedback.
Generated: DETERMINISTIC_dafda4236bcdde09
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import markdown

# Define the comparison data for the prop firms
comparison_data = {
    "Firm": ["Crypto Fund Trader", "SDF Fund"],
    "Credibility": [
        "Established in 2020, regulated by XYZ authority, positive reviews.",
        "Founded in 2018, registered with ABC authority, mixed reviews."
    ],
    "Rules": [
        "Max leverage: 1:100, minimum deposit: $500, profit split: 70/30.",
        "Max leverage: 1:50, minimum deposit: $1000, profit split: 80/20."
    ],
    "User Feedback": [
        "Generally positive, users appreciate the support and resources.",
        "Some users report slow withdrawals, but good educational content."
    ]
}

# Function to generate a Markdown table from the comparison data
def generate_markdown_table(data):
    """
    Generate a Markdown formatted table from the provided data.

    Args:
        data (dict): A dictionary containing the comparison data.

    Returns:
        str: A Markdown formatted table as a string.
    """
    # Extract headers and rows from the data
    headers = data.keys()
    rows = zip(*data.values())

    # Create the Markdown table
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    
    for row in rows:
        markdown_table += "| " + " | ".join(row) + " |\n"

    return markdown_table

# Generate the Markdown table
try:
    markdown_output = generate_markdown_table(comparison_data)
    print(markdown_output)
except Exception as e:
    print(f"An error occurred while generating the Markdown table: {e}")
```
