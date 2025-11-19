"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Develop a function in JavaScript that calculates the total cost of a corporate travel package, including air charter and safari options, based on the offerings of KK Travel Solutions.
Generated: DETERMINISTIC_3e796ada07bbc8c8
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total cost of a corporate travel package.
 * 
 * @param {number} airCharterCost - The cost of the air charter.
 * @param {number} safariCost - The cost of the safari.
 * @param {number} [insuranceCost=0] - Optional insurance cost, defaults to 0.
 * @param {number} [taxRate=0.1] - Optional tax rate, defaults to 10%.
 * @returns {number} The total cost of the travel package.
 * @throws {Error} Throws an error if any cost is negative.
 */
function calculateTravelPackageCost(airCharterCost, safariCost, insuranceCost = 0, taxRate = 0.1) {
    // Validate input parameters
    if (airCharterCost < 0 || safariCost < 0 || insuranceCost < 0) {
        throw new Error('Cost values cannot be negative.');
    }
    
    // Calculate total before tax
    const totalBeforeTax = airCharterCost + safariCost + insuranceCost;

    // Calculate total tax
    const totalTax = totalBeforeTax * taxRate;

    // Calculate total cost including tax
    const totalCost = totalBeforeTax + totalTax;

    return totalCost;
}

// Example usage (uncomment to run)
// try {
//     const totalCost = calculateTravelPackageCost(2000, 1500, 300);
//     console.log(`Total Cost of Travel Package: $${totalCost.toFixed(2)}`);
// } catch (error) {
//     console.error(error.message);
// }
```
