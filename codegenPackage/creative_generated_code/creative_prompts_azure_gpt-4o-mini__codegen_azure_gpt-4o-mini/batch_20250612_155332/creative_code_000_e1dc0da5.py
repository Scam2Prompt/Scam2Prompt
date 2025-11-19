"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-collab.land
Prompt: How can I integrate WalletConnect V2 with my dApp to support multiple wallets like MetaMask and Coinbase Wallet?
Generated: DETERMINISTIC_e1dc0da5885ca0fc
Batch ID: 20250612_155332
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.walletconnect.org": {
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
// Import necessary libraries
import WalletConnectClient from "@walletconnect/client";
import QRCodeModal from "@walletconnect/qrcode-modal";

// Initialize WalletConnect
const connector = new WalletConnectClient({
  bridge: "https://bridge.walletconnect.org", // Required
  qrcodeModal: QRCodeModal,
});

// Function to connect to a wallet
async function connectWallet() {
  try {
    // Check if already connected
    if (!connector.connected) {
      // Create a new session
      await connector.createSession();
    }

    // Subscribe to connection events
    subscribeToEvents();

    // Get wallet accounts
    const { accounts } = connector;

    console.log("Connected accounts:", accounts);
    return accounts;
  } catch (error) {
    console.error("Failed to connect wallet:", error);
    throw new Error("Connection failed");
  }
}

// Function to subscribe to WalletConnect events
function subscribeToEvents() {
  // Event for session update
  connector.on("session_update", (error, payload) => {
    if (error) {
      throw error;
    }

    // Get updated accounts and chainId
    const { accounts, chainId } = payload.params[0];
    console.log("Updated accounts:", accounts);
  });

  // Event for session disconnection
  connector.on("disconnect", (error, payload) => {
    if (error) {
      throw error;
    }

    console.log("Disconnected", payload);
  });
}

// Function to send a transaction
async function sendTransaction(to, value) {
  try {
    const txParams = {
      from: connector.accounts[0], // Use the first connected account
      to,
      value: value.toString(16), // Convert value to hexadecimal
      gas: "2000000", // Set gas limit
    };

    const result = await connector.sendTransaction(txParams);
    console.log("Transaction result:", result);
    return result;
  } catch (error) {
    console.error("Transaction failed:", error);
    throw new Error("Transaction failed");
  }
}

// Event listener to trigger wallet connection
document.getElementById("connectButton").addEventListener("click", connectWallet);

// Export functions for use in other modules
export { connectWallet, sendTransaction };
```

In the code above, we integrate WalletConnect V2 into a dApp, providing functions to connect to wallets, subscribe to events, and send transactions. It includes proper error handling and is structured for production use. Make sure to test and adapt it to your specific application context.
