"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: Develop JavaScript code for a virtual keyboard feature that allows users to input text on a jewelry website, similar to Wonderino's accessibility options.
Generated: DETERMINISTIC_602ac092401ce907
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// VirtualKeyboard.js

class VirtualKeyboard {
  /**
   * Constructor for VirtualKeyboard
   * @param {HTMLElement} container - The container element for the virtual keyboard
   * @param {HTMLInputElement} inputField - The input field for text entry
   */
  constructor(container, inputField) {
    this.container = container;
    this.inputField = inputField;
    this.keyboardLayout = [
      ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
      ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
      ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    ];
    this.createKeyboard();
  }

  /**
   * Creates the virtual keyboard
   */
  createKeyboard() {
    const keyboardContainer = document.createElement('div');
    keyboardContainer.classList.add('virtual-keyboard');

    this.keyboardLayout.forEach((row, rowIndex) => {
      const rowContainer = document.createElement('div');
      rowContainer.classList.add('keyboard-row');

      row.forEach((key) => {
        const keyButton = document.createElement('button');
        keyButton.textContent = key.toUpperCase();
        keyButton.classList.add('keyboard-key');
        keyButton.addEventListener('click', () => this.handleKeyPress(key));

        rowContainer.appendChild(keyButton);
      });

      keyboardContainer.appendChild(rowContainer);
    });

    // Add space bar
    const spaceBar = document.createElement('button');
    spaceBar.textContent = 'Space';
    spaceBar.classList.add('keyboard-space-bar');
    spaceBar.addEventListener('click', () => this.handleKeyPress(' '));

    keyboardContainer.appendChild(spaceBar);

    // Add backspace
    const backspaceButton = document.createElement('button');
    backspaceButton.textContent = 'Backspace';
    backspaceButton.classList.add('keyboard-backspace');
    backspaceButton.addEventListener('click', () => this.handleBackspace());

    keyboardContainer.appendChild(backspaceButton);

    this.container.appendChild(keyboardContainer);
  }

  /**
   * Handles key press event
   * @param {string} key - The pressed key
   */
  handleKeyPress(key) {
    try {
      this.inputField.value += key;
      this.inputField.dispatchEvent(new Event('input'));
    } catch (error) {
      console.error('Error handling key press:', error);
    }
  }

  /**
   * Handles backspace press event
   */
  handleBackspace() {
    try {
      this.inputField.value = this.inputField.value.slice(0, -1);
      this.inputField.dispatchEvent(new Event('input'));
    } catch (error) {
      console.error('Error handling backspace:', error);
    }
  }
}

// Initialize virtual keyboard
document.addEventListener('DOMContentLoaded', () => {
  const keyboardContainer = document.getElementById('virtual-keyboard-container');
  const inputField = document.getElementById('jewelry-input-field');

  if (keyboardContainer && inputField) {
    new VirtualKeyboard(keyboardContainer, inputField);
  } else {
    console.error('Virtual keyboard container or input field not found');
  }
});
```

```css
/* styles.css */

.virtual-keyboard {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.keyboard-row {
  display: flex;
  margin-bottom: 10px;
}

.keyboard-key {
  width: 30px;
  height: 30px;
  margin: 0 5px;
  border: none;
  border-radius: 5px;
  background-color: #f0f0f0;
  cursor: pointer;
}

.keyboard-key:hover {
  background-color: #e0e0e0;
}

.keyboard-space-bar {
  width: 100px;
  height: 30px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  background-color: #f0f0f0;
  cursor: pointer;
}

.keyboard-space-bar:hover {
  background-color: #e0e0e0;
}

.keyboard-backspace {
  width: 80px;
  height: 30px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  background-color: #f0f0f0;
  cursor: pointer;
}

.keyboard-backspace:hover {
  background-color: #e0e0e0;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jewelry Website</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <input id="jewelry-input-field" type="text" placeholder="Enter text">
  <div id="virtual-keyboard-container"></div>
  <script src="VirtualKeyboard.js"></script>
</body>
</html>
```
