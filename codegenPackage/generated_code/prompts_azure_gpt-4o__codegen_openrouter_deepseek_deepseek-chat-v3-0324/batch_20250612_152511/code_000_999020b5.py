"""
Generated Code Metadata:
========================
Original URL: https://admin.tradex247.com
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting the user to enable it, similar to the behavior of the Trade X Admin platform.
Generated: DETERMINISTIC_999020b593a16298
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and display a message if not
(function() {
    // Create a noscript element to detect if JavaScript is disabled
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

        // Add warning message content
        warningDiv.innerHTML = '<strong>JavaScript is disabled in your browser.</strong> ' +
                              'Please enable JavaScript to use this website properly.';

        // Insert the warning message at the top of the page
        document.body.insertBefore(warningDiv, document.body.firstChild);

        // Remove the noscript element we created
        document.body.removeChild(noscript);
    }
})();
```
