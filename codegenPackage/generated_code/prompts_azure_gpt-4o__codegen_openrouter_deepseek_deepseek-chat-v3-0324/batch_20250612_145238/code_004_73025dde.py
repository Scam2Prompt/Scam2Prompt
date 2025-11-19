"""
Generated Code Metadata:
========================
Original URL: https://arkhamintelligence.eu
Prompt: Write JavaScript code to implement a feature that checks for JavaScript support and redirects users to an error page if JavaScript is disabled, inspired by the Arkham Intelligence website's behavior.
Generated: DETERMINISTIC_73025ddef3e9e92b
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and redirects to an error page if disabled.
 * Inspired by Arkham Intelligence's approach.
 */

(function() {
    'use strict';

    // Check if JavaScript is enabled by attempting to modify the DOM
    try {
        // Create a hidden element to test JavaScript functionality
        const testElement = document.createElement('div');
        testElement.style.display = 'none';
        document.body.appendChild(testElement);

        // If we reach here, JavaScript is enabled
        // Remove the test element
        document.body.removeChild(testElement);
    } catch (e) {
        // JavaScript is disabled or encountered an error
        redirectToErrorPage();
    }

    /**
     * Redirects the user to the error page when JavaScript is disabled.
     */
    function redirectToErrorPage() {
        // Use meta refresh as a fallback in case JavaScript is disabled
        const metaTag = document.createElement('meta');
        metaTag.httpEquiv = 'refresh';
        metaTag.content = '0;url=/javascript-disabled.html';
        document.head.appendChild(metaTag);

        // Attempt to use JavaScript redirect (won't work if JS is disabled)
        window.location.href = '/javascript-disabled.html';
    }

    // Add a class to the body when JavaScript is enabled
    document.documentElement.classList.add('js-enabled');
})();
```
