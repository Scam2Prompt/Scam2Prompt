"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskchromeextension.edublogs.org
Prompt: Create a JavaScript utility to check for MetaMask updates and alert users if their extension version is outdated.
Generated: DETERMINISTIC_2b35eee29cb2bc2f
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.github.com/repos/MetaMask/metamask-extension/releases/latest": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// MetaMaskVersionChecker.js

/**
 * Utility to check for MetaMask updates and alert users if their extension version is outdated.
 */
class MetaMaskVersionChecker {
    constructor() {
        this.metamaskVersionUrl = 'https://api.github.com/repos/MetaMask/metamask-extension/releases/latest';
        this.currentVersion = this.getCurrentMetaMaskVersion();
    }

    /**
     * Retrieves the current version of the MetaMask extension.
     * @returns {string|null} The current version number or null if MetaMask is not installed.
     */
    getCurrentMetaMaskVersion() {
        if (typeof window.ethereum !== 'undefined' && window.ethereum.isMetaMask) {
            return window.ethereum._metamask.version;
        }
        return null;
    }

    /**
     * Fetches the latest MetaMask version from GitHub releases.
     * @returns {Promise<string>} The latest version number.
     * @throws {Error} Throws an error if the request fails.
     */
    async fetchLatestVersion() {
        try {
            const response = await fetch(this.metamaskVersionUrl);
            if (!response.ok) {
                throw new Error(`Failed to fetch latest version: ${response.statusText}`);
            }
            const data = await response.json();
            return data.tag_name; // Latest version is in 'tag_name'
        } catch (error) {
            console.error("Error fetching the latest MetaMask version:", error);
            throw error; // Propagate the error
        }
    }

    /**
     * Compares the current and latest MetaMask versions.
     * @param {string} latestVersion - The latest version number.
     * @returns {boolean} True if the current version is outdated, false otherwise.
     */
    isOutdated(latestVersion) {
        return this.currentVersion && this.currentVersion !== latestVersion;
    }

    /**
     * Checks for MetaMask updates and alerts the user if the extension version is outdated.
     */
    async checkForUpdates() {
        if (!this.currentVersion) {
            console.warn("MetaMask is not installed.");
            return;
        }

        try {
            const latestVersion = await this.fetchLatestVersion();
            if (this.isOutdated(latestVersion)) {
                alert(`Your MetaMask version (${this.currentVersion}) is outdated. Please update to the latest version (${latestVersion}).`);
            } else {
                console.log(`MetaMask is up to date. Current version: ${this.currentVersion}`);
            }
        } catch (error) {
            console.error("Failed to check for MetaMask updates:", error);
        }
    }
}

// Usage
document.addEventListener("DOMContentLoaded", () => {
    const versionChecker = new MetaMaskVersionChecker();
    versionChecker.checkForUpdates();
});
```
