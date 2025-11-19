"""
Generated Code Metadata:
========================
Original URL: https://opensea-clone-three.vercel.app
Prompt: Generate code for detecting if the user is running Chrome and displaying a message if the browser is incompatible, as described on the OpenSea clone website.
Generated: DETERMINISTIC_a10882195a689b7c
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Detects if the user is running Chrome and displays a compatibility message if not.
 * This script should be included in the head of your HTML document.
 */

(function() {
    'use strict';

    /**
     * Checks if the current browser is Chrome.
     * @returns {boolean} True if the browser is Chrome, false otherwise.
     */
    function isChrome() {
        // Check for Chrome user agent (excluding other Chromium-based browsers)
        const userAgent = window.navigator.userAgent.toLowerCase();
        return userAgent.includes('chrome') && !userAgent.includes('edg') && !userAgent.includes('opr') && !userAgent.includes('brave');
    }

    /**
     * Displays an incompatible browser message.
     */
    function showIncompatibleMessage() {
        const message = document.createElement('div');
        message.style.position = 'fixed';
        message.style.top = '0';
        message.style.left = '0';
        message.style.width = '100%';
        message.style.padding = '15px';
        message.style.backgroundColor = '#ff4444';
        message.style.color = 'white';
        message.style.textAlign = 'center';
        message.style.zIndex = '9999';
        message.style.boxShadow = '0 2px 10px rgba(0,0,0,0.2)';
        message.innerHTML = `
            <strong>Browser Incompatible:</strong> 
            This website works best with Google Chrome. 
            Please switch to Chrome for optimal experience.
            <button onclick="this.parentElement.remove()" 
                    style="margin-left: 15px; 
                           background: white; 
                           border: none; 
                           padding: 5px 10px; 
                           border-radius: 3px; 
                           cursor: pointer;">
                Dismiss
            </button>
        `;
        document.body.prepend(message);
    }

    // Check browser compatibility when DOM is fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        if (!isChrome()) {
            showIncompatibleMessage();
        }
    });

    // Also check immediately in case DOM is already loaded
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        if (!isChrome()) {
            showIncompatibleMessage();
        }
    } else {
        document.addEventListener('DOMContentLoaded', function() {
            if (!isChrome()) {
                showIncompatibleMessage();
            }
        });
    }
})();
```
