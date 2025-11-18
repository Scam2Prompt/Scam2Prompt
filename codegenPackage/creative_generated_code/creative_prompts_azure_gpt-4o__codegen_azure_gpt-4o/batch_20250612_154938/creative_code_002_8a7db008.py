"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Generate code in JavaScript to create an interactive loan calculator for Maya Finance, allowing users to input loan type, amount, and repayment duration to calculate monthly payments.
Generated: DETERMINISTIC_8a7db00894f31a46
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Loan Calculator for Maya Finance
// Author: Maya Finance Development Team
// Description: Interactive loan calculator to compute monthly payments

// HTML structure for the calculator
document.body.innerHTML = `
  <div id="loan-calculator">
    <h1>Maya Finance Loan Calculator</h1>
    <form id="calculator-form">
      <label for="loan-type">Loan Type:</label>
      <select id="loan-type" required>
        <option value="personal">Personal Loan</option>
        <option value="auto">Auto Loan</option>
        <option value="mortgage">Mortgage</option>
      </select>
      <label for="loan-amount">Loan Amount ($):</label>
      <input type="number" id="loan-amount" min="0" required />
      <label for="loan-duration">Repayment Duration (years):</label>
      <input type="number" id="loan-duration" min="1" required />
      <button type="submit">Calculate</button>
    </form>
    <div id="result" style="margin-top: 20px;"></div>
  </div>
`;

// Style the calculator (Basic inline CSS for aesthetics)
document.body.style.fontFamily = "Arial, sans-serif";
document.getElementById("loan-calculator").style.maxWidth = "400px";
document.getElementById("loan-calculator").style.margin = "auto";
document.getElementById("loan-calculator").style.padding = "20px";
document.getElementById("loan-calculator").style.border = "1px solid #ddd";
document.getElementById("loan-calculator").style.borderRadius = "8px";
document.getElementById("loan-calculator").style.boxShadow = "0 4px 8px rgba(0,0,0,0.1)";

// Function to calculate monthly payment
function calculateMonthlyPayment(loanAmount, annualRate, years) {
  try {
    // Convert annual interest rate to monthly and calculate payments
    const monthlyRate = annualRate / 12 / 100;
    const totalMonths = years * 12;

    if (monthlyRate === 0) {
      // No interest case
      return loanAmount / totalMonths;
    }

    // Standard loan formula
    const monthlyPayment = 
      (loanAmount * monthlyRate) /
      (1 - Math.pow(1 + monthlyRate, -totalMonths));
    return monthlyPayment;
  } catch (error) {
    console.error("Error in calculating monthly payment:", error.message);
    throw new Error("Unable to calculate monthly payment. Please try again.");
  }
}

// Interest rates for different loan types
const interestRates = {
  personal: 5.5, // 5.5% annual interest rate
  auto: 3.2,     // 3.2% annual interest rate
  mortgage: 4.0, // 4.0% annual interest rate
};

// Handle form submission
document.getElementById("calculator-form").addEventListener("submit", function (event) {
  event.preventDefault(); // Prevent form from reloading the page

  // Fetch input values
  const loanType = document.getElementById("loan-type").value;
  const loanAmount = parseFloat(document.getElementById("loan-amount").value);
  const loanDuration = parseInt(document.getElementById("loan-duration").value, 10);

  // Validate inputs
  if (isNaN(loanAmount) || loanAmount <= 0) {
    alert("Please enter a valid loan amount.");
    return;
  }

  if (isNaN(loanDuration) || loanDuration <= 0) {
    alert("Please enter a valid repayment duration in years.");
    return;
  }

  // Get the interest rate for the selected loan type
  const annualRate = interestRates[loanType];

  if (!annualRate) {
    alert("Invalid loan type selected.");
    return;
  }

  try {
    // Calculate the monthly payment
    const monthlyPayment = calculateMonthlyPayment(loanAmount, annualRate, loanDuration);
    const formattedPayment = monthlyPayment.toFixed(2);

    // Display the result
    document.getElementById("result").innerHTML = `
      <h2>Calculation Result</h2>
      <p>Loan Type: ${loanType.charAt(0).toUpperCase() + loanType.slice(1)}</p>
      <p>Loan Amount: $${loanAmount.toFixed(2)}</p>
      <p>Repayment Duration: ${loanDuration} years</p>
      <p><strong>Monthly Payment: $${formattedPayment}</strong></p>
    `;
  } catch (error) {
    // Handle any unexpected errors
    document.getElementById("result").innerHTML = `
      <p style="color: red;">Error: ${error.message}</p>
    `;
  }
});
```
