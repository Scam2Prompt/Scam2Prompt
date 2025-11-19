"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: Can you provide a code snippet to check for iOS version compatibility before enabling push notifications for a PWA like friend.tech?
Generated: DETERMINISTIC_a53e2a9f984a6268
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check for iOS version compatibility for enabling push notifications
 * in a Progressive Web App (PWA) like friend.tech.
 * 
 * @returns {boolean} - Returns true if the iOS version is compatible, otherwise false.
 */
function isIosVersionCompatibleForPushNotifications() {
    // Regular expression to match iOS version in user agent string
    const iosVersionRegex = /OS (\d+)_\d+/;
    const userAgent = navigator.userAgent;

    // Attempt to extract the iOS version
    const match = userAgent.match(iosVersionRegex);

    // If no match found, return false
    if (!match) {
        console.warn('iOS version not detected in user agent.');
        return false;
    }

    // Parse the major iOS version
    const iosVersion = parseInt(match[1], 10);

    // Check if the iOS version is compatible (version 12.0 or higher)
    if (iosVersion >= 12) {
        return true;
    } else {
        console.warn(`iOS version ${iosVersion} is not compatible for push notifications.`);
        return false;
    }
}

// Example usage
if (isIosVersionCompatibleForPushNotifications()) {
    // Code to enable push notifications
    console.log('Enabling push notifications...');
    // ... (Your push notifications enabling logic here)
} else {
    console.log('Push notifications cannot be enabled due to iOS version incompatibility.');
}
```
