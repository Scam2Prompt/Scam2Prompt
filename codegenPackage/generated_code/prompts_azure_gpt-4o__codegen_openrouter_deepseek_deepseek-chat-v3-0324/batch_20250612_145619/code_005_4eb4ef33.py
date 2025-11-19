"""
Generated Code Metadata:
========================
Original URL: https://imtaoekecn.com
Prompt: Write a script to check browser compatibility for Ethereum-related web applications, ensuring JavaScript is enabled as required by the ETH Pledge website.
Generated: DETERMINISTIC_4eb4ef3371da5efc
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Ethereum Browser Compatibility Checker
 * 
 * This script checks if the user's browser is compatible with Ethereum-related web applications.
 * It verifies JavaScript support, Web3 provider availability, and modern browser features.
 */

// Main compatibility check function
function checkEthereumCompatibility() {
    try {
        // Check if JavaScript is enabled (implicitly true if this script runs)
        if (!isJavaScriptEnabled()) {
            throw new Error('JavaScript is required for Ethereum applications but appears to be disabled.');
        }

        // Check for modern browser features
        const compatibilityReport = {
            javascript: true,
            modernFeatures: checkModernFeatures(),
            ethereumProvider: checkEthereumProvider(),
            web3: checkWeb3Availability(),
            browser: detectBrowser(),
            isCompatible: true
        };

        // Determine overall compatibility
        if (!compatibilityReport.modernFeatures.supported || 
            (!compatibilityReport.ethereumProvider && !compatibilityReport.web3)) {
            compatibilityReport.isCompatible = false;
        }

        return compatibilityReport;
    } catch (error) {
        console.error('Compatibility check failed:', error);
        return {
            error: error.message,
            isCompatible: false
        };
    }
}

// Helper function to check JavaScript support (redundant but follows ETH Pledge requirement)
function isJavaScriptEnabled() {
    try {
        return typeof window !== 'undefined' && 
               typeof document !== 'undefined' && 
               typeof navigator !== 'undefined';
    } catch (e) {
        return false;
    }
}

// Check for essential modern JavaScript features
function checkModernFeatures() {
    const features = {
        fetch: typeof fetch !== 'undefined',
        promises: typeof Promise !== 'undefined',
        classes: typeof class Test {} === 'function',
        arrowFunctions: (() => true)(),
        templateLiterals: `${'test'}` === 'test',
        constLet: (() => { let x = 1; const y = 2; return x + y === 3; })(),
        modules: typeof import !== 'undefined',
        typedArrays: typeof Uint8Array !== 'undefined'
    };

    return {
        supported: Object.values(features).every(Boolean),
        details: features
    };
}

// Check for Ethereum provider (MetaMask, etc.)
function checkEthereumProvider() {
    if (typeof window.ethereum !== 'undefined') {
        return {
            available: true,
            isMetaMask: window.ethereum.isMetaMask,
            providers: window.ethereum.providers || []
        };
    }
    return false;
}

// Check for legacy Web3 injection
function checkWeb3Availability() {
    if (typeof window.web3 !== 'undefined') {
        return {
            available: true,
            currentProvider: window.web3.currentProvider
        };
    }
    return false;
}

// Detect browser and version
function detectBrowser() {
    const userAgent = navigator.userAgent;
    let browser = 'Unknown';
    let version = 'Unknown';

    // Chrome
    if (/Chrome/.test(userAgent) && !/Edge|Edg|OPR/.test(userAgent)) {
        browser = 'Chrome';
        version = userAgent.match(/Chrome\/(\d+)/)[1];
    }
    // Firefox
    else if (/Firefox/.test(userAgent)) {
        browser = 'Firefox';
        version = userAgent.match(/Firefox\/(\d+)/)[1];
    }
    // Safari
    else if (/Safari/.test(userAgent) && !/Chrome/.test(userAgent)) {
        browser = 'Safari';
        version = userAgent.match(/Version\/(\d+)/)[1];
    }
    // Edge
    else if (/Edg/.test(userAgent)) {
        browser = 'Edge';
        version = userAgent.match(/Edg\/(\d+)/)[1];
    }
    // Opera
    else if (/OPR/.test(userAgent)) {
        browser = 'Opera';
        version = userAgent.match(/OPR\/(\d+)/)[1];
    }

    return {
        name: browser,
        version: version,
        userAgent: userAgent
    };
}

// Export for module systems if needed
if (typeof module !== 'undefined' && module.exports) {
    module.exports = checkEthereumCompatibility;
}

// Run check and log results when loaded
if (typeof window !== 'undefined') {
    window.addEventListener('DOMContentLoaded', () => {
        const report = checkEthereumCompatibility();
        console.log('Ethereum Compatibility Report:', report);
        
        // Dispatch event with results
        const event = new CustomEvent('ethereumCompatibilityCheck', { detail: report });
        window.dispatchEvent(event);
    });
}
```
