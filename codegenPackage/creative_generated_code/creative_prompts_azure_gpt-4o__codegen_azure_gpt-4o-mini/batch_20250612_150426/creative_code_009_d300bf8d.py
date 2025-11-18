"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Develop a JavaScript-based profit calculator for Steadfast Asset Innovation's investment plans, allowing users to select a plan and input their investment amount to calculate returns.
Generated: DETERMINISTIC_d300bf8d84c9c3fb
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Profit Calculator for Steadfast Asset Innovation's Investment Plans

// Investment plans with respective return rates (in percentage)
const investmentPlans = {
    "Basic Plan": 5,      // 5% return
    "Standard Plan": 10,  // 10% return
    "Premium Plan": 15,   // 15% return
};

// Function to calculate profit based on selected plan and investment amount
function calculateProfit(plan, investmentAmount) {
    // Validate input parameters
    if (!investmentPlans[plan]) {
        throw new Error("Invalid investment plan selected.");
    }
    if (isNaN(investmentAmount) || investmentAmount <= 0) {
        throw new Error("Investment amount must be a positive number.");
    }

    // Calculate profit
    const rate = investmentPlans[plan] / 100;
    const profit = investmentAmount * rate;

    // Return the calculated profit
    return profit;
}

// Function to handle user input and show results
function handleCalculation() {
    // Get selected plan and investment amount from user input
    const selectedPlan = document.getElementById("investmentPlan").value;
    const investmentAmount = parseFloat(document.getElementById("investmentAmount").value);

    try {
        // Calculate profit
        const profit = calculateProfit(selectedPlan, investmentAmount);
        
        // Display the result
        document.getElementById("result").textContent = `Estimated Profit: $${profit.toFixed(2)}`;
    } catch (error) {
        // Display error message
        document.getElementById("result").textContent = `Error: ${error.message}`;
    }
}

// HTML setup for user input
document.body.innerHTML = `
    <div>
        <h1>Investment Profit Calculator</h1>
        <label for="investmentPlan">Select Investment Plan:</label>
        <select id="investmentPlan">
            <option value="Basic Plan">Basic Plan</option>
            <option value="Standard Plan">Standard Plan</option>
            <option value="Premium Plan">Premium Plan</option>
        </select>
        <br /><br />
        <label for="investmentAmount">Enter Investment Amount ($):</label>
        <input type="number" id="investmentAmount" min="1" />
        <br /><br />
        <button onclick="handleCalculation()">Calculate Profit</button>
        <p id="result"></p>
    </div>
`;
```
