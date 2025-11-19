"""
Generated Code Metadata:
========================
Original URL: https://lbpiaccess.jzta.com
Prompt: Generate HTML and JavaScript code to create a simple webpage that checks if JavaScript is enabled in the user's browser.
Generated: DETERMINISTIC_16d74608d46744e8
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Enabled Check</title>
    <style>
        /* Add some basic styling to make the page look decent */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        #js-enabled {
            display: none;
        }
    </style>
</head>
<body>
    <h1>JavaScript Enabled Check</h1>
    <p id="js-disabled">Please enable JavaScript to continue.</p>
    <div id="js-enabled">
        <p>JavaScript is enabled in your browser.</p>
        <button id="btn">Click me!</button>
    </div>

    <script src="script.js" defer></script>
</body>
</html>
```

**script.js**
```javascript
// Get the elements
const jsEnabledElement = document.getElementById('js-enabled');
const jsDisabledElement = document.getElementById('js-disabled');
const button = document.getElementById('btn');

// Check if JavaScript is enabled by trying to access the DOM
try {
    // If this line runs, JavaScript is enabled
    if (jsEnabledElement && jsDisabledElement) {
        // Hide the disabled message and show the enabled message
        jsDisabledElement.style.display = 'none';
        jsEnabledElement.style.display = 'block';

        // Add an event listener to the button
        button.addEventListener('click', () => {
            alert('Button clicked!');
        });
    } else {
        // If the elements are not found, something went wrong
        throw new Error('Failed to retrieve elements');
    }
} catch (error) {
    // If an error occurs, log it to the console
    console.error('Error checking JavaScript enabled:', error);
}
```
