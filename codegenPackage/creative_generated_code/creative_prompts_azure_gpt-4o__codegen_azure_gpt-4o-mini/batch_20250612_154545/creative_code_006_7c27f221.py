"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bearmybrand.com
Prompt: Develop a JavaScript function to optimize paid advertising campaigns by dynamically adjusting ad spend based on performance metrics, in line with Bear My Brand's digital marketing strategies.
Generated: DETERMINISTIC_7c27f2214bb95cc3
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically adjust ad spend based on performance metrics.
 * @param {Object} campaign - The advertising campaign object.
 * @param {number} campaign.currentSpend - The current spend of the campaign.
 * @param {number} campaign.performanceScore - The performance score of the campaign (0-100).
 * @param {number} campaign.budgetLimit - The maximum budget limit for the campaign.
 * @returns {number} - The new ad spend amount after optimization.
 * @throws {Error} - Throws an error if campaign parameters are invalid.
 */
function optimizeAdSpend(campaign) {
    // Validate campaign object
    if (!campaign || typeof campaign !== 'object') {
        throw new Error("Invalid campaign object.");
    }
    if (typeof campaign.currentSpend !== 'number' || 
        typeof campaign.performanceScore !== 'number' || 
        typeof campaign.budgetLimit !== 'number') {
        throw new Error("Campaign properties must be numeric.");
    }
    if (campaign.performanceScore < 0 || campaign.performanceScore > 100) {
        throw new Error("Performance score must be between 0 and 100.");
    }
    
    // Define adjustment coefficients
    const increaseCoefficient = 0.2; // Increase spend by 20% for high performance
    const decreaseCoefficient = 0.3; // Decrease spend by 30% for low performance
    const performanceThreshold = 50; // Threshold score to determine performance level

    let newSpend;

    // Adjust ad spend based on performance score
    if (campaign.performanceScore >= performanceThreshold) {
        // Performance is satisfactory or excellent
        newSpend = campaign.currentSpend * (1 + increaseCoefficient);
    } else {
        // Performance is below expectations
        newSpend = campaign.currentSpend * (1 - decreaseCoefficient);
    }

    // Ensure new spend does not exceed budget limit
    if (newSpend > campaign.budgetLimit) {
        newSpend = campaign.budgetLimit;
    }

    // Return the optimized ad spend
    return parseFloat(newSpend.toFixed(2)); // Round to 2 decimal places
}

// Example usage
try {
    const campaign = {
        currentSpend: 1000,
        performanceScore: 75,
        budgetLimit: 1500
    };
    
    const optimizedSpend = optimizeAdSpend(campaign);
    console.log(`New optimized ad spend: $${optimizedSpend}`);
} catch (error) {
    console.error(error.message);
}
```
