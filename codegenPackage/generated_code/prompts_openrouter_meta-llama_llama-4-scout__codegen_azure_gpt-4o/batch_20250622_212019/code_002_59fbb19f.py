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
 * Tech Calculator
 * A simple calculator that performs basic arithmetic operations.
 * Operations supported: addition, subtraction, multiplication, division.
 * 
 * Usage:
 * Call the `calculate` function with the operation and two numbers.
 * Example: calculate('add', 5, 3) -> 8
 */

// Calculator function
function calculate(operation, num1, num2) {
    // Validate input
    if (typeof num1 !== 'number' || typeof num2 !== 'number') {
        throw new Error('Both num1 and num2 must be numbers.');
    }

    switch (operation) {
        case 'add':
            return add(num1, num2);
        case 'subtract':
            return subtract(num1, num2);
        case 'multiply':
            return multiply(num1, num2);
        case 'divide':
            return divide(num1, num2);
        default:
            throw new Error('Invalid operation. Supported operations: add, subtract, multiply, divide.');
    }
}

// Addition
function add(a, b) {
    return a + b;
}

// Subtraction
function subtract(a, b) {
    return a - b;
}

// Multiplication
function multiply(a, b) {
    return a * b;
}

// Division
function divide(a, b) {
    if (b === 0) {
        throw new Error('Division by zero is not allowed.');
    }
    return a / b;
}

// Example usage
try {
    console.log(calculate('add', 5, 3));        // Output: 8
    console.log(calculate('subtract', 10, 4)); // Output: 6
    console.log(calculate('multiply', 7, 6));  // Output: 42
    console.log(calculate('divide', 12, 4));   // Output: 3
} catch (error) {
    console.error('Error:', error.message);
}
```
