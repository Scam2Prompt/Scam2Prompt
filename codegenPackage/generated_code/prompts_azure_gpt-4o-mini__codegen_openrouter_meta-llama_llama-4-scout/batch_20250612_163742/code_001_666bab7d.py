"""
Generated Code Metadata:
========================
Original URL: https://sdddd.pages.dev
Prompt: Write a JavaScript function that checks if the user is on a desktop and prompts them to switch devices if they are not.
Generated: DETERMINISTIC_666bab7d8708cd79
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if the user is on a desktop device and prompts them to switch devices if they are not.
 */

/**
 * Function to check if user is on a desktop device
 * @returns {Boolean} True if user is on a desktop device, false otherwise
 */
function isDesktopDevice() {
    // Check if the user agent contains any mobile or tablet keywords
    const mobileKeywords = ['Mobile', 'iPhone', 'iPad', 'Android', 'Tablet'];
    const userAgent = navigator.userAgent;

    // Check if user agent is null or undefined
    if (!userAgent) {
        // If user agent is not available, assume it's a desktop device
        return true;
    }

    // Check for mobile or tablet keywords in user agent
    for (const keyword of mobileKeywords) {
        if (userAgent.includes(keyword)) {
            return false;
        }
    }

    // If no mobile or tablet keywords are found, assume it's a desktop device
    return true;
}

/**
 * Function to prompt user to switch devices
 */
function promptSwitchDevices() {
    // Create a prompt message
    const message = 'You seem to be on a mobile or tablet device. Please switch to a desktop device for a better experience.';

    // Display the prompt message
    if (confirm(message)) {
        // If user confirms, redirect to a URL or perform any other action
        // For now, just close the window or tab
        window.close();
    }
}

/**
 * Main function to check and prompt user
 */
function checkDeviceAndPrompt() {
    try {
        // Check if user is on a desktop device
        if (!isDesktopDevice()) {
            // If not, prompt user to switch devices
            promptSwitchDevices();
        }
    } catch (error) {
        // Log any errors that occur during execution
        console.error('Error checking device:', error);
    }
}

// Call the main function
checkDeviceAndPrompt();
```
