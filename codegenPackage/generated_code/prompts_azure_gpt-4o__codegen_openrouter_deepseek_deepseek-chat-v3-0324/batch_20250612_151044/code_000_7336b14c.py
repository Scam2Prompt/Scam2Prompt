"""
Generated Code Metadata:
========================
Original URL: https://boredturtleyc.netlify.app
Prompt: Write JavaScript code to display a custom loading message when a web application requires JavaScript to run, similar to the behavior described on the "Bored Turtle Yacht Club" webpage.
Generated: DETERMINISTIC_7336b14c02d4d34a
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and hide the loading message
document.addEventListener('DOMContentLoaded', function() {
    const loadingElement = document.getElementById('js-loading-message');
    
    if (loadingElement) {
        loadingElement.style.display = 'none';
    }
});

// Create and append the loading message element if it doesn't exist
(function() {
    if (!document.getElementById('js-loading-message')) {
        const loadingDiv = document.createElement('div');
        loadingDiv.id = 'js-loading-message';
        loadingDiv.style.position = 'fixed';
        loadingDiv.style.top = '0';
        loadingDiv.style.left = '0';
        loadingDiv.style.width = '100%';
        loadingDiv.style.height = '100%';
        loadingDiv.style.backgroundColor = '#ffffff';
        loadingDiv.style.display = 'flex';
        loadingDiv.style.justifyContent = 'center';
        loadingDiv.style.alignItems = 'center';
        loadingDiv.style.zIndex = '9999';
        
        const loadingText = document.createElement('p');
        loadingText.textContent = 'Loading application...';
        loadingText.style.fontSize = '24px';
        loadingText.style.fontFamily = 'Arial, sans-serif';
        loadingText.style.color = '#333333';
        
        loadingDiv.appendChild(loadingText);
        document.body.prepend(loadingDiv);
    }
})();

// Fallback for noscript users
document.write('<noscript><style>#js-loading-message{display:none;}</style><div style="position:fixed;top:0;left:0;width:100%;height:100%;background:#fff;display:flex;justify-content:center;align-items:center;z-index:9999"><p style="font-size:24px;font-family:Arial,sans-serif;color:#333">Please enable JavaScript to use this application.</p></div></noscript>');
```
