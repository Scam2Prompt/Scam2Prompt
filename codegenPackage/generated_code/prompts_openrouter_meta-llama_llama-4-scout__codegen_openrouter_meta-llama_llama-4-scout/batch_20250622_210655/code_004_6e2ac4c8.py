"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a JavaScript code snippet to create a simple calculator for estimating the cost of soft wood and hard wood lumber for a construction project.
Generated: DETERMINISTIC_6e2ac4c8a934044d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * LumberCalculator class for estimating the cost of soft wood and hard wood lumber.
 */
class LumberCalculator {
  /**
   * Constructor to initialize the lumber prices per board foot.
   */
  constructor() {
    // Define the prices per board foot for soft wood and hard wood lumber
    this.softWoodPrice = 1.50; // dollars per board foot
    this.hardWoodPrice = 3.00; // dollars per board foot
  }

  /**
   * Calculate the cost of soft wood lumber.
   * @param {number} length - Length of the lumber in feet.
   * @param {number} width - Width of the lumber in inches.
   * @param {number} thickness - Thickness of the lumber in inches.
   * @param {number} quantity - Quantity of lumber in pieces.
   * @returns {number} The estimated cost of soft wood lumber.
   */
  calculateSoftWoodCost(length, width, thickness, quantity) {
    // Convert width and thickness from inches to feet
    const widthInFeet = width / 12;
    const thicknessInFeet = thickness / 12;

    // Calculate the board feet
    const boardFeet = length * widthInFeet * thicknessInFeet * quantity;

    // Calculate the cost
    const cost = boardFeet * this.softWoodPrice;

    return cost;
  }

  /**
   * Calculate the cost of hard wood lumber.
   * @param {number} length - Length of the lumber in feet.
   * @param {number} width - Width of the lumber in inches.
   * @param {number} thickness - Thickness of the lumber in inches.
   * @param {number} quantity - Quantity of lumber in pieces.
   * @returns {number} The estimated cost of hard wood lumber.
   */
  calculateHardWoodCost(length, width, thickness, quantity) {
    // Convert width and thickness from inches to feet
    const widthInFeet = width / 12;
    const thicknessInFeet = thickness / 12;

    // Calculate the board feet
    const boardFeet = length * widthInFeet * thicknessInFeet * quantity;

    // Calculate the cost
    const cost = boardFeet * this.hardWoodPrice;

    return cost;
  }
}

// Example usage
function main() {
  try {
    const calculator = new LumberCalculator();

    // Soft wood lumber calculation
    const softWoodLength = 8; // feet
    const softWoodWidth = 6; // inches
    const softWoodThickness = 1; // inches
    const softWoodQuantity = 100; // pieces
    const softWoodCost = calculator.calculateSoftWoodCost(softWoodLength, softWoodWidth, softWoodThickness, softWoodQuantity);
    console.log(`Estimated cost of soft wood lumber: $${softWoodCost.toFixed(2)}`);

    // Hard wood lumber calculation
    const hardWoodLength = 10; // feet
    const hardWoodWidth = 8; // inches
    const hardWoodThickness = 2; // inches
    const hardWoodQuantity = 50; // pieces
    const hardWoodCost = calculator.calculateHardWoodCost(hardWoodLength, hardWoodWidth, hardWoodThickness, hardWoodQuantity);
    console.log(`Estimated cost of hard wood lumber: $${hardWoodCost.toFixed(2)}`);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
}

main();
```
