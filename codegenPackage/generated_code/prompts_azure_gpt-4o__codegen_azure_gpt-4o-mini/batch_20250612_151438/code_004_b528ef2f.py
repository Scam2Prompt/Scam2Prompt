"""
Generated Code Metadata:
========================
Original URL: https://hingehealth.eu
Prompt: Write a JavaScript function that dynamically updates the webpage content to notify users when JavaScript is disabled, mimicking the behavior of the hingehealth.eu site.
Generated: DETERMINISTIC_b528ef2f65f18deb
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a div element to display the notification
    const notificationDiv = document.createElement('div');
    notificationDiv.id = 'js-disabled-notification';
    notificationDiv.style.display = 'none'; // Initially hidden
    notificationDiv.style.position = 'fixed';
    notificationDiv.style.top = '0';
    notificationDiv.style.left = '0';
    notificationDiv.style.width = '100%';
    notificationDiv.style.backgroundColor = '#ffcc00';
    notificationDiv.style.color = '#000';
    notificationDiv.style.textAlign = 'center';
    notificationDiv.style.padding = '10px';
    notificationDiv.style.zIndex = '1000';
    notificationDiv.innerText = 'JavaScript is disabled in your browser. Please enable it for the best experience.';

    // Append the notification to the body
    document.body.appendChild(notificationDiv);

    // Function to show the notification
    function showNotification() {
        notificationDiv.style.display = 'block';
    }

    // Function to hide the notification
    function hideNotification() {
        notificationDiv.style.display = 'none';
    }

    // Check if JavaScript is enabled by setting a timeout
    setTimeout(() => {
        // If the timeout completes, it means JavaScript is enabled
        hideNotification();
    }, 1000); // 1 second delay to allow for JavaScript execution

    // Show the notification if JavaScript is disabled
    window.addEventListener('load', () => {
        showNotification();
    });
}

// Call the function to check for JavaScript
checkJavaScriptEnabled();
```

```html
<!-- HTML structure to include in your webpage -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Check</title>
    <script src="path/to/your/javascript-file.js" defer></script>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    <p>This is a sample webpage.</p>
</body>
</html>
```
