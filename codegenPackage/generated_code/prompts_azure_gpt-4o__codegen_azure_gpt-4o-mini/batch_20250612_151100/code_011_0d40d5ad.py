"""
Generated Code Metadata:
========================
Original URL: https://thehuskyinu-io.pages.dev
Prompt: Write code to display $HINU token allocation percentages (e.g., marketing, liquidity pool) in a visually appealing dashboard using JavaScript or Python.
Generated: DETERMINISTIC_0d40d5adbcddb2da
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import matplotlib.pyplot as plt

# Define the token allocation data
token_allocation = {
    'Marketing': 25,
    'Liquidity Pool': 30,
    'Development': 20,
    'Community Rewards': 15,
    'Reserve Fund': 10
}

def create_pie_chart(allocation_data):
    """
    Create a pie chart to display token allocation percentages.

    Parameters:
    allocation_data (dict): A dictionary containing allocation categories and their percentages.
    """
    try:
        # Extract labels and sizes from the allocation data
        labels = allocation_data.keys()
        sizes = allocation_data.values()

        # Create a pie chart
        plt.figure(figsize=(8, 8))
        wedges, texts, autotexts = plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.Paired.colors
        )

        # Beautify the chart
        plt.setp(autotexts, size=10, weight="bold", color="white")
        plt.setp(texts, size=12)
        plt.title('HINU Token Allocation Percentages', fontsize=16)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Show the pie chart
        plt.show()

    except Exception as e:
        print(f"An error occurred while creating the pie chart: {e}")

# Main function to execute the code
if __name__ == "__main__":
    create_pie_chart(token_allocation)
```

Make sure to have `matplotlib` installed in your Python environment. You can install it using pip:

```bash
pip install matplotlib
```
