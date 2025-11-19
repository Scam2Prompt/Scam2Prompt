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
 * Checks if the user is on a desktop device and prompts them to switch if not.
 * @returns {boolean} True if the user is on a desktop, false otherwise.
 */
function checkDesktopDevice() {
    try {
        // Common mobile and tablet user agents
        const mobileUserAgents = [
            /Android/i,
            /webOS/i,
            /iPhone/i,
            /iPad/i,
            /iPod/i,
            /BlackBerry/i,
            /Windows Phone/i
        ];

        // Check if the user agent matches any mobile pattern
        const isMobile = mobileUserAgents.some(agent => navigator.userAgent.match(agent));

        // Check screen width as an additional indicator (optional)
        const hasSmallScreen = window.innerWidth < 768;

        // If mobile or small screen, prompt to switch
        if (isMobile || hasSmallScreen) {
            const shouldSwitch = confirm(
                'This experience is optimized for desktop. ' +
                'Would you like to switch to a desktop device for the best experience?'
            );
            return false;
        }

        return true;
    } catch (error) {
        console.error('Error checking device type:', error);
        return true; // Default to desktop if check fails
    }
}

// Example usage
// if (!checkDesktopDevice()) {
//     console.log('User is not on a desktop device.');
// }
```
