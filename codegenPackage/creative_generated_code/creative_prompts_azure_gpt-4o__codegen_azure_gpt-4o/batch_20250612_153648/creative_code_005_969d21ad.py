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
// Import necessary modules
import React, { useState } from 'react';

// Deciphering tool function (mock implementation for demonstration purposes)
const decipherText = (cipherText, key) => {
  try {
    // Simulating a simple Caesar cipher decryption
    if (!key || isNaN(key)) throw new Error('Invalid key provided');
    const shift = parseInt(key, 10);
    return cipherText
      .split('')
      .map((char) => {
        if (char.match(/[a-z]/i)) {
          const code = char.charCodeAt(0);
          const offset = char >= 'a' ? 97 : 65;
          return String.fromCharCode(((code - offset - shift + 26) % 26) + offset);
        }
        return char; // Non-alphabetic characters remain unchanged
      })
      .join('');
  } catch (err) {
    throw new Error(`Deciphering failed: ${err.message}`);
  }
};

// React functional component
const DecipherTool = () => {
  // State hooks to manage input and output
  const [cipherText, setCipherText] = useState('');
  const [key, setKey] = useState('');
  const [decipheredText, setDecipheredText] = useState('');
  const [error, setError] = useState(null);

  // Handler for deciphering text
  const handleDecipher = () => {
    try {
      setError(null); // Reset error state
      const result = decipherText(cipherText, key);
      setDecipheredText(result); // Update state with deciphered text
    } catch (err) {
      setDecipheredText(''); // Clear output if error occurs
      setError(err.message); // Set error state
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h1>Deciphering Tool</h1>
      <div style={{ marginBottom: '20px' }}>
        <label>
          Cipher Text:
          <textarea
            value={cipherText}
            onChange={(e) => setCipherText(e.target.value)}
            rows="3"
            style={{ width: '100%', marginTop: '5px' }}
          />
        </label>
      </div>
      <div style={{ marginBottom: '20px' }}>
        <label>
          Key (Shift Value):
          <input
            type="number"
            value={key}
            onChange={(e) => setKey(e.target.value)}
            style={{ width: '100%', marginTop: '5px' }}
          />
        </label>
      </div>
      <button
        onClick={handleDecipher}
        style={{
          padding: '10px 20px',
          backgroundColor: '#007BFF',
          color: '#FFFFFF',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
        }}
      >
        Decipher
      </button>
      {error && (
        <div style={{ color: 'red', marginTop: '20px' }}>
          <strong>Error:</strong> {error}
        </div>
      )}
      {decipheredText && (
        <div style={{ marginTop: '20px', color: 'green' }}>
          <strong>Deciphered Text:</strong> {decipheredText}
        </div>
      )}
    </div>
  );
};

export default DecipherTool;
```

This code is a React functional component for a deciphering tool that uses a Caesar cipher decryption algorithm. It provides proper error handling, clean documentation, and follows best practices for state and event management in React.
