"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Write a function to check if a PWA is installed on a user's device and display a custom message encouraging installation if it is not detected.
Generated: DETERMINISTIC_a8e3647c6f3bef26
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if a Progressive Web App (PWA) is installed on the user's device.
 * If the PWA is not installed, it displays a custom message encouraging installation.
 */
function checkPWAInstallation() {
    // Check if the browser supports the 'beforeinstallprompt' event
    if ('serviceWorker' in navigator) {
        // Check if the PWA is already installed
        if (window.matchMedia('(display-mode: standalone)').matches) {
            console.log("PWA is already installed.");
            return; // PWA is installed, exit the function
        } else {
            // PWA is not installed, display a custom message
            displayInstallationMessage();
        }
    } else {
        console.error("Service Workers are not supported in this browser.");
    }
}

/**
 * Displays a custom message encouraging the user to install the PWA.
 */
function displayInstallationMessage() {
    const message = document.createElement('div');
    message.style.position = 'fixed';
    message.style.bottom = '20px';
    message.style.left = '20px';
    message.style.padding = '10px';
    message.style.backgroundColor = '#f8d7da';
    message.style.color = '#721c24';
    message.style.border = '1px solid #f5c6cb';
    message.style.borderRadius = '5px';
    message.style.zIndex = '1000';
    message.innerText = "This app is not installed. Consider installing it for a better experience!";
    
    // Append the message to the body
    document.body.appendChild(message);
    
    // Automatically remove the message after 10 seconds
    setTimeout(() => {
        message.remove();
    }, 10000);
}

// Call the function to check for PWA installation
checkPWAInstallation();
```
