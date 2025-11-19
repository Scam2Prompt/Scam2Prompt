"""
Generated Code Metadata:
========================
Original URL: https://www.rainbnb.live
Prompt: Write a script to detect whether JavaScript is enabled in a user's browser and display a warning message if it is disabled, as seen on RainBNB.
Generated: DETERMINISTIC_766530d379239736
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript detection script

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a hidden input field to store JavaScript status
    const jsEnabledInput = document.createElement('input');
    jsEnabledInput.type = 'hidden';
    jsEnabledInput.id = 'js-enabled';
    jsEnabledInput.value = 'true';

    // Add the input field to the page
    document.body.appendChild(jsEnabledInput);

    // Check if the input field still exists after 100ms
    setTimeout(() => {
        const jsEnabled = document.getElementById('js-enabled') !== null;
        displayJavaScriptStatus(jsEnabled);
    }, 100);
}

// Function to display JavaScript status
function displayJavaScriptStatus(enabled) {
    // Get the warning message element
    const warningMessageElement = document.getElementById('js-warning-message');

    // If JavaScript is disabled, display the warning message
    if (!enabled) {
        warningMessageElement.style.display = 'block';
    } else {
        warningMessageElement.style.display = 'none';
    }
}

// Function to initialize JavaScript detection
function initJavaScriptDetection() {
    try {
        // Check if JavaScript is enabled
        isJavaScriptEnabled();

        // Add event listener to window load
        window.addEventListener('load', () => {
            // Check JavaScript status on page load
            const jsEnabledInput = document.getElementById('js-enabled');
            if (jsEnabledInput) {
                const jsEnabled = jsEnabledInput.value === 'true';
                displayJavaScriptStatus(jsEnabled);
            }
        });
    } catch (error) {
        console.error('Error initializing JavaScript detection:', error);
    }
}

// Initialize JavaScript detection on document ready
document.addEventListener('DOMContentLoaded', initJavaScriptDetection);
```

```html
<!-- HTML code for warning message display -->

<!-- Warning message element -->
<div id="js-warning-message" style="display: none;">
    <p>JavaScript is disabled in your browser. Please enable JavaScript to use this site.</p>
</div>

<!-- noscript element for browsers without JavaScript -->
<noscript>
    <div>
        <p>JavaScript is disabled in your browser. Please enable JavaScript to use this site.</p>
    </div>
</noscript>
```

```css
/* CSS code for warning message styling */

/* Style the warning message */
#js-warning-message {
    background-color: #FFC080;
    border: 1px solid #FF9900;
    padding: 10px;
    text-align: center;
}

#js-warning-message p {
    margin: 0;
}
```
