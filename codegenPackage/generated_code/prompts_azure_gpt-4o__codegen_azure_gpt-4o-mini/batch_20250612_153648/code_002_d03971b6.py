"""
Generated Code Metadata:
========================
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Create a React-based frontend application that includes a deciphering feature and requires JavaScript to function properly.
Generated: DETERMINISTIC_d03971b6bd61abb6
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
import ReactDOM from 'react-dom';
import './styles.css'; // Importing CSS for styling

// Function to decipher a simple Caesar cipher
const decipherCaesarCipher = (text, shift) => {
    if (typeof text !== 'string' || typeof shift !== 'number') {
        throw new Error('Invalid input: text must be a string and shift must be a number.');
    }

    return text.split('').map(char => {
        if (char.match(/[a-z]/i)) {
            const code = char.charCodeAt(0);
            const base = code >= 65 && code <= 90 ? 65 : 97; // Uppercase or lowercase
            return String.fromCharCode(((code - base - shift + 26) % 26) + base);
        }
        return char; // Non-alphabetic characters are returned unchanged
    }).join('');
};

// Main App component
const App = () => {
    const [inputText, setInputText] = useState('');
    const [shiftValue, setShiftValue] = useState(0);
    const [decipheredText, setDecipheredText] = useState('');

    // Handle input change for text
    const handleTextChange = (event) => {
        setInputText(event.target.value);
    };

    // Handle input change for shift value
    const handleShiftChange = (event) => {
        const value = parseInt(event.target.value, 10);
        setShiftValue(isNaN(value) ? 0 : value);
    };

    // Handle deciphering action
    const handleDecipher = () => {
        try {
            const result = decipherCaesarCipher(inputText, shiftValue);
            setDecipheredText(result);
        } catch (error) {
            alert(error.message); // Alert user in case of error
        }
    };

    return (
        <div className="app-container">
            <h1>Caesar Cipher Decipher Tool</h1>
            <textarea
                placeholder="Enter text to decipher"
                value={inputText}
                onChange={handleTextChange}
                rows="4"
                cols="50"
            />
            <br />
            <input
                type="number"
                placeholder="Enter shift value"
                value={shiftValue}
                onChange={handleShiftChange}
            />
            <br />
            <button onClick={handleDecipher}>Decipher</button>
            <h2>Deciphered Text:</h2>
            <p>{decipheredText}</p>
        </div>
    );
};

// Render the App component to the DOM
ReactDOM.render(<App />, document.getElementById('root'));
```

```css
/* styles.css */
.app-container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    background-color: #f9f9f9;
}

h1 {
    text-align: center;
}

textarea {
    width: 100%;
    margin-bottom: 10px;
}

input[type="number"] {
    width: 100%;
    margin-bottom: 10px;
}

button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

h2 {
    margin-top: 20px;
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caesar Cipher Decipher Tool</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="root"></div>
    <script src="index.js" type="text/javascript"></script>
</body>
</html>
```

```javascript
// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App'; // Assuming App component is in App.js

ReactDOM.render(<App />, document.getElementById('root'));
```
