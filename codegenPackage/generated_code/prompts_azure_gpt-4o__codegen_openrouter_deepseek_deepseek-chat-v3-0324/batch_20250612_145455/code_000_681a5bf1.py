"""
Generated Code Metadata:
========================
Original URL: https://cpanel.sophon.am
Prompt: Write a JavaScript function to detect if JavaScript is disabled in a browser and display a warning message, similar to the functionality described on the cPanel login page.
Generated: DETERMINISTIC_681a5bf1d2db80bc
Batch ID: 20250612_145455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Detects if JavaScript is disabled in the browser and displays a warning message.
 * The warning message will be shown if JavaScript is disabled, otherwise it will be hidden.
 */
function detectJavaScriptDisabled() {
    // Create the warning message element if it doesn't exist
    let warningElement = document.getElementById('js-disabled-warning');
    
    if (!warningElement) {
        warningElement = document.createElement('div');
        warningElement.id = 'js-disabled-warning';
        warningElement.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            padding: 10px;
            background-color: #f8d7da;
            color: #721c24;
            border-bottom: 1px solid #f5c6cb;
            text-align: center;
            z-index: 9999;
        `;
        warningElement.innerHTML = `
            <strong>Warning:</strong> JavaScript is disabled in your browser. 
            Some features may not work properly.
        `;
        document.body.insertBefore(warningElement, document.body.firstChild);
    }

    // This script will only run if JavaScript is enabled, so we hide the warning
    warningElement.style.display = 'none';
}

// Execute the detection when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', detectJavaScriptDisabled);

// Fallback in case DOMContentLoaded doesn't fire (though modern browsers support it)
if (document.readyState === 'complete' || document.readyState === 'interactive') {
    detectJavaScriptDisabled();
} else {
    window.addEventListener('load', detectJavaScriptDisabled);
}

// Add noscript fallback for when JavaScript is actually disabled
document.write(`
    <noscript>
        <style type="text/css">
            #js-disabled-warning { display: block !important; }
        </style>
    </noscript>
`);
```
