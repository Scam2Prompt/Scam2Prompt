"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaperiyadh2.com
Prompt: Write a JavaScript function to filter and display only the disposable vape products from the Vape Riyadh 2 inventory.
Generated: DETERMINISTIC_d8d16ff8377e2d2e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters the inventory for disposable vape products and displays them.
 * 
 * @param {Array} inventory - The array of vape product objects.
 * @throws {Error} Will throw an error if the inventory is not an array.
 */
function filterDisposableVapes(inventory) {
    // Check if inventory is an array
    if (!Array.isArray(inventory)) {
        throw new Error("Invalid input: inventory must be an array.");
    }

    // Filter for disposable vape products
    const disposableVapes = inventory.filter(product => product.type === 'disposable');

    // Check if there are any disposable vape products
    if (disposableVapes.length === 0) {
        console.log("No disposable vape products found.");
        return;
    }

    // Display the filtered disposable vape products
    console.log("Disposable Vape Products:");
    disposableVapes.forEach(product => {
        console.log(`- ${product.name}: $${product.price}`);
    });
}

// Example usage
const vapeInventory = [
    { name: 'Vape Pen A', type: 'refillable', price: 29.99 },
    { name: 'Vape Pen B', type: 'disposable', price: 12.99 },
    { name: 'Vape Pen C', type: 'disposable', price: 15.99 },
    { name: 'Vape Pen D', type: 'refillable', price: 39.99 }
];

try {
    filterDisposableVapes(vapeInventory);
} catch (error) {
    console.error(error.message);
}
```
