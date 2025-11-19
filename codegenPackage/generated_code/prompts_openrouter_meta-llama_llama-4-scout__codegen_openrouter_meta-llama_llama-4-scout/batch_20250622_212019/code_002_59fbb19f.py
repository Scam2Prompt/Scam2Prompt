"""
Generated Code Metadata:
========================
Original URL: https://ravitechworld.com
Prompt: Generate code for a simple tech calculator using JavaScript.
Generated: DETERMINISTIC_59fbb19f8673502a
Batch ID: 20250622_212019
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simple Tech Calculator
 * 
 * Provides basic calculations for technical applications.
 */

// Calculator class
class Calculator {
  /**
   * Adds two numbers.
   * 
   * @param {number} a - The first number.
   * @param {number} b - The second number.
   * @returns {number} The sum of a and b.
   */
  add(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new Error('Both inputs must be numbers');
    }
    return a + b;
  }

  /**
   * Subtracts b from a.
   * 
   * @param {number} a - The first number.
   * @param {number} b - The second number.
   * @returns {number} The difference of a and b.
   */
  subtract(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new Error('Both inputs must be numbers');
    }
    return a - b;
  }

  /**
   * Multiplies two numbers.
   * 
   * @param {number} a - The first number.
   * @param {number} b - The second number.
   * @returns {number} The product of a and b.
   */
  multiply(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new Error('Both inputs must be numbers');
    }
    return a * b;
  }

  /**
   * Divides a by b.
   * 
   * @param {number} a - The dividend.
   * @param {number} b - The divisor.
   * @returns {number} The quotient of a and b.
   */
  divide(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new Error('Both inputs must be numbers');
    }
    if (b === 0) {
      throw new Error('Cannot divide by zero');
    }
    return a / b;
  }

  /**
   * Calculates the power of a number.
   * 
   * @param {number} base - The base number.
   * @param {number} exponent - The exponent.
   * @returns {number} The result of base raised to the power of exponent.
   */
  power(base, exponent) {
    if (typeof base !== 'number' || typeof exponent !== 'number') {
      throw new Error('Both inputs must be numbers');
    }
    return Math.pow(base, exponent);
  }

  /**
   * Calculates the square root of a number.
   * 
   * @param {number} number - The number.
   * @returns {number} The square root of the number.
   */
  sqrt(number) {
    if (typeof number !== 'number') {
      throw new Error('Input must be a number');
    }
    if (number < 0) {
      throw new Error('Cannot calculate square root of a negative number');
    }
    return Math.sqrt(number);
  }
}

// Main function
function main() {
  const calculator = new Calculator();

  // Example usage
  try {
    console.log(calculator.add(5, 3)); // Output: 8
    console.log(calculator.subtract(10, 4)); // Output: 6
    console.log(calculator.multiply(7, 2)); // Output: 14
    console.log(calculator.divide(9, 3)); // Output: 3
    console.log(calculator.power(2, 3)); // Output: 8
    console.log(calculator.sqrt(16)); // Output: 4
  } catch (error) {
    console.error(error.message);
  }
}

// Run the main function
main();
```
