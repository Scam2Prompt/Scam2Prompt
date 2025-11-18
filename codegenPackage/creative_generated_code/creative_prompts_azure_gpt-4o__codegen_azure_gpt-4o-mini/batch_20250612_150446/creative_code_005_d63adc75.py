"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eunitedcryptofx.com
Prompt: Create a web application feature that allows users to view live investment and withdrawal data, similar to the "Latest Investors and Withdraws" section on eunitedcryptofx.com.
Generated: DETERMINISTIC_d63adc758c73b9d1
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify
import random
import threading
import time

app = Flask(__name__)

# Sample data to simulate live investment and withdrawal information
investments = []
withdrawals = []

# Function to generate sample data for investments and withdrawals
def generate_sample_data():
    while True:
        # Simulating an investment
        investment = {
            'user': f'User{random.randint(1, 100)}',
            'amount': round(random.uniform(10, 1000), 2),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        investments.append(investment)

        # Simulating a withdrawal
        withdrawal = {
            'user': f'User{random.randint(1, 100)}',
            'amount': round(random.uniform(10, 500), 2),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        }
        withdrawals.append(withdrawal)

        # Keep the sample data fresh by limiting the number of records
        if len(investments) > 10:
            investments.pop(0)
        if len(withdrawals) > 10:
            withdrawals.pop(0)

        time.sleep(5)  # Generate new data every 5 seconds

# Start the sample data generation in a separate thread
threading.Thread(target=generate_sample_data, daemon=True).start()

@app.route('/')
def index():
    """
    Render the main page to display live investment and withdrawal data.
    """
    return render_template('index.html')

@app.route('/api/investments', methods=['GET'])
def get_investments():
    """
    API endpoint to retrieve the latest investments.
    """
    try:
        return jsonify(investments), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/withdrawals', methods=['GET'])
def get_withdrawals():
    """
    API endpoint to retrieve the latest withdrawals.
    """
    try:
        return jsonify(withdrawals), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application on the default Flask port 5000
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Investment and Withdrawal Data</title>
    <script>
        // Function to fetch investments and withdrawals data and update the page
        async function fetchData() {
            try {
                const investmentsResponse = await fetch('/api/investments');
                const investmentsData = await investmentsResponse.json();

                const withdrawalsResponse = await fetch('/api/withdrawals');
                const withdrawalsData = await withdrawalsResponse.json();

                // Update the display with the latest investments and withdrawals
                document.getElementById('investments').innerHTML = JSON.stringify(investmentsData, null, 2);
                document.getElementById('withdrawals').innerHTML = JSON.stringify(withdrawalsData, null, 2);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        }

        // Fetch data every 5 seconds
        setInterval(fetchData, 5000);
        window.onload = fetchData; // Initial fetch on page load
    </script>
</head>
<body>
    <h1>Latest Investments</h1>
    <pre id="investments"></pre>

    <h1>Latest Withdrawals</h1>
    <pre id="withdrawals"></pre>
</body>
</html>
```
