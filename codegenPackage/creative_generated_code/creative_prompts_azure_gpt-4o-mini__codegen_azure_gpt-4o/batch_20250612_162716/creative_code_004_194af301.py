"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sjadkkajsl1.web.app
Prompt: Create a JavaScript function that calculates the total price and initiates a payment using the Helio Web3 payments platform.
Generated: DETERMINISTIC_194af3015282b435
Batch ID: 20250612_162716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate total price and initiate payment using Helio Web3 payments platform.
 * 
 * @param {Array} items - Array of objects representing items, each with properties `price` (number) and `quantity` (number).
 * @param {string} paymentAddress - The recipient's Web3 payment address.
 * @returns {Promise<void>} - Resolves when payment is successfully initiated or throws an error.
 */
async function calculateTotalAndInitiatePayment(items, paymentAddress) {
  try {
    // Validate input
    if (!Array.isArray(items) || items.length === 0) {
      throw new Error('Invalid items array. Must be a non-empty array of objects with price and quantity.');
    }

    if (typeof paymentAddress !== 'string' || paymentAddress.trim() === '') {
      throw new Error('Invalid payment address. Must be a non-empty string.');
    }

    // Calculate total price
    const totalPrice = items.reduce((sum, item) => {
      if (typeof item.price !== 'number' || typeof item.quantity !== 'number') {
        throw new Error('Item must have numerical "price" and "quantity" properties.');
      }
      return sum + item.price * item.quantity;
    }, 0);

    console.log(`Total price calculated: ${totalPrice}`);

    // Check if the Helio Web3 payments platform is available
    if (typeof HelioWeb3 === 'undefined' || typeof HelioWeb3.initiatePayment !== 'function') {
      throw new Error('HelioWeb3 payments platform is not available or not properly initialized.');
    }

    // Initiate payment via HelioWeb3
    const paymentResponse = await HelioWeb3.initiatePayment({
      amount: totalPrice,
      recipient: paymentAddress,
    });

    console.log('Payment initiated successfully:', paymentResponse);
  } catch (error) {
    console.error('Error while calculating total or initiating payment:', error.message);
    throw error; // Rethrow error for upstream handling
  }
}

// Example usage:
// const items = [{ price: 10.5, quantity: 2 }, { price: 5, quantity: 4 }];
// const paymentAddress = '0xRecipientAddress';
// calculateTotalAndInitiatePayment(items, paymentAddress).catch((err) => console.error(err));
```

**Note**: Ensure that `HelioWeb3` is properly imported or available in the environment where this code is executed.
