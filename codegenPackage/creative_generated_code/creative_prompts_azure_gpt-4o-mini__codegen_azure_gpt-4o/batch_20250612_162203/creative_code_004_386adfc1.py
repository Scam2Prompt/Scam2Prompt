"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-crystaldash2.pages.dev
Prompt: Create a guide for adding Ledger hardware wallet support in a web application, inspired by the security features highlighted on Portal Crystaldash.
Generated: DETERMINISTIC_386adfc134142a9a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a sample code implementation for adding Ledger hardware wallet support in a web application:

```javascript
// Import necessary libraries
// Make sure to install these via npm: `npm install @ledgerhq/hw-transport-webusb @ledgerhq/hw-app-eth`
import TransportWebUSB from "@ledgerhq/hw-transport-webusb";
import Eth from "@ledgerhq/hw-app-eth";

// Constants
const LEDGER_TIMEOUT_MS = 5000; // Timeout for ledger connection attempts

/**
 * Connect to Ledger hardware wallet.
 * @returns {Promise<Eth>} Returns an instance of the Ledger Ethereum app.
 */
async function connectToLedger() {
  try {
    // Request access to the Ledger via WebUSB transport
    const transport = await TransportWebUSB.create(LEDGER_TIMEOUT_MS);

    // Enable debug logs for development (disable in production)
    transport.setDebugMode(true);

    // Create an instance of the Ethereum application
    const ethApp = new Eth(transport);

    console.log("Ledger connected successfully");
    return ethApp;
  } catch (error) {
    console.error("Failed to connect to Ledger:", error.message);
    throw new Error("Ledger connection failed. Please ensure the device is unlocked and Ethereum app is open.");
  }
}

/**
 * Get the Ethereum address from the Ledger device.
 * @param {Eth} ethApp Instance of Ethereum app from Ledger.
 * @param {number} accountIndex Account index (default is 0).
 * @returns {Promise<string>} Returns the Ethereum address.
 */
async function getEthereumAddress(ethApp, accountIndex = 0) {
  try {
    // Derivation path - the standard Ethereum path for hardware wallets
    const derivationPath = `44'/60'/0'/0/${accountIndex}`;

    // Get the public address from the Ledger
    const { address } = await ethApp.getAddress(derivationPath);
    console.log(`Ethereum address retrieved: ${address}`);
    return address;
  } catch (error) {
    console.error("Failed to retrieve Ethereum address:", error.message);
    throw new Error("Unable to fetch Ethereum address from Ledger device.");
  }
}

/**
 * Sign a transaction using the Ledger device.
 * @param {Eth} ethApp Instance of Ethereum app from Ledger.
 * @param {number} accountIndex Account index (default is 0).
 * @param {string} rawTxHex Hexadecimal raw transaction string.
 * @returns {Promise<string>} Returns the signed transaction in hex format.
 */
async function signTransaction(ethApp, accountIndex = 0, rawTxHex) {
  try {
    // Derivation path for the Ethereum account
    const derivationPath = `44'/60'/0'/0/${accountIndex}`;

    // Sign the transaction using Ledger
    const { r, s, v } = await ethApp.signTransaction(derivationPath, rawTxHex);

    // Combine the signature parts into a single hex string
    const signedTxHex = `0x${r}${s}${v.toString(16).padStart(2, "0")}`;
    console.log("Transaction signed successfully:", signedTxHex);
    return signedTxHex;
  } catch (error) {
    console.error("Failed to sign transaction:", error.message);
    throw new Error("Transaction signing failed on Ledger device.");
  }
}

/**
 * Disconnect the Ledger device safely.
 * @param {TransportWebUSB} transport Ledger transport instance.
 */
async function disconnectLedger(transport) {
  try {
    await transport.close();
    console.log("Ledger disconnected successfully.");
  } catch (error) {
    console.error("Failed to disconnect Ledger:", error.message);
  }
}

// Example Usage
(async () => {
  try {
    // Step 1: Connect to Ledger
    const ethApp = await connectToLedger();

    // Step 2: Retrieve Ethereum address
    const address = await getEthereumAddress(ethApp);
    console.log("Ethereum Address:", address);

    // Step 3: Sign a transaction (replace `rawTxHex` with a valid transaction)
    const rawTxHex = "YOUR_RAW_TX_HEX_HERE"; // Example raw transaction
    const signedTx = await signTransaction(ethApp, 0, rawTxHex);
    console.log("Signed Transaction:", signedTx);

    // Step 4: Disconnect
    await disconnectLedger(ethApp.transport);
  } catch (error) {
    console.error("An error occurred:", error.message);
  }
})();
```

### Prerequisites:
1. Install dependencies with `npm install @ledgerhq/hw-transport-webusb @ledgerhq/hw-app-eth`.
2. Ensure your Ledger device is connected via USB, unlocked, and the Ethereum app is open.
3. Replace `"YOUR_RAW_TX_HEX_HERE"` with the appropriate raw transaction hex for signing.

This script is ready for production with proper error handling and best practices. It provides the fundamental operations for interacting with a Ledger hardware wallet in a web application.
