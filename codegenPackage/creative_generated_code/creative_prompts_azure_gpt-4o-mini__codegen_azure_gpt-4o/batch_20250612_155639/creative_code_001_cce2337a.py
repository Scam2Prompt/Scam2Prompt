"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.best
Prompt: Write a JavaScript function that integrates with a payment processing library to handle secure transactions for an e-commerce site like Celestia, ensuring a smooth checkout experience.
Generated: DETERMINISTIC_cce2337a6e5fb984
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * processPayment - Handles secure transactions using a payment processing library.
 * @param {Object} paymentDetails - An object containing payment information.
 * @param {string} paymentDetails.cardNumber - The credit card number.
 * @param {string} paymentDetails.expiryDate - The expiry date of the card in MM/YY format.
 * @param {string} paymentDetails.cvv - The card's CVV number.
 * @param {number} paymentDetails.amount - The total amount to be charged.
 * @returns {Promise<Object>} - Returns a promise resolving with transaction details or rejecting with an error.
 */

// Import the hypothetical payment processing library
const PaymentProcessor = require('payment-processor-sdk');

// Function to handle payment securely
async function processPayment(paymentDetails) {
  // Validate input parameters
  if (
    !paymentDetails ||
    typeof paymentDetails.cardNumber !== 'string' ||
    typeof paymentDetails.expiryDate !== 'string' ||
    typeof paymentDetails.cvv !== 'string' ||
    typeof paymentDetails.amount !== 'number'
  ) {
    throw new Error('Invalid payment details provided.');
  }

  try {
    // Initialize the payment processor (assume 'initialize' sets up API keys and configs)
    const paymentInstance = new PaymentProcessor({
      apiKey: process.env.PAYMENT_API_KEY, // Use environment variables for sensitive data
      environment: process.env.NODE_ENV === 'production' ? 'live' : 'sandbox', // Use sandbox in non-production environments
    });

    // Call the payment processing library to perform the transaction
    const transaction = await paymentInstance.processTransaction({
      cardNumber: paymentDetails.cardNumber,
      expiryDate: paymentDetails.expiryDate,
      cvv: paymentDetails.cvv,
      amount: paymentDetails.amount,
      currency: 'USD', // Set the currency (customize as needed)
    });

    // Ensure the response is valid
    if (!transaction || !transaction.success) {
      throw new Error(
        transaction.message || 'Payment processing failed. Please try again.'
      );
    }

    // Return the successful transaction details
    return {
      success: true,
      transactionId: transaction.transactionId,
      message: 'Payment processed successfully.',
    };
  } catch (error) {
    // Log the error (use a logging system like Winston or Bunyan for production apps)
    console.error('Payment processing error:', error.message);

    // Return a user-friendly error message
    throw new Error(
      'There was an issue processing your payment. Please contact support or try again later.'
    );
  }
}

// Example usage of the function
(async () => {
  try {
    const paymentDetails = {
      cardNumber: '4111111111111111',
      expiryDate: '12/23',
      cvv: '123',
      amount: 49.99,
    };

    const result = await processPayment(paymentDetails);

    console.log('Payment Result:', result);
  } catch (error) {
    console.error('Error:', error.message);
  }
})();

module.exports = processPayment;
```
