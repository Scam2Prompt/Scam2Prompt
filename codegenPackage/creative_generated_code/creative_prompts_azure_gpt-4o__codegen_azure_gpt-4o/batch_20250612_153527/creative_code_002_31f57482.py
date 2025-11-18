"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinnice.xyz
Prompt: Generate code to enable JavaScript-based interaction with Ethereum wallets for DeFi transactions.
Generated: DETERMINISTIC_31f574828828a5a4
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries. Ensure these are installed via npm (`npm install ethers`).
const { ethers } = require("ethers");

// Define a function to connect to an Ethereum wallet using MetaMask.
async function connectWallet() {
    try {
        // Check if the browser has MetaMask installed
        if (!window.ethereum) {
            throw new Error("MetaMask is not installed in your browser.");
        }

        // Request wallet connection
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

        // Return the connected wallet address
        return accounts[0];
    } catch (error) {
        console.error("Error connecting wallet:", error.message);
        throw error;
    }
}

// Define a function to initialize a provider and signer for interacting with Ethereum
function initializeProvider() {
    try {
        // Create an ethers.js provider using MetaMask
        const provider = new ethers.providers.Web3Provider(window.ethereum);

        // Get the signer (used for signing transactions)
        const signer = provider.getSigner();

        return { provider, signer };
    } catch (error) {
        console.error("Error initializing provider:", error.message);
        throw error;
    }
}

// Define a function to send a transaction to a DeFi smart contract
async function sendTransaction(contractAddress, abi, functionName, params, value = "0") {
    try {
        const { signer } = initializeProvider();

        // Create a contract instance
        const contract = new ethers.Contract(contractAddress, abi, signer);

        // Send the transaction (value is optional, default is 0 ETH)
        const tx = await contract[functionName](...params, { value: ethers.utils.parseEther(value) });

        console.log(`Transaction sent: ${tx.hash}`);

        // Wait for the transaction to be mined
        const receipt = await tx.wait();

        console.log(`Transaction mined in block ${receipt.blockNumber}`);
        return receipt;
    } catch (error) {
        console.error("Error sending transaction:", error.message);
        throw error;
    }
}

// Define a function to monitor wallet changes
function monitorWalletChanges(onWalletChange, onNetworkChange) {
    // Listen for account changes
    window.ethereum.on("accountsChanged", (accounts) => {
        console.log("Wallet changed:", accounts);
        if (onWalletChange) {
            onWalletChange(accounts);
        }
    });

    // Listen for network changes
    window.ethereum.on("chainChanged", (chainId) => {
        console.log("Network changed:", chainId);
        if (onNetworkChange) {
            onNetworkChange(chainId);
        }
    });
}

// Sample usage:
// Ensure your app wraps these calls in appropriate UI flow (button clicks, etc.)

(async () => {
    try {
        // Connect wallet
        const walletAddress = await connectWallet();
        console.log(`Connected wallet: ${walletAddress}`);

        // Monitor changes
        monitorWalletChanges(
            (accounts) => console.log("Accounts changed:", accounts),
            (chainId) => console.log("Chain ID changed:", chainId)
        );

        // Example interaction with a DeFi contract
        const contractAddress = "<YOUR_CONTRACT_ADDRESS>";
        const abi = []; // Replace with your contract's ABI
        const functionName = "yourFunctionName"; // Replace with your function name
        const params = []; // Replace with your function's parameters
        const value = "0"; // Replace with the ETH value to send (if needed)

        const receipt = await sendTransaction(contractAddress, abi, functionName, params, value);
        console.log("Transaction receipt:", receipt);
    } catch (error) {
        console.error("Error in application:", error.message);
    }
})();
```
