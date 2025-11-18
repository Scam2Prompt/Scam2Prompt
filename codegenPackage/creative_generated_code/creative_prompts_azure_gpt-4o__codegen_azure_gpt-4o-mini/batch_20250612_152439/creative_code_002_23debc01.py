"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-signetfaucet.pages.dev
Prompt: Generate a code snippet to integrate the Signet Faucet functionality into a dApp, allowing users to claim tokens directly through their Coinbase Wallet app.
Generated: DETERMINISTIC_23debc013c63e69b
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ethers } from "ethers";
// Replace with the actual ABI of the Signet Faucet contract
import FaucetABI from './FaucetABI.json';

// Define constants
const FAUCET_ADDRESS = "0xYourFaucetAddress"; // Replace with the actual faucet contract address

// Initialize the provider and wallet
async function initProvider() {
    // Check if Coinbase Wallet is installed
    if (typeof window.ethereum !== 'undefined') {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []); // Request account access
        return provider;
    } else {
        throw new Error("Please install Coinbase Wallet to use this dApp.");
    }
}

// Claim tokens from the Signet Faucet
async function claimTokens() {
    try {
        const provider = await initProvider();
        const signer = provider.getSigner();
        
        // Create a contract instance
        const faucetContract = new ethers.Contract(FAUCET_ADDRESS, FaucetABI, signer);
        
        // Call the claim function on the faucet contract
        const tx = await faucetContract.claimTokens();
        await tx.wait(); // Wait for transaction to be confirmed

        console.log("Tokens claimed successfully:", tx);
    } catch (error) {
        console.error("Error claiming tokens:", error);
        alert("An error occurred while claiming tokens. Please try again later.");
    }
}

// Event listener for the Claim Tokens button
document.getElementById("claim-button").addEventListener("click", claimTokens);
```

Make sure to replace `FAUCET_ADDRESS` and import the correct ABI for the faucet contract. The button with the ID `claim-button` should exist in your HTML for the event listener to work.
