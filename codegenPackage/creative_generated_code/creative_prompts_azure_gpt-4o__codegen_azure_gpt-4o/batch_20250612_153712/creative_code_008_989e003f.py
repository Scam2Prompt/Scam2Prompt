"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metymascklogini.webflow.io
Prompt: Provide a JavaScript example for interacting with the MetaMask extension to retrieve account details and initiate a transaction on the Ethereum blockchain.
Generated: DETERMINISTIC_989e003f1477964a
Batch ID: 20250612_153712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script demonstrates how to interact with the MetaMask extension to retrieve account details
// and initiate a transaction on the Ethereum blockchain.

// Ensure the code is executed after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", async () => {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === "undefined") {
      console.error("MetaMask is not installed. Please install MetaMask to continue.");
      return;
    }

    // Request account access from MetaMask
    const accounts = await ethereum.request({ method: "eth_requestAccounts" });

    // Log the connected account(s)
    console.log("Connected account(s):", accounts);

    // If no account is connected, stop execution
    if (accounts.length === 0) {
      console.error("No accounts found. Please ensure your MetaMask wallet is unlocked.");
      return;
    }

    // Retrieve the currently selected account
    const selectedAccount = accounts[0];
    console.log("Selected account:", selectedAccount);

    // Example: Sending a transaction
    const transactionParameters = {
      to: "0xRecipientAddressHere", // Replace with the recipient's Ethereum address
      from: selectedAccount,       // Sender's Ethereum address
      value: "0x29a2241af62c0000", // Amount to send in Wei (example: 0.1 ETH in Wei)
      gas: "0x5208",               // Gas limit (example: 21000 in hexadecimal)
    };

    try {
      // Initiate the transaction via MetaMask
      const txHash = await ethereum.request({
        method: "eth_sendTransaction",
        params: [transactionParameters],
      });

      // Log the transaction hash
      console.log("Transaction successful. Hash:", txHash);
    } catch (error) {
      // Handle transaction errors
      console.error("Transaction failed:", error.message);
    }
  } catch (error) {
    // Handle general errors
    console.error("An error occurred:", error.message);
  }
});
```
