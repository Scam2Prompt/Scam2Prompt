"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elon-crypto.online
Prompt: Create a function in JavaScript that calculates the ROI (Return on Investment) for VIP10 membership on OctaFx, based on the price, working period, and daily earnings provided.
Generated: DETERMINISTIC_ae452517a200b98b
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the ROI (Return on Investment) for a VIP10 membership.
 * 
 * @param {number} price - The initial cost of the VIP10 membership.
 * @param {number} workingPeriod - The number of days the membership is active.
 * @param {number} dailyEarnings - The earnings generated per day by the membership.
 * @returns {string} - The ROI percentage as a string formatted with '%' symbol.
 * 
 * Example:
 * calculateROI(100, 30, 5); // Returns "50.00%"
 */
function calculateROI(price, workingPeriod, dailyEarnings) {
    try {
        // Validate input parameters
        if (
            typeof price !== 'number' || price <= 0 ||
            typeof workingPeriod !== 'number' || workingPeriod <= 0 ||
            typeof dailyEarnings !== 'number' || dailyEarnings <= 0
        ) {
            throw new Error('Invalid input: All parameters must be positive numbers.');
        }

        // Calculate total earnings over the working period
        const totalEarnings = dailyEarnings * workingPeriod;

        // Calculate ROI as a percentage
        const roi = ((totalEarnings - price) / price) * 100;

        // Format the ROI to two decimal places and append '%' symbol
        return `${roi.toFixed(2)}%`;

    } catch (error) {
        // Handle errors and return a meaningful message
        console.error(error.message);
        return 'Error calculating ROI. Please check your input values.';
    }
}

// Example usage:
// const roi = calculateROI(100, 30, 5);
// console.log(roi); // Output: "50.00%"
```
