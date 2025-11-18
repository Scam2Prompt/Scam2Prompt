"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://printserves.com
Prompt: Create a function in JavaScript that simulates the checkout process for Printserves Nigeria, including payment options like ATM card and bank transfer.
Generated: DETERMINISTIC_6f184e421995da68
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates the checkout process for Printserves Nigeria.
 * This function allows users to select a payment method and processes the payment accordingly.
 * 
 * @param {number} totalAmount - The total amount for the purchase.
 * @param {string} paymentMethod - The chosen payment method: 'ATM Card' or 'Bank Transfer'.
 * @returns {string} - A message indicating the result of the payment process.
 * @throws {Error} - Throws an error if the payment method is invalid or if the total amount is not a positive number.
 */

function checkout(totalAmount, paymentMethod) {
    // Validate total amount
    if (typeof totalAmount !== 'number' || totalAmount <= 0) {
        throw new Error('Invalid total amount. It must be a positive number.');
    }

    // Validate payment method
    const validPaymentMethods = ['ATM Card', 'Bank Transfer'];
    if (!validPaymentMethods.includes(paymentMethod)) {
        throw new Error('Invalid payment method. Choose either "ATM Card" or "Bank Transfer".');
    }

    // Simulate payment processing
    try {
        switch (paymentMethod) {
            case 'ATM Card':
                return processAtmCardPayment(totalAmount);
            case 'Bank Transfer':
                return processBankTransferPayment(totalAmount);
            default:
                throw new Error('Unknown payment method.');
        }
    } catch (error) {
        // Log the error and return a failure message
        console.error('Payment processing error:', error);
        return 'Payment processing failed. Please try again.';
    }
}

/**
 * Processes an ATM card payment.
 * 
 * @param {number} amount - The amount to be processed.
 * @returns {string} - Confirmation message for ATM card payment.
 */
function processAtmCardPayment(amount) {
    // Simulating the payment process
    // In a real application, this would involve API calls to payment gateways
    return `ATM Card payment of NGN ${amount.toFixed(2)} processed successfully.`;
}

/**
 * Processes a bank transfer payment.
 * 
 * @param {number} amount - The amount to be processed.
 * @returns {string} - Confirmation message for bank transfer payment.
 */
function processBankTransferPayment(amount) {
    // Simulating the payment process
    // In a real application, this could involve sending transfer details to the user
    return `Bank Transfer of NGN ${amount.toFixed(2)} initiated successfully. Please check your bank for confirmation.`;
}

// Example usage:
try {
    const result = checkout(5000, 'ATM Card');
    console.log(result);
} catch (error) {
    console.error(error.message);
}
```
