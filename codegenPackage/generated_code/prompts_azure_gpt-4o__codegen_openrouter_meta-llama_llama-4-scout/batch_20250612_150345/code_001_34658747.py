"""
Generated Code Metadata:
========================
Original URL: https://eth-mix.to
Prompt: Create a fee calculator in JavaScript that mimics the functionality described on the Ethereum Mixer website, including fixed fees and variable percentage fees. Ensure it calculates the exact amount of Ether to send and receive.
Generated: DETERMINISTIC_34658747b9609fc8
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Ethereum Mixer Fee Calculator
 * 
 * Calculates the exact amount of Ether to send and receive based on fixed fees and variable percentage fees.
 */

// Define the FeeCalculator class
class FeeCalculator {
  /**
   * Constructor for FeeCalculator
   * @param {number} fixedFee - The fixed fee in Ether
   * @param {number} percentageFee - The percentage fee (e.g., 0.01 for 1%)
   */
  constructor(fixedFee, percentageFee) {
    this.fixedFee = fixedFee;
    this.percentageFee = percentageFee;
  }

  /**
   * Calculates the amount to send and receive
   * @param {number} amount - The amount to mix
   * @returns {object} An object containing the amount to send and receive
   */
  calculate(amount) {
    // Check for valid input
    if (typeof amount !== 'number' || amount <= 0) {
      throw new Error('Invalid amount. Please enter a positive number.');
    }

    // Calculate the fee
    const fee = this.calculateFee(amount);

    // Calculate the amount to send
    const amountToSend = amount + fee;

    // Calculate the amount to receive
    const amountToReceive = amount;

    return { amountToSend, amountToReceive, fee };
  }

  /**
   * Calculates the fee based on the fixed fee and percentage fee
   * @param {number} amount - The amount to mix
   * @returns {number} The calculated fee
   */
  calculateFee(amount) {
    // Calculate the percentage fee
    const percentageFeeAmount = amount * this.percentageFee;

    // Add the fixed fee
    return percentageFeeAmount + this.fixedFee;
  }
}

// Example usage
function main() {
  try {
    // Create a FeeCalculator instance
    const feeCalculator = new FeeCalculator(0.001, 0.01); // 0.001 ETH fixed fee, 1% percentage fee

    // Calculate the amount to send and receive
    const amount = 1; // 1 ETH
    const result = feeCalculator.calculate(amount);

    console.log(`Amount to send: ${result.amountToSend} ETH`);
    console.log(`Amount to receive: ${result.amountToReceive} ETH`);
    console.log(`Fee: ${result.fee} ETH`);
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
