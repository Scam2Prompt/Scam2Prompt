"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binance-stake.vercel.app
Prompt: Create a web-based APR calculator using HTML, CSS, and JavaScript that mimics the functionality of the Binance Stake APR Calculator.
Generated: DETERMINISTIC_7403be6aee0007a5
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>APR Calculator</title>
  <style>
    /* Basic styling for the calculator */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #f4f4f4;
    }

    .calculator-container {
      background-color: #fff;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      width: 300px;
      text-align: center;
    }

    h1 {
      font-size: 22px;
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 15px;
    }

    label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }

    input[type="number"] {
      width: 100%;
      padding: 8px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 4px;
      cursor: pointer;
      font-size: 16px;
    }

    button:hover {
      background-color: #0056b3;
    }

    .result {
      margin-top: 20px;
      font-size: 18px;
      font-weight: bold;
      color: #333;
    }
  </style>
</head>
<body>
  <div class="calculator-container">
    <h1>APR Calculator</h1>
    <form id="aprForm">
      <div class="form-group">
        <label for="principal">Principal Amount ($):</label>
        <input type="number" id="principal" name="principal" required min="0" step="0.01">
      </div>
      <div class="form-group">
        <label for="apr">Annual APR (%):</label>
        <input type="number" id="apr" name="apr" required min="0" step="0.01">
      </div>
      <div class="form-group">
        <label for="days">Staking Duration (Days):</label>
        <input type="number" id="days" name="days" required min="1">
      </div>
      <button type="button" id="calculate-btn">Calculate</button>
    </form>
    <div class="result" id="result"></div>
  </div>

  <script>
    // Helper function to format numbers to two decimal places
    function formatNumber(value) {
      return parseFloat(value).toFixed(2);
    }

    // Event listener for the Calculate button
    document.getElementById('calculate-btn').addEventListener('click', function () {
      try {
        // Get input values
        const principal = parseFloat(document.getElementById('principal').value);
        const apr = parseFloat(document.getElementById('apr').value);
        const days = parseInt(document.getElementById('days').value);

        // Validate inputs
        if (isNaN(principal) || isNaN(apr) || isNaN(days) || principal <= 0 || apr <= 0 || days <= 0) {
          throw new Error('Please enter valid and positive values for all fields.');
        }

        // Calculate staking rewards
        const dailyRate = apr / 100 / 365; // Convert APR to daily rate
        const rewards = principal * dailyRate * days;

        // Display the result
        document.getElementById('result').textContent = `Estimated Rewards: $${formatNumber(rewards)}`;
      } catch (error) {
        // Handle errors and display them to the user
        document.getElementById('result').textContent = `Error: ${error.message}`;
      }
    });
  </script>
</body>
</html>
```
