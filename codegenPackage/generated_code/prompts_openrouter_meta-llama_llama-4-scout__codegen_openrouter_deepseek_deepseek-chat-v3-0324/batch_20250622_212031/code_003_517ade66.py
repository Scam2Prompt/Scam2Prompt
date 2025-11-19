"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Create a JavaScript function to calculate the cost of installation for a Gree Versati III heat pump based on the provided pricing on frigoterm.ro."
Generated: DETERMINISTIC_517ade66122aa961
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the installation cost for a Gree Versati III heat pump based on pricing from frigoterm.ro.
 * 
 * @param {string} model - The model of the Gree Versati III heat pump (e.g., 'GWH09AAA-D3DNA1A')
 * @param {number} installationComplexity - Complexity factor (1-3) where 1=simple, 2=moderate, 3=complex
 * @param {number} additionalMaterialsCost - Cost of any additional materials needed (in RON)
 * @returns {number} Total installation cost in RON
 * @throws {Error} If invalid model or parameters are provided
 */
function calculateInstallationCost(model, installationComplexity, additionalMaterialsCost = 0) {
    // Validate input parameters
    if (typeof model !== 'string' || !model.startsWith('GWH')) {
        throw new Error('Invalid Gree Versati III model provided');
    }

    if (![1, 2, 3].includes(installationComplexity)) {
        throw new Error('Installation complexity must be 1, 2, or 3');
    }

    if (typeof additionalMaterialsCost !== 'number' || additionalMaterialsCost < 0) {
        throw new Error('Additional materials cost must be a positive number');
    }

    // Base prices from frigoterm.ro (as of knowledge cutoff)
    const modelPrices = {
        'GWH09AAA-D3DNA1A': 5499,    // 9kW model
        'GWH12AAA-D3DNA1A': 6499,    // 12kW model
        'GWH18AAA-D3DNA1A': 8999,    // 18kW model
        'GWH24AAA-D3DNA1A': 11999    // 24kW model
    };

    // Installation complexity multipliers
    const complexityMultipliers = {
        1: 0.15,  // Simple installation (15% of unit price)
        2: 0.25,  // Moderate installation (25% of unit price)
        3: 0.35   // Complex installation (35% of unit price)
    };

    // Get base price for the model
    const basePrice = modelPrices[model];
    if (!basePrice) {
        throw new Error('Model not found in pricing database');
    }

    // Calculate installation cost
    const installationCost = basePrice * complexityMultipliers[installationComplexity];
    
    // Calculate total cost
    const totalCost = installationCost + additionalMaterialsCost;

    // Round to nearest integer (RON doesn't have smaller denominations)
    return Math.round(totalCost);
}
```
