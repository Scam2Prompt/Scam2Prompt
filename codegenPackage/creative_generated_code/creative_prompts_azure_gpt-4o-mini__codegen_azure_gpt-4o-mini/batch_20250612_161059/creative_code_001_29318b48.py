"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialcocoro.xyz
Prompt: Write a JavaScript function that allows users to purchase items from the Official Doge Store, ensuring that a portion of the sale goes to charity.
Generated: DETERMINISTIC_29318b48c66bf8d7
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Purchase an item from the Official Doge Store.
 * A portion of the sale goes to charity.
 *
 * @param {string} itemId - The unique identifier of the item being purchased.
 * @param {number} quantity - The number of items to purchase.
 * @param {number} itemPrice - The price of a single item.
 * @param {number} charityPercentage - The percentage of the sale that goes to charity (0-100).
 * @returns {Promise<string>} - A message indicating the purchase result.
 * @throws {Error} - Throws an error if the input parameters are invalid.
 */
async function purchaseItem(itemId, quantity, itemPrice, charityPercentage) {
    // Validate inputs
    if (typeof itemId !== 'string' || itemId.trim() === '') {
        throw new Error('Invalid item ID. It must be a non-empty string.');
    }

    if (typeof quantity !== 'number' || quantity <= 0) {
        throw new Error('Invalid quantity. It must be a positive number.');
    }

    if (typeof itemPrice !== 'number' || itemPrice < 0) {
        throw new Error('Invalid item price. It cannot be negative.');
    }

    if (typeof charityPercentage !== 'number' || charityPercentage < 0 || charityPercentage > 100) {
        throw new Error('Invalid charity percentage. It must be between 0 and 100.');
    }

    // Calculate total price and charity donation
    const totalAmount = itemPrice * quantity;
    const charityAmount = (charityPercentage / 100) * totalAmount;

    // Simulate an asynchronous purchase process (e.g., API call)
    try {
        // Mocking a successful purchase process (replace with actual API logic)
        await new Promise((resolve) => setTimeout(resolve, 1000));

        // Log the transaction details
        console.log(`Purchased ${quantity} of item ID: ${itemId} for $${totalAmount.toFixed(2)}.`);
        console.log(`Donating $${charityAmount.toFixed(2)} to charity.`);

        return `Purchase successful! You bought ${quantity} of item ${itemId}. Thank you for your support!`;
    } catch (error) {
        // Handle any errors that may occur during the purchase process
        throw new Error('Purchase failed. Please try again later. Error: ' + error.message);
    }
}

// Example usage (uncomment to test):
// purchaseItem('doge-tshirt', 2, 19.99, 10)
//     .then((message) => console.log(message))
//     .catch((error) => console.error(error.message));
```
