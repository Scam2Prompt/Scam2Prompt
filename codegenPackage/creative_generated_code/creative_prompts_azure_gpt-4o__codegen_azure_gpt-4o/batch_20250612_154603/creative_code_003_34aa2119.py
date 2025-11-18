"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accessnodeapp.com
Prompt: Provide a step-by-step guide to building a decentralized application (DApp) with multichain functionality and self-custodial wallet integration, referencing features described on AccessNodeApp.com.
Generated: DETERMINISTIC_34aa2119e3d58939
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a production-ready implementation of a decentralized application (DApp) with multichain functionality and self-custodial wallet integration. The code is written in JavaScript and leverages commonly used libraries such as `ethers.js` for Ethereum blockchain interaction and `@walletconnect/web3-provider` for multichain wallet integration.

---

### `package.json`
First, ensure the necessary dependencies are installed:
```json
{
  "name": "multichain-dapp",
  "version": "1.0.0",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "ethers": "^5.8.0",
    "@walletconnect/web3-provider": "^1.9.0",
    "dotenv": "^16.0.3"
  }
}
```

---

### `.env`
Store sensitive credentials securely:
```plaintext
INFURA_PROJECT_ID=your-infura-project-id
ALCHEMY_API_KEY=your-alchemy-api-key
```

---

### `index.js`
Main DApp implementation:
```javascript
// Import required modules and libraries
const { ethers } = require("ethers");
const WalletConnectProvider = require("@walletconnect/web3-provider");
require("dotenv").config(); // Load environment variables from .env file

// Initialize multichain support
const supportedChains = {
  1: "Ethereum Mainnet",    // Chain ID: 1
  137: "Polygon Mainnet",   // Chain ID: 137
};

// Initialize provider options for WalletConnect
const walletConnectProviderOptions = {
  infuraId: process.env.INFURA_PROJECT_ID, // Required for Ethereum Mainnet
  alchemy: process.env.ALCHEMY_API_KEY,   // Required for Polygon Mainnet
};

// Initialize WalletConnect provider
async function initializeWalletConnectProvider() {
  try {
    const provider = new WalletConnectProvider(walletConnectProviderOptions);

    // Enable the provider (connect to wallet)
    await provider.enable();

    // Create an ethers.js instance using WalletConnect provider
    const web3Provider = new ethers.providers.Web3Provider(provider);

    console.log("Wallet connected!");

    // Detect active chain
    const network = await web3Provider.getNetwork();
    console.log(`Connected to chain: ${supportedChains[network.chainId] || "Unknown chain"}`);

    return web3Provider;
  } catch (error) {
    console.error("Failed to initialize WalletConnect provider:", error.message);
    throw error;
  }
}

// Function to fetch the user's wallet address
async function getWalletAddress(provider) {
  try {
    const signer = provider.getSigner();
    const address = await signer.getAddress();
    console.log("Wallet address:", address);
    return address;
  } catch (error) {
    console.error("Failed to fetch wallet address:", error.message);
    throw error;
  }
}

// Function to send a transaction
async function sendTransaction(provider, recipient, value) {
  try {
    const signer = provider.getSigner();

    // Build the transaction
    const tx = {
      to: recipient,
      value: ethers.utils.parseEther(value), // Convert ETH to wei
    };

    console.log("Sending transaction:", tx);
    const txResponse = await signer.sendTransaction(tx);
    console.log("Transaction sent! Transaction hash:", txResponse.hash);

    // Wait for the transaction to be mined
    const txReceipt = await txResponse.wait();
    console.log("Transaction mined! Receipt:", txReceipt);

    return txReceipt;
  } catch (error) {
    console.error("Failed to send transaction:", error.message);
    throw error;
  }
}

// Main function to run the DApp
async function main() {
  try {
    console.log("Initializing WalletConnect provider...");
    const provider = await initializeWalletConnectProvider();

    console.log("Fetching wallet address...");
    const walletAddress = await getWalletAddress(provider);

    console.log("Sending a test transaction...");
    const recipient = "0x0000000000000000000000000000000000000000"; // Replace with a valid address
    const value = "0.01"; // ETH to send
    const receipt = await sendTransaction(provider, recipient, value);

    console.log("Transaction completed successfully:", receipt);
  } catch (error) {
    console.error("An error occurred in the DApp:", error.message);
  }
}

// Run the main function
main();
```

---

### Notes
1. Replace `INFURA_PROJECT_ID` and `ALCHEMY_API_KEY` in the `.env` file with your actual API keys.
2. Supported chains can be extended in the `supportedChains` object.
3. The recipient address in `sendTransaction` is a placeholder; replace it with a valid address.

---

### Run Instructions
1. Install dependencies:
   ```bash
   npm install
   ```
2. Run the application:
   ```bash
   npm start
   ```

Make sure you have WalletConnect-compatible wallets, such as MetaMask or Trust Wallet, for testing.
