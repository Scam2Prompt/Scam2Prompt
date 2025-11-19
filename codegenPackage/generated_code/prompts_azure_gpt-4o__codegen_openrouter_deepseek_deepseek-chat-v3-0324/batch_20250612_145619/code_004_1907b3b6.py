"""
Generated Code Metadata:
========================
Original URL: https://ethvnq.com
Prompt: Write a JavaScript snippet to detect mobile devices and display a custom error message if JavaScript is disabled, specifically for BTC pledge services.
Generated: DETERMINISTIC_1907b3b6d0d54ef0
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Detects mobile devices and checks if JavaScript is enabled.
 * Displays a custom error message if JavaScript is disabled for BTC pledge services.
 */

(function() {
    // Check if JavaScript is enabled
    document.documentElement.className = 'js';
    
    // Mobile device detection
    function isMobileDevice() {
        return (typeof window.orientation !== "undefined") || 
               (navigator.userAgent.indexOf('IEMobile') !== -1) ||
               (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent));
    }
    
    // Display error message if JS is disabled
    document.addEventListener('DOMContentLoaded', function() {
        var errorContainer = document.createElement('div');
        errorContainer.id = 'js-error-message';
        errorContainer.style.display = 'none';
        errorContainer.style.padding = '20px';
        errorContainer.style.backgroundColor = '#f8d7da';
        errorContainer.style.color = '#721c24';
        errorContainer.style.border = '1px solid #f5c6cb';
        errorContainer.style.borderRadius = '4px';
        errorContainer.style.margin = '20px 0';
        errorContainer.style.textAlign = 'center';
        
        var errorMessage = document.createElement('p');
        errorMessage.textContent = 'JavaScript is required for BTC pledge services. Please enable JavaScript in your browser settings.';
        
        if (isMobileDevice()) {
            errorMessage.textContent += ' Mobile devices are supported, but JavaScript must be enabled.';
        }
        
        errorContainer.appendChild(errorMessage);
        document.body.insertBefore(errorContainer, document.body.firstChild);
        
        // Remove the error message if JS is enabled
        document.getElementById('js-error-message').style.display = 'none';
    });
    
    // Fallback for noscript tag
    var noscriptFallback = document.createElement('noscript');
    var noscriptMessage = document.createElement('div');
    noscriptMessage.style.padding = '20px';
    noscriptMessage.style.backgroundColor = '#f8d7da';
    noscriptMessage.style.color = '#721c24';
    noscriptMessage.style.border = '1px solid #f5c6cb';
    noscriptMessage.style.borderRadius = '4px';
    noscriptMessage.style.margin = '20px 0';
    noscriptMessage.style.textAlign = 'center';
    noscriptMessage.textContent = 'JavaScript is disabled. BTC pledge services require JavaScript to function properly.';
    
    if (isMobileDevice()) {
        noscriptMessage.textContent += ' Mobile devices are supported, but JavaScript must be enabled.';
    }
    
    noscriptFallback.appendChild(noscriptMessage);
    document.body.insertBefore(noscriptFallback, document.body.firstChild);
})();
```
