"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.meta.electrosil14.com
Prompt: Create a script that listens for account or network changes in MetaMask and updates the UI accordingly.
Generated: DETERMINISTIC_5360b137c7831ac2
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: metamask-listener.js
// This script listens for account and network changes in MetaMask and updates the UI accordingly.

// Ensure the DOM is fully loaded before running the script
document.addEventListener("DOMContentLoaded", () => {
  // Check if MetaMask is available
  if (typeof window.ethereum === "undefined") {
    console.error("MetaMask is not installed or unavailable.");
    alert("Please install MetaMask to use this feature.");
    return;
  }

  // UI Elements
  const accountDisplay = document.getElementById("account");
  const networkDisplay = document.getElementById("network");

  // Helper function to update the displayed account
  const updateAccount = (accounts) => {
    if (accounts.length > 0) {
      accountDisplay.textContent = `Account: ${accounts[0]}`;
    } else {
      accountDisplay.textContent = "Account: Not connected";
    }
  };

  // Helper function to update the displayed network
  const updateNetwork = async () => {
    try {
      const chainId = await ethereum.request({ method: "eth_chainId" });
      networkDisplay.textContent = `Network ID: ${parseInt(chainId, 16)}`;
    } catch (error) {
      console.error("Failed to fetch network ID:", error);
      networkDisplay.textContent = "Network: Error fetching network";
    }
  };

  // Listen for account changes
  ethereum.on("accountsChanged", (accounts) => {
    console.log("Accounts changed:", accounts);
    updateAccount(accounts);
  });

  // Listen for network changes
  ethereum.on("chainChanged", (chainId) => {
    console.log("Network changed to:", chainId);
    updateNetwork();
  });

  // Initialize the UI with current account and network
  const initialize = async () => {
    try {
      const accounts = await ethereum.request({ method: "eth_accounts" });
      updateAccount(accounts);
      updateNetwork();
    } catch (error) {
      console.error("Error initializing MetaMask listener:", error);
      accountDisplay.textContent = "Account: Error fetching account";
      networkDisplay.textContent = "Network: Error fetching network";
    }
  };

  // Start initialization
  initialize();
});

/* 
  To use this script:
  1. Include it in your HTML file.
  2. Ensure your HTML contains elements with IDs "account" and "network" 
     where the account and network information will be displayed.
  Example:
  <div id="account">Account: Not connected</div>
  <div id="network">Network: Not connected</div>
*/
```
