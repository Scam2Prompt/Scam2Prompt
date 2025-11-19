"""
Generated Code Metadata:
========================
Original URL: https://morpho-frontend.pages.dev
Prompt: Develop a JavaScript snippet to display a warning message if JavaScript is disabled in a Morpho-based app.
Generated: DETERMINISTIC_50766a1d11192944
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and displays a warning message if it's disabled.
 * This is specifically designed for Morpho-based applications.
 */
(function() {
    'use strict';

    // Create a noscript element fallback for when JavaScript is disabled
    var noscriptElement = document.createElement('noscript');
    
    // Create warning message container
    var warningDiv = document.createElement('div');
    warningDiv.style.cssText = 'position: fixed; top: 0; left: 0; width: 100%; ' +
                              'background-color: #ffeb3b; color: #000; ' +
                              'padding: 15px; text-align: center; z-index: 9999; ' +
                              'box-shadow: 0 2px 5px rgba(0,0,0,0.2);';
    
    // Warning message content
    var warningText = document.createElement('p');
    warningText.textContent = 'Warning: JavaScript is disabled in your browser. ' +
                             'This Morpho-based application requires JavaScript to function properly. ' +
                             'Please enable JavaScript to continue.';
    
    // Append elements
    warningDiv.appendChild(warningText);
    noscriptElement.appendChild(warningDiv);
    
    // Insert the warning at the beginning of the body
    document.body.insertBefore(noscriptElement, document.body.firstChild);
    
    // Additional check for JavaScript support (though this won't run if JS is disabled)
    try {
        if (typeof Morpho === 'undefined') {
            console.warn('Morpho framework not detected');
        }
    } catch (e) {
        console.error('Error checking for Morpho framework:', e);
    }
})();
```
