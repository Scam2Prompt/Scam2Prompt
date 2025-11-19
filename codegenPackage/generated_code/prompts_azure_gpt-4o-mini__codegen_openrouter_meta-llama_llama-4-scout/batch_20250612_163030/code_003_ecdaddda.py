"""
Generated Code Metadata:
========================
Original URL: https://coinlist-acurast.com
Prompt: What are the implications of using `document.write()` after the page has loaded, and how can it affect the DOM?
Generated: DETERMINISTIC_ecdaddda00cb75b5
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document Write Example</title>
</head>
<body>
    <h1 id="header">Initial Header</h1>
    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js
/**
 * Demonstrates the implications of using document.write() after the page has loaded.
 */

// Get the initial header element
const headerElement = document.getElementById('header');

/**
 * Logs the initial innerHTML of the header element.
 */
function logInitialHeader() {
    console.log('Initial Header:', headerElement.innerHTML);
}

/**
 * Uses document.write() to modify the page content.
 * @param {string} content The content to write to the document.
 */
function modifyDocument(content) {
    try {
        // Attempt to write to the document
        document.write(content);
    } catch (error) {
        console.error('Error using document.write():', error);
    }
}

/**
 * Logs the modified innerHTML of the header element.
 */
function logModifiedHeader() {
    console.log('Modified Header:', headerElement.innerHTML);
}

// Log the initial header
logInitialHeader();

// Simulate a user interaction or asynchronous operation
setTimeout(() => {
    // Attempt to modify the document using document.write()
    modifyDocument('<h1>Modified Header</h1>');

    // Log the modified header
    logModifiedHeader();
}, 2000);
```
