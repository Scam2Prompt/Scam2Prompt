"""
Generated Code Metadata:
========================
Original URL: https://sdddd.pages.dev
Prompt: Generate code to detect whether a user is accessing a website from a desktop or mobile device and display an optimized message, similar to the desktop usage optimization mentioned on the chimpers-dojo website.
Generated: DETERMINISTIC_51e38f1b01895b6f
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Detects if the user is accessing the website from a mobile device or desktop
 * and displays an optimized message accordingly.
 */

(function() {
    'use strict';

    /**
     * Check if the user agent indicates a mobile device.
     * @returns {boolean} True if mobile, false otherwise.
     */
    function isMobileDevice() {
        return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
    }

    /**
     * Displays an optimized message based on the device type.
     */
    function displayOptimizedMessage() {
        const messageContainer = document.createElement('div');
        messageContainer.style.position = 'fixed';
        messageContainer.style.bottom = '0';
        messageContainer.style.left = '0';
        messageContainer.style.right = '0';
        messageContainer.style.padding = '10px';
        messageContainer.style.textAlign = 'center';
        messageContainer.style.backgroundColor = '#f8f9fa';
        messageContainer.style.borderTop = '1px solid #dee2e6';
        messageContainer.style.zIndex = '1000';

        if (isMobileDevice()) {
            messageContainer.textContent = 'Optimized for mobile experience. Tap to explore!';
            messageContainer.style.color = '#007bff';
        } else {
            messageContainer.textContent = 'Optimized for desktop experience. Enjoy browsing!';
            messageContainer.style.color = '#28a745';
        }

        document.body.appendChild(messageContainer);

        // Remove the message after 5 seconds
        setTimeout(() => {
            document.body.removeChild(messageContainer);
        }, 5000);
    }

    // Ensure the DOM is fully loaded before executing
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', displayOptimizedMessage);
    } else {
        displayOptimizedMessage();
    }
})();
```
