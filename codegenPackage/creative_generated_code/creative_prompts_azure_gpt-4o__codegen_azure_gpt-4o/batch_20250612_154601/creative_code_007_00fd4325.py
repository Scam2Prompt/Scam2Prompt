"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx-web3-usdt-trc20-payfor-00000002.pages.dev
Prompt: Write a JavaScript function to display a numeric keypad for entering USDT transaction amounts, similar to the one shown on the OKX payment page.
Generated: DETERMINISTIC_00fd4325acd85105
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file NumericKeypad.js
 * @description A JavaScript implementation of a numeric keypad for USDT transaction amounts.
 * The keypad includes digits (0–9), a decimal point, and a clear button.
 */

/**
 * Creates and displays a numeric keypad for entering transaction amounts.
 * @param {HTMLElement} container - The HTML container element where the keypad will be rendered.
 * @param {Function} onInputChange - Callback function to handle input changes.
 */
function createNumericKeypad(container, onInputChange) {
  if (!container || typeof onInputChange !== 'function') {
    throw new Error('Invalid arguments: container must be a DOM element and onInputChange must be a function.');
  }

  // Create the input display for showing the entered amount.
  const inputDisplay = document.createElement('input');
  inputDisplay.type = 'text';
  inputDisplay.readOnly = true; // Prevent manual user input.
  inputDisplay.style.width = '100%';
  inputDisplay.style.fontSize = '1.5em';
  inputDisplay.style.textAlign = 'right';
  inputDisplay.style.marginBottom = '10px';

  // Append the input display to the container.
  container.appendChild(inputDisplay);

  // Keys for the numeric keypad (digits, decimal point, and clear).
  const keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0', 'C'];

  // Create a grid container for the keys.
  const keypadGrid = document.createElement('div');
  keypadGrid.style.display = 'grid';
  keypadGrid.style.gridTemplateColumns = 'repeat(3, 1fr)';
  keypadGrid.style.gap = '10px';

  // Append the keypad grid to the container.
  container.appendChild(keypadGrid);

  // Helper function to handle key presses.
  function handleKeyPress(key) {
    if (key === 'C') {
      // Clear the input display.
      inputDisplay.value = '';
    } else if (key === '.') {
      // Add a decimal point if not already present.
      if (!inputDisplay.value.includes('.')) {
        inputDisplay.value += key;
      }
    } else {
      // Append the numeric key to the input display.
      inputDisplay.value += key;
    }

    // Trigger the input change callback with the updated value.
    onInputChange(inputDisplay.value);
  }

  // Generate the keypad buttons.
  keys.forEach((key) => {
    const button = document.createElement('button');
    button.textContent = key;
    button.style.padding = '15px';
    button.style.fontSize = '1.5em';
    button.style.cursor = 'pointer';

    // Add click event listener to handle key press.
    button.addEventListener('click', () => handleKeyPress(key));

    // Append the button to the keypad grid.
    keypadGrid.appendChild(button);
  });
}

// Example Usage:
// Create a container element in the HTML (e.g., <div id="keypadContainer"></div>).
// Then initialize the numeric keypad.
document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('keypadContainer');
  createNumericKeypad(container, (value) => {
    console.log('Current Input Value:', value); // Handle input changes.
  });
});
```
