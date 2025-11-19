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
// Import necessary libraries
import React, { useState } from 'react';

// A simple deciphering function that shifts characters by a given number
const decipherText = (text, shift) => {
    return text.split('').map(char => {
        // Check if character is a letter
        if (/[a-zA-Z]/.test(char)) {
            const code = char.charCodeAt(0);
            const base = code >= 65 && code <= 90 ? 65 : 97; // ASCII base for uppercase and lowercase
            return String.fromCharCode(((code - base - shift + 26) % 26) + base);
        }
        return char; // Non-letter characters are returned unchanged
    }).join('');
};

// Main component for the deciphering tool
const DecipherTool = () => {
    // State variables for input text, shift value, and output text
    const [inputText, setInputText] = useState('');
    const [shiftValue, setShiftValue] = useState(0);
    const [outputText, setOutputText] = useState('');

    // Handler for deciphering the text
    const handleDecipher = () => {
        try {
            // Validate shift value
            const shift = parseInt(shiftValue, 10);
            if (isNaN(shift)) {
                throw new Error('Shift value must be a number');
            }
            // Decipher the input text
            const deciphered = decipherText(inputText, shift);
            setOutputText(deciphered);
        } catch (error) {
            // Handle errors gracefully
            console.error('Error during deciphering:', error);
            alert(error.message);
        }
    };

    return (
        <div style={{ padding: '20px', maxWidth: '400px', margin: 'auto' }}>
            <h2>Decipher Tool</h2>
            <textarea
                rows="4"
                placeholder="Enter text to decipher"
                value={inputText}
                onChange={(e) => setInputText(e.target.value)}
                style={{ width: '100%', marginBottom: '10px' }}
            />
            <input
                type="number"
                placeholder="Enter shift value"
                value={shiftValue}
                onChange={(e) => setShiftValue(e.target.value)}
                style={{ width: '100%', marginBottom: '10px' }}
            />
            <button onClick={handleDecipher} style={{ width: '100%' }}>
                Decipher
            </button>
            <h3>Output:</h3>
            <textarea
                rows="4"
                readOnly
                value={outputText}
                style={{ width: '100%' }}
            />
        </div>
    );
};

// Export the component for use in other parts of the application
export default DecipherTool;
```
