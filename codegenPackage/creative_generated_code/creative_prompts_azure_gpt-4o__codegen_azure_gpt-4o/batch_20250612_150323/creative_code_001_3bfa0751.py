"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.network
Prompt: Generate a script that uses the WalletConnect API to establish a connection between a wallet and a decentralized application (dApp).
Generated: DETERMINISTIC_3bfa07517fb07b16
Batch ID: 20250612_150323
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
// Import necessary dependencies
const WalletConnect = require("@walletconnect/client");
const QRCodeModal = require("@walletconnect/qrcode-modal");

// Initialize WalletConnect client
const connector = new WalletConnect({
  bridge: "https://bridge.walletconnect.org", // Required
});

// Function to establish connection with wallet
async function connectWallet() {
  try {
    // Check if the connector is already connected
    if (!connector.connected) {
      // Create a new session
      await connector.createSession();

      // Display QR Code modal to connect wallet
      QRCodeModal.open(connector.uri);
    }

    // Listen for connection events
    connector.on("connect", (error, payload) => {
      if (error) {
        console.error("Error during connection:", error);
        return;
      }

      // Connection established
      QRCodeModal.close(); // Close the QR Code modal
      const { accounts, chainId } = payload.params[0];
      console.log("Connected:", { accounts, chainId });
    });

    // Listen for session update events
    connector.on("session_update", (error, payload) => {
      if (error) {
        console.error("Session update error:", error);
        return;
      }

      // Session updated
      const { accounts, chainId } = payload.params[0];
      console.log("Session updated:", { accounts, chainId });
    });

    // Listen for disconnect events
    connector.on("disconnect", (error) => {
      if (error) {
        console.error("Error during disconnection:", error);
        return;
      }

      // Disconnected
      console.log("Disconnected from wallet");
    });
  } catch (err) {
    console.error("Failed to connect wallet:", err);
  }
}

// Function to disconnect wallet
function disconnectWallet() {
  try {
    if (connector.connected) {
      connector.killSession();
      console.log("Disconnected manually from wallet");
    } else {
      console.log("No active wallet session to disconnect");
    }
  } catch (err) {
    console.error("Error during disconnect:", err);
  }
}

// Example usage
(async () => {
  console.log("Attempting to connect wallet...");
  await connectWallet();

  // Example: Call disconnect wallet after some time
  setTimeout(() => {
    disconnectWallet();
  }, 60000); // Disconnect after 60 seconds
})();
```

### Notes:
- Ensure you install the required dependencies using `npm install @walletconnect/client @walletconnect/qrcode-modal`.
- Update the `bridge` URL if a custom WalletConnect bridge is to be used.
- The above code is designed to be production-ready with proper error handling and event management.
