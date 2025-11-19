"""
Generated Code Metadata:
========================
Original URL: https://www.seedify.cloud
Prompt: Write JavaScript code to create a CAPTCHA system that asks users to solve math problems before submitting a form, similar to the verification process on seedify.cloud.
Generated: DETERMINISTIC_f0cc8182f6ef3289
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Captcha.js

class Captcha {
  /**
   * Creates a new Captcha instance.
   */
  constructor() {
    this.numbers = [];
    this.operators = [
      { symbol: "+", func: (a, b) => a + b },
      { symbol: "-", func: (a, b) => a - b },
      { symbol: "*", func: (a, b) => a * b },
    ];
    this.generateCaptcha();
  }

  /**
   * Generates a new CAPTCHA.
   */
  generateCaptcha() {
    this.numbers = [this.getRandomNumber(), this.getRandomNumber()];
    const operator = this.operators[Math.floor(Math.random() * this.operators.length)];
    this.captcha = {
      num1: this.numbers[0],
      operator: operator.symbol,
      num2: this.numbers[1],
      solution: operator.func(this.numbers[0], this.numbers[1]),
    };
  }

  /**
   * Returns a random number between 1 and 10.
   * @returns {number}
   */
  getRandomNumber() {
    return Math.floor(Math.random() * 10) + 1;
  }

  /**
   * Validates the user's answer.
   * @param {number} userAnswer
   * @returns {boolean}
   */
  validateAnswer(userAnswer) {
    return userAnswer === this.captcha.solution;
  }
}

// FormHandler.js

class FormHandler {
  /**
   * Creates a new FormHandler instance.
   * @param {HTMLFormElement} form
   * @param {Captcha} captcha
   */
  constructor(form, captcha) {
    this.form = form;
    this.captcha = captcha;
    this.init();
  }

  /**
   * Initializes the form handler.
   */
  init() {
    this.form.addEventListener("submit", (e) => this.handleSubmit(e));
  }

  /**
   * Handles the form submission.
   * @param {Event} e
   */
  handleSubmit(e) {
    e.preventDefault();
    const userAnswer = parseInt(document.getElementById("captcha-answer").value);
    if (this.captcha.validateAnswer(userAnswer)) {
      // Submit the form programmatically or allow it to submit normally
      console.log("CAPTCHA solved correctly. Allowing form submission...");
      // this.form.submit(); // Uncomment to submit the form programmatically
    } else {
      alert("Incorrect CAPTCHA answer. Please try again.");
      this.captcha.generateCaptcha();
      this.updateCaptchaDisplay();
    }
  }

  /**
   * Updates the CAPTCHA display.
   */
  updateCaptchaDisplay() {
    document.getElementById("captcha-question").innerText = `${this.captcha.captcha.num1} ${this.captcha.captcha.operator} ${this.captcha.captcha.num2}`;
    document.getElementById("captcha-answer").value = ""; // Clear the input field
  }
}

// Main execution
document.addEventListener("DOMContentLoaded", () => {
  const captcha = new Captcha();
  const form = document.getElementById("myForm");
  const formHandler = new FormHandler(form, captcha);

  // Initialize CAPTCHA display
  document.getElementById("captcha-question").innerText = `${captcha.captcha.num1} ${captcha.captcha.operator} ${captcha.captcha.num2}`;
});

// Example HTML
// <form id="myForm">
//   <p id="captcha-question"></p>
//   <input type="number" id="captcha-answer">
//   <button type="submit">Submit</button>
// </form>
```
