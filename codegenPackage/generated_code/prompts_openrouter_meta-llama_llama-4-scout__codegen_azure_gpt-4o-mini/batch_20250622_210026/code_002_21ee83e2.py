"""
Generated Code Metadata:
========================
Original URL: https://demo9969.infinityfreeapp.com
Prompt: Generate HTML and JavaScript code to create a simple demo site similar to https://demo9969.infinityfreeapp.com, assuming the site is not accessible due to JavaScript being disabled.
Generated: DETERMINISTIC_21ee83e257977dc5
Batch ID: 20250622_210026
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
    <title>Simple Demo Site</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Welcome to the Simple Demo Site</h1>
        <p>This site demonstrates a simple HTML and JavaScript application.</p>
    </header>
    
    <main>
        <section id="content">
            <h2>Content Section</h2>
            <p id="demoText">Click the button below to see a demo message.</p>
            <button id="demoButton">Show Demo Message</button>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Simple Demo Site. All rights reserved.</p>
    </footer>

    <noscript>
        <style>
            body {
                display: none;
            }
            .no-js-message {
                display: block;
                color: red;
                font-weight: bold;
                text-align: center;
                margin-top: 20px;
            }
        </style>
        <div class="no-js-message">
            JavaScript is disabled in your browser. Please enable it to view the content of this site.
        </div>
    </noscript>
</body>
</html>
```

```javascript
// script.js

// Function to display a demo message when the button is clicked
function showDemoMessage() {
    const demoText = document.getElementById('demoText');
    demoText.textContent = 'Hello! This is your demo message.';
}

// Event listener for the button click
document.addEventListener('DOMContentLoaded', () => {
    const demoButton = document.getElementById('demoButton');
    
    // Check if the button exists before adding the event listener
    if (demoButton) {
        demoButton.addEventListener('click', showDemoMessage);
    } else {
        console.error('Demo button not found in the DOM.');
    }
});
```

```css
/* styles.css */

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #007BFF;
    color: white;
    padding: 10px 0;
    text-align: center;
}

/* Main content styling */
main {
    margin: 20px 0;
}

/* Footer styling */
footer {
    text-align: center;
    margin-top: 20px;
    font-size: 0.8em;
}
```
