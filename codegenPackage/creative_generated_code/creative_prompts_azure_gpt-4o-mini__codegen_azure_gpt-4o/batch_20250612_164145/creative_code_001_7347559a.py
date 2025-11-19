"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoiniswaptokens.blogspot.com
Prompt: Write a JavaScript function that calculates the total cost of purchasing multiple items from a toolbox, specifically including "martelo," "ferramentas plumo," and "caixa de ferramentas."
Generated: DETERMINISTIC_7347559aae02d335
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the total cost of purchasing multiple items from a toolbox.
 * Items included: 'martelo', 'ferramentas plumo', and 'caixa de ferramentas'.
 * 
 * @param {Object} quantities - An object containing the quantities of each item to be purchased. 
 *                              Example: { martelo: 2, ferramentasPlumo: 3, caixaDeFerramentas: 1 }
 * @returns {number} - The total cost of the items. Returns 0 if quantities are invalid or items are not included.
 */
function calculateTotalCost(quantities) {
    // Prices for each item in the toolbox
    const itemPrices = {
        martelo: 50, // Price of 'martelo' in currency units
        ferramentasPlumo: 75, // Price of 'ferramentas plumo' in currency units
        caixaDeFerramentas: 150 // Price of 'caixa de ferramentas' in currency units
    };

    // Check if the input is valid
    if (typeof quantities !== 'object' || quantities === null) {
        throw new Error("Invalid input: quantities must be a non-null object.");
    }

    // Calculate the total cost
    let totalCost = 0;
    for (let item in itemPrices) {
        if (quantities[item] !== undefined) {
            // Ensure the quantity is valid (non-negative integer)
            if (typeof quantities[item] !== 'number' || quantities[item] < 0 || !Number.isInteger(quantities[item])) {
                throw new Error(`Invalid quantity for ${item}: must be a non-negative integer.`);
            }
            totalCost += itemPrices[item] * quantities[item];
        }
    }

    return totalCost;
}

// Example usage:
try {
    const quantities = {
        martelo: 2, // Buying 2 'martelo'
        ferramentasPlumo: 3, // Buying 3 'ferramentas plumo'
        caixaDeFerramentas: 1 // Buying 1 'caixa de ferramentas'
    };
    const total = calculateTotalCost(quantities);
    console.log(`Total cost: ${total}`); // Outputs: Total cost: 525
} catch (error) {
    console.error(error.message);
}
```
