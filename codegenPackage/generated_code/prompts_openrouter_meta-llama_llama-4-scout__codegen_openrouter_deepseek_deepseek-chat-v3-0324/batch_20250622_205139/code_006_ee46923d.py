"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.foundation
Prompt: Create a code example demonstrating how to use WalletConnect for connecting a user's wallet to a web3 application, enabling seamless UX interactions.
Generated: DETERMINISTIC_ee46923df71455cd
Batch ID: 20250622_205139
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

# Generated Code:
# ===============

```javascript
// Import required libraries
import WalletConnect from "@walletconnect/client";
import QRCodeModal from "@walletconnect/qrcode-modal";
import Web3 from "web3";

// WalletConnect configuration
const walletConnectConfig = {
  bridge: "https://bridge.walletconnect.org", // WalletConnect bridge URL
  qrcodeModal: QRCodeModal,
};

// Initialize WalletConnect connector
let connector = null;

// Initialize Web3 provider
let web3 = null;

// Function to initialize WalletConnect connection
async function initWalletConnect() {
  try {
    // Create a new connector
    connector = new WalletConnect(walletConnectConfig);

    // Check if connection is already established
    if (!connector.connected) {
      // Create new session
      await connector.createSession();
      
      // Display QR Code modal
      QRCodeModal.open(connector.uri, () => {
        console.log("QR Code Modal closed");
      });
    }

    // Subscribe to connection events
    subscribeToEvents();

    return connector;
  } catch (error) {
    console.error("WalletConnect initialization failed:", error);
    throw error;
  }
}

// Function to subscribe to WalletConnect events
function subscribeToEvents() {
  if (!connector) return;

  // Subscribe to session connection
  connector.on("connect", (error, payload) => {
    if (error) {
      throw error;
    }

    // Get provided accounts and chainId
    const { accounts, chainId } = payload.params[0];
    onConnect(accounts, chainId);
  });

  // Subscribe to session disconnection
  connector.on("disconnect", (error) => {
    if (error) {
      throw error;
    }

    onDisconnect();
  });

  // Subscribe to session update
  connector.on("session_update", (error, payload) => {
    if (error) {
      throw error;
    }

    const { accounts, chainId } = payload.params[0];
    onSessionUpdate(accounts, chainId);
  });
}

// Function to handle successful connection
function onConnect(accounts, chainId) {
  console.log("Connected with accounts:", accounts);
  console.log("Connected to chainId:", chainId);

  // Create Web3 provider
  web3 = new Web3(connector);

  // Close QR Code Modal
  QRCodeModal.close();
}

// Function to handle disconnection
function onDisconnect() {
  console.log("Disconnected");
  
  // Reset connector and web3
  connector = null;
  web3 = null;
}

// Function to handle session updates
function onSessionUpdate(accounts, chainId) {
  console.log("Session updated with accounts:", accounts);
  console.log("Session updated to chainId:", chainId);
}

// Function to disconnect wallet
function disconnectWallet() {
  if (connector) {
    connector.killSession();
  }
}

// Function to send a transaction
async function sendTransaction(txParams) {
  if (!web3 || !connector.connected) {
    throw new Error("Wallet not connected");
  }

  try {
    const txHash = await web3.eth.sendTransaction(txParams);
    return txHash;
  } catch (error) {
    console.error("Transaction failed:", error);
    throw error;
  }
}

// Function to sign a message
async function signMessage(message, address) {
  if (!web3 || !connector.connected) {
    throw new Error("Wallet not connected");
  }

  try {
    const signature = await web3.eth.personal.sign(message, address);
    return signature;
  } catch (error) {
    console.error("Message signing failed:", error);
    throw error;
  }
}

// Example usage
async function exampleUsage() {
  try {
    // Initialize WalletConnect
    await initWalletConnect();

    // Example transaction
    const txParams = {
      from: connector.accounts[0], // Use connected account
      to: "0x...", // Recipient address
      value: web3.utils.toWei("0.01", "ether"), // 0.01 ETH
    };

    // Send transaction
    const txHash = await sendTransaction(txParams);
    console.log("Transaction hash:", txHash);

    // Sign message
    const message = "Hello WalletConnect!";
    const signature = await signMessage(message, connector.accounts[0]);
    console.log("Message signature:", signature);

  } catch (error) {
    console.error("Example usage failed:", error);
  } finally {
    // Disconnect when done
    disconnectWallet();
  }
}

// Export functions for use in application
export {
  initWalletConnect,
  disconnectWallet,
  sendTransaction,
  signMessage,
  exampleUsage,
};
```
