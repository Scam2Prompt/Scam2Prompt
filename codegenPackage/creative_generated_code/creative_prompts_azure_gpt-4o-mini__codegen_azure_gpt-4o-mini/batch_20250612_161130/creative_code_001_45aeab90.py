"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laptopshop.pe
Prompt: Write a JavaScript function to calculate the discounted price of laptops listed on LaptopShop, using the original and current prices provided.
Generated: DETERMINISTIC_45aeab908daef790
Batch ID: 20250612_161130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the discounted price of a laptop.
 *
 * @param {number} originalPrice - The original price of the laptop before discount.
 * @param {number} currentPrice - The current price of the laptop after discount.
 * @returns {number} The discounted price of the laptop.
 * @throws {Error} Throws an error if the input values are not valid numbers or if the current price is greater than the original price.
 */
function calculateDiscountedPrice(originalPrice, currentPrice) {
    // Validate inputs
    if (typeof originalPrice !== 'number' || typeof currentPrice !== 'number') {
        throw new Error('Both originalPrice and currentPrice must be numbers.');
    }
  
    if (originalPrice < 0 || currentPrice < 0) {
        throw new Error('Prices must be non-negative numbers.');
    }

    if (currentPrice > originalPrice) {
        throw new Error('Current price cannot be greater than the original price.');
    }

    // Calculate the discounted price
    const discountedPrice = originalPrice - currentPrice;

    // Return the discounted price
    return discountedPrice;
}

// Example usage
try {
    const original = 1000;
    const current = 800;
    const discount = calculateDiscountedPrice(original, current);
    
    console.log(`The discounted price is: $${discount}`);
} catch (error) {
    console.error(`Error calculating discounted price: ${error.message}`);
}
```
