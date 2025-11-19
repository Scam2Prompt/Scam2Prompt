"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Develop a simple HTML form that allows users to input their investment amount and select a plan from Apex Digital Limited, then calculates expected profits.
Generated: DETERMINISTIC_ff671943542bc1e8
Batch ID: 20250612_160124
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
  <title>Investment Profit Calculator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    form {
      max-width: 400px;
      margin: auto;
    }
    label {
      display: block;
      margin-bottom: 8px;
    }
    input, select, button {
      width: 100%;
      padding: 10px;
      margin-bottom: 16px;
    }
    button {
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
    .result {
      margin-top: 20px;
      font-size: 1.2em;
      color: #333;
    }
  </style>
</head>
<body>
  <h1>Investment Profit Calculator</h1>
  <p>Calculate your expected profits with Apex Digital Limited.</p>
  <form id="investmentForm">
    <!-- Input for investment amount -->
    <label for="investmentAmount">Investment Amount ($):</label>
    <input type="number" id="investmentAmount" name="investmentAmount" min="1" required>

    <!-- Dropdown to select investment plan -->
    <label for="investmentPlan">Select Plan:</label>
    <select id="investmentPlan" name="investmentPlan" required>
      <option value="" disabled selected>Select a plan</option>
      <option value="0.05">Starter Plan (5% profit)</option>
      <option value="0.10">Growth Plan (10% profit)</option>
      <option value="0.15">Premium Plan (15% profit)</option>
    </select>

    <!-- Calculate button -->
    <button type="submit">Calculate Profit</button>
  </form>

  <!-- Result display -->
  <div class="result" id="result"></div>

  <!-- JavaScript to handle form submission and profit calculation -->
  <script>
    // Error handling and profit calculation logic
    document.getElementById('investmentForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent form submission reload
      
      // Get user input values
      const investmentAmount = parseFloat(document.getElementById('investmentAmount').value);
      const investmentPlan = parseFloat(document.getElementById('investmentPlan').value);

      // Validate input
      if (isNaN(investmentAmount) || investmentAmount < 1) {
        alert('Please enter a valid investment amount greater than 0.');
        return;
      }

      if (isNaN(investmentPlan)) {
        alert('Please select a valid investment plan.');
        return;
      }

      // Calculate profit
      const profit = investmentAmount * investmentPlan;

      // Display result
      document.getElementById('result').textContent = `Your expected profit is $${profit.toFixed(2)}.`;
    });
  </script>
</body>
</html>
```
