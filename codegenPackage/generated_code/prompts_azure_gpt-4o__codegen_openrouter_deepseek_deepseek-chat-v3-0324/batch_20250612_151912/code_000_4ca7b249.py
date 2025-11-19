"""
Generated Code Metadata:
========================
Original URL: https://raiden.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message instructing them to enable it, similar to the functionality described on the Raiden Online domain details page.
Generated: DETERMINISTIC_4ca7b2495ee4ca9e
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and display a message if it's not
(function() {
    // Create a noscript element to check if JavaScript is disabled
    var noscript = document.createElement('noscript');
    document.body.appendChild(noscript);

    // Check if the noscript element is still in the DOM (JavaScript is disabled)
    if (document.body.contains(noscript)) {
        // Create a warning message container
        var warningDiv = document.createElement('div');
        warningDiv.style.position = 'fixed';
        warningDiv.style.top = '0';
        warningDiv.style.left = '0';
        warningDiv.style.width = '100%';
        warningDiv.style.padding = '20px';
        warningDiv.style.backgroundColor = '#ffeb3b';
        warningDiv.style.color = '#000';
        warningDiv.style.textAlign = 'center';
        warningDiv.style.zIndex = '9999';
        warningDiv.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';

        // Add the warning message
        warningDiv.innerHTML = '<strong>JavaScript is disabled in your browser.</strong> ' +
                               'Please enable JavaScript to properly use this website.';

        // Insert the warning at the top of the page
        document.body.insertBefore(warningDiv, document.body.firstChild);

        // Remove the noscript element we created
        document.body.removeChild(noscript);
    }
})();
```
