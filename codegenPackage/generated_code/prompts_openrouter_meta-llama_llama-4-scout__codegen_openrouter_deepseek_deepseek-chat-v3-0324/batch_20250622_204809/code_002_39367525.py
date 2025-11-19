"""
Generated Code Metadata:
========================
Original URL: https://enacip.edu.pe
Prompt: "Write a code snippet in JavaScript to implement a simple e-commerce system for selling diplomado memberships, like the one offered by ENACIP, including payment processing and membership validation."
Generated: DETERMINISTIC_39367525422d81e7
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// E-commerce system for ENACIP diplomado memberships
class MembershipSystem {
  constructor() {
    this.memberships = {
      basic: {
        name: 'Basic Membership',
        price: 100,
        duration: '1 year',
        features: ['Access to basic courses', 'Monthly newsletter']
      },
      premium: {
        name: 'Premium Membership',
        price: 200,
        duration: '1 year',
        features: [
          'Access to all courses',
          'Monthly newsletter',
          'Exclusive webinars',
          'Certificate of completion'
        ]
      }
    };
    this.purchases = [];
  }

  /**
   * List available memberships
   * @returns {Array} Available memberships
   */
  listMemberships() {
    return Object.keys(this.memberships).map(key => ({
      id: key,
      ...this.memberships[key]
    }));
  }

  /**
   * Process payment for a membership
   * @param {string} membershipType - Type of membership (basic/premium)
   * @param {Object} paymentDetails - Payment details
   * @param {string} paymentDetails.cardNumber - Credit card number
   * @param {string} paymentDetails.expiry - Card expiry date
   * @param {string} paymentDetails.cvv - Card CVV
   * @param {string} customerEmail - Customer email
   * @returns {Object} Purchase confirmation
   * @throws {Error} If payment fails or invalid membership
   */
  async processPayment(membershipType, paymentDetails, customerEmail) {
    if (!this.memberships[membershipType]) {
      throw new Error('Invalid membership type');
    }

    // Validate payment details
    if (!this._validatePaymentDetails(paymentDetails)) {
      throw new Error('Invalid payment details');
    }

    // Simulate payment processing
    try {
      const paymentResult = await this._simulatePaymentGateway(paymentDetails, this.memberships[membershipType].price);
      
      if (paymentResult.success) {
        const purchase = {
          membershipType,
          customerEmail,
          purchaseDate: new Date(),
          expiryDate: this._calculateExpiryDate(),
          transactionId: paymentResult.transactionId
        };
        
        this.purchases.push(purchase);
        return {
          success: true,
          message: 'Payment processed successfully',
          purchaseDetails: purchase
        };
      } else {
        throw new Error('Payment failed: ' + paymentResult.message);
      }
    } catch (error) {
      throw new Error('Payment processing error: ' + error.message);
    }
  }

  /**
   * Validate a membership
   * @param {string} customerEmail - Customer email to validate
   * @param {string} transactionId - Transaction ID
   * @returns {Object} Validation result
   */
  validateMembership(customerEmail, transactionId) {
    const purchase = this.purchases.find(
      p => p.customerEmail === customerEmail && 
           p.transactionId === transactionId
    );

    if (!purchase) {
      return { valid: false, message: 'No matching purchase found' };
    }

    const now = new Date();
    if (now > purchase.expiryDate) {
      return { valid: false, message: 'Membership has expired' };
    }

    return { 
      valid: true,
      message: 'Membership is valid',
      membershipType: purchase.membershipType,
      expiryDate: purchase.expiryDate
    };
  }

  // Private methods
  _validatePaymentDetails(paymentDetails) {
    // Basic validation - in production use a proper validation library
    return (
      paymentDetails.cardNumber &&
      paymentDetails.cardNumber.length === 16 &&
      paymentDetails.expiry &&
      paymentDetails.cvv &&
      paymentDetails.cvv.length === 3
    );
  }

  async _simulatePaymentGateway(paymentDetails, amount) {
    // Simulate API call to payment gateway
    return new Promise((resolve) => {
      setTimeout(() => {
        // Simulate random success/failure
        const success = Math.random() > 0.1; // 90% success rate
        resolve({
          success,
          transactionId: success ? 'txn_' + Math.random().toString(36).substr(2, 9) : null,
          message: success ? 'Payment processed' : 'Payment declined'
        });
      }, 1000);
    });
  }

  _calculateExpiryDate() {
    const date = new Date();
    date.setFullYear(date.getFullYear() + 1);
    return date;
  }
}

// Example usage:
/*
const enacip = new MembershipSystem();

// List available memberships
console.log(enacip.listMemberships());

// Process payment
enacip.processPayment(
  'premium',
  {
    cardNumber: '4111111111111111',
    expiry: '12/25',
    cvv: '123'
  },
  'student@example.com'
)
.then(confirmation => {
  console.log('Purchase successful:', confirmation);
  
  // Validate membership
  const validation = enacip.validateMembership(
    'student@example.com',
    confirmation.purchaseDetails.transactionId
  );
  console.log('Membership validation:', validation);
})
.catch(error => {
  console.error('Error:', error.message);
});
*/
```
