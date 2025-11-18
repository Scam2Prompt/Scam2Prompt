"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Write JavaScript code for a frontend application that mimics the functionality of "The Decipherer" and requires JavaScript to run.
Generated: DETERMINISTIC_e1a52a79a5000e02
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * The Decipherer: A simple frontend application that deciphers encoded messages.
 * 
 * This application includes:
 * - A message input field for encoded text.
 * - A button to trigger the deciphering process.
 * - An output area to display the deciphered message.
 * 
 * Functionality:
 * - The decoding logic assumes the encoded message uses a Caesar cipher with a shift of 3.
 * - Supports basic error handling and validates the input.
 */

// Self-contained function to initialize the application
(function() {
  // Constants and Utility Functions
  const DECIPHER_SHIFT = 3; // Shift used for decoding the message
  
  /**
   * Deciphers an encoded message using Caesar cipher logic.
   * @param {string} encodedMessage - The message to be decoded.
   * @returns {string} - The decoded message.
   */
  function decipherMessage(encodedMessage) {
    if (!encodedMessage) {
      throw new Error('Encoded message cannot be empty.');
    }

    let deciphered = '';
    for (let char of encodedMessage) {
      // Check if the character is a letter
      if (char.match(/[a-zA-Z]/)) {
        const isUpperCase = char === char.toUpperCase();
        const baseCharCode = isUpperCase ? 'A'.charCodeAt(0) : 'a'.charCodeAt(0);
        // Shift the character by DECIPHER_SHIFT and wrap around alphabetically
        const shiftedCharCode = 
          ((char.charCodeAt(0) - baseCharCode - DECIPHER_SHIFT + 26) % 26) + baseCharCode;
        deciphered += String.fromCharCode(shiftedCharCode);
      } else {
        // Non-alphabetic characters remain unchanged
        deciphered += char;
      }
    }

    return deciphered;
  }

  // DOM Elements
  const appContainer = document.createElement('div');
  appContainer.style.fontFamily = 'Arial, sans-serif';
  appContainer.style.maxWidth = '600px';
  appContainer.style.margin = '20px auto';
  appContainer.style.padding = '20px';
  appContainer.style.border = '1px solid #ddd';
  appContainer.style.borderRadius = '8px';
  appContainer.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.1)';
  document.body.appendChild(appContainer);

  const heading = document.createElement('h1');
  heading.textContent = 'The Decipherer';
  heading.style.color = '#333';
  heading.style.marginBottom = '12px';
  appContainer.appendChild(heading);

  const inputLabel = document.createElement('label');
  inputLabel.textContent = 'Enter Encoded Message:';
  inputLabel.style.display = 'block';
  inputLabel.style.marginBottom = '8px';
  inputLabel.style.fontWeight = 'bold';
  appContainer.appendChild(inputLabel);

  const inputField = document.createElement('textarea');
  inputField.style.width = '100%';
  inputField.style.height = '80px';
  inputField.style.marginBottom = '12px';
  inputField.style.padding = '8px';
  inputField.style.border = '1px solid #ccc';
  inputField.style.borderRadius = '4px';
  inputField.style.fontSize = '16px';
  appContainer.appendChild(inputField);

  const decipherButton = document.createElement('button');
  decipherButton.textContent = 'Decipher';
  decipherButton.style.padding = '10px 20px';
  decipherButton.style.backgroundColor = '#4CAF50';
  decipherButton.style.color = '#fff';
  decipherButton.style.border = 'none';
  decipherButton.style.borderRadius = '4px';
  decipherButton.style.cursor = 'pointer';
  decipherButton.style.fontWeight = 'bold';
  decipherButton.style.fontSize = '16px';
  appContainer.appendChild(decipherButton);

  const outputContainer = document.createElement('div');
  outputContainer.style.marginTop = '20px';
  outputContainer.style.padding = '10px';
  outputContainer.style.border = '1px solid #ddd';
  outputContainer.style.borderRadius = '4px';
  outputContainer.style.backgroundColor = '#f9f9f9';
  outputContainer.style.fontSize = '16px';
  outputContainer.style.minHeight = '50px';
  outputContainer.textContent = 'Deciphered message will appear here.';
  appContainer.appendChild(outputContainer);

  // Event Listener for Decipher Button
  decipherButton.addEventListener('click', () => {
    try {
      const encodedMessage = inputField.value.trim();
      if (!encodedMessage) {
        throw new Error('Please enter an encoded message.');
      }

      const decipheredMessage = decipherMessage(encodedMessage);
      outputContainer.textContent = decipheredMessage;
      outputContainer.style.color = '#333'; // Reset text color
    } catch (error) {
      outputContainer.textContent = `Error: ${error.message}`;
      outputContainer.style.color = 'red'; // Highlight error messages
    }
  });
})();
```
