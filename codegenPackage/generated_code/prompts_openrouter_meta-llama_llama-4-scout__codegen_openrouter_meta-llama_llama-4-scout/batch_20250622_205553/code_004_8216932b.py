"""
Generated Code Metadata:
========================
Original URL: https://eveandevan.com
Prompt: Write a JavaScript function to implement a 10% discount on men's clothing products, similar to the ones offered on Evan Mens, with a condition to apply the discount only on specific product categories.
Generated: DETERMINISTIC_8216932b39274b38
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Applies a 10% discount on men's clothing products in specific categories.
 * 
 * @param {Object} product - The product object with properties: id, name, price, category.
 * @param {Array} eligibleCategories - The list of categories eligible for the discount.
 * @returns {Object} The updated product object with discount applied if eligible.
 */
function applyDiscount(product, eligibleCategories) {
    // Check if product is valid
    if (!product || typeof product !== 'object') {
        throw new Error('Invalid product object');
    }

    // Check if eligible categories is valid
    if (!eligibleCategories || !Array.isArray(eligibleCategories)) {
        throw new Error('Invalid eligible categories array');
    }

    // Define the discount percentage
    const discountPercentage = 0.10;

    // Check if product category is eligible for discount
    if (eligibleCategories.includes(product.category)) {
        // Calculate the discount amount
        const discountAmount = product.price * discountPercentage;

        // Apply the discount
        product.discountedPrice = product.price - discountAmount;
        product.discount = discountAmount.toFixed(2);
    } else {
        product.discountedPrice = product.price;
        product.discount = 0.00;
    }

    return product;
}

// Example usage:
const eligibleCategories = ['Tops', 'Shirts'];
const product = {
    id: 1,
    name: 'Men\'s Fashion Shirt',
    price: 50.00,
    category: 'Shirts'
};

try {
    const updatedProduct = applyDiscount(product, eligibleCategories);
    console.log(updatedProduct);
} catch (error) {
    console.error(error.message);
}
```
