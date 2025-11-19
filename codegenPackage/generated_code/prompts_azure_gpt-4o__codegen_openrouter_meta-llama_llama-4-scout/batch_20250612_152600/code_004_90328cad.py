"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Create a responsive web design for an Ethereum-based platform that displays a warning message when JavaScript is disabled, inspired by ETH Pledge's implementation.
Generated: DETERMINISTIC_90328cadc8499133
Batch ID: 20250612_152600
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
    <title>Ethereum-based Platform</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Warning message for JavaScript disabled users -->
    <noscript>
        <div class="warning-message">
            <p>JavaScript is disabled. Please enable JavaScript to use this platform.</p>
        </div>
    </noscript>

    <!-- Main content -->
    <div class="container">
        <h1>Ethereum-based Platform</h1>
        <!-- Add platform content here -->
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
/* Global styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Warning message styles */
.warning-message {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #ff9800;
    color: #fff;
    padding: 1em;
    text-align: center;
    z-index: 1000;
}

.warning-message p {
    margin: 0;
}

/* Responsive design styles */
.container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
    .container {
        margin: 20px auto;
        padding: 10px;
    }
}

@media (max-width: 480px) {
    .container {
        margin: 10px auto;
        padding: 5px;
    }
}
```

**script.js**
```javascript
// Check if JavaScript is enabled
document.addEventListener("DOMContentLoaded", function () {
    // Remove warning message when JavaScript is enabled
    const warningMessage = document.querySelector(".warning-message");
    if (warningMessage) {
        warningMessage.style.display = "none";
    }
});

// Add event listeners for responsive design
window.addEventListener("resize", function () {
    // Add responsive design logic here
});

// Error handling for script errors
window.onerror = function (message, source, lineno, colno, error) {
    console.error("Script error:", message, source, lineno, colno, error);
};
```
