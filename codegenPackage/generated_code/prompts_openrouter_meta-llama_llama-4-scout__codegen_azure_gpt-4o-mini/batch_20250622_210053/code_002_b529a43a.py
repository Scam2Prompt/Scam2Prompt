"""
Generated Code Metadata:
========================
Original URL: https://etherealspamassagetherapist.com
Prompt: Generate a JavaScript function to calculate the total cost of a 90-minute Deep Tissue massage with Hot Stone enhancement at $120 for the massage and $5 for the enhancement.
Generated: DETERMINISTIC_b529a43a610e37a5
Batch ID: 20250622_210053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a Deep Tissue massage with Hot Stone enhancement.
 * 
 * @param {number} massageCost - The cost of the massage.
 * @param {number} enhancementCost - The cost of the enhancement.
 * @returns {number} The total cost of the massage including enhancements.
 * @throws {Error} Throws an error if the input costs are not valid numbers.
 */
function calculateTotalCost(massageCost, enhancementCost) {
    // Validate input types
    if (typeof massageCost !== 'number' || typeof enhancementCost !== 'number') {
        throw new Error('Invalid input: Both massageCost and enhancementCost must be numbers.');
    }

    // Validate input values
    if (massageCost < 0 || enhancementCost < 0) {
        throw new Error('Invalid input: Costs must be non-negative.');
    }

    // Calculate total cost
    const totalCost = massageCost + enhancementCost;

    return totalCost;
}

// Constants for the massage and enhancement costs
const MASSAGE_COST = 120; // Cost of the Deep Tissue massage
const ENHANCEMENT_COST = 5; // Cost of the Hot Stone enhancement

try {
    // Calculate the total cost
    const total = calculateTotalCost(MASSAGE_COST, ENHANCEMENT_COST);
    console.log(`The total cost of the massage is: $${total.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
