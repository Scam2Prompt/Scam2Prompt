"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bijenwasdoek.nl
Prompt: Write a JavaScript snippet that calculates the cost savings of using reusable beeswax wraps compared to disposable plastic bags over a year.
Generated: DETERMINISTIC_17fdc4535a00874e
Batch ID: 20250612_161441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the cost savings of using reusable beeswax wraps
 * compared to disposable plastic bags over a year.
 * 
 * @param {number} beeswaxWrapCost - The initial cost of a beeswax wrap.
 * @param {number} plasticBagCost - The cost of a single plastic bag.
 * @param {number} bagsPerWeek - The average number of plastic bags used per week.
 * @param {number} weeksPerYear - The number of weeks in a year.
 * @returns {number} The annual cost savings.
 */
function calculateCostSavings(beeswaxWrapCost, plasticBagCost, bagsPerWeek, weeksPerYear = 52) {
    // Input validation
    if (beeswaxWrapCost < 0 || plasticBagCost < 0 || bagsPerWeek < 0 || weeksPerYear <= 0) {
        throw new Error("All input values must be non-negative and weeksPerYear must be greater than zero.");
    }

    // Calculate the annual cost of using plastic bags
    const annualPlasticBagCost = plasticBagCost * bagsPerWeek * weeksPerYear;

    // Assuming beeswax wraps are reusable for a certain number of uses,
    // we need to define the lifespan of one beeswax wrap in terms of usage.
    const usableWrapsPerYear = 1; // For simplicity, assume one beeswax wrap can be used all year round.
    
    // Calculate the annual cost of using beeswax wraps
    const annualBeeswaxWrapCost = beeswaxWrapCost / usableWrapsPerYear;

    // Calculate cost savings
    const savings = annualPlasticBagCost - annualBeeswaxWrapCost;

    // Return the savings value
    return savings;
}

// Example usage
try {
    const savings = calculateCostSavings(20, 0.10, 5);
    console.log(`Annual cost savings by using beeswax wraps: $${savings.toFixed(2)}`);
} catch (error) {
    console.error("Error calculating savings:", error.message);
}
```
