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
 * Filters and displays disposable vape products from the Vape Riyadh inventory.
 * @param {Array} inventory - The list of vape products.
 * @returns {Array} - A list of disposable vape products.
 */
function getDisposableVapes(inventory) {
    // Validate that the input is an array
    if (!Array.isArray(inventory)) {
        throw new Error("Invalid input: inventory must be an array.");
    }

    // Filter disposable vape products
    const disposableVapes = inventory.filter((product) => {
        // Ensure product has required properties
        if (!product || typeof product !== "object") {
            throw new Error("Invalid product format in inventory.");
        }
        return product.type === "disposable";
    });

    // Return the filtered list
    return disposableVapes;
}

// Example usage:

// Vape Riyadh 2 inventory data
const vapeRiyadhInventory = [
    { id: 1, name: "Vape A", type: "disposable", price: 50 },
    { id: 2, name: "Vape B", type: "rechargeable", price: 80 },
    { id: 3, name: "Vape C", type: "disposable", price: 60 },
    { id: 4, name: "Vape D", type: "pod", price: 100 },
];

try {
    const disposableVapes = getDisposableVapes(vapeRiyadhInventory);
    console.log("Disposable Vapes:", disposableVapes);
} catch (error) {
    console.error("Error:", error.message);
}
```
