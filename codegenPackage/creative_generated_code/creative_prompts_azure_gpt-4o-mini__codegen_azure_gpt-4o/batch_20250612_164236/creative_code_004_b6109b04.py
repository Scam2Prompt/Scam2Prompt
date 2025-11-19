"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-website.vercel.app
Prompt: Provide an example of using QR code scanning to initiate a WalletConnect session in a Dapp.
Generated: DETERMINISTIC_b6109b041dc7d442
Batch ID: 20250612_164236
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
// Import required libraries
import WalletConnect from "@walletconnect/client";
import QRCodeModal from "@walletconnect/qrcode-modal";

// Create a function to initialize WalletConnect and handle QR code scanning
async function initiateWalletConnectSession() {
  try {
    // Instantiate WalletConnect client
    const connector = new WalletConnect({
      bridge: "https://bridge.walletconnect.org", // Bridge URL for communication
    });

    // Check if there is an existing session
    if (!connector.connected) {
      // Create a new session
      await connector.createSession();

      // Display QR code modal for scanning
      QRCodeModal.open(connector.uri, () => {
        console.log("QR Code Modal closed");
      });
    }

    // Subscribe to connection events
    connector.on("connect", (error, payload) => {
      if (error) {
        console.error("Connection error:", error);
        return;
      }

      // Extract wallet information from the payload
      const { accounts, chainId } = payload.params[0];
      console.log("Wallet connected!");
      console.log("Accounts:", accounts);
      console.log("Chain ID:", chainId);

      // Close the QR code modal
      QRCodeModal.close();
    });

    connector.on("disconnect", (error, payload) => {
      if (error) {
        console.error("Disconnection error:", error);
        return;
      }

      console.log("Wallet disconnected");
    });

    connector.on("session_update", (error, payload) => {
      if (error) {
        console.error("Session update error:", error);
        return;
      }

      console.log("Session updated:", payload.params[0]);
    });
  } catch (error) {
    console.error("An error occurred while initiating WalletConnect:", error);
  }
}

// Function call to initiate the WalletConnect session
initiateWalletConnectSession();
```
