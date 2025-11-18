"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Create a JavaScript utility to check for MetaMask updates and alert users if their extension version is outdated.
Generated: DETERMINISTIC_2b35eee29cb2bc2f
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Utility to check for MetaMask version updates and alert the user if their extension version is outdated.
 * This assumes a known minimum required version of MetaMask.
 */

// Configuration
const MINIMUM_METAMASK_VERSION = '10.25.0'; // Example minimum version, update as needed.

/**
 * Compares two semantic version strings.
 * @param {string} currentVersion - The current version string.
 * @param {string} minimumVersion - The minimum required version string.
 * @returns {boolean} - Returns true if the current version is greater or equal to the minimum version, otherwise false.
 */
function isVersionOutdated(currentVersion, minimumVersion) {
  try {
    const currentParts = currentVersion.split('.').map(Number);
    const minimumParts = minimumVersion.split('.').map(Number);

    for (let i = 0; i < Math.max(currentParts.length, minimumParts.length); i++) {
      const currentPart = currentParts[i] || 0;
      const minimumPart = minimumParts[i] || 0;

      if (currentPart > minimumPart) return false;
      if (currentPart < minimumPart) return true;
    }

    return false; // Versions are equal.
  } catch (error) {
    console.error('Error comparing versions:', error);
    return true; // Default to outdated if comparison fails.
  }
}

/**
 * Checks the MetaMask extension version and alerts the user if it is outdated.
 */
async function checkMetaMaskVersion() {
  if (!window.ethereum || !window.ethereum.isMetaMask) {
    console.warn('MetaMask is not detected. Please install MetaMask to use this feature.');
    alert('MetaMask is required but not detected. Please install MetaMask.');
    return;
  }

  try {
    const metaMaskVersion = window.ethereum._metamask.version; // Access MetaMask version (undocumented API).
    if (!metaMaskVersion) {
      console.warn('Unable to detect MetaMask version.');
      alert('Unable to detect MetaMask version. Please ensure you are using the latest version.');
      return;
    }

    if (isVersionOutdated(metaMaskVersion, MINIMUM_METAMASK_VERSION)) {
      alert(
        `Your MetaMask version (${metaMaskVersion}) is outdated. Please update to version ${MINIMUM_METAMASK_VERSION} or later.`
      );
    } else {
      console.log('MetaMask is up-to-date.');
    }
  } catch (error) {
    console.error('Error checking MetaMask version:', error);
    alert('An error occurred while checking the MetaMask version. Please try again later.');
  }
}

// Example usage:
checkMetaMaskVersion();
```
