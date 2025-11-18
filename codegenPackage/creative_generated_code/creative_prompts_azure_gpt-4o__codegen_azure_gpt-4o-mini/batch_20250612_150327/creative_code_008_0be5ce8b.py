"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-v3.devpq.com
Prompt: Write code to send a transaction from a wallet to a dApp using WalletConnect V3, based on PQ WalletConnect V3.
Generated: DETERMINISTIC_0be5ce8b6a0fdb11
Batch ID: 20250612_150327
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
import WalletConnect from "@walletconnect/client"; // WalletConnect client
import QRCodeModal from "@walletconnect/qrcode-modal"; // QR Code Modal for WalletConnect
import { ethers } from "ethers"; // Ethers.js for Ethereum interaction

// Initialize a WalletConnect connector
const connector = new WalletConnect({
  bridge: "https://bridge.walletconnect.org", // Bridge server for WalletConnect
  qrcodeModal: QRCodeModal, // QR code modal for connecting wallets
});

/**
 * Function to send a transaction from a wallet to a dApp
 * @param {string} to - The address of the dApp to send the transaction to
 * @param {string} amount - The amount of Ether to send (in wei)
 */
async function sendTransaction(to, amount) {
  try {
    // Check if the connector is connected
    if (!connector.connected) {
      // Create a new session if not connected
      await connector.createSession();
    }

    // Get the accounts from the connector
    const accounts = connector.accounts;
    
    // Prepare the transaction details
    const transaction = {
      from: accounts[0], // Sender's account
      to: to, // Recipient's address (dApp)
      value: ethers.BigNumber.from(amount), // Transaction amount (in wei)
      gasLimit: ethers.BigNumber.from("21000"), // Basic gas limit for a simple transfer
      chainId: 1, // Mainnet chain ID
    };

    // Send the transaction
    const result = await connector.sendTransaction(transaction);

    // Log the transaction result
    console.log("Transaction successful:", result);
  } catch (error) {
    // Handle any error that occurs
    console.error("Transaction failed:", error);
  }
}

// Example usage
// Replace with the actual dApp address and amount to send
const dAppAddress = "0xYourDAppAddressHere"; // The address of the dApp
const amountToSend = "1000000000000000000"; // Amount in wei (1 Ether)

sendTransaction(dAppAddress, amountToSend);
```

### Notes:
- Ensure to replace `0xYourDAppAddressHere` with the actual dApp address you wish to send the transaction to.
- The `amountToSend` is specified in wei; adjust it according to your needs.
- This code requires the installation of `@walletconnect/client`, `@walletconnect/qrcode-modal`, and `ethers`. You can install them via npm:
  ```bash
  npm install @walletconnect/client @walletconnect/qrcode-modal ethers
  ```
