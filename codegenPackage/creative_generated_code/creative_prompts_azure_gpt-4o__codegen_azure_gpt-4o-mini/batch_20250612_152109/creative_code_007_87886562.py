"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextools-io-app.pages.dev
Prompt: Generate code to simulate SPONGE token trades using DEXTools' Extra Simulator feature and display the results in a web app.
Generated: DETERMINISTIC_87886562e945fdac
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import random
import json

# Initialize Flask application
app = Flask(__name__)

# Sample SPONGE token trade simulation data
class TradeSimulator:
    def __init__(self):
        self.price = 1.0  # Starting price of SPONGE token
        self.trade_history = []

    def simulate_trade(self, trade_amount):
        # Simulate a random price change
        price_change = random.uniform(-0.1, 0.1)  # Random price fluctuation
        self.price += price_change
        
        # Ensure price does not drop below zero
        if self.price < 0:
            self.price = 0
        
        # Record the trade
        trade_record = {
            'trade_amount': trade_amount,
            'trade_price': self.price,
            'total_cost': trade_amount * self.price,
            'trade_time': self.get_current_time()
        }
        self.trade_history.append(trade_record)
        
        return trade_record

    @staticmethod
    def get_current_time():
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Instantiate TradeSimulator
simulator = TradeSimulator()

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for simulating trades
@app.route('/simulate_trade', methods=['POST'])
def simulate_trade():
    try:
        trade_amount = request.json.get('trade_amount', 0)
        
        if trade_amount <= 0:
            return jsonify({'error': 'Invalid trade amount'}), 400
        
        trade_record = simulator.simulate_trade(trade_amount)
        return jsonify({'trade_record': trade_record}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

# HTML Template (index.html)
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SPONGE Token Trade Simulator</title>
</head>
<body>
    <h1>SPONGE Token Trade Simulator</h1>
    <input type="number" id="tradeAmount" placeholder="Trade Amount" />
    <button onclick="simulateTrade()">Simulate Trade</button>
    <div id="result"></div>

    <script>
        async function simulateTrade() {
            const tradeAmount = document.getElementById('tradeAmount').value;
            const response = await fetch('/simulate_trade', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ trade_amount: parseFloat(tradeAmount) })
            });

            const resultDiv = document.getElementById('result');
            if (response.ok) {
                const data = await response.json();
                resultDiv.innerHTML = `Trade Successful: ${JSON.stringify(data.trade_record)}`;
            } else {
                const errorData = await response.json();
                resultDiv.innerHTML = `Error: ${errorData.error}`;
            }
        }
    </script>
</body>
</html>
'''
```

This code provides a minimal Flask web application that simulates SPONGE token trades with appropriate error handling and user interaction through a simple HTML interface.
