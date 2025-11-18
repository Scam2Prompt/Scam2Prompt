"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://australiawidewealth.com
Prompt: Write JavaScript code for a web-based financial calculator that factors in superannuation tax structures and retirement income goals, inspired by the Australia Wide Wealth Services content.
Generated: DETERMINISTIC_28e591aac340e4f2
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Financial Calculator for Superannuation and Retirement Income Goals
// Author: Your Name
// Date: October 2023

// Function to calculate retirement savings based on user input
function calculateRetirementSavings(
    initialInvestment,
    annualContribution,
    annualReturnRate,
    yearsToRetirement,
    superannuationTaxRate
) {
    // Validate inputs
    if (initialInvestment < 0 || annualContribution < 0 || yearsToRetirement < 0) {
        throw new Error("Initial investment, annual contributions, and years to retirement must be non-negative.");
    }
    if (annualReturnRate < 0 || superannuationTaxRate < 0) {
        throw new Error("Annual return rate and superannuation tax rate must be non-negative.");
    }

    let totalSavings = initialInvestment;

    // Calculate total savings over the specified years
    for (let year = 0; year < yearsToRetirement; year++) {
        totalSavings += annualContribution; // Add annual contributions
        totalSavings *= 1 + (annualReturnRate / 100); // Compound returns
    }

    // Apply superannuation tax
    const taxAmount = totalSavings * (superannuationTaxRate / 100);
    totalSavings -= taxAmount; // Deduct tax from total savings

    return totalSavings.toFixed(2); // Return total savings formatted to 2 decimal places
}

// Function to handle form submission and display results
function handleFormSubmission(event) {
    event.preventDefault(); // Prevent default form submission behavior

    // Gather input values from the form
    const initialInvestment = parseFloat(document.getElementById("initialInvestment").value);
    const annualContribution = parseFloat(document.getElementById("annualContribution").value);
    const annualReturnRate = parseFloat(document.getElementById("annualReturnRate").value);
    const yearsToRetirement = parseInt(document.getElementById("yearsToRetirement").value, 10);
    const superannuationTaxRate = parseFloat(document.getElementById("superannuationTaxRate").value);

    try {
        // Calculate retirement savings
        const totalSavings = calculateRetirementSavings(
            initialInvestment,
            annualContribution,
            annualReturnRate,
            yearsToRetirement,
            superannuationTaxRate
        );

        // Display results to the user
        document.getElementById("result").innerText = `Total Retirement Savings: $${totalSavings}`;
    } catch (error) {
        // Handle errors gracefully
        document.getElementById("result").innerText = `Error: ${error.message}`;
    }
}

// Event listener for form submission
document.getElementById("retirementForm").addEventListener("submit", handleFormSubmission);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Retirement Savings Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        input {
            margin: 10px 0;
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
        }
        button {
            padding: 10px 15px;
        }
        #result {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Retirement Savings Calculator</h1>
    <form id="retirementForm">
        <label for="initialInvestment">Initial Investment ($):</label>
        <input type="number" id="initialInvestment" required>
        
        <label for="annualContribution">Annual Contribution ($):</label>
        <input type="number" id="annualContribution" required>
        
        <label for="annualReturnRate">Annual Return Rate (%):</label>
        <input type="number" id="annualReturnRate" required>
        
        <label for="yearsToRetirement">Years to Retirement:</label>
        <input type="number" id="yearsToRetirement" required>
        
        <label for="superannuationTaxRate">Superannuation Tax Rate (%):</label>
        <input type="number" id="superannuationTaxRate" required>
        
        <button type="submit">Calculate</button>
    </form>
    
    <div id="result"></div>

    <script src="calculator.js"></script>
</body>
</html>
```
