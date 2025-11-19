"""
Generated Code Metadata:
========================
Original URL: https://foxylinea.presale.com
Prompt: "Generate JavaScript code to enable conditional content display based on JavaScript support in the browser."
Generated: DETERMINISTIC_7e0f55e3d14ab722
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and conditionally displays content
 * based on the result. Adds a 'js-enabled' class to the document element if JavaScript
 * is supported, allowing CSS to style elements differently when JS is available.
 */
(function() {
    'use strict';

    /**
     * Main function to handle JS detection and content display
     */
    function init() {
        try {
            // Add js-enabled class to root element
            document.documentElement.classList.add('js-enabled');

            // Hide no-js elements and show js elements
            const noJsElements = document.querySelectorAll('.no-js');
            const jsElements = document.querySelectorAll('.js-only');

            noJsElements.forEach(function(element) {
                element.style.display = 'none';
            });

            jsElements.forEach(function(element) {
                element.style.display = '';
            });

            // Dispatch custom event for other scripts to listen to
            const event = new CustomEvent('jsSupportDetected', {
                detail: { supported: true }
            });
            document.dispatchEvent(event);
        } catch (error) {
            console.error('Error in JavaScript support detection:', error);
            // Dispatch event indicating JS support check failed
            const event = new CustomEvent('jsSupportDetected', {
                detail: { supported: false }
            });
            document.dispatchEvent(event);
        }
    }

    // Run initialization when DOM is fully loaded
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        init();
    } else {
        document.addEventListener('DOMContentLoaded', init);
    }
})();
```
