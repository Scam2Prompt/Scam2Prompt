"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Create a simple investment calculator in JavaScript that allows users to input their investment amount and select a plan from Welforcevest Capital to see potential returns.
Generated: DETERMINISTIC_90cae9aaac40d21e
Batch ID: 20250612_160411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Investment Calculator for Welforcevest Capital

// Function to calculate potential returns
function calculateReturns(investmentAmount, plan) {
  // Plans and their respective annual return rates
  const plans = {
    "Basic": 0.05,   // 5% annual return
    "Premium": 0.10, // 10% annual return
    "Elite": 0.15    // 15% annual return
  };

  // Error handling: Validate plan selection
  if (!plans[plan]) {
    throw new Error("Invalid investment plan selected. Please choose 'Basic', 'Premium', or 'Elite'.");
  }

  // Error handling: Validate investment amount
  if (isNaN(investmentAmount) || investmentAmount <= 0) {
    throw new Error("Invalid investment amount. Please enter a positive number.");
  }

  // Calculate returns based on the selected plan
  const annualRate = plans[plan];
  const potentialReturns = investmentAmount * annualRate;

  return potentialReturns.toFixed(2); // Return formatted result
}

// Function to display the result
function displayResult() {
  try {
    // Get user inputs
    const investmentAmount = parseFloat(document.getElementById("investmentAmount").value);
    const plan = document.getElementById("investmentPlan").value;

    // Calculate returns
    const result = calculateReturns(investmentAmount, plan);

    // Display result to the user
    document.getElementById("result").innerText = `Potential annual returns: $${result}`;
  } catch (error) {
    // Handle errors and display appropriate messages
    document.getElementById("result").innerText = `Error: ${error.message}`;
  }
}

// Attach event listener to the "Calculate" button
document.getElementById("calculateButton").addEventListener("click", displayResult);

/* HTML & CSS (to be included in your project for full functionality)
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Investment Calculator</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 20px; }
    label, select, input, button { display: block; margin: 10px 0; }
    #result { margin-top: 20px; font-weight: bold; }
  </style>
</head>
<body>
  <h1>Welforcevest Capital Investment Calculator</h1>
  <label for="investmentAmount">Investment Amount ($):</label>
  <input type="number" id="investmentAmount" placeholder="Enter amount">

  <label for="investmentPlan">Select Investment Plan:</label>
  <select id="investmentPlan">
    <option value="Basic">Basic (5% Annual Return)</option>
    <option value="Premium">Premium (10% Annual Return)</option>
    <option value="Elite">Elite (15% Annual Return)</option>
  </select>

  <button id="calculateButton">Calculate Returns</button>

  <div id="result"></div>

  <script src="investment-calculator.js"></script>
</body>
</html>
*/
```
