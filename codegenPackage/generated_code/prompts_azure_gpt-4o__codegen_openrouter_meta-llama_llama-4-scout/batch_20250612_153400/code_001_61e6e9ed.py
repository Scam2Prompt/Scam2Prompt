"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Create a script that checks the iOS version of a device and displays a message prompting users to update to iOS 17.2 or later for proper push notification functionality in PWAs like friend.tech.
Generated: DETERMINISTIC_61e6e9edbb0dd1fa
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ios-version-check.js

/**
 * Checks the iOS version of a device and prompts users to update to iOS 17.2 or later
 * for proper push notification functionality in PWAs like friend.tech.
 */

// Define the minimum required iOS version
const MIN_REQUIRED_IOS_VERSION = '17.2';

/**
 * Get the user agent string from the navigator object
 * @type {string}
 */
const userAgent = navigator.userAgent;

/**
 * Regular expression to match iOS versions in the user agent string
 * @type {RegExp}
 */
const iosVersionRegex = /iPhone OS (\d+(?:_\d+)*)/;

/**
 * Extract the iOS version from the user agent string
 * @returns {string|null} The iOS version or null if not found
 */
function getIosVersion() {
  const match = userAgent.match(iosVersionRegex);
  return match && match[1];
}

/**
 * Compare two iOS version strings
 * @param {string} version1 - The first version string
 * @param {string} version2 - The second version string
 * @returns {number} A negative value if version1 is less than version2,
 *                   a positive value if version1 is greater than version2,
 *                   0 if version1 is equal to version2
 */
function compareIosVersions(version1, version2) {
  const version1Parts = version1.split('_').map(Number);
  const version2Parts = version2.split('_').map(Number);

  for (let i = 0; i < Math.max(version1Parts.length, version2Parts.length); i++) {
    const part1 = version1Parts[i] || 0;
    const part2 = version2Parts[i] || 0;

    if (part1 < part2) {
      return -1;
    } else if (part1 > part2) {
      return 1;
    }
  }

  return 0;
}

/**
 * Check if the device's iOS version is less than the minimum required version
 * @returns {boolean} True if the device's iOS version is less than the minimum required version
 */
function needsUpdate() {
  const iosVersion = getIosVersion();
  return iosVersion && compareIosVersions(iosVersion, MIN_REQUIRED_IOS_VERSION) < 0;
}

// Check if the device needs an update
if (needsUpdate()) {
  // Display a message prompting users to update to iOS 17.2 or later
  alert('Please update your device to iOS 17.2 or later for proper push notification functionality in PWAs like friend.tech.');
} else {
  // console.log('Device is running a compatible iOS version.');
}

// Example usage:
// You can call the needsUpdate function and handle the result as needed
// if (needsUpdate()) {
//   console.log('Device needs an update');
// } else {
//   console.log('Device is up-to-date');
// }
```
