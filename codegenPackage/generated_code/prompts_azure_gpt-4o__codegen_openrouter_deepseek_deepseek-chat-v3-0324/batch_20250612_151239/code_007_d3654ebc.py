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
 * Text Reversal Tool
 * 
 * This script provides functionality to reverse text strings in a browser-based tool.
 * It handles user input, processes the text, and displays the reversed result.
 */

// DOM Elements
const inputTextArea = document.getElementById('inputText');
const outputTextArea = document.getElementById('outputText');
const reverseButton = document.getElementById('reverseButton');
const copyButton = document.getElementById('copyButton');
const clearButton = document.getElementById('clearButton');

/**
 * Reverses the given text string
 * @param {string} text - The input text to reverse
 * @returns {string} The reversed text
 */
function reverseText(text) {
    if (typeof text !== 'string') {
        throw new TypeError('Input must be a string');
    }
    return text.split('').reverse().join('');
}

/**
 * Handles the text reversal process
 */
function handleReverse() {
    try {
        const inputText = inputTextArea.value;
        const reversedText = reverseText(inputText);
        outputTextArea.value = reversedText;
    } catch (error) {
        console.error('Error reversing text:', error);
        outputTextArea.value = 'Error: ' + error.message;
    }
}

/**
 * Copies the output text to clipboard
 */
function handleCopy() {
    try {
        outputTextArea.select();
        document.execCommand('copy');
        
        // Visual feedback
        const originalText = copyButton.textContent;
        copyButton.textContent = 'Copied!';
        setTimeout(() => {
            copyButton.textContent = originalText;
        }, 2000);
    } catch (error) {
        console.error('Error copying text:', error);
        alert('Failed to copy text. Please try again.');
    }
}

/**
 * Clears both input and output text areas
 */
function handleClear() {
    inputTextArea.value = '';
    outputTextArea.value = '';
}

// Event Listeners
reverseButton.addEventListener('click', handleReverse);
copyButton.addEventListener('click', handleCopy);
clearButton.addEventListener('click', handleClear);

// Initialize with example text (optional)
document.addEventListener('DOMContentLoaded', () => {
    inputTextArea.value = 'Example text to reverse';
    handleReverse();
});
```
