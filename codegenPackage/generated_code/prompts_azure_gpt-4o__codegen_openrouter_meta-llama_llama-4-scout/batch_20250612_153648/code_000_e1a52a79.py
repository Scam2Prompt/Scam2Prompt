"""
Generated Code Metadata:
========================
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Write JavaScript code for a frontend application that mimics the functionality of "The Decipherer" and requires JavaScript to run.
Generated: DETERMINISTIC_e1a52a79a5000e02
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// The Decipherer Application

/**
 * The Decipherer application is a frontend tool that deciphers and encrypts messages.
 */

// Get the DOM elements
const messageInput = document.getElementById('message');
const cipherTypeSelect = document.getElementById('cipher-type');
const shiftInput = document.getElementById('shift');
const resultElement = document.getElementById('result');

// Supported cipher types
const CIPHERS = {
  caesar: 'caesar',
  atbash: 'atbash',
  rot13: 'rot13',
};

/**
 * Handles the deciphering and encrypting of messages.
 */
class TheDecipherer {
  /**
   * Deciphers or encrypts a message based on the selected cipher type and shift.
   * @param {string} message The message to decipher or encrypt.
   * @param {string} cipherType The type of cipher to use.
   * @param {number} shift The shift value for Caesar cipher.
   * @returns {string} The deciphered or encrypted message.
   */
  processMessage(message, cipherType, shift) {
    switch (cipherType) {
      case CIPHERS.caesar:
        return this.caesarCipher(message, shift);
      case CIPHERS.atbash:
        return this.atbashCipher(message);
      case CIPHERS.rot13:
        return this.rot13Cipher(message);
      default:
        throw new Error(`Unsupported cipher type: ${cipherType}`);
    }
  }

  /**
   * Caesar cipher implementation.
   * @param {string} message The message to cipher.
   * @param {number} shift The shift value.
   * @returns {string} The ciphered message.
   */
  caesarCipher(message, shift) {
    return message.split('').map(char => {
      if (char.match(/[a-zA-Z]/)) {
        const asciiOffset = char.charCodeAt(0) < 97 ? 65 : 97;
        return String.fromCharCode((char.charCodeAt(0) - asciiOffset + shift) % 26 + asciiOffset);
      }
      return char;
    }).join('');
  }

  /**
   * Atbash cipher implementation.
   * @param {string} message The message to cipher.
   * @returns {string} The ciphered message.
   */
  atbashCipher(message) {
    return message.split('').map(char => {
      if (char.match(/[a-zA-Z]/)) {
        const asciiOffset = char.charCodeAt(0) < 97 ? 65 : 97;
        return String.fromCharCode(asciiOffset + (25 - (char.charCodeAt(0) - asciiOffset)));
      }
      return char;
    }).join('');
  }

  /**
   * ROT13 cipher implementation.
   * @param {string} message The message to cipher.
   * @returns {string} The ciphered message.
   */
  rot13Cipher(message) {
    return this.caesarCipher(message, 13);
  }
}

// Initialize the Decipherer instance
const decipherer = new TheDecipherer();

// Add event listener to the process button
document.getElementById('process-button').addEventListener('click', () => {
  try {
    const message = messageInput.value.trim();
    const cipherType = cipherTypeSelect.value;
    const shift = parseInt(shiftInput.value, 10);

    if (!message) {
      throw new Error('Please enter a message');
    }

    if (cipherType === CIPHERS.caesar && isNaN(shift)) {
      throw new Error('Please enter a valid shift value for Caesar cipher');
    }

    const result = decipherer.processMessage(message, cipherType, shift);
    resultElement.textContent = result;
  } catch (error) {
    resultElement.textContent = `Error: ${error.message}`;
  }
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Decipherer</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #container {
      max-width: 400px;
      margin: 40px auto;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <div id="container">
    <h1>The Decipherer</h1>
    <label for="message">Message:</label>
    <textarea id="message" rows="5"></textarea>
    <br>
    <label for="cipher-type">Cipher Type:</label>
    <select id="cipher-type">
      <option value="caesar">Caesar</option>
      <option value="atbash">Atbash</option>
      <option value="rot13">ROT13</option>
    </select>
    <br>
    <label for="shift">Shift (for Caesar cipher):</label>
    <input id="shift" type="number" value="3">
    <br>
    <button id="process-button">Process</button>
    <p id="result"></p>
  </div>

  <script src="script.js"></script>
</body>
</html>
```
