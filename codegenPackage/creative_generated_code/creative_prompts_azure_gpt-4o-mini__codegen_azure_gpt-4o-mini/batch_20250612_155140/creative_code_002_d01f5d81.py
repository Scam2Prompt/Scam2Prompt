"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Write a function in JavaScript that displays a special price for users identified as best friends on a shopping platform.
Generated: DETERMINISTIC_d01f5d8133f2b734
Batch ID: 20250612_155140
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to display a special price for best friends on a shopping platform.
 * @param {Object} user - The user object containing user information.
 * @param {number} originalPrice - The original price of the product.
 * @returns {number} - The special price for best friends or the original price if not a best friend.
 * @throws {Error} - Throws an error if the user object is invalid or if the price is negative.
 */
function getSpecialPrice(user, originalPrice) {
    // Validate input parameters
    if (typeof user !== 'object' || user === null) {
        throw new Error('Invalid user object. Please provide a valid user.');
    }
    
    if (typeof originalPrice !== 'number' || originalPrice < 0) {
        throw new Error('Invalid price. Price must be a non-negative number.');
    }

    // Check if the user is a best friend
    const isBestFriend = user.isBestFriend === true;

    // Define the special discount for best friends
    const discountRate = 0.20; // 20% discount

    // Calculate the special price if the user is a best friend
    if (isBestFriend) {
        const specialPrice = originalPrice * (1 - discountRate);
        return parseFloat(specialPrice.toFixed(2)); // Return the special price rounded to 2 decimal places
    }

    // Return the original price if not a best friend
    return parseFloat(originalPrice.toFixed(2)); // Return the original price rounded to 2 decimal places
}

// Example usage
try {
    const user = { name: 'Alice', isBestFriend: true };
    const originalPrice = 100;
    const specialPrice = getSpecialPrice(user, originalPrice);
    console.log(`Special Price for ${user.name}: $${specialPrice}`); // Outputs: Special Price for Alice: $80.00
} catch (error) {
    console.error(error.message);
}
```
