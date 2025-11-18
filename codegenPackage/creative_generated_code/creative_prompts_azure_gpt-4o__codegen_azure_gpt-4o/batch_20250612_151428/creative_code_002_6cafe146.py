"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marant.com.mx
Prompt: Create a function in JavaScript that filters Marant's skincare products by cruelty-free status and recyclable packaging, as highlighted on the website.
Generated: DETERMINISTIC_6cafe146c527c93e
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters Marant's skincare products based on cruelty-free status and recyclable packaging.
 * 
 * @param {Array} products - An array of product objects. Each object should have the following properties:
 *                           - name {string}: The name of the product.
 *                           - crueltyFree {boolean}: Indicates whether the product is cruelty-free.
 *                           - recyclablePackaging {boolean}: Indicates whether the product has recyclable packaging.
 * @returns {Array} - An array of product objects that are both cruelty-free and have recyclable packaging.
 */
function filterProductsByEthicalCriteria(products) {
    // Validate input is an array
    if (!Array.isArray(products)) {
        throw new Error("Invalid input: 'products' must be an array.");
    }

    // Filter products based on cruelty-free status and recyclable packaging
    return products.filter(product => {
        // Ensure each product object has the required properties
        if (typeof product !== 'object' || product === null) {
            throw new Error("Invalid product entry: Each product must be a non-null object.");
        }
        if (typeof product.crueltyFree !== 'boolean' || typeof product.recyclablePackaging !== 'boolean') {
            throw new Error(
                "Invalid product entry: Each product must have 'crueltyFree' and 'recyclablePackaging' as boolean properties."
            );
        }

        // Return products that meet the criteria
        return product.crueltyFree && product.recyclablePackaging;
    });
}

// Example usage
const marantSkincareProducts = [
    { name: "Hydrating Serum", crueltyFree: true, recyclablePackaging: true },
    { name: "Brightening Cream", crueltyFree: true, recyclablePackaging: false },
    { name: "Night Repair Oil", crueltyFree: false, recyclablePackaging: true },
    { name: "Daily Sunscreen", crueltyFree: true, recyclablePackaging: true },
];

try {
    const ethicalProducts = filterProductsByEthicalCriteria(marantSkincareProducts);
    console.log("Filtered Products:", ethicalProducts);
} catch (error) {
    console.error("Error filtering products:", error.message);
}
```
