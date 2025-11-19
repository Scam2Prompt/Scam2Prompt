"""
Generated Code Metadata:
========================
Original URL: https://metamask-web-utils-prod.app.greate.eu
Prompt: Create a script that mimics the functionality of the Metamask Web Utils domain details page by detecting JavaScript support and prompting users to enable it for proper app functionality.
Generated: DETERMINISTIC_db3365c7d8bda81a
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * MetaMask Web Utils - Domain Details Page
 * This script checks for JavaScript support and prompts users to enable it if disabled.
 */

(function() {
    'use strict';

    /**
     * Checks if JavaScript is enabled in the browser.
     * @returns {boolean} True if JavaScript is enabled, false otherwise.
     */
    function isJavaScriptEnabled() {
        try {
            return typeof window !== 'undefined' && 
                   typeof document !== 'undefined' && 
                   'querySelector' in document && 
                   'addEventListener' in window;
        } catch (e) {
            return false;
        }
    }

    /**
     * Displays a message prompting the user to enable JavaScript.
     */
    function showJavaScriptRequiredMessage() {
        const message = document.createElement('div');
        message.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 20px;
            background-color: #f8d7da;
            color: #721c24;
            text-align: center;
            font-family: Arial, sans-serif;
            z-index: 9999;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        `;
        message.innerHTML = `
            <strong>JavaScript is disabled!</strong> 
            This application requires JavaScript to function properly. 
            Please enable JavaScript in your browser settings and refresh the page.
        `;
        document.body.appendChild(message);
    }

    /**
     * Initializes the script and checks JavaScript support.
     */
    function init() {
        if (!isJavaScriptEnabled()) {
            showJavaScriptRequiredMessage();
        }
    }

    // Run the initialization when the DOM is fully loaded
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
```
