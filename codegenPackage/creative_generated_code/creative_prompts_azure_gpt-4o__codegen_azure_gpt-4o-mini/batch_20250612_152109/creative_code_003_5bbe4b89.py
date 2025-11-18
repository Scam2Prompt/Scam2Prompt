"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim--entangle.pages.dev
Prompt: Write a script using Web3.js or ethers.js to connect a wallet and claim $NGL tokens from the Entangle infrastructure, referencing the token address `0x12652C6d93FDB6F4f37d48A8687783C782BB0d10`.
Generated: DETERMINISTIC_5bbe4b89a0109d9d
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
const { ethers } = require("ethers");

// Define the required constants
const TOKEN_ADDRESS = "0x12652C6d93FDB6F4f37d48A8687783C782BB0d10";
const ENTANGLE_CONTRACT_ADDRESS = "YOUR_ENTANGLE_CONTRACT_ADDRESS"; // Replace with the actual Entangle contract address
const ABI = [
    // Replace with the actual ABI of the Entangle contract containing the claim function
    "function claim() external",
];

// Initialize the provider and wallet
let provider;
let wallet;

// Function to connect to a wallet
async function connectWallet() {
    // Check if the user has a Web3 provider
    if (typeof window.ethereum !== "undefined") {
        try {
            // Request account access
            await window.ethereum.request({ method: "eth_requestAccounts" });
            provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            wallet = signer;
            console.log("Wallet connected successfully.");
        } catch (error) {
            console.error("User denied account access:", error);
            throw new Error("Wallet connection failed.");
        }
    } else {
        console.error("No Ethereum provider detected. Please install MetaMask.");
        throw new Error("No Ethereum provider detected.");
    }
}

// Function to claim $NGL tokens
async function claimTokens() {
    if (!wallet) {
        console.error("Wallet is not connected. Please connect first.");
        return;
    }

    // Create an instance of the contract
    const contract = new ethers.Contract(ENTANGLE_CONTRACT_ADDRESS, ABI, wallet);

    try {
        // Call the claim function
        const tx = await contract.claim();
        console.log("Claim transaction sent:", tx.hash);
        
        // Wait for the transaction to be confirmed
        const receipt = await tx.wait();
        console.log("Transaction confirmed in block:", receipt.blockNumber);
    } catch (error) {
        console.error("Error while claiming tokens:", error);
        throw new Error("Token claim failed.");
    }
}

// Main function to execute the script
(async () => {
    try {
        await connectWallet();
        await claimTokens();
    } catch (error) {
        console.error("An error occurred:", error.message);
    }
})();
```

### Important Notes:
- Replace `YOUR_ENTANGLE_CONTRACT_ADDRESS` with the actual Entangle contract address.
- Populate the `ABI` array with the actual ABI of the Entangle contract that contains the claim function.
- Ensure that this script is executed in a browser environment with an Ethereum provider like MetaMask installed.
