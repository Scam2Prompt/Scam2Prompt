"""
Generated Code Metadata:
========================
Original URL: https://celestiacelestia.com
Prompt: Write a JavaScript check to see if the document has JavaScript enabled, and display a message if it doesn't.
Generated: DETERMINISTIC_2d2afac84cc8bece
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled in the browser
(function() {
    // Create a div element to display the message
    const messageDiv = document.createElement('div');
    
    // Set the message content and style
    messageDiv.textContent = "JavaScript is disabled in your browser. Please enable it for a better experience.";
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '0';
    messageDiv.style.left = '0';
    messageDiv.style.width = '100%';
    messageDiv.style.backgroundColor = 'red';
    messageDiv.style.color = 'white';
    messageDiv.style.textAlign = 'center';
    messageDiv.style.padding = '10px';
    messageDiv.style.zIndex = '1000';
    
    // Function to show the message
    function showMessage() {
        document.body.appendChild(messageDiv);
    }

    // Function to hide the message
    function hideMessage() {
        if (document.body.contains(messageDiv)) {
            document.body.removeChild(messageDiv);
        }
    }

    // Check if JavaScript is enabled by setting a flag
    window.onload = function() {
        hideMessage(); // Hide the message if JavaScript is enabled
    };

    // Show the message if JavaScript is disabled
    showMessage();
})();
```
