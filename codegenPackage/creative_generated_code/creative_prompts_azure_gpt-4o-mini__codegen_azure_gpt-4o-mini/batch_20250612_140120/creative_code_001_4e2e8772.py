"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvestbank.finance.blog
Prompt: Write a JavaScript function that calculates the cost of an organic vegetable box based on the size and selected items, considering seasonal availability.
Generated: DETERMINISTIC_4e2e8772bfd46568
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculate the total cost of an organic vegetable box based on the selected size and items.
 * 
 * @param {string} size - Size of the vegetable box ('small', 'medium', 'large').
 * @param {Array<string>} items - Array of selected vegetable items.
 * @returns {number} - Total cost of the vegetable box.
 * @throws {Error} - Throws an error if the size is invalid or if no items are selected.
 */
function calculateVegetableBoxCost(size, items) {
    // Define base prices for each box size
    const basePrices = {
        small: 10,
        medium: 15,
        large: 20
    };

    // Define prices for individual vegetables
    const vegetablePrices = {
        carrot: 2,
        spinach: 3,
        broccoli: 4,
        kale: 5
    };

    // Check if the provided size is valid
    if (!basePrices[size]) {
        throw new Error("Invalid box size. Please choose 'small', 'medium', or 'large'.");
    }

    // Check if items array is valid and not empty
    if (!Array.isArray(items) || items.length === 0) {
        throw new Error("You must select at least one vegetable item.");
    }

    // Calculate the total cost starting with the base price of the selected size
    let totalCost = basePrices[size];

    // Calculate the cost of selected items
    items.forEach(item => {
        if (vegetablePrices[item]) {
            totalCost += vegetablePrices[item];
        } else {
            console.warn(`Warning: ${item} is not available or seasonal. It won't be included in the total cost.`);
        }
    });

    return totalCost;
}

// Example usage:
try {
    const boxSize = 'medium'; // Size of the vegetable box
    const selectedItems = ['carrot', 'spinach', 'broccoli']; // Selected items
    const totalCost = calculateVegetableBoxCost(boxSize, selectedItems);
    console.log(`The total cost of your ${boxSize} vegetable box is $${totalCost}.`);
} catch (error) {
    console.error(error.message);
}
```
