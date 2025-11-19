"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write a JavaScript function that simulates the pricing algorithm used on medebooks.shop for calculating discounts on medical courses.
Generated: DETERMINISTIC_961013721b9e4d08
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the final price of a medical course after applying discounts.
 * 
 * @param {number} originalPrice - The original price of the course.
 * @param {number} discountPercentage - The discount percentage to apply.
 * @param {boolean} isMember - Indicates if the user is a member (eligible for additional discount).
 * @returns {number} - The final price after applying the discount.
 * @throws {Error} - Throws an error if originalPrice or discountPercentage are invalid.
 */
function calculateFinalPrice(originalPrice, discountPercentage, isMember) {
    // Validate input parameters
    if (typeof originalPrice !== 'number' || originalPrice < 0) {
        throw new Error('Invalid original price. It must be a non-negative number.');
    }
    if (typeof discountPercentage !== 'number' || discountPercentage < 0 || discountPercentage > 100) {
        throw new Error('Invalid discount percentage. It must be a number between 0 and 100.');
    }
    if (typeof isMember !== 'boolean') {
        throw new Error('Invalid membership status. It must be a boolean value.');
    }

    // Calculate the discount amount
    let discountAmount = (originalPrice * discountPercentage) / 100;

    // Apply an additional member discount if applicable
    if (isMember) {
        discountAmount += (originalPrice * 5) / 100; // Additional 5% discount for members
    }

    // Calculate the final price
    const finalPrice = originalPrice - discountAmount;

    // Return the final price, ensuring it does not go below zero
    return Math.max(finalPrice, 0);
}

// Example usage
try {
    const originalPrice = 200; // Original course price
    const discountPercentage = 10; // Discount percentage
    const isMember = true; // Membership status

    const finalPrice = calculateFinalPrice(originalPrice, discountPercentage, isMember);
    console.log(`The final price after discount is: $${finalPrice.toFixed(2)}`);
} catch (error) {
    console.error(`Error calculating final price: ${error.message}`);
}
```
