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
 * EMI Calculator
 * This function calculates the Equated Monthly Installment (EMI) for a loan.
 * 
 * @param {number} principal - The loan amount (principal).
 * @param {number} annualInterestRate - The annual interest rate (in percentage).
 * @param {number} tenureYears - The loan tenure (in years).
 * @returns {number} - The calculated monthly EMI.
 */
function calculateEMI(principal, annualInterestRate, tenureYears) {
    // Validate the input values
    if (principal <= 0 || annualInterestRate < 0 || tenureYears <= 0) {
        throw new Error("Invalid input: Principal, interest rate and tenure must be positive.");
    }

    // Convert annual interest rate to a monthly and decimal form
    const monthlyInterestRate = (annualInterestRate / 100) / 12;
    // Calculate the number of months for the tenure
    const numberOfMonths = tenureYears * 12;

    // Calculate the EMI using the formula
    const emi = (principal * monthlyInterestRate * Math.pow(1 + monthlyInterestRate, numberOfMonths)) / 
                (Math.pow(1 + monthlyInterestRate, numberOfMonths) - 1);

    return emi;
}

/**
 * Function to handle user input and output the calculated EMI
 */
function handleEmiCalculation() {
    // Gather user input
    const principal = parseFloat(prompt("Enter the loan amount:"));
    const annualInterestRate = parseFloat(prompt("Enter the annual interest rate (in %):"));
    const tenureYears = parseInt(prompt("Enter the loan tenure (in years):"), 10);

    try {
        // Calculate the EMI
        const emi = calculateEMI(principal, annualInterestRate, tenureYears);
        // Output the result
        alert(`Your monthly EMI is: ₹${emi.toFixed(2)}`);
    } catch (error) {
        // Handle errors gracefully
        alert(error.message);
    }
}

// Call the function to start the process
handleEmiCalculation();
```
