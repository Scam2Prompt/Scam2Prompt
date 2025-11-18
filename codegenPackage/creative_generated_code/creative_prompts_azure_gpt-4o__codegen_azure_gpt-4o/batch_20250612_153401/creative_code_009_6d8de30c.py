"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://main-b47.pages.dev
Prompt: Provide an example of integrating MultiChainsFI into a dApp to support decentralized wallet connections across Ethereum and Avalanche.
Generated: DETERMINISTIC_6d8de30c942196d7
Batch ID: 20250612_153401
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.avax.network/ext/bc/C/rpc": {
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
// Import required libraries and dependencies
import Web3 from "web3";
import { MultiChainsFI } from "multichainsfi-sdk"; // Hypothetical SDK for MultiChainsFI

// Configuration for Ethereum and Avalanche networks
const networkConfig = {
  ethereum: {
    chainId: "0x1", // Mainnet chain ID
    rpcUrl: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Replace with your Infura endpoint
  },
  avalanche: {
    chainId: "0xa86a", // Avalanche C-Chain ID
    rpcUrl: "https://api.avax.network/ext/bc/C/rpc", // Avalanche RPC endpoint
  },
};

// Initialize MultiChainsFI SDK
const multiChainsFI = new MultiChainsFI({
  supportedChains: [networkConfig.ethereum, networkConfig.avalanche],
});

// Function to connect to wallet
async function connectWallet(chainName) {
  try {
    // Ensure the requested chain exists in the configuration
    const chainConfig = networkConfig[chainName.toLowerCase()];
    if (!chainConfig) throw new Error("Unsupported chain selected.");

    // Initialize Web3 for the selected chain
    const web3 = new Web3(chainConfig.rpcUrl);

    // Connect and request wallet access
    const accounts = await multiChainsFI.connect(chainConfig.chainId);

    if (accounts && accounts.length > 0) {
      console.log(`Connected wallet address: ${accounts[0]}`);
      return { web3, accounts };
    } else {
      throw new Error("No wallet connected or user rejected the connection.");
    }
  } catch (error) {
    console.error(`Failed to connect wallet: ${error.message}`);
    throw error;
  }
}

// Function to switch chains
async function switchChain(chainName) {
  try {
    const chainConfig = networkConfig[chainName.toLowerCase()];
    if (!chainConfig) throw new Error("Unsupported chain selected.");

    // Request chain switch using MultiChainsFI SDK
    const switched = await multiChainsFI.switchChain(chainConfig.chainId);

    if (switched) {
      console.log(`Successfully switched to chain: ${chainName}`);
    } else {
      throw new Error(`Failed to switch to ${chainName}.`);
    }
  } catch (error) {
    console.error(`Error switching chain: ${error.message}`);
    throw error;
  }
}

// Example usage
(async function initializeDApp() {
  try {
    // Connect to Ethereum wallet
    const { web3, accounts } = await connectWallet("ethereum");
    console.log("Ethereum wallet connected.");

    // Perform operations using Web3.js here...

    // Optionally, switch to Avalanche
    await switchChain("avalanche");
    console.log("Switched to Avalanche successfully.");
  } catch (error) {
    console.error("Error initializing dApp:", error.message);
  }
})();
```
