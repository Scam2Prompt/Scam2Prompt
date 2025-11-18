"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetdappsite.firebaseapp.com
Prompt: Explain how to integrate StarkGate functionality into a dApp for bridging ETH between Ethereum and Starknet, with code examples for wallet connection and balance updates.
Generated: DETERMINISTIC_d7c558167804bbb8
Batch ID: 20250612_155015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required packages
import { ethers } from "ethers"; // For Ethereum interaction
import StarkGate from "starkgate-sdk"; // Hypothetical StarkGate SDK
import Web3Modal from "web3modal"; // For wallet connection

// Define constants
const STARK_GATE_CONTRACT_ADDRESS = "0xYourStarkGateContractAddress"; // Replace with actual contract address

// Initialize global variables
let provider; // For wallet provider
let signer; // For signer
let starkGate; // Instance of the StarkGate SDK

/**
 * Initialize the Web3Modal and StarkGate
 */
async function init() {
    // Create an instance of Web3Modal
    const web3Modal = new Web3Modal({
        cacheProvider: true,
        providerOptions: {} // Define provider options if needed
    });

    try {
        // Connect to the wallet
        provider = await web3Modal.connect();
        signer = new ethers.providers.Web3Provider(provider).getSigner();

        // Initialize StarkGate SDK with the required parameters
        starkGate = new StarkGate(STARK_GATE_CONTRACT_ADDRESS, signer);
        console.log("StarkGate initialized successfully.");
    } catch (error) {
        console.error("Failed to connect wallet:", error);
    }
}

/**
 * Fetch and update the user's ETH balance
 */
async function updateBalance() {
    try {
        // Get the current user's wallet address
        const address = await signer.getAddress();
        
        // Fetch the balance from the Ethereum network
        const balance = await signer.getBalance();
        
        // Convert balance from Wei to Ether
        const balanceInEther = ethers.utils.formatEther(balance);
        
        console.log(`ETH Balance for ${address}: ${balanceInEther} ETH`);
        
        // Update UI or state management framework with the new balance
        // Example: setState({ balance: balanceInEther });
    } catch (error) {
        console.error("Failed to fetch balance:", error);
    }
}

/**
 * Bridge ETH from Ethereum to Starknet
 * @param {string} amount - Amount of ETH to bridge
 */
async function bridgeETH(amount) {
    try {
        // Validate the amount
        if (parseFloat(amount) <= 0) {
            throw new Error("Amount must be greater than zero.");
        }

        // Convert the amount to Wei
        const amountInWei = ethers.utils.parseEther(amount);
        
        // Call the StarkGate contract to bridge ETH
        const tx = await starkGate.bridgeETH(amountInWei);
        
        console.log(`Transaction sent: ${tx.hash}`);
        
        // Wait for the transaction to be confirmed
        await tx.wait();
        console.log("Transaction confirmed:", tx.hash);
    } catch (error) {
        console.error("Failed to bridge ETH:", error);
    }
}

// Execute the initialization sequence
init().then(async () => {
    // Example usage: update balance and bridge ETH
    await updateBalance();
    // Uncomment the line below to bridge ETH (ensure amount is valid)
    // await bridgeETH("0.1"); // Example amount to bridge
});
```

**Note:** Ensure to replace `"0xYourStarkGateContractAddress"` with the actual StarkGate contract address and configure the `providerOptions` as needed. The StarkGate SDK is hypothetical; replace it with the actual implementation as per the SDK documentation.
