"""
Generated Code Metadata:
========================
Original URL: https://www.arclerdesk.com
Prompt: Create a simple browser support tool using web development frameworks, providing optimized browser support services similar to Arcler Desk.
Generated: DETERMINISTIC_84a666b6bf4d6bfb
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Browser Support Tool</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Browser Support Tool</h1>
        <p>Check your browser's compatibility with various web features.</p>
    </header>
    <main>
        <section id="browser-info">
            <h2>Your Browser Information</h2>
            <div id="info"></div>
        </section>
        <section id="feature-check">
            <h2>Check Feature Support</h2>
            <input type="text" id="feature" placeholder="Enter feature (e.g., fetch)">
            <button id="check-btn">Check Support</button>
            <div id="result"></div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Browser Support Tool</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Section styling */
section {
    margin-bottom: 20px;
    padding: 20px;
    background: #ffffff;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Button styling */
button {
    padding: 10px 15px;
    background: #35424a;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #2c3e50;
}
```

```javascript
// script.js

// Function to get browser information
function getBrowserInfo() {
    const userAgent = navigator.userAgent;
    const browserInfo = {
        name: '',
        version: '',
        isSupported: false
    };

    // Detect browser name and version
    if (userAgent.includes("Chrome")) {
        browserInfo.name = "Chrome";
        browserInfo.version = userAgent.match(/Chrome\/(\d+\.\d+)/)[1];
    } else if (userAgent.includes("Firefox")) {
        browserInfo.name = "Firefox";
        browserInfo.version = userAgent.match(/Firefox\/(\d+\.\d+)/)[1];
    } else if (userAgent.includes("Safari")) {
        browserInfo.name = "Safari";
        browserInfo.version = userAgent.match(/Version\/(\d+\.\d+)/)[1];
    } else if (userAgent.includes("MSIE") || userAgent.includes("Trident")) {
        browserInfo.name = "Internet Explorer";
        browserInfo.version = userAgent.match(/(?:MSIE |rv:)(\d+\.\d+)/)[1];
    } else {
        browserInfo.name = "Unknown";
        browserInfo.version = "Unknown";
    }

    // Display browser information
    document.getElementById('info').innerText = `Browser: ${browserInfo.name}, Version: ${browserInfo.version}`;
}

// Function to check feature support
function checkFeatureSupport(feature) {
    const resultElement = document.getElementById('result');
    resultElement.innerText = ''; // Clear previous results

    // Check for feature support
    if (feature in window) {
        resultElement.innerText = `${feature} is supported in your browser.`;
    } else {
        resultElement.innerText = `${feature} is NOT supported in your browser.`;
    }
}

// Event listener for the check button
document.getElementById('check-btn').addEventListener('click', () => {
    const feature = document.getElementById('feature').value.trim();
    if (feature) {
        checkFeatureSupport(feature);
    } else {
        alert('Please enter a feature to check.');
    }
});

// Initialize browser info on page load
window.onload = getBrowserInfo;
```
