"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ultimateexperttrade24.com
Prompt: Create a dashboard using JavaScript or Python to visualize daily returns and referral bonuses for the investment plans listed on Ultimateexperttrade24.com.
Generated: DETERMINISTIC_df4fd08a614c17bd
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Sample data simulation (In a real-world scenario, replace it with API calls or database queries)
def fetch_investment_data():
    """
    Fetch investment data for daily returns and referral bonuses.
    Replace this with the actual data source in production.
    """
    data = {
        "date": pd.date_range(start="2023-01-01", periods=10, freq="D"),  # Example dates
        "plan_name": ["Plan A", "Plan B", "Plan C", "Plan A", "Plan B", "Plan C", "Plan A", "Plan B", "Plan C", "Plan A"],
        "daily_return": [20, 15, 25, 30, 10, 18, 22, 16, 28, 35],  # Example daily returns
        "referral_bonus": [5, 3, 8, 4, 2, 6, 7, 3, 9, 4]  # Example referral bonuses
    }
    return pd.DataFrame(data)

# Visualization function
def generate_visualizations(dataframe):
    """
    Generate visualizations for daily returns and referral bonuses.
    """
    # Set up the style using seaborn
    sns.set_theme(style="darkgrid")

    # Daily Returns Visualization
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=dataframe, x="date", y="daily_return", hue="plan_name", marker="o")
    plt.title("Daily Returns for Investment Plans")
    plt.xlabel("Date")
    plt.ylabel("Daily Return ($)")
    plt.legend(title="Plan Name")
    plt.tight_layout()
    plt.savefig("static/daily_returns.png")  # Save the plot to a file
    plt.close()

    # Referral Bonuses Visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(data=dataframe, x="date", y="referral_bonus", hue="plan_name")
    plt.title("Referral Bonuses for Investment Plans")
    plt.xlabel("Date")
    plt.ylabel("Referral Bonus ($)")
    plt.legend(title="Plan Name")
    plt.tight_layout()
    plt.savefig("static/referral_bonuses.png")  # Save the plot to a file
    plt.close()

# Route for the dashboard
@app.route("/")
def dashboard():
    """
    Render the investment dashboard.
    """
    try:
        # Fetch data
        data = fetch_investment_data()

        # Generate visualizations
        generate_visualizations(data)

        # Render the HTML template
        return render_template("dashboard.html")
    except Exception as e:
        # Handle any errors gracefully
        return f"An error occurred: {str(e)}"

# HTML Template for the dashboard (Save this as 'templates/dashboard.html')
"""
<!DOCTYPE html>
<html>
<head>
    <title>Investment Dashboard</title>
</head>
<body>
    <h1>Investment Dashboard</h1>
    <h2>Daily Returns</h2>
    <img src="/static/daily_returns.png" alt="Daily Returns">
    <h2>Referral Bonuses</h2>
    <img src="/static/referral_bonuses.png" alt="Referral Bonuses">
</body>
</html>
"""

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
1. Save the HTML template as `templates/dashboard.html` in the project directory.
2. Ensure you have the Flask, pandas, matplotlib, and seaborn libraries installed (`pip install flask pandas matplotlib seaborn`).
3. Replace the data simulation function with actual data from the UltimateExpertTrade24.com service.
