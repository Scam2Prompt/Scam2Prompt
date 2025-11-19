"""
Generated Code Metadata:
========================
Original URL: https://riotplatforms-analyze.com
Prompt: Generate code to detect and notify users when JavaScript is disabled on a web application like "Workbench."
Generated: DETERMINISTIC_cce442b971572643
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript detection and notification script

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a hidden input field to store JavaScript status
    const jsEnabledInput = document.createElement('input');
    jsEnabledInput.type = 'hidden';
    jsEnabledInput.id = 'js-enabled';
    jsEnabledInput.value = 'true';

    // Add the input field to the page
    document.body.appendChild(jsEnabledInput);

    // Check if the input field is still present after 1 second
    setTimeout(() => {
        const jsEnabled = document.getElementById('js-enabled');
        if (jsEnabled) {
            // If the input field is still present, JavaScript is enabled
            jsEnabled.value = 'true';
        } else {
            // If the input field is not present, JavaScript is disabled
            notifyUser();
        }
    }, 1000);
}

// Function to notify the user when JavaScript is disabled
function notifyUser() {
    // Create a notification container
    const notificationContainer = document.createElement('div');
    notificationContainer.id = 'js-disabled-notification';

    // Create a notification message
    const notificationMessage = document.createElement('p');
    notificationMessage.textContent = 'JavaScript is disabled. Please enable JavaScript to use Workbench.';

    // Add the notification message to the container
    notificationContainer.appendChild(notificationMessage);

    // Add the notification container to the page
    document.body.appendChild(notificationContainer);

    // Style the notification container
    notificationContainer.style.position = 'fixed';
    notificationContainer.style.top = '0';
    notificationContainer.style.left = '0';
    notificationContainer.style.width = '100%';
    notificationContainer.style.background = '#FFC080';
    notificationContainer.style.color = '#666';
    notificationContainer.style.padding = '1em';
    notificationContainer.style.textAlign = 'center';
    notificationContainer.style.zIndex = '1000';
}

// Check if JavaScript is enabled on page load
document.addEventListener('DOMContentLoaded', () => {
    isJavaScriptEnabled();
});

// Fallback for older browsers that don't support the DOMContentLoaded event
window.onload = () => {
    isJavaScriptEnabled();
};

// Fallback for browsers that have JavaScript disabled from the start
try {
    if (typeof document !== 'undefined' && document.readyState === 'complete') {
        isJavaScriptEnabled();
    }
} catch (error) {
    // Ignore error and continue
}
```

```html
<!-- NoScript detection HTML fallback -->
<noscript>
    <div id="js-disabled-notification">
        <p>JavaScript is disabled. Please enable JavaScript to use Workbench.</p>
    </div>
</noscript>
```
