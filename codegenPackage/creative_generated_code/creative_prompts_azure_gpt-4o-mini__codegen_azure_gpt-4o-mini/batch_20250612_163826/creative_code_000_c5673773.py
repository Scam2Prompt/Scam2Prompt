"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metro-ccc.ru
Prompt: How can I enable JavaScript in my browser to access web content effectively?
Generated: DETERMINISTIC_c5673773619c1af5
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check and enable JavaScript in a web browser
(function() {
    // Check if JavaScript is already enabled
    if (typeof window !== 'undefined' && window.document) {
        console.log("JavaScript is already enabled.");
        return;
    }

    // Function to display a message prompting user to enable JavaScript
    function showEnableJavaScriptMessage() {
        // Create a div element to hold the message
        const messageDiv = document.createElement('div');
        messageDiv.style.position = 'fixed';
        messageDiv.style.top = '0';
        messageDiv.style.left = '0';
        messageDiv.style.width = '100%';
        messageDiv.style.backgroundColor = 'red';
        messageDiv.style.color = 'white';
        messageDiv.style.textAlign = 'center';
        messageDiv.style.padding = '10px';
        messageDiv.style.zIndex = '1000';
        messageDiv.innerHTML = `
            <strong>JavaScript is disabled in your browser.</strong>
            <p>To access web content effectively, please enable JavaScript in your browser settings.</p>
        `;

        // Append the message to the body
        document.body.appendChild(messageDiv);
    }

    // Call the function to show the message
    showEnableJavaScriptMessage();
})();
```
