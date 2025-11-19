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
 * @param {number} originalPrice - The original price of the filter.
 * @param {number} discountPercentage - The discount percentage to apply (0-100).
 * @returns {number} - The discounted price of the filter.
 * @throws {Error} - Throws an error if the original price is negative or if the discount percentage is not between 0 and 100.
 */
function calculateDiscountedPrice(originalPrice, discountPercentage) {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || originalPrice < 0) {
        throw new Error('Original price must be a non-negative number.');
    }
    if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 100) {
        throw new Error('Discount percentage must be a number between 0 and 100.');
    }

    // Calculate the discount amount
    const discountAmount = (originalPrice * discountPercentage) / 100;

    // Calculate the final discounted price
    const discountedPrice = originalPrice - discountAmount;

    // Return the discounted price, rounded to two decimal places
    return parseFloat(discountedPrice.toFixed(2));
}

// Example usage
try {
    const originalPrice = 25.99; // Example original price
    const discountPercentage = 15; // Example discount percentage
    const finalPrice = calculateDiscountedPrice(originalPrice, discountPercentage);
    console.log(`The discounted price is: $${finalPrice}`);
} catch (error) {
    console.error(error.message);
}
```
