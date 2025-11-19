"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://regency-towel.com
Prompt: Create a function in JavaScript that displays a list of available towel products, including specifications like size and material, based on the Regency Towel product range.
Generated: DETERMINISTIC_3b63d7af96866f7a
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Represents a towel product with its specifications.
 * @constructor
 * @param {string} name - The name of the towel product.
 * @param {string} size - The size of the towel.
 * @param {string} material - The material of the towel.
 */
class TowelProduct {
    constructor(name, size, material) {
        this.name = name;
        this.size = size;
        this.material = material;
    }
}

/**
 * Displays a list of available towel products along with their specifications.
 * @param {TowelProduct[]} products - An array of towel products.
 */
function displayTowelProducts(products) {
    // Check if products is an array
    if (!Array.isArray(products)) {
        console.error("Invalid input: Expected an array of TowelProduct.");
        return;
    }

    // Check if the array is empty
    if (products.length === 0) {
        console.log("No towel products available.");
        return;
    }

    // Create a header for the display
    console.log("Available Towel Products:");
    console.log("--------------------------");

    // Iterate over each product and display its specifications
    products.forEach(product => {
        if (product instanceof TowelProduct) {
            console.log(`Name: ${product.name}`);
            console.log(`Size: ${product.size}`);
            console.log(`Material: ${product.material}`);
            console.log("--------------------------");
        } else {
            console.warn("Invalid product encountered. Skipping!");
        }
    });
}

// Example usage
const towelProducts = [
    new TowelProduct("Regency Bath Towel", "30x56 inches", "Cotton"),
    new TowelProduct("Regency Hand Towel", "16x30 inches", "Microfiber"),
    new TowelProduct("Regency Beach Towel", "30x70 inches", "Bamboo"),
];

// Display the towel products
displayTowelProducts(towelProducts);
```
