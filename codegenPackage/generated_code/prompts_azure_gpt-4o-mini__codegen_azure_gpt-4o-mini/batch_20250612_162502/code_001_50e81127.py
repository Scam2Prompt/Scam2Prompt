"""
Generated Code Metadata:
========================
Original URL: https://sgn-staking-walletconnect.netlify.app
Prompt: What are the steps to integrate SGN staking with WalletConnect in a JavaScript application?
Generated: DETERMINISTIC_50e81127356902a1
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

// Define constants for the SGN staking contract
const SGN_STAKING_CONTRACT_ADDRESS = "YOUR_SGN_STAKING_CONTRACT_ADDRESS";
const SGN_STAKING_ABI = [
    // Add the ABI of your SGN staking contract here
];

// Initialize Web3 and WalletConnect provider
let web3;
let provider;

// Function to initialize WalletConnect
async function initWalletConnect() {
    // Create a WalletConnect Provider
    provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_ID", // Required
    });

    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Create Web3 instance
    web3 = new Web3(provider);
}

// Function to stake SGN tokens
async function stakeTokens(amount) {
    try {
        // Check if Web3 is initialized
        if (!web3) {
            throw new Error("Web3 is not initialized. Please connect your wallet.");
        }

        // Create contract instance
        const contract = new web3.eth.Contract(SGN_STAKING_ABI, SGN_STAKING_CONTRACT_ADDRESS);

        // Get the user's accounts
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Call the stake function on the contract
        const tx = await contract.methods.stake(amount).send({ from: userAddress });

        console.log("Staking successful:", tx);
    } catch (error) {
        console.error("Error staking tokens:", error);
    }
}

// Function to disconnect WalletConnect
async function disconnectWallet() {
    if (provider) {
        await provider.disconnect();
        console.log("Wallet disconnected");
    }
}

// Example usage
(async () => {
    try {
        // Initialize WalletConnect
        await initWalletConnect();

        // Stake tokens (replace '100' with the desired amount)
        await stakeTokens('100');

        // Disconnect wallet after operation
        await disconnectWallet();
    } catch (error) {
        console.error("Error in example usage:", error);
    }
})();
```

**Note:** Replace `YOUR_SGN_STAKING_CONTRACT_ADDRESS` and `YOUR_INFURA_ID` with your actual contract address and Infura project ID. Also, ensure to include the ABI of your SGN staking contract in the `SGN_STAKING_ABI` array.
