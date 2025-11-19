"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: How can I implement a loan EMI calculator in JavaScript that takes user input for loan amount, interest rate, and tenure, and calculates the monthly EMI?
Generated: DETERMINISTIC_a6ad0f315d40de2c
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Loan EMI Calculator
 * This script calculates the monthly EMI (Equated Monthly Installment) for a loan
 * based on user input for loan amount, annual interest rate, and loan tenure in years.
 */

// Function to calculate EMI
function calculateEMI(loanAmount, annualInterestRate, tenureYears) {
  try {
    // Validate inputs
    if (loanAmount <= 0 || annualInterestRate <= 0 || tenureYears <= 0) {
      throw new Error("All inputs must be positive numbers.");
    }

    // Convert annual interest rate to monthly interest rate (in decimal)
    const monthlyInterestRate = annualInterestRate / (12 * 100);

    // Convert tenure from years to months
    const tenureMonths = tenureYears * 12;

    // EMI formula: EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
    const emi =
      (loanAmount * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, tenureMonths)) /
      (Math.pow(1 + monthlyInterestRate, tenureMonths) - 1);

    // Return the calculated EMI rounded to two decimal places
    return emi.toFixed(2);
  } catch (error) {
    // Handle errors gracefully
    console.error("Error calculating EMI:", error.message);
    return null;
  }
}

// Function to get user input and display the EMI
function getUserInputAndCalculateEMI() {
  // Prompt user for loan amount, interest rate, and tenure
  const loanAmount = parseFloat(prompt("Enter loan amount (e.g., 500000):"));
  const annualInterestRate = parseFloat(prompt("Enter annual interest rate (e.g., 7.5):"));
  const tenureYears = parseInt(prompt("Enter loan tenure in years (e.g., 5):"), 10);

  // Calculate EMI
  const emi = calculateEMI(loanAmount, annualInterestRate, tenureYears);

  // Display the result
  if (emi !== null) {
    alert(`Your monthly EMI is: ₹${emi}`);
  } else {
    alert("Failed to calculate EMI. Please check your inputs.");
  }
}

// Run the EMI calculator
getUserInputAndCalculateEMI();
```
