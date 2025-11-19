"""
Generated Code Metadata:
========================
Original URL: https://imseoa.com
Prompt: "Create a basic webpage template in HTML/CSS/JavaScript that requires enabling JavaScript to view content, similar to imseoa.com's current page."
Generated: DETERMINISTIC_6d705f21fc5da5bd
Batch ID: 20250622_204829
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
    <title>Basic Webpage Template</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <noscript>
        <div class="noscript-container">
            <h1>JavaScript is required to view this content</h1>
            <p>Please enable JavaScript in your browser to continue.</p>
        </div>
    </noscript>
    <div id="content-container" class="hidden">
        <!-- Page content will be loaded here -->
        <h1>Welcome to our webpage!</h1>
        <p>This is a basic webpage template.</p>
        <button id="example-button">Click me!</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.noscript-container {
    text-align: center;
    margin-top: 20vh;
}

.hidden {
    display: none;
}

#content-container {
    padding: 20px;
    text-align: center;
}

#example-button {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#example-button:hover {
    background-color: #3e8e41;
}
```

**script.js**
```javascript
// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function () {
    // Get the content container and noscript elements
    const contentContainer = document.getElementById('content-container');
    const noscriptContainer = document.querySelector('.noscript-container');

    // Check if JavaScript is enabled
    if (contentContainer) {
        // Show the content container and hide the noscript container
        contentContainer.classList.remove('hidden');
        // Add event listener to the example button
        document.getElementById('example-button').addEventListener('click', function () {
            alert('Button clicked!');
        });
    } else {
        // If JavaScript is disabled, the noscript container will be displayed
        console.error('JavaScript is required to view this content');
    }
});

// Error handling for any uncaught exceptions
window.addEventListener('error', function (event) {
    console.error('An error occurred:', event.error);
});
```
