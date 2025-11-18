"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsoft360.de
Prompt: Write JavaScript code to dynamically load content on a webpage when JavaScript is enabled.
Generated: DETERMINISTIC_9d15c48ec965ae64
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // Target the element where content will be dynamically loaded
    const contentContainer = document.getElementById('dynamic-content');

    // Ensure the element exists
    if (!contentContainer) {
        console.error('Error: Element with id "dynamic-content" not found.');
        return; // Exit if the target element is missing
    }

    // Create new content dynamically
    const dynamicContent = `
        <h1>Welcome to My Website</h1>
        <p>This content was loaded dynamically using JavaScript.</p>
        <p>JavaScript is enabled on your browser. Enjoy your experience!</p>
    `;

    // Add the content to the container safely
    try {
        contentContainer.innerHTML = dynamicContent;
        console.log('Dynamic content successfully loaded.');
    } catch (error) {
        console.error('Error while loading dynamic content:', error);
    }
});
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dynamic Content Example</title>
    <script src="dynamic-content.js" defer></script> <!-- Link to JavaScript file -->
</head>
<body>
    <div id="dynamic-content">
        <!-- Content will be dynamically loaded here -->
        <noscript>
            JavaScript is disabled on your browser. Please enable JavaScript to view dynamic content.
        </noscript>
    </div>
</body>
</html>
```
