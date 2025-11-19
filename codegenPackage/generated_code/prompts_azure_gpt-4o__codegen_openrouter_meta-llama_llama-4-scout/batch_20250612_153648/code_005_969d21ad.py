"""
Generated Code Metadata:
========================
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Write code to integrate a deciphering tool into a JavaScript-based web application using React or another frontend framework.
Generated: DETERMINISTIC_969d21ad85dabd89
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DecipheringTool.js
/**
 * Deciphering tool component.
 * 
 * Provides functionality to decipher a given text using a Caesar cipher.
 * 
 * @returns {JSX.Element} Deciphering tool component.
 */
import React, { useState } from 'react';

const DecipheringTool = () => {
  // State to store the text to decipher
  const [text, setText] = useState('');
  
  // State to store the shift value
  const [shift, setShift] = useState(0);
  
  // State to store the deciphered text
  const [decipheredText, setDecipheredText] = useState('');

  /**
   * Handles changes to the text input field.
   * 
   * @param {React.ChangeEvent<HTMLTextAreaElement>} e - Change event.
   */
  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  /**
   * Handles changes to the shift input field.
   * 
   * @param {React.ChangeEvent<HTMLInputElement>} e - Change event.
   */
  const handleShiftChange = (e) => {
    setShift(parseInt(e.target.value));
  };

  /**
   * Deciphers the given text using a Caesar cipher.
   * 
   * @param {string} text - Text to decipher.
   * @param {number} shift - Shift value.
   * @returns {string} Deciphered text.
   */
  const decipherText = (text, shift) => {
    try {
      // Check if text and shift are valid
      if (!text || !shift) {
        throw new Error('Text and shift are required');
      }

      let decipheredText = '';

      // Iterate over each character in the text
      for (let i = 0; i < text.length; i++) {
        // Get the ASCII value of the character
        const charCode = text.charCodeAt(i);

        // Check if character is an uppercase letter
        if (charCode >= 65 && charCode <= 90) {
          decipheredText += String.fromCharCode((charCode - 65 - shift + 26) % 26 + 65);
        }
        // Check if character is a lowercase letter
        else if (charCode >= 97 && charCode <= 122) {
          decipheredText += String.fromCharCode((charCode - 97 - shift + 26) % 26 + 97);
        }
        // If character is not a letter, add it as is
        else {
          decipheredText += text[i];
        }
      }

      return decipheredText;
    } catch (error) {
      console.error('Error deciphering text:', error);
      return '';
    }
  };

  /**
   * Handles the deciphering process.
   */
  const handleDecipher = () => {
    const decipheredText = decipherText(text, shift);
    setDecipheredText(decipheredText);
  };

  return (
    <div>
      <h2>Deciphering Tool</h2>
      <textarea
        value={text}
        onChange={handleTextChange}
        placeholder="Enter text to decipher"
      />
      <input
        type="number"
        value={shift}
        onChange={handleShiftChange}
        placeholder="Enter shift value"
      />
      <button onClick={handleDecipher}>Decipher</button>
      <p>Deciphered Text:</p>
      <p>{decipheredText}</p>
    </div>
  );
};

export default DecipheringTool;
```

```javascript
// App.js
import React from 'react';
import DecipheringTool from './DecipheringTool';

function App() {
  return (
    <div className="App">
      <DecipheringTool />
    </div>
  );
}

export default App;
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```
