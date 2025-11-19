"""
Generated Code Metadata:
========================
Original URL: https://seedify.cloud
Prompt: Provide JavaScript code to dynamically generate math problems (e.g., "6 + 10") for CAPTCHA verification on a webpage.
Generated: DETERMINISTIC_2fd99490b8b29a17
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CAPTCHA Math Problem Generator
 * Generates simple math problems for CAPTCHA verification
 */

class MathCaptcha {
  /**
   * Initialize the CAPTCHA generator with configuration
   * @param {Object} config - Configuration options
   * @param {number} config.min - Minimum number value
   * @param {number} config.max - Maximum number value
   * @param {string[]} config.operators - Allowed operators (+, -, *)
   */
  constructor(config = {}) {
    this.config = {
      min: 1,
      max: 20,
      operators: ['+', '-', '*'],
      ...config
    };
    this.currentProblem = null;
    this.currentAnswer = null;
  }

  /**
   * Generate a random integer between min and max (inclusive)
   * @param {number} min - Minimum value
   * @param {number} max - Maximum value
   * @returns {number} Random integer
   */
  _getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  /**
   * Generate a new math problem
   * @returns {Object} Problem and answer {problem: string, answer: number}
   */
  generate() {
    const num1 = this._getRandomInt(this.config.min, this.config.max);
    const num2 = this._getRandomInt(this.config.min, this.config.max);
    const operator = this.config.operators[
      this._getRandomInt(0, this.config.operators.length - 1)
    ];

    let answer;
    switch (operator) {
      case '+':
        answer = num1 + num2;
        break;
      case '-':
        answer = num1 - num2;
        break;
      case '*':
        answer = num1 * num2;
        break;
      default:
        throw new Error(`Unsupported operator: ${operator}`);
    }

    this.currentProblem = `${num1} ${operator} ${num2}`;
    this.currentAnswer = answer;

    return {
      problem: this.currentProblem,
      answer: this.currentAnswer
    };
  }

  /**
   * Verify user's answer against the current problem
   * @param {number|string} userAnswer - User's answer to verify
   * @returns {boolean} True if answer is correct, false otherwise
   */
  verify(userAnswer) {
    if (this.currentAnswer === null) {
      throw new Error('No problem generated yet');
    }

    const parsedAnswer = typeof userAnswer === 'string' 
      ? parseInt(userAnswer, 10) 
      : userAnswer;

    if (isNaN(parsedAnswer)) {
      return false;
    }

    return parsedAnswer === this.currentAnswer;
  }

  /**
   * Get the current problem (without regenerating)
   * @returns {string} Current math problem
   */
  getCurrentProblem() {
    if (!this.currentProblem) {
      throw new Error('No problem generated yet');
    }
    return this.currentProblem;
  }
}

// Example usage:
/*
const captcha = new MathCaptcha();
const { problem, answer } = captcha.generate();
console.log(`Solve: ${problem}`);

// Simulate user input
const userAnswer = prompt(`What is ${problem}?`);
const isValid = captcha.verify(userAnswer);
console.log(isValid ? 'Correct!' : 'Incorrect, please try again.');
*/
```
