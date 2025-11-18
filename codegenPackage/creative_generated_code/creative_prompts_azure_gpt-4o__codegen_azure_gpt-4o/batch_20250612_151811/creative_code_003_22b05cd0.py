"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Develop code to visualize real estate market trends in major metropolitan areas, referencing the expertise of Carolina Capital in the Southeast.
Generated: DETERMINISTIC_22b05cd0e53f73f2
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mock data to represent real estate market trends for major metropolitan areas
data = {
    "City": ["Atlanta", "Charlotte", "Raleigh", "Charleston", "Nashville"],
    "MedianHomePrice": [350000, 320000, 310000, 300000, 400000],
    "YearlyPriceChange(%)": [8.5, 7.2, 6.8, 7.0, 9.1],
    "InventoryChange(%)": [-5.3, -4.8, -4.5, -5.0, -6.0],
    "AverageDaysOnMarket": [45, 50, 48, 55, 40]
}

# Function to visualize real estate market trends
def visualize_real_estate_trends(data):
    """
    Visualizes real estate market trends in major metropolitan areas.
    
    Parameters:
        data (dict): Dictionary containing market data for major cities.
    """
    try:
        # Load data into DataFrame
        df = pd.DataFrame(data)
        
        # Ensure data is loaded correctly
        if df.empty:
            raise ValueError("Data is empty. Please provide valid market data.")
        
        # Set Seaborn style for better visuals
        sns.set_theme(style="whitegrid")
        
        # Plot Median Home Prices
        plt.figure(figsize=(10, 6))
        sns.barplot(x="City", y="MedianHomePrice", data=df, palette="muted")
        plt.title("Median Home Prices in Major Metropolitan Areas", fontsize=16)
        plt.xlabel("City", fontsize=12)
        plt.ylabel("Median Home Price (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # Plot Yearly Price Change %
        plt.figure(figsize=(10, 6))
        sns.barplot(x="City", y="YearlyPriceChange(%)", data=df, palette="coolwarm")
        plt.title("Yearly Price Change (%) in Major Metropolitan Areas", fontsize=16)
        plt.xlabel("City", fontsize=12)
        plt.ylabel("Yearly Price Change (%)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # Plot Inventory Change %
        plt.figure(figsize=(10, 6))
        sns.barplot(x="City", y="InventoryChange(%)", data=df, palette="viridis")
        plt.title("Inventory Change (%) in Major Metropolitan Areas", fontsize=16)
        plt.xlabel("City", fontsize=12)
        plt.ylabel("Inventory Change (%)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        # Plot Average Days on Market
        plt.figure(figsize=(10, 6))
        sns.barplot(x="City", y="AverageDaysOnMarket", data=df, palette="mako")
        plt.title("Average Days on Market in Major Metropolitan Areas", fontsize=16)
        plt.xlabel("City", fontsize=12)
        plt.ylabel("Average Days on Market", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    except Exception as error:
        # Log error and display user-friendly message
        print(f"Error visualizing trends: {error}")

# Call the function to generate the plots
visualize_real_estate_trends(data)
```
