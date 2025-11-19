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
 * A calculator that performs basic arithmetic operations:
 * - Addition
 * - Subtraction
 * - Multiplication
 * - Division
 * 
 * Features:
 * - Error handling for invalid inputs
 * - Clear functionality
 * - Supports decimal numbers
 */

class Calculator {
    constructor() {
        this.currentInput = '0';
        this.previousInput = '';
        this.operation = null;
        this.resetScreen = false;
    }

    /**
     * Clears all calculator state
     */
    clear() {
        this.currentInput = '0';
        this.previousInput = '';
        this.operation = null;
        this.resetScreen = false;
    }

    /**
     * Appends a number to the current input
     * @param {string} number - The number to append
     */
    appendNumber(number) {
        if (this.currentInput === '0' || this.resetScreen) {
            this.currentInput = number;
            this.resetScreen = false;
        } else {
            this.currentInput += number;
        }
    }

    /**
     * Adds a decimal point to the current input
     */
    addDecimal() {
        if (this.resetScreen) {
            this.currentInput = '0.';
            this.resetScreen = false;
            return;
        }
        if (!this.currentInput.includes('.')) {
            this.currentInput += '.';
        }
    }

    /**
     * Sets the operation to perform
     * @param {string} op - The operation to set (+, -, *, /)
     */
    chooseOperation(op) {
        if (this.currentInput === '') return;
        if (this.previousInput !== '') {
            this.compute();
        }
        this.operation = op;
        this.previousInput = this.currentInput;
        this.resetScreen = true;
    }

    /**
     * Computes the result of the operation
     */
    compute() {
        let computation;
        const prev = parseFloat(this.previousInput);
        const current = parseFloat(this.currentInput);

        if (isNaN(prev) || isNaN(current)) return;

        switch (this.operation) {
            case '+':
                computation = prev + current;
                break;
            case '-':
                computation = prev - current;
                break;
            case '*':
                computation = prev * current;
                break;
            case '/':
                if (current === 0) {
                    alert("Cannot divide by zero");
                    this.clear();
                    return;
                }
                computation = prev / current;
                break;
            default:
                return;
        }

        this.currentInput = computation.toString();
        this.operation = null;
        this.previousInput = '';
        this.resetScreen = true;
    }

    /**
     * Updates the display with the current input
     * @param {HTMLElement} display - The display element to update
     */
    updateDisplay(display) {
        display.textContent = this.currentInput;
    }
}

// DOM Elements
const numberButtons = document.querySelectorAll('[data-number]');
const operationButtons = document.querySelectorAll('[data-operation]');
const equalsButton = document.querySelector('[data-equals]');
const clearButton = document.querySelector('[data-clear]');
const decimalButton = document.querySelector('[data-decimal]');
const display = document.querySelector('[data-display]');

// Create calculator instance
const calculator = new Calculator();

// Event Listeners
numberButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.appendNumber(button.textContent);
        calculator.updateDisplay(display);
    });
});

operationButtons.forEach(button => {
    button.addEventListener('click', () => {
        calculator.chooseOperation(button.textContent);
        calculator.updateDisplay(display);
    });
});

equalsButton.addEventListener('click', () => {
    calculator.compute();
    calculator.updateDisplay(display);
});

clearButton.addEventListener('click', () => {
    calculator.clear();
    calculator.updateDisplay(display);
});

decimalButton.addEventListener('click', () => {
    calculator.addDecimal();
    calculator.updateDisplay(display);
});
```
