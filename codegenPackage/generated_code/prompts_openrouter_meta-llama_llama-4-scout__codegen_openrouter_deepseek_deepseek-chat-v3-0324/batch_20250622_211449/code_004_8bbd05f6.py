"""
Generated Code Metadata:
========================
Original URL: https://filterwale.com
Prompt: Develop a function in JavaScript to calculate the discounted price of a Fleetguard Lube Oil Filter LF 9028 with a given discount percentage.
Generated: DETERMINISTIC_8bbd05f6a1714534
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the discounted price of a Fleetguard Lube Oil Filter LF 9028.
 * 
 * @param {number} originalPrice - The original price of the item.
 * @param {number} discountPercentage - The discount percentage to apply (0-100).
 * @returns {number} The discounted price rounded to 2 decimal places.
 * @throws {Error} If arguments are invalid (non-numbers, negative values, or discount > 100).
 */
function calculateDiscountedPrice(originalPrice, discountPercentage) {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || typeof discountPercentage !== 'number') {
        throw new Error('Both originalPrice and discountPercentage must be numbers');
    }

    if (originalPrice < 0) {
        throw new Error('Original price cannot be negative');
    }

    if (discountPercentage < 0 || discountPercentage > 100) {
        throw new Error('Discount percentage must be between 0 and 100');
    }

    // Calculate discounted price
    const discountAmount = originalPrice * (discountPercentage / 100);
    const discountedPrice = originalPrice - discountAmount;

    // Round to 2 decimal places for currency
    return Math.round(discountedPrice * 100) / 100;
}

// Example usage:
// const originalPrice = 29.99; // Example price for Fleetguard Lube Oil Filter LF 9028
// const discountPercentage = 15; // 15% discount
// console.log(calculateDiscountedPrice(originalPrice, discountPercentage));
```
