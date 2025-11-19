"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purebite.fi
Prompt: Create a JavaScript function that calculates the total price for a three-course meal set, based on the pricing model used by Purebite for their weekend offers.
Generated: DETERMINISTIC_9f32c79c430d8296
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Calculates the total price for a three-course meal set based on Purebite's pricing model for weekend offers.
 *
 * @param {number} starterPrice - The price of the starter.
 * @param {number} mainCoursePrice - The price of the main course.
 * @param {number} dessertPrice - The price of the dessert.
 * @param {number} discountPercentage - The discount percentage applicable (if any).
 * @returns {number} The total price after applying the discount.
 * @throws {Error} Throws an error if any price is negative or discount percentage is out of bounds.
 */
function calculateMealTotal(starterPrice, mainCoursePrice, dessertPrice, discountPercentage = 0) {
    // Validate input parameters
    if (starterPrice < 0 || mainCoursePrice < 0 || dessertPrice < 0) {
        throw new Error("Prices cannot be negative.");
    }
    if (discountPercentage < 0 || discountPercentage > 100) {
        throw new Error("Discount percentage must be between 0 and 100.");
    }

    // Calculate the subtotal for the meal
    const subtotal = starterPrice + mainCoursePrice + dessertPrice;

    // Calculate discount amount
    const discountAmount = (subtotal * discountPercentage) / 100;

    // Calculate total price after discount
    const totalPrice = subtotal - discountAmount;

    // Return total price rounded to two decimal places
    return parseFloat(totalPrice.toFixed(2));
}

// Example usage:
try {
    const total = calculateMealTotal(10, 20, 5, 10);
    console.log(`The total price for the meal is: $${total}`);
} catch (error) {
    console.error(error.message);
}
```
