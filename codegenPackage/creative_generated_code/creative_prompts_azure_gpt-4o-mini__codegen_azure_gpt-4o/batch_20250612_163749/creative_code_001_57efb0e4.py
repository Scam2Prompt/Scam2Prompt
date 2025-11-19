"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a JavaScript function that calculates shipping costs for tire purchases based on user input, similar to the features on the dcpneus webpage.
Generated: DETERMINISTIC_57efb0e4952f5aba
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates shipping costs for tire purchases based on user input.
 * 
 * @param {number} numTires - The number of tires being purchased.
 * @param {string} destination - The destination for shipping ('domestic' or 'international').
 * @param {boolean} expedited - Whether expedited shipping is requested.
 * @returns {number} - The calculated shipping cost.
 * @throws {Error} - Throws an error for invalid input.
 */
function calculateShippingCost(numTires, destination, expedited) {
    // Validate inputs
    if (typeof numTires !== 'number' || numTires <= 0) {
        throw new Error("Invalid number of tires. Must be a positive number.");
    }
    if (destination !== 'domestic' && destination !== 'international') {
        throw new Error("Invalid destination. Must be 'domestic' or 'international'.");
    }
    if (typeof expedited !== 'boolean') {
        throw new Error("Invalid expedited value. Must be true or false.");
    }

    // Base costs
    const domesticRate = 5; // Cost per tire for domestic shipping
    const internationalRate = 15; // Cost per tire for international shipping
    const expeditedFee = 10; // Flat fee for expedited shipping

    // Calculate cost based on destination
    let baseCost;
    if (destination === 'domestic') {
        baseCost = numTires * domesticRate;
    } else if (destination === 'international') {
        baseCost = numTires * internationalRate;
    }

    // Add expedited shipping fee if applicable
    if (expedited) {
        baseCost += expeditedFee;
    }

    return baseCost;
}

// Example usage:
try {
    const numTires = 4; // Number of tires purchased
    const destination = 'domestic'; // Shipping destination
    const expedited = true; // Expedited shipping requested

    const shippingCost = calculateShippingCost(numTires, destination, expedited);
    console.log(`The shipping cost is $${shippingCost}`);
} catch (error) {
    console.error(error.message);
}
```
