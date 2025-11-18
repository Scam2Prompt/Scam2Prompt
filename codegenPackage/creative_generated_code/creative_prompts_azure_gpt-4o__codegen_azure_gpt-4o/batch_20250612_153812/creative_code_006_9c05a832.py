"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspet.web.app
Prompt: Write a Python script to analyze the token supply data of $Cheems, including burned tokens and current supply, and generate visualizations using Matplotlib.
Generated: DETERMINISTIC_9c05a832a92ae3c6
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import logging

# Set up logging to handle errors and provide useful information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_token_supply(token_data):
    """
    Analyzes the token supply data and generates visualizations.

    Args:
        token_data (dict): Dictionary containing token supply information with the following structure:
                           {
                               "total_supply": int,  # Total issued tokens
                               "burned_tokens": int, # Tokens that have been burned
                               "current_supply": int # Tokens in circulation
                           }

    Returns:
        None
    """
    try:
        # Extract relevant data
        total_supply = token_data.get("total_supply", 0)
        burned_tokens = token_data.get("burned_tokens", 0)
        current_supply = token_data.get("current_supply", 0)

        if total_supply != burned_tokens + current_supply:
            logging.warning("Total supply does not match burned tokens + current supply. Check data consistency.")

        # Data for visualization
        labels = ['Burned Tokens', 'Current Supply']
        values = [burned_tokens, current_supply]

        # Create a pie chart to visualize token distribution
        plt.figure(figsize=(8, 6))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=['red', 'green'])
        plt.title('$Cheems Token Supply Distribution')
        plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.

        # Save visualization to a file
        plt.savefig('cheems_token_supply_distribution.png')
        logging.info("Token supply distribution visualization saved as 'cheems_token_supply_distribution.png'.")
        plt.show()

        # Create a bar chart for better comparison
        plt.figure(figsize=(8, 6))
        plt.bar(labels, values, color=['red', 'green'])
        plt.title('$Cheems Token Supply Analysis')
        plt.xlabel('Token Status')
        plt.ylabel('Number of Tokens')
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Save visualization to a file
        plt.savefig('cheems_token_supply_analysis.png')
        logging.info("Token supply analysis visualization saved as 'cheems_token_supply_analysis.png'.")
        plt.show()

    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")

# Example token data (replace with actual data)
token_data = {
    "total_supply": 1000000,
    "burned_tokens": 200000,
    "current_supply": 800000
}

# Perform the analysis and generate visualizations
analyze_token_supply(token_data)
```
