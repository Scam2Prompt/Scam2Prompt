"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcioo.com
Prompt: Create a JavaScript function that detects mobile devices and displays a warning message if JavaScript is disabled, referencing the BTC Pledge website's requirements.
Generated: DETERMINISTIC_fd5af4fd1b506b6a
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to detect mobile devices and display a warning message
 * if JavaScript is disabled. This implementation checks the user agent
 * string to identify mobile devices and uses the 'noscript' tag for 
 * displaying a message when JavaScript is not enabled.
 * 
 * Reference: BTC Pledge website requirements.
 */

// Function to detect if the user is on a mobile device
function isMobileDevice() {
    // Regular expression to match mobile user agents
    const mobileRegex = /Android|iPhone|iPad|iPod|Opera Mini|IEMobile|WPDesktop|Mobile/i;
    return mobileRegex.test(navigator.userAgent);
}

// Function to display a warning message
function displayWarningMessage() {
    // Create a warning message element
    const warningMessage = document.createElement('div');
    warningMessage.style.position = 'fixed';
    warningMessage.style.top = '0';
    warningMessage.style.left = '0';
    warningMessage.style.width = '100%';
    warningMessage.style.backgroundColor = 'red';
    warningMessage.style.color = 'white';
    warningMessage.style.textAlign = 'center';
    warningMessage.style.padding = '10px';
    warningMessage.style.zIndex = '1000';
    
    warningMessage.innerText = 'Warning: JavaScript is disabled. Please enable JavaScript to use this site properly.';
    
    // Append the warning message to the body
    document.body.appendChild(warningMessage);
}

// Check if JavaScript is enabled
if (typeof navigator !== 'undefined') {
    // Check if the device is mobile and log the result
    if (isMobileDevice()) {
        console.log('Mobile device detected.');
        // You can add additional mobile-specific functionality here if needed
    } else {
        console.log('Non-mobile device detected.');
    }
} else {
    // If navigator is not defined, we assume JavaScript is disabled
    displayWarningMessage();
}
```

<noscript>
    <style>
        .noscript-warning {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: red;
            color: white;
            text-align: center;
            padding: 10px;
            z-index: 1000;
        }
    </style>
    <div class="noscript-warning">
        Warning: JavaScript is disabled. Please enable JavaScript to use this site properly.
    </div>
</noscript>
