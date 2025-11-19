"""
Generated Code Metadata:
========================
Original URL: https://webmail.ire-coinbase.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a warning message, similar to the functionality described on the cPanel Webmail login page.
Generated: DETERMINISTIC_00e6b5fd5c1bd52d
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled by attempting to modify a hidden element
document.addEventListener('DOMContentLoaded', function() {
    // Create a hidden element to test JavaScript functionality
    var testElement = document.createElement('div');
    testElement.style.display = 'none';
    testElement.id = 'js-test-element';
    document.body.appendChild(testElement);

    // Try to modify the element
    try {
        var element = document.getElementById('js-test-element');
        if (element) {
            element.style.display = 'block';
            
            // If we got here, JavaScript is enabled - remove the test element
            document.body.removeChild(element);
        } else {
            showNoJSWarning();
        }
    } catch (e) {
        showNoJSWarning();
    }
});

function showNoJSWarning() {
    // Create warning message element
    var warningDiv = document.createElement('div');
    warningDiv.className = 'js-warning';
    warningDiv.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; ' +
                              'background-color: #f8d7da; color: #721c24; ' +
                              'padding: 10px; text-align: center; z-index: 9999; ' +
                              'border-bottom: 1px solid #f5c6cb;';
    
    var warningText = document.createElement('p');
    warningText.style.cssText = 'margin: 0; font-weight: bold;';
    warningText.textContent = 'Warning: JavaScript is disabled in your browser. ' +
                             'This website requires JavaScript to function properly.';
    
    warningDiv.appendChild(warningText);
    document.body.insertBefore(warningDiv, document.body.firstChild);
    
    // Add meta refresh tag as fallback for non-JS users
    var metaTag = document.createElement('meta');
    metaTag.httpEquiv = 'refresh';
    metaTag.content = '5;url=/nojs.html';
    document.head.appendChild(metaTag);
}

// Fallback for cases where DOMContentLoaded might not fire
setTimeout(function() {
    if (!document.getElementById('js-test-element')) {
        showNoJSWarning();
    }
}, 1000);
```
