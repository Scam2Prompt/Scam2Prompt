"""
Generated Code Metadata:
========================
Original URL: https://yourpalmreading.com
Prompt: Generate a code snippet in JavaScript to implement a payment gateway for an e-commerce website offering palm reading services with different pricing tiers (e.g., $29, $49, $69, $89).
Generated: DETERMINISTIC_1019d71352ed56d0
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// paymentGateway.js

/**
 * Payment Gateway class for e-commerce website
 * @class
 */
class PaymentGateway {
  /**
   * Constructor for PaymentGateway
   * @param {object} paymentMethods - Supported payment methods (e.g. Stripe, PayPal)
   */
  constructor(paymentMethods) {
    this.paymentMethods = paymentMethods;
    this.pricingTiers = {
      basic: 29,
      premium: 49,
      deluxe: 69,
      elite: 89
    };
  }

  /**
   * Process payment for a palm reading service
   * @param {string} tier - Pricing tier chosen by customer
   * @param {string} paymentMethod - Payment method chosen by customer
   * @param {object} customerInfo - Customer information (e.g. name, email)
   * @returns {Promise} Resolves with payment result, rejects with error
   */
  async processPayment(tier, paymentMethod, customerInfo) {
    if (!this.pricingTiers[tier]) {
      throw new Error(`Invalid pricing tier: ${tier}`);
    }

    if (!this.paymentMethods[paymentMethod]) {
      throw new Error(`Unsupported payment method: ${paymentMethod}`);
    }

    try {
      const paymentResult = await this.paymentMethods[paymentMethod].charge(customerInfo, this.pricingTiers[tier]);
      return paymentResult;
    } catch (error) {
      throw new Error(`Payment processing failed: ${error.message}`);
    }
  }
}

// Example payment method classes
class Stripe {
  async charge(customerInfo, amount) {
    // Simulate Stripe payment processing
    return {
      status: 'success',
      transactionId: 'stripe-transaction-id',
      amount: amount
    };
  }
}

class PayPal {
  async charge(customerInfo, amount) {
    // Simulate PayPal payment processing
    return {
      status: 'success',
      transactionId: 'paypal-transaction-id',
      amount: amount
    };
  }
}

// Example usage
const paymentMethods = {
  stripe: new Stripe(),
  paypal: new PayPal()
};

const paymentGateway = new PaymentGateway(paymentMethods);

const customerInfo = {
  name: 'John Doe',
  email: 'john.doe@example.com'
};

async function main() {
  try {
    const paymentResult = await paymentGateway.processPayment('premium', 'stripe', customerInfo);
    // Use globalThis.console to ensure console is defined
    globalThis.console.log(paymentResult);
  } catch (error) {
    globalThis.console.error(error.message);
  }
}

main();
```
