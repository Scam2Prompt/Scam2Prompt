"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: "Create a JavaScript function to implement a simple discount calculator for products like the 3D Energy Globe, considering different discount rates."
Generated: DETERMINISTIC_95f7f5916292b969
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the discounted price for a product based on given discount rates.
 * 
 * @param {number} originalPrice - The original price of the product.
 * @param {number} discountRate - The discount rate to apply (0-100).
 * @returns {Object} An object containing the discounted price and discount amount.
 * @throws {Error} If input parameters are invalid.
 */
function calculateDiscount(originalPrice, discountRate) {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || typeof discountRate !== 'number') {
        throw new Error('Both originalPrice and discountRate must be numbers');
    }
    
    if (originalPrice <= 0) {
        throw new Error('Original price must be greater than 0');
    }
    
    if (discountRate < 0 || discountRate > 100) {
        throw new Error('Discount rate must be between 0 and 100');
    }

    // Calculate discount amount and discounted price
    const discountAmount = originalPrice * (discountRate / 100);
    const discountedPrice = originalPrice - discountAmount;

    return {
        originalPrice: originalPrice,
        discountRate: discountRate,
        discountAmount: parseFloat(discountAmount.toFixed(2)),
        discountedPrice: parseFloat(discountedPrice.toFixed(2))
    };
}

/**
 * Example usage for a 3D Energy Globe product
 */
function exampleUsage() {
    try {
        const product = {
            name: '3D Energy Globe',
            price: 99.99
        };

        const discountRate = 15; // 15% discount

        const result = calculateDiscount(product.price, discountRate);
        
        console.log(`Product: ${product.name}`);
        console.log(`Original Price: $${result.originalPrice.toFixed(2)}`);
        console.log(`Discount Rate: ${result.discountRate}%`);
        console.log(`Discount Amount: $${result.discountAmount.toFixed(2)}`);
        console.log(`Discounted Price: $${result.discountedPrice.toFixed(2)}`);
    } catch (error) {
        console.error('Error calculating discount:', error.message);
    }
}

// Uncomment to run example
// exampleUsage();
```
