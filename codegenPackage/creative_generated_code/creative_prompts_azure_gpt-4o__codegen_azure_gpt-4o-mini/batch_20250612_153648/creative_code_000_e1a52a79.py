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
// The Decipherer - A simple frontend application to encode and decode messages
// This application uses a basic Caesar cipher for encryption and decryption

// Function to encode a message using Caesar cipher
function encodeMessage(message, shift) {
    // Ensure shift is within the range of 0-25
    const validShift = (shift % 26 + 26) % 26; 
    return message.split('').map(char => {
        // Check if the character is a letter
        if (/[a-zA-Z]/.test(char)) {
            const base = char.charCodeAt(0) < 91 ? 65 : 97; // ASCII base for uppercase or lowercase
            return String.fromCharCode(((char.charCodeAt(0) - base + validShift) % 26) + base);
        }
        return char; // Non-letter characters remain unchanged
    }).join('');
}

// Function to decode a message using Caesar cipher
function decodeMessage(message, shift) {
    // Decode by shifting in the opposite direction
    return encodeMessage(message, -shift);
}

// Event listener for the encode button
document.getElementById('encodeButton').addEventListener('click', () => {
    try {
        const message = document.getElementById('inputMessage').value;
        const shift = parseInt(document.getElementById('shiftValue').value, 10);

        if (isNaN(shift)) {
            throw new Error('Shift value must be a number.');
        }

        const encodedMessage = encodeMessage(message, shift);
        document.getElementById('outputMessage').innerText = `Encoded Message: ${encodedMessage}`;
    } catch (error) {
        console.error(error);
        alert(`Error: ${error.message}`);
    }
});

// Event listener for the decode button
document.getElementById('decodeButton').addEventListener('click', () => {
    try {
        const message = document.getElementById('inputMessage').value;
        const shift = parseInt(document.getElementById('shiftValue').value, 10);

        if (isNaN(shift)) {
            throw new Error('Shift value must be a number.');
        }

        const decodedMessage = decodeMessage(message, shift);
        document.getElementById('outputMessage').innerText = `Decoded Message: ${decodedMessage}`;
    } catch (error) {
        console.error(error);
        alert(`Error: ${error.message}`);
    }
});

// HTML structure for the application
document.addEventListener('DOMContentLoaded', () => {
    const appMarkup = `
        <div>
            <h1>The Decipherer</h1>
            <textarea id="inputMessage" placeholder="Enter your message here..."></textarea><br>
            <label for="shiftValue">Shift Value:</label>
            <input type="number" id="shiftValue" value="3" min="0" max="25"/><br>
            <button id="encodeButton">Encode</button>
            <button id="decodeButton">Decode</button>
            <h2 id="outputMessage"></h2>
        </div>
    `;
    document.body.innerHTML = appMarkup;
});
```

This complete JavaScript code provides a simple encoding and decoding functionality using a Caesar cipher, with appropriate error handling, event listeners for user interactions, and a basic HTML structure generated dynamically upon loading the document.
