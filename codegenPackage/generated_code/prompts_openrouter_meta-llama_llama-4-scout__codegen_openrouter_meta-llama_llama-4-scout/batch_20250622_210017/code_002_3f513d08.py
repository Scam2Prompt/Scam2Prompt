"""
Generated Code Metadata:
========================
Original URL: https://exodusn.com
Prompt: "Generate code for a simple web page that uses JavaScript to dynamically change its content when a user clicks a button."
Generated: DETERMINISTIC_3f513d08ee7e3e41
Batch ID: 20250622_210017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Content Page</title>
    <style>
        /* Basic styling for the page */
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        #content {
            margin: 20px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>

<button id="changeContentBtn">Change Content</button>
<div id="content">Initial content. Click the button to change me!</div>

<script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js

/**
 * Get the button and content elements from the DOM.
 */
const changeContentBtn = document.getElementById('changeContentBtn');
const contentDiv = document.getElementById('content');

/**
 * Define a function to change the content of the page.
 */
function changeContent() {
    try {
        // Generate a random message to display.
        const messages = [
            'You clicked the button!',
            'Dynamic content is awesome!',
            'JavaScript makes it happen!',
        ];
        const randomMessage = messages[Math.floor(Math.random() * messages.length)];

        // Update the content of the page.
        contentDiv.innerText = randomMessage;
    } catch (error) {
        console.error('Error changing content:', error);
        contentDiv.innerText = 'An error occurred. Please try again!';
    }
}

/**
 * Add an event listener to the button to change the content on click.
 */
changeContentBtn.addEventListener('click', changeContent);
```
