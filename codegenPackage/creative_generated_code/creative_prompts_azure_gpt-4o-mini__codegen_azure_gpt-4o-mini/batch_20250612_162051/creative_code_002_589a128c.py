"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Create a JavaScript function that enables online payment processing for property rentals, inspired by the online payment options mentioned on the Félix Trujillo Falla website.
Generated: DETERMINISTIC_589a128ce6b9286a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Processes an online payment for property rentals.
 * This function simulates the payment processing logic, including
 * validation of payment details and potential error handling.
 * 
 * @param {Object} paymentData - An object containing payment details.
 * @param {string} paymentData.cardNumber - Credit card number.
 * @param {string} paymentData.expiryDate - Expiry date of the card (MM/YY).
 * @param {string} paymentData.cvc - CVC code of the card.
 * @param {number} paymentData.amount - Amount to be charged.
 * @returns {Promise<string>} - A promise that resolves to a success message or rejects with an error.
 */
async function processRentalPayment(paymentData) {
    // Basic validation of payment data
    if (!paymentData || typeof paymentData !== 'object') {
        throw new Error('Invalid payment data provided.');
    }
    
    const { cardNumber, expiryDate, cvc, amount } = paymentData;

    // Validate card number (simple length check for demonstration)
    if (!cardNumber || cardNumber.length !== 16) {
        throw new Error('Invalid credit card number.');
    }

    // Validate expiry date (basic format check)
    const expiryRegex = /^(0[1-9]|1[0-2])\/\d{2}$/;
    if (!expiryDate || !expiryRegex.test(expiryDate)) {
        throw new Error('Invalid expiry date. Format must be MM/YY.');
    }

    // Validate CVC (basic length check for demonstration)
    if (!cvc || cvc.length !== 3) {
        throw new Error('Invalid CVC code.');
    }

    // Validate amount
    if (typeof amount !== 'number' || amount <= 0) {
        throw new Error('Invalid payment amount.');
    }

    // Simulate payment processing (replace this with actual payment gateway API call)
    try {
        console.log(`Processing payment of $${amount}...`);
        
        // Simulate a network request (mocking a delay for demonstration)
        await new Promise((resolve, reject) => {
            setTimeout(() => {
                // Randomly simulate success or failure
                Math.random() > 0.1 ? resolve() : reject(new Error('Payment processing failed.'));
            }, 2000);
        });

        console.log('Payment processed successfully.');
        return 'Payment successful! Thank you for your rental payment.';
    } catch (error) {
        throw new Error(`Payment processing error: ${error.message}`);
    }
}

// Example usage (uncomment to run)
// processRentalPayment({
//     cardNumber: '1234567812345678',
//     expiryDate: '12/23',
//     cvc: '123',
//     amount: 150.00
// })
// .then(successMessage => console.log(successMessage))
// .catch(error => console.error(error));
```
