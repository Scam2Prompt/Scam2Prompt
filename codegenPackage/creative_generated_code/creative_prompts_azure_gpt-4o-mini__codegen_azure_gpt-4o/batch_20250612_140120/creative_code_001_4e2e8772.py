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
 * Calculate the cost of an organic vegetable box based on size and selected items.
 * 
 * @param {string} boxSize - The size of the box ("small", "medium", "large").
 * @param {Array<string>} selectedItems - Array of selected vegetables.
 * @returns {number} - Total cost of the vegetable box.
 * @throws Will throw an error if boxSize is invalid or selectedItems contains unavailable items.
 */

// Seasonal availability: vegetables and their prices per unit
const vegetablePricing = {
    carrots: { price: 2, available: true },
    potatoes: { price: 1.5, available: true },
    spinach: { price: 3, available: false }, // Not available this season
    onions: { price: 1, available: true },
    broccoli: { price: 2.5, available: true }
};

// Box size multiplier
const boxSizeMultiplier = {
    small: 1,
    medium: 1.5,
    large: 2
};

function calculateBoxCost(boxSize, selectedItems) {
    // Validate box size
    if (!boxSizeMultiplier.hasOwnProperty(boxSize)) {
        throw new Error(`Invalid box size: ${boxSize}. Valid sizes are "small", "medium", or "large".`);
    }

    // Initialize total cost
    let totalCost = 0;

    // Validate and calculate cost for each selected item
    selectedItems.forEach((item) => {
        const vegetable = vegetablePricing[item];
        if (!vegetable) {
            throw new Error(`Invalid vegetable: ${item}.`);
        }
        if (!vegetable.available) {
            throw new Error(`${item} is not available this season.`);
        }
        totalCost += vegetable.price;
    });

    // Apply box size multiplier
    totalCost *= boxSizeMultiplier[boxSize];

    return totalCost;
}

// Example usage:
try {
    const boxCost = calculateBoxCost("medium", ["carrots", "potatoes", "broccoli"]);
    console.log(`The total cost of your vegetable box is: $${boxCost}`);
} catch (error) {
    console.error(error.message);
}
```
