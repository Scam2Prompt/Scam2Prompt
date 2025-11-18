"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spicydao.finance
Prompt: Generate JavaScript code to detect wallet connectivity status and display a "Loading..." message, as seen on SpicyDAO's platform.
Generated: DETERMINISTIC_e981430481864a4e
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check wallet connectivity status and display appropriate messages
(function () {
  // Wait for the DOM to load completely
  document.addEventListener("DOMContentLoaded", () => {
    // Get reference to the element where messages will be displayed
    const statusElement = document.getElementById("wallet-status");

    if (!statusElement) {
      console.error("Element with id 'wallet-status' not found.");
      return;
    }

    // Display a loading message while checking wallet status
    statusElement.textContent = "Loading...";

    // Function to check wallet connectivity
    const checkWalletConnectivity = async () => {
      try {
        // Check if the browser supports Ethereum wallets (e.g., MetaMask)
        if (window.ethereum) {
          // Try requesting accounts from the wallet
          const accounts = await window.ethereum.request({ method: "eth_accounts" });

          // Detect connectivity based on accounts array
          if (accounts && accounts.length > 0) {
            statusElement.textContent = "Wallet Connected";
          } else {
            statusElement.textContent = "Wallet Not Connected";
          }
        } else {
          // No wallet provider detected
          statusElement.textContent = "No Wallet Detected";
        }
      } catch (error) {
        // Catch and display errors
        console.error("Error checking wallet connectivity:", error);
        statusElement.textContent = "Error Checking Wallet Connectivity";
      }
    };

    // Invoke the wallet connectivity check
    checkWalletConnectivity();
  });
})();
```

```html
<!-- HTML Structure -->
<div id="wallet-status"></div>
```

Ensure that the `wallet-status` div is present in your HTML for the script to work properly. This script assumes modern browser support for JavaScript and Ethereum wallets like MetaMask.
