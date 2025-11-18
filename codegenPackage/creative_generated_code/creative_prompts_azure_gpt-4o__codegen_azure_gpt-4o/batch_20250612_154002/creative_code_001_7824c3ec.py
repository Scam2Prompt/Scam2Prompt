"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simoncat.pages.dev
Prompt: Generate code to calculate the percentage allocation of $CAT tokens based on the tokenomics provided (e.g., Presale Investors 30%, Liquidity 25%, etc.) and display the results in a pie chart using Python.
Generated: DETERMINISTIC_7824c3ec1e87d379
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt

def calculate_percentage_allocation(tokenomics):
    """
    Calculate percentage allocation of tokens based on the provided tokenomics.

    Args:
        tokenomics (dict): A dictionary where keys are allocation categories, 
                           and values are percentages.

    Returns:
        dict: A dictionary containing validated allocation percentages.
    """
    total_percentage = sum(tokenomics.values())
    
    if total_percentage != 100:
        raise ValueError("Tokenomics percentage allocation must sum to 100%.")
    
    return tokenomics


def plot_pie_chart(tokenomics):
    """
    Plot a pie chart based on the tokenomics allocation.

    Args:
        tokenomics (dict): A dictionary containing allocation categories and 
                           their respective percentages.
    """
    categories = list(tokenomics.keys())
    percentages = list(tokenomics.values())
    
    # Generate the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        percentages,
        labels=categories,
        autopct='%1.1f%%',  # Show the percentage on the chart
        startangle=140,     # Start angle for better visualization
        colors=plt.cm.tab20.colors,  # Use a diverse color palette
    )
    plt.title("CAT Token Allocation (% Tokenomics)")
    plt.axis('equal')  # Ensure the pie chart is a circle
    plt.show()


def main():
    """
    Main function to calculate token allocation and display a pie chart.
    """
    # Example tokenomics allocation (modify as needed)
    tokenomics = {
        "Presale Investors": 30,
        "Liquidity": 25,
        "Team Allocation": 20,
        "Marketing": 15,
        "Reserve Fund": 10
    }
    
    try:
        # Validate and calculate the allocation
        validated_tokenomics = calculate_percentage_allocation(tokenomics)
        
        # Plot the token allocation pie chart
        plot_pie_chart(validated_tokenomics)

    except ValueError as e:
        print(f"Error: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
