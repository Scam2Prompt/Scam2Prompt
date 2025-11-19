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
 * 
 * @param {string} materialType - Type of material (e.g., 'businessCard', 'brochure', etc.)
 * @param {number} quantity - Number of items to print
 * @param {string} [size='A4'] - Size of the material (default: 'A4')
 * @param {string} [color='black'] - Color of the print (default: 'black')
 * @returns {number} The total cost of printing
 */
function calculatePrintingCost(materialType, quantity, size = 'A4', color = 'black') {
    // Define pricing model for different materials
    const pricingModel = {
        businessCard: {
            Detalj: 0.5,
            glossy: 0.75,
            matte: 0.6
        },
        brochure: {
            A4: {
                black: 0.2,
                color: 0.5
            },
            A3: {
                black: 0.3,
                color: 0.7
            }
        }
        // Add more materials and their pricing models as needed
    };

    // Check if material type is supported
    if (!pricingModel[materialType]) {
        throw new Error(`Unsupported material type: ${materialType}`);
    }

    let cost;
    if (materialType === 'businessCard') {
        // Business card pricing based on material type
        if (!['Detalj', 'glossy', 'matte'].includes(size)) {
            throw new Error(`Unsupported business card material size: ${size}`);
        }
        cost = pricingModel[materialType][size] * quantity;
    } else {
        // Brochure pricing based on size and color
        if (!['A4', 'A3'].includes(size)) {
            throw new Error(`Unsupported brochure size: ${size}`);
        }
        if (!['black', 'color'].includes(color)) {
            throw new Error(`Unsupported color: ${color}`);
        }
        cost = pricingModel[materialType][size][color] * quantity;
    }

    // Apply discounts for bulk orders
    if (quantity >= 1000) {
        cost *= 0.9; // 10% discount for orders over 1000
    } else if (quantity >= 500) {
        cost *= 0.95; // 5% discount for orders over 500
    }

    return cost;
}

// Example usage:
try {
    const businessCardCost = calculatePrintingCost('businessCard', 500, 'Detalj');
    console.log(`Business card printing cost: $${businessCardCost.toFixed(2)}`);

    const brochureCost = calculatePrintingCost('brochure', 2000, 'A4', 'color');
    console.log(`Brochure printing cost: $${brochureCost.toFixed(2)}`);
} catch (error) {
    console.error(error.message);
}
```
