"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Create a JavaScript function to calculate the cost of printing services, such as business card printing, based on the quantity and type of material, like Detalj Reklam's pricing model."
Generated: DETERMINISTIC_bd2e5ca21aa9596c
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of printing services based on quantity and material type.
 * Pricing model inspired by Detalj Reklam's business card printing.
 * 
 * @param {string} materialType - Type of material ('standard', 'premium', 'luxury')
 * @param {number} quantity - Number of items to print (must be positive integer)
 * @returns {number} Total cost in SEK
 * @throws {Error} If invalid parameters are provided
 */
function calculatePrintingCost(materialType, quantity) {
    // Validate input parameters
    if (typeof quantity !== 'number' || !Number.isInteger(quantity) || quantity <= 0) {
        throw new Error('Quantity must be a positive integer');
    }

    const validMaterials = ['standard', 'premium', 'luxury'];
    if (!validMaterials.includes(materialType)) {
        throw new Error(`Invalid material type. Must be one of: ${validMaterials.join(', ')}`);
    }

    // Base prices per material type (SEK per 100 units)
    const materialPrices = {
        standard: 199,
        premium: 299,
        luxury: 399
    };

    // Discount tiers based on quantity
    const discountTiers = [
        { min: 500, discount: 0.15 },
        { min: 1000, discount: 0.25 },
        { min: 2000, discount: 0.35 }
    ];

    // Calculate base price
    const basePricePer100 = materialPrices[materialType];
    const baseCost = Math.ceil(quantity / 100) * basePricePer100;

    // Apply quantity discount if applicable
    let discount = 0;
    for (const tier of discountTiers) {
        if (quantity >= tier.min) {
            discount = tier.discount;
        } else {
            break;
        }
    }

    const totalCost = baseCost * (1 - discount);

    // Round to nearest whole number (SEK doesn't have smaller denominations)
    return Math.round(totalCost);
}

// Example usage:
// try {
//     const cost = calculatePrintingCost('premium', 1200);
//     console.log(`Total printing cost: ${cost} SEK`);
// } catch (error) {
//     console.error('Error calculating printing cost:', error.message);
// }
```
