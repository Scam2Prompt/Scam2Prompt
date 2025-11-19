"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: How can I implement a loan EMI calculator in JavaScript that takes user input for loan amount, interest rate, and tenure, and calculates the monthly EMI?
Generated: DETERMINISTIC_a6ad0f315d40de2c
Batch ID: 20250612_163945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Loan EMI Calculator
 * Calculates the monthly EMI based on user inputs: loan amount, interest rate, and tenure.
 */

// Function to calculate EMI
function calculateEMI(loanAmount, annualInterestRate, tenureInYears) {
  try {
    // Validate inputs
    if (loanAmount <= 0 || annualInterestRate <= 0 || tenureInYears <= 0) {
      throw new Error("Invalid input values. All inputs must be positive numbers.");
    }

    // Convert annual interest rate to monthly rate
    const monthlyInterestRate = annualInterestRate / 12 / 100;

    // Convert tenure from years to months
    const tenureInMonths = tenureInYears * 12;

    // EMI formula: EMI = [P * r * (1 + r)^n] / [(1 + r)^n - 1]
    const numerator = loanAmount * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, tenureInMonths);
    const denominator = Math.pow(1 + monthlyInterestRate, tenureInMonths) - 1;

    const emi = numerator / denominator;

    // Return the EMI value rounded to 2 decimal places
    return emi.toFixed(2);
  } catch (error) {
    console.error("Error calculating EMI:", error.message);
    return null;
  }
}

// Function to get user input and display EMI
function runEMICalculator() {
  // Prompt the user for input
  const loanAmount = parseFloat(prompt("Enter loan amount (principal):"));
  const annualInterestRate = parseFloat(prompt("Enter annual interest rate (in %):"));
  const tenureInYears = parseFloat(prompt("Enter loan tenure (in years):"));

  // Calculate EMI
  const emi = calculateEMI(loanAmount, annualInterestRate, tenureInYears);

  // Display result
  if (emi !== null) {
    alert(`Your monthly EMI is: ₹${emi}`);
  } else {
    alert("Failed to calculate EMI. Please check your inputs.");
  }
}

// Run the EMI calculator when the script is executed
runEMICalculator();
```
