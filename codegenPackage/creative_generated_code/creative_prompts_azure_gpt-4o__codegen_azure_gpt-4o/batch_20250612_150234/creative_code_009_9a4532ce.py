"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourmemebot.com
Prompt: Generate a comparison chart of Joxi Plus features versus free Joxi features using Python.
Generated: DETERMINISTIC_9a4532cef9be1832
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

def generate_comparison_chart():
    """
    Generates a comparison chart for Joxi Plus features vs Free Joxi features.
    The chart will be saved as an HTML file and displayed as a dataframe.
    """

    try:
        # Define the features and their availability in each plan
        features = [
            "Unlimited cloud storage",
            "No ads",
            "Screenshot annotation tools",
            "Custom hotkeys",
            "Priority support",
            "Team collaboration tools",
            "Full HD video recording",
            "Offline mode"
        ]

        joxi_plus = [
            "Available",
            "Available",
            "Available",
            "Available",
            "Available",
            "Available",
            "Available",
            "Available"
        ]

        joxi_free = [
            "Not available",
            "Not available",
            "Available",
            "Available",
            "Not available",
            "Not available",
            "Available",
            "Not available"
        ]

        # Create a DataFrame for the comparison chart
        data = {
            "Features": features,
            "Joxi Plus": joxi_plus,
            "Joxi Free": joxi_free
        }

        df = pd.DataFrame(data)

        # Save the chart as an HTML file
        output_file = "joxi_comparison_chart.html"
        df.to_html(output_file, index=False)
        print(f"Comparison chart saved as '{output_file}'.")

        # Display the chart
        print("\nComparison Chart:")
        print(df)

    except Exception as e:
        print(f"An error occurred while generating the comparison chart: {e}")

# Main execution
if __name__ == "__main__":
    generate_comparison_chart()
```
