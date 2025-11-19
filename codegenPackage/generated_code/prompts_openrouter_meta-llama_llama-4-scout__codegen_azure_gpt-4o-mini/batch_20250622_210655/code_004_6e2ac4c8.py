"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a JavaScript code snippet to create a simple calculator for estimating the cost of soft wood and hard wood lumber for a construction project.
Generated: DETERMINISTIC_6e2ac4c8a934044d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator for Estimating Lumber Costs
 * This program calculates the total cost of softwood and hardwood lumber
 * based on user input for quantity and price per unit.
 */

// Function to calculate total cost
function calculateLumberCost(quantity, pricePerUnit) {
    // Validate input
    if (isNaN(quantity) || isNaN(pricePerUnit) || quantity < 0 || pricePerUnit < 0) {
        throw new Error("Invalid input: Quantity and price per unit must be non-negative numbers.");
    }
    return quantity * pricePerUnit;
}

// Function to get user input and display the cost
function estimateLumberCost() {
    try {
        // Prompt user for lumber type
        const lumberType = prompt("Enter lumber type (softwood/hardwood):").toLowerCase();
        
        // Validate lumber type
        if (lumberType !== "softwood" && lumberType !== "hardwood") {
            throw new Error("Invalid lumber type. Please enter 'softwood' or 'hardwood'.");
        }

        // Prompt user for quantity
        const quantity = parseFloat(prompt("Enter the quantity of lumber (in units):"));
        
        // Prompt user for price per unit
        const pricePerUnit = parseFloat(prompt("Enter the price per unit (in dollars):"));

        // Calculate total cost
        const totalCost = calculateLumberCost(quantity, pricePerUnit);

        // Display the result
        alert(`The total cost for ${quantity} units of ${lumberType} lumber is $${totalCost.toFixed(2)}`);
    } catch (error) {
        // Handle errors gracefully
        alert(`Error: ${error.message}`);
    }
}

// Run the calculator
estimateLumberCost();
```
