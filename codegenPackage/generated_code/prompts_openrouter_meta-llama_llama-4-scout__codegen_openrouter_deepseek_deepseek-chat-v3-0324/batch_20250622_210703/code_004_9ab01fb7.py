"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write a JavaScript function to calculate the cost of a customized engraving project based on material, size, and complexity.
Generated: DETERMINISTIC_9ab01fb7088a70df
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of a customized engraving project.
 * 
 * @param {string} material - The material to be engraved ('wood', 'metal', 'glass', 'plastic').
 * @param {string} size - The size of the engraving ('small', 'medium', 'large', 'xlarge').
 * @param {number} complexity - The complexity level (1-5) where 1 is simplest and 5 is most complex.
 * @returns {number} The total cost of the engraving project.
 * @throws {Error} If invalid parameters are provided.
 */
function calculateEngravingCost(material, size, complexity) {
    // Validate input parameters
    if (!['wood', 'metal', 'glass', 'plastic'].includes(material)) {
        throw new Error('Invalid material. Must be one of: wood, metal, glass, plastic');
    }
    
    if (!['small', 'medium', 'large', 'xlarge'].includes(size)) {
        throw new Error('Invalid size. Must be one of: small, medium, large, xlarge');
    }
    
    if (typeof complexity !== 'number' || complexity < 1 || complexity > 5) {
        throw new Error('Invalid complexity. Must be a number between 1 and 5');
    }
    
    // Base prices for materials
    const materialPrices = {
        wood: 10,
        metal: 20,
        glass: 15,
        plastic: 8
    };
    
    // Size multipliers
    const sizeMultipliers = {
        small: 1,
        medium: 1.5,
        large: 2,
        xlarge: 3
    };
    
    // Complexity multipliers
    const complexityMultipliers = {
        1: 1,
        2: 1.2,
        3: 1.5,
        4: 2,
        5: 3
    };
    
    // Calculate total cost
    const baseCost = materialPrices[material];
    const sizeCost = baseCost * sizeMultipliers[size];
    const totalCost = sizeCost * complexityMultipliers[complexity];
    
    // Round to 2 decimal places for currency
    return Math.round(totalCost * 100) / 100;
}

// Example usage:
// try {
//     const cost = calculateEngravingCost('metal', 'medium', 3);
//     console.log(`Total engraving cost: $${cost}`);
// } catch (error) {
//     console.error('Error calculating engraving cost:', error.message);
// }
```
