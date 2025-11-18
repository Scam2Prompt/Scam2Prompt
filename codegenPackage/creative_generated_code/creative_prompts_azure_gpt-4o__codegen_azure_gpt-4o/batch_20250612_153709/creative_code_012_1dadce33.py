"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueswhale.pages.dev
Prompt: Build a system to extract and visualize AI-powered wallet insights for enterprises seeking targeted outreach.
Generated: DETERMINISTIC_1dadce33f9b41d82
Batch ID: 20250612_153709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import os
import logging

# Initialize the Flask app
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dummy data for demonstration purposes
wallet_data = {
    "Company": ["Enterprise A", "Enterprise B", "Enterprise C"],
    "MonthlyRevenue": [50000, 120000, 75000],
    "SpendingCategory": ["Tech", "Marketing", "Operations"],
    "AIEngagementScore": [87, 92, 78]
}

# Convert the dummy data into a DataFrame
wallet_df = pd.DataFrame(wallet_data)

@app.route('/get_wallet_insights', methods=['GET'])
def get_wallet_insights():
    """
    Endpoint to retrieve wallet insights in JSON format.
    """
    try:
        # Convert the DataFrame to JSON
        insights_json = wallet_df.to_dict(orient="records")
        logging.info("Wallet insights successfully retrieved.")
        return jsonify(insights_json)
    except Exception as e:
        logging.error(f"Error retrieving wallet insights: {e}")
        return jsonify({"error": "Failed to retrieve wallet insights"}), 500

@app.route('/visualize_wallet_insights', methods=['GET'])
def visualize_wallet_insights():
    """
    Endpoint to visualize wallet insights.
    This generates a bar chart and saves it as a static image.
    """
    try:
        # Generate a bar chart for Monthly Revenue
        plt.figure(figsize=(10, 6))
        plt.bar(wallet_df["Company"], wallet_df["MonthlyRevenue"], color='skyblue')
        plt.title("Monthly Revenue by Company")
        plt.xlabel("Company")
        plt.ylabel("Revenue ($)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Save the plot as an image
        chart_path = "static/revenue_chart.png"
        os.makedirs("static", exist_ok=True)
        plt.savefig(chart_path)
        plt.close()
        
        logging.info("Wallet insights visualization generated successfully.")
        return jsonify({"message": "Visualization generated", "chart_path": chart_path})
    except Exception as e:
        logging.error(f"Error visualizing wallet insights: {e}")
        return jsonify({"error": "Failed to visualize wallet insights"}), 500

@app.route('/add_wallet_data', methods=['POST'])
def add_wallet_data():
    """
    Endpoint to add new wallet data via POST request.
    Expected JSON format:
    {
        "Company": "Enterprise D",
        "MonthlyRevenue": 95000,
        "SpendingCategory": "R&D",
        "AIEngagementScore": 85
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input data"}), 400
        
        # Validate required fields
        required_fields = ["Company", "MonthlyRevenue", "SpendingCategory", "AIEngagementScore"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Append new data to the DataFrame
        global wallet_df
        wallet_df = wallet_df.append(data, ignore_index=True)
        logging.info(f"New wallet data added successfully: {data}")
        return jsonify({"message": "Wallet data added successfully"}), 201
    except Exception as e:
        logging.error(f"Error adding wallet data: {e}")
        return jsonify({"error": "Failed to add wallet data"}), 500

# Entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
