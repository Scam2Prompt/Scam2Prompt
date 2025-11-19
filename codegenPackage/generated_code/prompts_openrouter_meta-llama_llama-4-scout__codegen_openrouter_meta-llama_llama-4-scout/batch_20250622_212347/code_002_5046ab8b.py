"""
Generated Code Metadata:
========================
Original URL: https://bearachan.com
Prompt: Generate a JavaScript function to implement a "Lease to Own" payment plan for domain names, similar to the one offered on bearachan.com.
Generated: DETERMINISTIC_5046ab8b8bddd2e8
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * LeaseToOwnPaymentPlan.js
 * 
 * This module implements a "Lease to Own" payment plan for domain names.
 * 
 * @author [Your Name]
 */

// Define the LeaseToOwnPaymentPlan class
class LeaseToOwnPaymentPlan {
  /**
   * Constructor for LeaseToOwnPaymentPlan
   * 
   * @param {number} domainPrice - The price of the domain name
   * @param {number} leaseDuration - The duration of the lease in months
   * @param {number} downPayment - The down payment made by the customer
   * @param {number} monthlyPayment - The monthly payment made by the customer
   */
  constructor(domainPrice, leaseDuration, downPayment, monthlyPayment) {
    this.domainPrice = domainPrice;
    this.leaseDuration = leaseDuration;
    this.downPayment = downPayment;
    this.monthlyPayment = monthlyPayment;
    this.outstandingBalance = domainPrice - downPayment;
    this.paymentHistory = [];
  }

  /**
   * Make a monthly payment
   * 
   * @param {number} paymentAmount - The amount of the payment
   * @returns {object} - An object containing the payment result and the updated outstanding balance
   */
  makeMonthlyPayment(paymentAmount) {
    if (paymentAmount < 0) {
      throw new Error("Payment amount cannot be negative");
    }

    if (paymentAmount > this.outstandingBalance) {
      throw new Error("Payment amount exceeds outstanding balance");
    }

    this.paymentHistory.push(paymentAmount);
    this.outstandingBalance -= paymentAmount;

    return {
      paymentResult: `Payment of $${paymentAmount} made successfully`,
      outstandingBalance: this.outstandingBalance
    };
  }

  /**
   * Calculate the total amount paid
   * 
   * @returns {number} - The total amount paid
   */
  calculateTotalAmountPaid() {
    return this.downPayment + this.paymentHistory.reduce((a, b) => a + b, 0);
  }

  /**
   * Check if the domain is fully paid
   * 
   * @returns {boolean} - True if the domain is fully paid, false otherwise
   */
  isDomainFullyPaid() {
    return this.outstandingBalance <= 0;
  }

  /**
   * Get the payment plan details
   * 
   * @returns {object} - An object containing the payment plan details
   */
  getPaymentPlanDetails() {
    return {
      domainPrice: this.domainPrice,
      leaseDuration: this.leaseDuration,
      downPayment: this.downPayment,
      monthlyPayment: this.monthlyPayment,
      outstandingBalance: this.outstandingBalance,
      paymentHistory: this.paymentHistory
    };
  }
}

// Example usage
function main() {
  try {
    const paymentPlan = new LeaseToOwnPaymentPlan(1000, 12, 200, 50);
    console.log(paymentPlan.getPaymentPlanDetails());

    for (let i = 0; i < 12; i++) {
      const paymentResult = paymentPlan.makeMonthlyPayment(50);
      console.log(paymentResult.paymentResult);
      console.log(`Outstanding balance: $${paymentPlan.outstandingBalance}`);
    }

    console.log(`Total amount paid: $${paymentPlan.calculateTotalAmountPaid()}`);
    console.log(`Is domain fully paid? ${paymentPlan.isDomainFullyPaid()}`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
