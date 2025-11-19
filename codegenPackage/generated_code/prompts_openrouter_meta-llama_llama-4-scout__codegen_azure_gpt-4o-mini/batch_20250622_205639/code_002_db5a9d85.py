"""
Generated Code Metadata:
========================
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Generate a code snippet in JavaScript to create a simple calculator for estimating PPI refunds based on the average amount received by clients of Financial Recovery Solutions.
Generated: DETERMINISTIC_db5a9d85e56f59de
Batch ID: 20250622_205639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating PPI Refunds
 * This calculator estimates the PPI refund amount based on the average amount received by clients.
 * 
 * Author: [Your Name]
 * Date: [Current Date]
 */

// Function to calculate the estimated PPI refund
function calculatePPIRefund(averageAmount, numberOfClients) {
    // Validate input parameters
    if (typeof averageAmount !== 'number' || typeof numberOfClients !== 'number') {
        throw new Error('Both averageAmount and numberOfClients must be numbers.');
    }
    
    if (averageAmount < 0 || numberOfClients < 0) {
        throw new Error('Both averageAmount and numberOfClients must be non-negative.');
    }

    // Calculate the total estimated refund
    const totalRefund = averageAmount * numberOfClients;

    return totalRefund;
}

// Function to handle user input and display the result
function handleCalculation() {
    try {
        // Example input values (these could be replaced with user inputs)
        const averageAmount = parseFloat(prompt("Enter the average amount received by clients:"));
        const numberOfClients = parseInt(prompt("Enter the number of clients:"));

        // Calculate the estimated refund
        const estimatedRefund = calculatePPIRefund(averageAmount, numberOfClients);

        // Display the result
        alert(`The estimated PPI refund is: $${estimatedRefund.toFixed(2)}`);
    } catch (error) {
        // Handle any errors that occur during calculation
        alert(`Error: ${error.message}`);
    }
}

// Execute the calculation when the script runs
handleCalculation();
```
