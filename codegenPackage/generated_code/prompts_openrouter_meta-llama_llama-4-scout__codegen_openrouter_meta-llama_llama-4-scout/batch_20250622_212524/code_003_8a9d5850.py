"""
Generated Code Metadata:
========================
Original URL: https://avilhasdolarbraz.blogspot.com
Prompt: Create a JavaScript function to calculate the total cost of items in a shopping cart, considering discounts and installment plans with interest.
Generated: DETERMINISTIC_8a9d5850ff423963
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of items in a shopping cart, considering discounts and installment plans with interest.
 */

/**
 * Represents an item in the shopping cart.
 */
class CartItem {
  /**
   * Creates a new CartItem.
   * @param {string} name - The name of the item.
   * @param {number} price - The price of the item.
   * @param {number} [discount=0] - The discount percentage for the item (default is 0).
   */
  constructor(name, price, discount = 0) {
    this.name = name;
    this.price = price;
    this.discount = discount;
  }

  /**
   * Calculates the price of the item after discount.
   * @returns {number} The price after discount.
   */
  getPriceAfterDiscount() {
    return this.price * (1 - this.discount / 100);
  }
}

/**
 * Represents an installment plan.
 */
class InstallmentPlan {
  /**
   * Creates a new InstallmentPlan.
   * @param {number} interestRate - The interest rate for the installment plan.
   * @param {number} numberOfInstallments - The number of installments.
   */
  constructor(interestRate, numberOfInstallments) {
    this.interestRate = interestRate;
    this.numberOfInstallments = numberOfInstallments;
  }

  /**
   * Calculates the total interest for the installment plan.
   * @param {number} totalCost - The total cost of the items.
   * @returns {number} The total interest.
   */
  calculateInterest(totalCost) {
    // Calculate the monthly interest rate
    const monthlyInterestRate = this.interestRate / 100 / 12;

    // Calculate the total interest using the formula for monthly payments (M) on a fixed rate loan:
    // M = P[r(1+r)^n]/[(1+r)^n – 1]
    // Where:
    //   P = principal loan amount (the initial amount borrowed)
    //   r = monthly interest rate (annual rate / 12)
    //   n = number of payments (the number of months the money is borrowed for)
    const totalInterest =
      totalCost *
        (monthlyInterestRate *
          Math.pow(1 + monthlyInterestRate, this.numberOfInstallments)) /
        (Math.pow(1 + monthlyInterestRate, this.numberOfInstallments) - 1) *
        this.numberOfInstallments -
      totalCost;

    return totalInterest;
  }
}

/**
 * Calculates the total cost of items in a shopping cart, considering discounts and installment plans with interest.
 */
function calculateTotalCost(cartItems, installmentPlan = null) {
  try {
    // Validate input parameters
    if (!Array.isArray(cartItems) || cartItems.length === 0) {
      throw new Error("Cart items must be a non-empty array.");
    }

    let totalCost = 0;

    // Calculate the total cost of items after discounts
    cartItems.forEach((item) => {
      if (!(item instanceof CartItem)) {
        throw new Error("Each cart item must be an instance of CartItem.");
      }
      totalCost += item.getPriceAfterDiscount();
    });

    // If an installment plan is provided, calculate the total interest
    if (installmentPlan instanceof InstallmentPlan) {
      const totalInterest = installmentPlan.calculateInterest(totalCost);
      totalCost += totalInterest;
    }

    return totalCost;
  } catch (error) {
    // Use globalThis.console to ensure console is defined
    globalThis.console.error("Error calculating total cost:", error.message);
    throw error;
  }
}

// Example usage:
function main() {
  try {
    const cartItem1 = new CartItem("Item 1", 100, 10); // 10% discount
    const cartItem2 = new CartItem("Item 2", 200);

    const cartItems = [cartItem1, cartItem2];

    const installmentPlan = new InstallmentPlan(12, 6); // 12% interest rate, 6 installments

    const totalCost = calculateTotalCost(cartItems, installmentPlan);
    globalThis.console.log(`Total cost: $${totalCost.toFixed(2)}`);

    // Test without installment plan
    const totalCostWithoutInstallmentPlan = calculateTotalCost(cartItems);
    globalThis.console.log(`Total cost without installment plan: $${totalCostWithoutInstallmentPlan.toFixed(2)}`);
  } catch (error) {
    globalThis.console.error("Error in main:", error.message);
  }
}

main();
```
