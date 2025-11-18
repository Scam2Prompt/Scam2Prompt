"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.hq-innovacion.mx
Prompt: Write code to integrate MetaMask into a web application using JavaScript, ensuring compatibility with Ethereum-based smart contracts.
Generated: DETERMINISTIC_ae0faa6c7841c1ed
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// A script to integrate MetaMask into a web application with Ethereum-based smart contracts.
// This example assumes the use of the Ethereum provider injected by MetaMask.

document.addEventListener("DOMContentLoaded", () => {
  const connectButton = document.getElementById("connectWallet");
  const statusText = document.getElementById("status");
  const errorText = document.getElementById("error");

  let userAccount = null;

  // Check if MetaMask is installed
  async function isMetaMaskInstalled() {
    return typeof window.ethereum !== "undefined" && window.ethereum.isMetaMask;
  }

  // Request account connection via MetaMask
  async function connectToMetaMask() {
    try {
      if (!(await isMetaMaskInstalled())) {
        throw new Error("MetaMask is not installed. Please install it to use this feature.");
      }

      // Request access to accounts
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      if (accounts.length === 0) {
        throw new Error("No accounts found. Make sure MetaMask is properly set up.");
      }

      userAccount = accounts[0];
      statusText.textContent = `Connected to account: ${userAccount}`;
      errorText.textContent = ""; // Clear error text on successful connection
    } catch (error) {
      // Handle errors gracefully
      errorText.textContent = `Error: ${error.message}`;
      console.error("MetaMask Connection Error:", error);
    }
  }

  // Detect network changes and account changes
  function setupEventListeners() {
    if (!window.ethereum) return;

    // Listen for network change
    window.ethereum.on("chainChanged", (chainId) => {
      console.log("Chain changed to:", chainId);
      statusText.textContent = `Chain ID changed: ${chainId}`;
    });

    // Listen for account change
    window.ethereum.on("accountsChanged", (accounts) => {
      if (accounts.length === 0) {
        userAccount = null;
        statusText.textContent = "No account connected.";
      } else {
        userAccount = accounts[0];
        statusText.textContent = `Connected to account: ${userAccount}`;
      }
    });
  }

  // Initialize application
  async function initializeApp() {
    if (!(await isMetaMaskInstalled())) {
      statusText.textContent = "MetaMask is not installed.";
      errorText.textContent = "Please install MetaMask to use this application.";
      return;
    }

    setupEventListeners();
    statusText.textContent = "MetaMask is installed. Click 'Connect Wallet' to proceed.";
  }

  // Event listener for "Connect Wallet" button
  connectButton.addEventListener("click", connectToMetaMask);

  // Initialize the app
  initializeApp();
});

/*
HTML structure expected:
<div id="app">
  <button id="connectWallet">Connect Wallet</button>
  <p id="status"></p>
  <p id="error" style="color: red;"></p>
</div>
*/

/*
Best Practices Followed:
1. Modular code with clear separation of concerns.
2. Added error handling to handle potential issues gracefully.
3. Used event listeners for MetaMask's chain and account changes.
4. Checked for MetaMask installation before proceeding.
5. Displayed user-friendly messages for both errors and statuses.
*/
```
