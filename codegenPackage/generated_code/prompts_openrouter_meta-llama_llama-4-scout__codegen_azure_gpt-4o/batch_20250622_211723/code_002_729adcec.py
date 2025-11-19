"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Generate code for a mortgage calculator that can be integrated into a website, using the mortgage information and services offered by Genesis Investment Credit Union as a reference.
Generated: DETERMINISTIC_729adcec405a89f4
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Mortgage Calculator Script
// This script calculates monthly mortgage payments based on user input.
// It is designed to be integrated into a website and uses best practices for JavaScript development.

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // Function to calculate monthly mortgage payment
  function calculateMortgage(principal, annualInterestRate, years) {
    try {
      // Validate input
      if (principal <= 0 || annualInterestRate <= 0 || years <= 0) {
        throw new Error("All input values must be positive numbers.");
      }

      // Convert annual interest rate to monthly interest rate
      const monthlyInterestRate = annualInterestRate / 100 / 12;

      // Total number of payments (months)
      const totalPayments = years * 12;

      // Calculate monthly payment using the formula:
      // M = P[r(1+r)^n] / [(1+r)^n - 1]
      const numerator = principal * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, totalPayments);
      const denominator = Math.pow(1 + monthlyInterestRate, totalPayments) - 1;
      const monthlyPayment = numerator / denominator;

      // Return the monthly payment rounded to two decimal places
      return monthlyPayment.toFixed(2);
    } catch (error) {
      console.error("Error calculating mortgage:", error.message);
      return null;
    }
  }

  // Function to handle form submission
  function handleFormSubmit(event) {
    event.preventDefault(); // Prevent default form submission behavior

    // Get user input from the form
    const principal = parseFloat(document.getElementById("principal").value);
    const annualInterestRate = parseFloat(document.getElementById("annualInterestRate").value);
    const years = parseInt(document.getElementById("years").value, 10);

    // Calculate the monthly payment
    const monthlyPayment = calculateMortgage(principal, annualInterestRate, years);

    // Display the result to the user
    const resultElement = document.getElementById("result");
    if (monthlyPayment) {
      resultElement.textContent = `Your monthly payment is $${monthlyPayment}`;
    } else {
      resultElement.textContent = "Invalid input. Please check your values and try again.";
    }
  }

  // Attach event listener to the form
  const mortgageForm = document.getElementById("mortgageForm");
  mortgageForm.addEventListener("submit", handleFormSubmit);
});

// HTML structure for the mortgage calculator form
// This code assumes the following HTML structure:
// <form id="mortgageForm">
//   <label for="principal">Loan Amount ($):</label>
//   <input type="number" id="principal" required>
//   <label for="annualInterestRate">Annual Interest Rate (%):</label>
//   <input type="number" id="annualInterestRate" step="0.01" required>
//   <label for="years">Loan Term (Years):</label>
//   <input type="number" id="years" required>
//   <button type="submit">Calculate</button>
// </form>
// <div id="result"></div>
```
