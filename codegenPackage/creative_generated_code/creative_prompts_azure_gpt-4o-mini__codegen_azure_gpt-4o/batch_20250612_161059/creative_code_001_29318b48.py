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
 * Function to handle purchases from the Official Doge Store.
 * Ensures a portion of the sale goes to charity.
 *
 * @param {string} itemName - Name of the item being purchased.
 * @param {number} itemPrice - Price of the item in USD.
 * @param {number} charityPercentage - Percentage of the sale to go to charity (0-100).
 * @returns {object} - Transaction summary including itemName, totalPaid, charityAmount, and storeEarnings.
 */
function purchaseItem(itemName, itemPrice, charityPercentage) {
  // Input validation
  if (typeof itemName !== 'string' || itemName.trim() === '') {
    throw new Error('Invalid item name. Please provide a valid string.');
  }
  if (typeof itemPrice !== 'number' || itemPrice <= 0) {
    throw new Error('Invalid item price. Please provide a positive number.');
  }
  if (typeof charityPercentage !== 'number' || charityPercentage < 0 || charityPercentage > 100) {
    throw new Error('Invalid charity percentage. Please provide a number between 0 and 100.');
  }

  // Calculate the charity amount and store earnings
  const charityAmount = (itemPrice * charityPercentage) / 100;
  const storeEarnings = itemPrice - charityAmount;

  // Create transaction summary
  const transactionSummary = {
    itemName: itemName,
    totalPaid: itemPrice.toFixed(2),
    charityAmount: charityAmount.toFixed(2),
    storeEarnings: storeEarnings.toFixed(2),
  };

  // Simulate processing the transaction (e.g., deduct funds, update store inventory)
  console.log('Processing transaction...');
  console.log('Transaction successful!');

  // Log transaction summary
  console.log('Transaction Summary:', transactionSummary);

  // Return the transaction summary
  return transactionSummary;
}

// Example usage:
try {
  const result = purchaseItem('Doge T-shirt', 20.0, 10);
  console.log('Result:', result);
} catch (error) {
  console.error('Error:', error.message);
}
```
