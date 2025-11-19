"""
Generated Code Metadata:
========================
Original URL: https://presales-friend.pages.dev
Prompt: Generate JavaScript code snippet to check if a user's iOS version is compatible with friend.tech's PWA notification features.
Generated: DETERMINISTIC_b5a5499c9d339437
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if the user's iOS version is compatible with friend.tech's PWA notification features.
 * @returns {boolean} True if compatible, false otherwise.
 */
function isIOSVersionCompatible() {
    try {
        // Parse user agent to detect iOS
        const userAgent = window.navigator.userAgent;
        const isIOS = /iPad|iPhone|iPod/.test(userAgent) && !window.MSStream;
        
        if (!isIOS) {
            // Not iOS, assume compatible
            return true;
        }

        // Extract iOS version from user agent
        const iosVersionMatch = userAgent.match(/OS (\d+)_(\d+)_?(\d+)?/);
        if (!iosVersionMatch) {
            console.warn('Could not detect iOS version');
            return false;
        }

        // Convert version parts to number
        const majorVersion = parseInt(iosVersionMatch[1], 10);
        const minorVersion = parseInt(iosVersionMatch[2], 10);
        const patchVersion = iosVersionMatch[3] ? parseInt(iosVersionMatch[3], 10) : 0;

        // friend.tech requires iOS 16.4+ for PWA notifications
        if (majorVersion > 16) {
            return true;
        } else if (majorVersion === 16) {
            if (minorVersion > 4) {
                return true;
            } else if (minorVersion === 4) {
                return patchVersion >= 0;
            }
        }

        return false;
    } catch (error) {
        console.error('Error checking iOS version:', error);
        return false;
    }
}
```
