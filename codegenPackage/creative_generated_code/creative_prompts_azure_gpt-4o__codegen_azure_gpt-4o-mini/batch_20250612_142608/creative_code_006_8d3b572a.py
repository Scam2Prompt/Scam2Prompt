"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Generate JavaScript code to detect if the MetaMask browser extension is installed and prompt the user to install it if missing, based on the "MetaMask钱包安装视频" section.
Generated: DETERMINISTIC_8d3b572a16b1b88a
Batch ID: 20250612_142608
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://metamask.io/download.html": {
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
// Function to detect if MetaMask is installed
function detectMetaMask() {
    // Check if the window object contains the ethereum property
    if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');
        return true;
    } else {
        console.warn('MetaMask is not installed.');
        return false;
    }
}

// Function to prompt user to install MetaMask
function promptInstallMetaMask() {
    // Create a message to inform the user about MetaMask installation
    const message = "MetaMask is not detected. Please install it to continue using this application.";
    
    // Open a dialog to prompt the user
    if (confirm(message)) {
        // Redirect user to MetaMask installation page
        window.open('https://metamask.io/download.html', '_blank');
    }
}

// Main function to check for MetaMask installation and prompt if necessary
function checkMetaMaskInstallation() {
    try {
        // Detect MetaMask installation
        if (!detectMetaMask()) {
            // Prompt user to install MetaMask if not installed
            promptInstallMetaMask();
        }
    } catch (error) {
        // Log error message in the console for debugging
        console.error('An error occurred while checking MetaMask installation:', error);
    }
}

// Run the check when the document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    checkMetaMaskInstallation();
});
```
