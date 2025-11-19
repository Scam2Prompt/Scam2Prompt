"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-hq126qa8s-offchain-labs.vercel.app
Prompt: Provide code examples for integrating WalletConnect with the Arbitrum Token Bridge, ensuring compatibility with the latest WalletConnect upgrade.
Generated: DETERMINISTIC_ea79e0f71f74e4e7
Batch ID: 20250612_150440
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://rinkeby.arbitrum.io/rpc": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://arb1.arbitrum.io/rpc": {
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
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";
import { Bridge } from "arb-ts";

// Initialize WalletConnect provider
const provider = new WalletConnectProvider({
  rpc: {
    42161: "https://arb1.arbitrum.io/rpc", // Arbitrum mainnet RPC
    421611: "https://rinkeby.arbitrum.io/rpc", // Arbitrum testnet RPC
  },
  chainId: 42161, // Default to Arbitrum mainnet
});

// Connect to WalletConnect
async function connectWallet() {
  try {
    // Enable session (triggers QR code modal)
    await provider.enable();

    // Create Web3 instance
    const web3 = new Web3(provider);

    // Get accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Connected accounts:", accounts);

    return { web3, accounts };
  } catch (error) {
    console.error("WalletConnect connection error:", error);
    throw error;
  }
}

// Initialize Arbitrum Bridge
async function initArbitrumBridge(web3, account) {
  try {
    const bridge = await Bridge.init(web3.currentProvider, account);
    console.log("Arbitrum Bridge initialized");
    return bridge;
  } catch (error) {
    console.error("Bridge initialization error:", error);
    throw error;
  }
}

// Token deposit to Arbitrum
async function depositToken(bridge, tokenAddress, amount, recipient) {
  try {
    const tx = await bridge.deposit({
      erc20L1Address: tokenAddress,
      amount: amount.toString(),
      l2Recipient: recipient,
    });

    console.log("Deposit transaction hash:", tx.hash);
    return tx;
  } catch (error) {
    console.error("Deposit error:", error);
    throw error;
  }
}

// Token withdrawal from Arbitrum
async function withdrawToken(bridge, tokenAddress, amount, recipient) {
  try {
    const tx = await bridge.withdraw({
      erc20L2Address: tokenAddress,
      amount: amount.toString(),
      l1Recipient: recipient,
    });

    console.log("Withdrawal transaction hash:", tx.hash);
    return tx;
  } catch (error) {
    console.error("Withdrawal error:", error);
    throw error;
  }
}

// Disconnect WalletConnect session
async function disconnectWallet() {
  try {
    await provider.disconnect();
    console.log("WalletConnect session disconnected");
  } catch (error) {
    console.error("Disconnection error:", error);
    throw error;
  }
}

// Event listeners for WalletConnect
provider.on("connect", (error, payload) => {
  if (error) {
    console.error("WalletConnect connection error:", error);
    return;
  }
  console.log("WalletConnect connected:", payload);
});

provider.on("disconnect", (error, payload) => {
  if (error) {
    console.error("WalletConnect disconnection error:", error);
    return;
  }
  console.log("WalletConnect disconnected:", payload);
});

// Example usage
async function exampleUsage() {
  try {
    // Connect wallet
    const { web3, accounts } = await connectWallet();
    const [account] = accounts;

    // Initialize bridge
    const bridge = await initArbitrumBridge(web3, account);

    // Example token deposit
    const tokenAddress = "0xYourTokenAddress";
    const amount = web3.utils.toWei("1", "ether");
    const recipient = account; // or any other address

    await depositToken(bridge, tokenAddress, amount, recipient);

    // Example token withdrawal
    await withdrawToken(bridge, tokenAddress, amount, recipient);

    // Disconnect when done
    await disconnectWallet();
  } catch (error) {
    console.error("Example usage error:", error);
  }
}

// Export functions for module usage
export {
  connectWallet,
  initArbitrumBridge,
  depositToken,
  withdrawToken,
  disconnectWallet,
};
```
