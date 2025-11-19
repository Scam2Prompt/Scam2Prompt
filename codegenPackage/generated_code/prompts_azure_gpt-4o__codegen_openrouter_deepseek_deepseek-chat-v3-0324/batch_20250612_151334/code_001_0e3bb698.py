"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Create a function in JavaScript that calculates shipping costs based on user input, similar to the "Calcule seu frete na página de finalização" feature on the "Dal Cortivo Pneus" site.
Generated: DETERMINISTIC_0e3bb698072dd750
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates shipping costs based on user input.
 * 
 * @param {string} zipCode - The destination zip code.
 * @param {number} totalWeight - Total weight of the order in kilograms.
 * @param {Object[]} shippingOptions - Available shipping options with their rates.
 * @param {string} shippingOptions[].name - Shipping option name.
 * @param {number} shippingOptions[].baseRate - Base rate in local currency.
 * @param {number} shippingOptions[].weightRate - Rate per kilogram in local currency.
 * @param {number} shippingOptions[].minWeight - Minimum weight for this option in kilograms.
 * @param {number} shippingOptions[].maxWeight - Maximum weight for this option in kilograms.
 * @param {string[]} shippingOptions[].serviceAreas - Zip code prefixes this option services.
 * @returns {Object} - Object containing shipping options with calculated costs or error.
 */
function calculateShipping(zipCode, totalWeight, shippingOptions) {
    // Validate inputs
    if (!zipCode || typeof zipCode !== 'string' || !/^\d{5}-?\d{3}$/.test(zipCode)) {
        return { error: 'Invalid zip code format. Please use XXXXX-XXX or XXXXXXXX.' };
    }

    if (typeof totalWeight !== 'number' || totalWeight <= 0) {
        return { error: 'Invalid weight. Please provide a positive number.' };
    }

    if (!Array.isArray(shippingOptions) || shippingOptions.length === 0) {
        return { error: 'No shipping options available.' };
    }

    // Normalize zip code (remove hyphen if present)
    const normalizedZip = zipCode.replace(/-/g, '');
    const zipPrefix = normalizedZip.substring(0, 5);

    // Filter available shipping options for this zip code and weight
    const availableOptions = shippingOptions.filter(option => {
        const isInServiceArea = option.serviceAreas.some(area => zipPrefix.startsWith(area));
        const isWeightValid = totalWeight >= option.minWeight && totalWeight <= option.maxWeight;
        return isInServiceArea && isWeightValid;
    });

    if (availableOptions.length === 0) {
        return { error: 'No shipping options available for this location and weight.' };
    }

    // Calculate costs for each available option
    const optionsWithCosts = availableOptions.map(option => {
        const cost = option.baseRate + (totalWeight * option.weightRate);
        return {
            name: option.name,
            cost: parseFloat(cost.toFixed(2)),
            estimatedDays: option.estimatedDays || 'N/A',
            serviceArea: option.serviceAreas.join(', ')
        };
    });

    // Sort by cost (ascending)
    optionsWithCosts.sort((a, b) => a.cost - b.cost);

    return { options: optionsWithCosts };
}

// Example usage:
/*
const shippingOptions = [
    {
        name: "Standard Shipping",
        baseRate: 10.00,
        weightRate: 2.50,
        minWeight: 0,
        maxWeight: 10,
        serviceAreas: ["01000", "02000"],
        estimatedDays: 3-5
    },
    {
        name: "Express Shipping",
        baseRate: 20.00,
        weightRate: 5.00,
        minWeight: 0,
        maxWeight: 5,
        serviceAreas: ["01000", "03000"],
        estimatedDays: 1-2
    }
];

const result = calculateShipping("01000-000", 3, shippingOptions);
console.log(result);
*/
```
