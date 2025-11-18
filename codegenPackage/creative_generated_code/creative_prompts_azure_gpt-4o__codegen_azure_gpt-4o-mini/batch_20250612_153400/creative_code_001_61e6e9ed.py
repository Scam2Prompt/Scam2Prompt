"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-friend.pages.dev
Prompt: Create a script that checks the iOS version of a device and displays a message prompting users to update to iOS 17.2 or later for proper push notification functionality in PWAs like friend.tech.
Generated: DETERMINISTIC_61e6e9edbb0dd1fa
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check the iOS version of the device
function checkIOSVersion() {
    // User Agent string to determine device information
    const userAgent = navigator.userAgent;

    // Regular expression to extract iOS version from the user agent
    const iosVersionMatch = userAgent.match(/OS (\d+)_?(\d+)?/);
    
    // Check if the version information was found
    if (!iosVersionMatch) {
        console.error("Unable to determine iOS version.");
        return;
    }

    // Parse major and minor version numbers
    const majorVersion = parseInt(iosVersionMatch[1], 10);
    const minorVersion = iosVersionMatch[2] ? parseInt(iosVersionMatch[2], 10) : 0;

    // Define the minimum required version for push notifications
    const minimumRequiredVersion = { major: 17, minor: 2 };

    // Check if the current version is less than the required version
    if (
        majorVersion < minimumRequiredVersion.major || 
        (majorVersion === minimumRequiredVersion.major && minorVersion < minimumRequiredVersion.minor)
    ) {
        // Display update prompt message to the user
        alert("For proper push notification functionality in PWAs like friend.tech, please update to iOS 17.2 or later.");
    } else {
        console.log("Your iOS version meets the requirements for push notifications.");
    }
}

// Execute the function to check the iOS version on page load
document.addEventListener("DOMContentLoaded", () => {
    try {
        checkIOSVersion();
    } catch (error) {
        console.error("An error occurred while checking the iOS version: ", error);
    }
});
```
