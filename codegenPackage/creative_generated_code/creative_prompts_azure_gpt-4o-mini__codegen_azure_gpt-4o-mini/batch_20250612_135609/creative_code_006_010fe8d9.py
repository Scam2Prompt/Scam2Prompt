"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Write a JavaScript function that generates a quote for packaging materials based on the product specifications from Cartonerías Andinas del Sur.
Generated: DETERMINISTIC_010fe8d99744e4aa
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Generates a quote for packaging materials based on product specifications.
 * 
 * @param {Object} product - The product specifications object.
 * @param {number} product.width - The width of the product in cm.
 * @param {number} product.height - The height of the product in cm.
 * @param {number} product.depth - The depth of the product in cm.
 * @param {number} product.quantity - The quantity of products.
 * @param {string} material - The type of packaging material (e.g., 'cardboard', 'plastic').
 * @returns {Object} - The quote object containing total cost and breakdown.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
function generatePackagingQuote(product, material) {
    // Validate input parameters
    if (!product || typeof product !== 'object') {
        throw new Error('Invalid product specifications.');
    }
    const { width, height, depth, quantity } = product;
    
    if (typeof width !== 'number' || typeof height !== 'number' || typeof depth !== 'number' || typeof quantity !== 'number') {
        throw new Error('Product specifications must include numbers for width, height, depth, and quantity.');
    }

    if (quantity <= 0 || width <= 0 || height <= 0 || depth <= 0) {
        throw new Error('Width, height, depth, and quantity must be positive numbers.');
    }

    // Define cost per cubic centimeter for different materials
    const materialCosts = {
        cardboard: 0.0005,  // Cost per cm³ for cardboard
        plastic: 0.0015,     // Cost per cm³ for plastic
    };

    // Validate material type
    if (!(material in materialCosts)) {
        throw new Error(`Invalid material type. Supported types are: ${Object.keys(materialCosts).join(', ')}`);
    }

    // Calculate volume of the product
    const volume = width * height * depth; // in cubic centimeters

    // Calculate cost for the specified material
    const costPerUnit = materialCosts[material];
    const totalCost = costPerUnit * volume * quantity; // Total cost for the specified quantity

    // Prepare the quote object
    const quote = {
        material: material,
        volume: volume,
        totalCost: parseFloat(totalCost.toFixed(2)), // Round to 2 decimal places
        breakdown: {
            costPerUnit: parseFloat(costPerUnit.toFixed(4)),
            totalVolume: volume * quantity,
        },
    };

    return quote;
}

// Example usage:
try {
    const productSpecs = {
        width: 10,   // in cm
        height: 20,  // in cm
        depth: 5,    // in cm
        quantity: 100 // number of products
    };
    const quote = generatePackagingQuote(productSpecs, 'cardboard');
    console.log('Packaging Quote:', quote);
} catch (error) {
    console.error('Error generating quote:', error.message);
}
```
