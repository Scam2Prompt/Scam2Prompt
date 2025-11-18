"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.network
Prompt: Provide an example of integrating WalletConnect Certified wallets into a dApp, adhering to the highest UX standards outlined in WalletGuide.
Generated: DETERMINISTIC_d628ee481a25fa62
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
// Import dependencies
import WalletConnect from "@walletconnect/client";
import QRCodeModal from "@walletconnect/qrcode-modal";

// Define constants for WalletConnect integration
const WALLETCONNECT_BRIDGE_URL = "https://bridge.walletconnect.org"; // WalletConnect bridge URL
const REQUIRED_CHAIN_ID = 1; // Example: Ethereum Mainnet Chain ID

// Initialize WalletConnect Connector
const connector = new WalletConnect({
  bridge: WALLETCONNECT_BRIDGE_URL,
  qrcodeModal: QRCodeModal
});

// Function to initiate connection to WalletConnect
async function connectWallet() {
  try {
    // Check if connection is already established
    if (!connector.connected) {
      // Create a new session
      await connector.createSession();
    }

    // Subscribe to connection events
    subscribeToEvents();
  } catch (error) {
    console.error("Error connecting to wallet:", error);
    alert("Unable to connect to wallet. Please try again.");
  }
}

// Function to subscribe to WalletConnect events
function subscribeToEvents() {
  // Session update event
  connector.on("session_update", (error, payload) => {
    if (error) {
      console.error("Session update error:", error);
      return;
    }

    // Extract updated accounts and chainId
    const { accounts, chainId } = payload.params[0];
    handleAccountAndChainIdUpdate(accounts, chainId);
  });

  // Disconnect event
  connector.on("disconnect", (error) => {
    if (error) {
      console.error("Disconnect error:", error);
      return;
    }

    // Handle wallet disconnection
    handleDisconnect();
  });

  // Connection established event
  connector.on("connect", (error, payload) => {
    if (error) {
      console.error("Connection error:", error);
      return;
    }

    // Extract accounts and chainId
    const { accounts, chainId } = payload.params[0];
    handleAccountAndChainIdUpdate(accounts, chainId);
  });
}

// Handle account and chainId updates
function handleAccountAndChainIdUpdate(accounts, chainId) {
  // Check if the connected chainId is supported
  if (chainId !== REQUIRED_CHAIN_ID) {
    console.warn("Unsupported chain ID:", chainId);
    alert("Please connect to the Ethereum Mainnet.");
    return;
  }

  // Persist accounts and chainId to the dApp state
  console.log("Connected accounts:", accounts);
  console.log("Current chainId:", chainId);
  alert(`Wallet connected with account: ${accounts[0]}`);
}

// Handle wallet disconnection
function handleDisconnect() {
  console.log("Wallet disconnected");
  alert("Wallet disconnected. Please reconnect.");
}

// Function to send a test transaction
async function sendTransaction() {
  if (!connector.connected) {
    alert("Please connect your wallet first.");
    return;
  }

  try {
    // Define a sample transaction object
    const tx = {
      from: connector.accounts[0], // Wallet address
      to: "0xRecipientAddressHere", // Replace with recipient address
      value: "0x1", // Amount in wei (example: 1 wei)
      gas: "0x5208", // 21000 gas limit
      gasPrice: "0x3B9ACA00", // 1 Gwei
      data: "0x" // Optional data field
    };

    // Send the transaction request
    const result = await connector.sendTransaction(tx);
    console.log("Transaction sent:", result);
    alert(`Transaction sent successfully. TX Hash: ${result}`);
  } catch (error) {
    console.error("Transaction error:", error);
    alert("Failed to send transaction. Please try again.");
  }
}

// Function to disconnect wallet
function disconnectWallet() {
  if (!connector.connected) {
    alert("No wallet connected.");
    return;
  }

  try {
    connector.killSession();
    console.log("Session terminated successfully");
    alert("Disconnected from wallet.");
  } catch (error) {
    console.error("Disconnection error:", error);
    alert("Failed to disconnect wallet. Please try again.");
  }
}

// Example UI bindings (for demonstration purposes)
document.getElementById("connect-btn").addEventListener("click", connectWallet);
document.getElementById("send-tx-btn").addEventListener("click", sendTransaction);
document.getElementById("disconnect-btn").addEventListener("click", disconnectWallet);

// Ensure the UI follows WalletGuide best practices
// Example: Provide clear feedback for connection states, use tooltips and modals for better UX
```
