"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dolphiniran.com
Prompt: Write a function in JavaScript to dynamically display discounted prices for products like "آویز حوله دلفین مدل 2530-C-G" and "شلف دیواری دلفین مدل wd-5010-R" on an e-commerce website.
Generated: DETERMINISTIC_dfa89b998b4a316f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to dynamically display discounted prices for products on an e-commerce website.
 * 
 * @param {Array} products - An array of product objects, each containing name, originalPrice, and discountPercentage.
 * @returns {Array} - An array of objects containing product names and their discounted prices.
 */
function calculateDiscountedPrices(products) {
    // Validate input
    if (!Array.isArray(products) || products.length === 0) {
        throw new Error("Invalid input: Expected an array of products.");
    }

    // Array to hold products with discounted prices
    const discountedProducts = products.map(product => {
        // Destructure product details
        const { name, originalPrice, discountPercentage } = product;

        // Validate product properties
        if (typeof name !== 'string' || typeof originalPrice !== 'number' || typeof discountPercentage !== 'number') {
            throw new Error(`Invalid product data: ${JSON.stringify(product)}`);
        }

        // Calculate the discounted price
        const discountAmount = (originalPrice * discountPercentage) / 100;
        const discountedPrice = originalPrice - discountAmount;

        // Return the product with the discounted price
        return {
            name: name,
            discountedPrice: discountedPrice.toFixed(2) // Format to 2 decimal places
        };
    });

    return discountedProducts;
}

// Sample usage
try {
    const products = [
        { name: "آویز حوله دلفین مدل 2530-C-G", originalPrice: 100.00, discountPercentage: 20 },
        { name: "شلف دیواری دلفین مدل wd-5010-R", originalPrice: 150.00, discountPercentage: 15 }
    ];

    const discountedPrices = calculateDiscountedPrices(products);
    console.log(discountedPrices);
} catch (error) {
    console.error("Error calculating discounted prices:", error.message);
}
```
