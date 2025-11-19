"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welcome-metamask-cdnn.bravesites.com
Prompt: Can you explain how to integrate MetaMask with a decentralized application (dApp) and provide example code?
Generated: DETERMINISTIC_414d2b704342f597
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Integration of MetaMask with a decentralized application (dApp).
 * This code allows users to connect their MetaMask wallet to your dApp
 * and displays their Ethereum address upon successful connection.
 */

// Ensure the code runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  // HTML elements
  const connectButton = document.getElementById("connectMetaMask");
  const statusText = document.getElementById("status");

  // Check if MetaMask is installed
  if (typeof window.ethereum === "undefined") {
    statusText.textContent = "MetaMask is not installed. Please install it to use this dApp.";
    connectButton.disabled = true; // Disable the connect button if MetaMask is unavailable
    return;
  }

  /**
   * Connect MetaMask wallet on button click.
   */
  connectButton.addEventListener("click", async () => {
    try {
      // Request account access from the user
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

      // Update UI with the user's Ethereum address
      const userAddress = accounts[0]; // Fetch the first account (default account)
      statusText.textContent = `Connected: ${userAddress}`;
      console.log("User Address:", userAddress);
    } catch (error) {
      // Handle errors during the wallet connection process
      console.error("Error connecting to MetaMask:", error);
      statusText.textContent = `Error: ${error.message}`;
    }
  });

  /**
   * Listen for account changes and update the address dynamically.
   * MetaMask triggers this when the user switches accounts or disconnects.
   */
  window.ethereum.on("accountsChanged", (accounts) => {
    if (accounts.length === 0) {
      statusText.textContent = "MetaMask is disconnected.";
    } else {
      statusText.textContent = `Connected: ${accounts[0]}`;
      console.log("Updated User Address:", accounts[0]);
    }
  });
});

/**
 * Example HTML:
 * <button id="connectMetaMask">Connect MetaMask</button>
 * <p id="status">Status: Not Connected</p>
 */
```
