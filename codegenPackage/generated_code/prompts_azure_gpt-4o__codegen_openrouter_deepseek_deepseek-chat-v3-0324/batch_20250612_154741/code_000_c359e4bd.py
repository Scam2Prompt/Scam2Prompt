"""
Generated Code Metadata:
========================
Original URL: https://trade.94la.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on the Trade website.
Generated: DETERMINISTIC_c359e4bdbdafe144
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and hide the no-js message if it is
(function() {
    'use strict';

    // Check if the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        try {
            // Remove the no-js class from the HTML element if JavaScript is enabled
            document.documentElement.classList.remove('no-js');
            
            // Find and hide the no-js message element if it exists
            var noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        } catch (error) {
            console.error('Error in JavaScript detection:', error);
        }
    });

    // Fallback: If DOMContentLoaded doesn't fire, run the check when window loads
    window.addEventListener('load', function() {
        try {
            document.documentElement.classList.remove('no-js');
            var noJsMessage = document.getElementById('no-js-message');
            if (noJsMessage) {
                noJsMessage.style.display = 'none';
            }
        } catch (error) {
            console.error('Error in JavaScript detection fallback:', error);
        }
    });
})();

// HTML structure that should be included in the page:
/*
<html class="no-js">
    <head>
        <noscript>
            <style>
                .no-js-message { display: none; }
                #no-js-message { display: block; }
            </style>
        </noscript>
    </head>
    <body>
        <div id="no-js-message" class="no-js-message">
            JavaScript is disabled in your browser. Please enable JavaScript for full functionality.
        </div>
        <!-- Rest of your content -->
    </body>
</html>
*/
```
