"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://add-truthgpt.pages.dev
Prompt: Write a script to interact with the TruthGPT Bridge dApp API for approving $TRUTH tokens and setting a bridging amount using a connected MetaMask wallet.
Generated: DETERMINISTIC_293896cfcdbd4765
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const Web3 = require('web3');
const abiDecoder = require('abi-decoder'); // Library for decoding ABI
const prompt = require('prompt-sync')(); // Library for console input

// Configuration constants
const TRUTH_TOKEN_ADDRESS = "0xYourTruthTokenAddress"; // Replace with actual $TRUTH token contract address
const BRIDGE_DAPP_ADDRESS = "0xYourBridgeDAppAddress"; // Replace with actual TruthGPT Bridge dApp contract address
const TOKEN_ABI = [ /* Replace with the actual $TRUTH token contract ABI */ ];
const DAPP_ABI = [ /* Replace with the actual TruthGPT Bridge dApp ABI */ ];

// Initialize Web3 instance
let web3;

// Function to initialize Web3 and connect to MetaMask
async function initializeWeb3() {
    if (window.ethereum) {
        web3 = new Web3(window.ethereum);
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' }); // Request MetaMask connection
        } catch (error) {
            console.error("User denied MetaMask connection", error);
            return null;
        }
    } else {
        console.error("MetaMask is not installed. Please install MetaMask to continue.");
        return null;
    }

    return web3;
}

// Function to approve $TRUTH tokens
async function approveTokens(amount) {
    try {
        const accounts = await web3.eth.getAccounts(); // Fetch connected accounts
        const senderAddress = accounts[0]; // Use the first connected account

        const tokenContract = new web3.eth.Contract(TOKEN_ABI, TRUTH_TOKEN_ADDRESS);

        // Interact with the approve function of the $TRUTH token contract
        const tx = await tokenContract.methods.approve(BRIDGE_DAPP_ADDRESS, web3.utils.toWei(amount.toString(), 'ether'))
            .send({ from: senderAddress });

        console.log(`Approval transaction successful. Hash: ${tx.transactionHash}`);
    } catch (error) {
        console.error("Error approving tokens:", error);
    }
}

// Function to set bridging amount
async function setBridgeAmount(amount) {
    try {
        const accounts = await web3.eth.getAccounts(); // Fetch connected accounts
        const senderAddress = accounts[0]; // Use the first connected account

        const bridgeContract = new web3.eth.Contract(DAPP_ABI, BRIDGE_DAPP_ADDRESS);

        // Interact with the setBridgeAmount function of the dApp contract
        const tx = await bridgeContract.methods.setBridgeAmount(web3.utils.toWei(amount.toString(), 'ether'))
            .send({ from: senderAddress });

        console.log(`Bridge amount set successfully. Transaction hash: ${tx.transactionHash}`);
    } catch (error) {
        console.error("Error setting bridge amount:", error);
    }
}

// Main function to execute the script
async function main() {
    const web3Instance = await initializeWeb3();
    if (!web3Instance) return;

    // Prompt user for input
    const amount = parseFloat(prompt("Enter the amount of $TRUTH tokens to approve and bridge: "));
    if (isNaN(amount) || amount <= 0) {
        console.error("Invalid amount entered.");
        return;
    }

    console.log("Approving $TRUTH tokens...");
    await approveTokens(amount);

    console.log("Setting bridging amount...");
    await setBridgeAmount(amount);

    console.log("Process completed successfully.");
}

// Execute the script
main();
```

### Notes:
1. Replace `0xYourTruthTokenAddress` and `0xYourBridgeDAppAddress` with actual contract addresses.
2. Replace `TOKEN_ABI` and `DAPP_ABI` with the actual ABI definitions for the $TRUTH token and TruthGPT Bridge dApp contracts.
3. Ensure that the user has MetaMask installed and the correct network selected.
