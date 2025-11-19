"""
Generated Code Metadata:
========================
Original URL: https://itls-iso.com
Prompt: "Develop a simple calculator in JavaScript to estimate potential cost savings and ROI for organizations adopting the iTLS methodology."
Generated: DETERMINISTIC_8de4162db171d275
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Calculator to Estimate Cost Savings and ROI for Organizations Adopting iTLS Methodology
 * 
 * This calculator takes inputs for current costs, expected savings percentage, 
 * and initial investment to calculate potential cost savings and ROI.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

// Function to calculate cost savings and ROI
function calculateSavingsAndROI(currentCost, savingsPercentage, initialInvestment) {
    try {
        // Input validation
        if (typeof currentCost !== 'number' || currentCost <= 0) {
            throw new Error("Invalid current cost. Please provide a positive number.");
        }
        if (typeof savingsPercentage !== 'number' || savingsPercentage < 0 || savingsPercentage > 100) {
            throw new Error("Invalid savings percentage. Please provide a number between 0 and 100.");
        }
        if (typeof initialInvestment !== 'number' || initialInvestment < 0) {
            throw new Error("Invalid initial investment. Please provide a non-negative number.");
        }

        // Calculate potential cost savings
        const costSavings = (currentCost * savingsPercentage) / 100;

        // Calculate ROI (Return on Investment)
        const roi = ((costSavings - initialInvestment) / initialInvestment) * 100;

        // Return results
        return {
            costSavings: costSavings.toFixed(2), // Rounded to 2 decimal places
            roi: roi.toFixed(2) // Rounded to 2 decimal places
        };
    } catch (error) {
        // Handle errors gracefully
        console.error("Error calculating savings and ROI:", error.message);
        return null;
    }
}

// Example usage
const currentCost = 50000; // Current annual cost in dollars
const savingsPercentage = 20; // Expected savings percentage
const initialInvestment = 10000; // Initial investment in dollars

const result = calculateSavingsAndROI(currentCost, savingsPercentage, initialInvestment);

if (result) {
    console.log("Potential Cost Savings: $", result.costSavings);
    console.log("ROI: ", result.roi, "%");
} else {
    console.log("Failed to calculate savings and ROI. Please check your inputs.");
}
```
