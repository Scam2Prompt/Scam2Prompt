"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Write code to integrate a deciphering tool into a JavaScript-based web application using React or another frontend framework.
Generated: DETERMINISTIC_969d21ad85dabd89
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';

// Define a functional component for the deciphering tool
const DecipherTool = () => {
  // State to hold the input text and the deciphered output
  const [inputText, setInputText] = useState('');
  const [decipheredText, setDecipheredText] = useState('');

  // Function to handle input change
  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  // Function to decipher the input text
  const decipherText = (text) => {
    // Basic Caesar Cipher Deciphering (Shift of 3 for example)
    return text.replace(/[a-zA-Z]/g, (char) => {
      const code = char.charCodeAt(0);
      // Determine if character is uppercase or lowercase
      const base = code >= 65 && code <= 90 ? 65 : 97;
      // Shift back by 3, wrap around using modulo
      return String.fromCharCode(((code - base - 3 + 26) % 26) + base);
    });
  };

  // Function to handle deciphering when the button is clicked
  const handleDecipher = () => {
    try {
      // Validate input
      if (!inputText) {
        throw new Error('Input text is required for deciphering.');
      }
      // Decipher the input text
      const result = decipherText(inputText);
      // Update deciphered text state
      setDecipheredText(result);
    } catch (error) {
      // Log error and notify user
      console.error('Error during deciphering:', error);
      alert(error.message);
    }
  };

  // Render the component
  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
      <h2>Deciphering Tool</h2>
      <textarea 
        rows="4" 
        cols="50" 
        value={inputText} 
        onChange={handleInputChange} 
        placeholder="Enter text to decipher"
      />
      <br />
      <button onClick={handleDecipher}>Decipher</button>
      <h3>Deciphered Text:</h3>
      <textarea 
        rows="4" 
        cols="50" 
        value={decipheredText} 
        readOnly 
        placeholder="Deciphered text will appear here"
      />
    </div>
  );
};

// Export the component for use in other parts of the application
export default DecipherTool;
```
