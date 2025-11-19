"""
Generated Code Metadata:
========================
Original URL: https://www.metisassets.com
Prompt: Generate a JavaScript code snippet for a simple calculator that estimates the cash offer for a house in San Francisco Bay Area based on user input.
Generated: DETERMINISTIC_ae3d2d7c542b2778
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the estimated cash offer for a house in San Francisco Bay Area.
 */

// Define the Calculator class
class BayAreaHouseCalculator {
  /**
   * Constructor for the calculator.
   * @param {number} purchasePrice - The purchase price of the house.
   * @param {number} rehabCost - The cost of rehabilitation.
   * @param {number} desiredProfit - The desired profit margin.
   * @param {number} closingCost - The closing cost percentage.
   * @param {number} wholesaleFee - The wholesale fee percentage.
   */
  constructor(purchasePrice, rehabCost, desiredProfit, closingCost = 2, wholesaleFee = 5) {
    this.purchasePrice = purchasePrice;
    this.rehabCost = rehabCost;
    this.desiredProfit = desiredProfit;
    this.closingCost = closingCost / 100; // convert to decimal
    this.wholesaleFee = wholesaleFee / 100; // convert to decimal
  }

  /**
   * Calculates the estimated cash offer.
   * @returns {number} The estimated cash offer.
   */
  calculateCashOffer() {
    // Calculate the total cost
    const totalCost = this.purchasePrice + this.rehabCost;

    // Calculate the desired selling price
    const desiredSellingPrice = totalCost + this.desiredProfit;

    // Calculate the estimated cash offer
    const estimatedCashOffer = desiredSellingPrice - (desiredSellingPrice * this.closingCost) - (desiredSellingPrice * this.wholesaleFee);

    return estimatedCashOffer;
  }
}

// Main function
function main() {
  try {
    // Get user input
    const purchasePrice = parseFloat(prompt("Enter the purchase price of the house: $"));
    const rehabCost = parseFloat(prompt("Enter the rehabilitation cost: $"));
    const desiredProfit = parseFloat(prompt("Enter the desired profit: $"));

    // Validate user input
    if (isNaN(purchasePrice) || isNaN(rehabCost) || isNaN(desiredProfit)) {
      throw new Error("Invalid input. Please enter a valid number.");
    }

    // Create a new calculator instance
    const calculator = new BayAreaHouseCalculator(purchasePrice, rehabCost, desiredProfit);

    // Calculate and display the estimated cash offer
    const estimatedCashOffer = calculator.calculateCashOffer();
    console.log(`The estimated cash offer is: $${estimatedCashOffer.toFixed(2)}`);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

// Call the main function
main();
```
