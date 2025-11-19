"""
Generated Code Metadata:
========================
Original URL: https://cxconnect1-dss.coinbase.co.za
Prompt: Create a script that checks for JavaScript functionality and redirects users to an alternative page if JavaScript is disabled, inspired by the requirements of the Coinbase domain details page.
Generated: DETERMINISTIC_c67c5969cf6e91fc
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript_redirect.js

/**
 * Checks if JavaScript is enabled and redirects to an alternative page if not.
 */

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a hidden input element
    const inputElement = document.createElement('input');
    inputElement.type = 'hidden';
    inputElement.name = 'javascript_enabled';
    inputElement.value = 'true';

    // Add the input element to the page
    document.body.appendChild(inputElement);

    // Check if the input element is still hidden
    // If JavaScript is disabled, the input element will not be added
    return inputElement.offsetParent !== null;
}

// Function to redirect to an alternative page
function redirectToAlternativePage(url) {
    // Check if the current page is the alternative page
    if (window.location.href !== url) {
        // Redirect to the alternative page
        window.location.href = url;
    }
}

// Main function
function main() {
    // URL of the alternative page
    const alternativePageUrl = '/alternative-page'; // Replace with your alternative page URL

    // Check if JavaScript is enabled
    if (!isJavaScriptEnabled()) {
        // Redirect to the alternative page if JavaScript is disabled
        redirectToAlternativePage(alternativePageUrl);
    }
}

// Run the main function when the page loads
document.addEventListener('DOMContentLoaded', main);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Redirect Test</title>
    <script src="noscript_redirect.js" defer></script>
</head>
<body>
    <noscript>
        <meta http-equiv="refresh" content="0;url=/alternative-page">
    </noscript>
    <!-- Your page content here -->
</body>
</html>
```

```python
# app.py (using Flask)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alternative-page')
def alternative_page():
    return render_template('alternative_page.html')

if __name__ == '__main__':
    app.run(debug=True)
```
