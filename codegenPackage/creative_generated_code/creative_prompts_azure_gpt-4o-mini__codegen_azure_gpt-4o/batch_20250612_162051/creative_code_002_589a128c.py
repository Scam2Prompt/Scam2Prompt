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
 * processRentalPayment
 * 
 * This function processes online payments for property rentals. It integrates with a mock payment gateway, validates inputs,
 * handles potential errors, and ensures smooth transaction flow.
 * 
 * @param {string} renterName - The name of the renter.
 * @param {string} propertyId - The unique identifier of the rental property.
 * @param {number} amount - The amount to be paid for the rental.
 * @param {string} paymentMethod - The payment method chosen by the renter (e.g., 'credit_card', 'paypal').
 * @param {object} paymentDetails - Contains payment method details (e.g., card number, expiration date, etc.).
 * @returns {Promise<string>} - A Promise resolving to the payment confirmation message.
 */
async function processRentalPayment(renterName, propertyId, amount, paymentMethod, paymentDetails) {
    // Validate inputs
    if (!renterName || typeof renterName !== 'string') {
        throw new Error("Invalid renter name.");
    }
    if (!propertyId || typeof propertyId !== 'string') {
        throw new Error("Invalid property ID.");
    }
    if (isNaN(amount) || amount <= 0) {
        throw new Error("Invalid payment amount. Must be a positive number.");
    }
    if (!paymentMethod || typeof paymentMethod !== 'string' || !['credit_card', 'paypal'].includes(paymentMethod)) {
        throw new Error("Invalid payment method. Accepted methods are 'credit_card' or 'paypal'.");
    }
    if (!paymentDetails || typeof paymentDetails !== 'object') {
        throw new Error("Invalid payment details.");
    }

    // Mock Payment Gateway Integration
    const mockPaymentGateway = async (paymentInfo) => {
        // Simulate payment processing delay
        await new Promise(resolve => setTimeout(resolve, 2000));

        // Return a successful transaction response
        return {
            status: "success",
            transactionId: "TXN12345678",
            message: "Payment processed successfully."
        };
    };

    try {
        // Construct payment information object
        const paymentInfo = {
            renterName,
            propertyId,
            amount,
            paymentMethod,
            paymentDetails
        };

        // Process payment through the gateway
        const response = await mockPaymentGateway(paymentInfo);

        // Check response status
        if (response.status === "success") {
            return `Payment successful! Transaction ID: ${response.transactionId}. Message: ${response.message}`;
        } else {
            throw new Error("Payment failed. Please try again later.");
        }
    } catch (error) {
        // Log the error (could be sent to a monitoring service)
        console.error("Error processing payment:", error);

        // Return error message
        throw new Error("An error occurred while processing the payment. Please contact support.");
    }
}

// Example usage:
// processRentalPayment('John Doe', 'PROP001', 1200, 'credit_card', { cardNumber: '4111111111111111', expiry: '12/24' })
//     .then(console.log)
//     .catch(console.error);
```
