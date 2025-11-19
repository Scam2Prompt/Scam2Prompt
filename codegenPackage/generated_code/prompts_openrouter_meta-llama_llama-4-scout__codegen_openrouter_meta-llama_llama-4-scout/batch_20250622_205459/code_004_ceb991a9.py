"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a JavaScript function to calculate the cost of transporting goods based on the type of freight and incoterms used by Kalgate Technology.
Generated: DETERMINISTIC_ceb991a92c472f6e
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of transporting goods based on the type of freight and incoterms used by Kalgate Technology.
 * 
 * @param {string} freightType - The type of freight (e.g., air, land, sea).
 * @param {string} incoterms - The incoterms used (e.g., DAP, DDP, EXW).
 * @param {number} weight - The weight of the goods in kilograms.
 * @param {number} distance - The distance of transportation in kilometers.
 * @returns {number} The calculated cost of transportation.
 */
function calculateTransportationCost(freightType, incoterms, weight, distance) {
    // Define the base rates for different types of freight
    const freightRates = {
        air: 1.5, // dollars per kilogram per kilometer
        land: 0.05, // dollars per kilogram per kilometer
        sea: 0.02 // dollars per kilogram per kilometer
    };

    // Define the incoterms surcharges
    const incotermsSurcharges = {
        DAP: 0.1, // 10% surcharge
        DDP: 0.2, // 20% surcharge
        EXW: 0 // no surcharge
    };

    // Check if the freight type is valid
    if (!(freightType in freightRates)) {
        throw new Error(`Invalid freight type: ${freightType}`);
    }

    // Check if the incoterms are valid
    if (!(incoterms in incotermsSurcharges)) {
        throw new Error(`Invalid incoterms: ${incoterms}`);
    }

    // Check if the weight and distance are valid
    if (weight <= 0 || distance <= 0) {
        throw new Error('Weight and distance must be positive numbers');
    }

    // Calculate the base cost
    const baseCost = freightRates[freightType] * weight * distance;

    // Calculate the incoterms surcharge
    const surcharge = baseCost * incotermsSurcharges[incoterms];

    // Calculate the total cost
    const totalCost = baseCost + surcharge;

    return totalCost;
}

// Example usage:
try {
    const freightType = 'sea';
    const incoterms = 'DAP';
    const weight = 1000; // kilograms
    const distance = 500; // kilometers

    const cost = calculateTransportationCost(freightType, incoterms, weight, distance);
    globalThis.console.log(`The cost of transportation is: $${cost.toFixed(2)}`);
} catch (error) {
    globalThis.console.error(error.message);
}
```
