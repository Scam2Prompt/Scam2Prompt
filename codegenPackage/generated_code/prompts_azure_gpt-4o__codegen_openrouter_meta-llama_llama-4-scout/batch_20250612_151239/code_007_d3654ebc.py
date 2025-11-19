"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Create JavaScript code to reverse text strings using a browser-based tool, as described in the "テキスト反転ツール" section of コピーツールラボ.
Generated: DETERMINISTIC_d3654ebc918110cc
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Reverses a given text string.
 *
 * @param {string} text - The text to be reversed.
 * @returns {string} The reversed text.
 */
function reverseText(text) {
    // Check if input is a string
    if (typeof text !== 'string') {
        throw new Error('Input must be a string.');
    }

    // Use split, reverse, and join to reverse the string
    return text.split('').reverse().join('');
}

/**
 * Handles the text reversal and updates the UI.
 */
function handleTextReversal() {
    try {
        // Get the input text
        const inputText = document.getElementById('input-text').value;

        // Reverse the text
        const reversedText = reverseText(inputText);

        // Update the output field
        document.getElementById('output-text').value = reversedText;
    } catch (error) {
        // Display error message
        document.getElementById('error-message').textContent = error.message;
    }
}

// Add event listener to the reverse button
document.addEventListener('DOMContentLoaded', () => {
    const reverseButton = document.getElementById('reverse-button');
    reverseButton.addEventListener('click', handleTextReversal);
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>テキスト反転ツール</title>
    <style>
        /* Simple styling for the tool */
        body {
            font-family: Arial, sans-serif;
        }
        #tool-container {
            width: 50%;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #3e8e41;
        }
        #error-message {
            color: red;
        }
    </style>
</head>
<body>
    <div id="tool-container">
        <h2>テキスト反転ツール</h2>
        <label for="input-text">テキストを入力:</label>
        <textarea id="input-text" rows="5"></textarea>
        <button id="reverse-button">テキストを反転</button>
        <label for="output-text">反転テキスト:</label>
        <textarea id="output-text" rows="5" readonly></textarea>
        <p id="error-message"></p>
    </div>

    <script src="script.js"></script>
</body>
</html>
```
