"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqwu.com
Prompt: Create a code snippet using ethers.js to enable wallet connection and interact with DeFi protocols on Ethereum.
Generated: DETERMINISTIC_d2adcb0743dee29d
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js library
import { ethers } from "ethers";

// Define a function to connect to the user's Ethereum wallet
async function connectWallet() {
    if (typeof window.ethereum === 'undefined') {
        console.error("MetaMask is not installed. Please install it to use this app.");
        return;
    }

    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        console.log("Connected account:", accounts[0]);
        return { provider, signer };
    } catch (error) {
        console.error("Error connecting to wallet:", error);
    }
}

// Define a function to interact with a DeFi protocol (example: Uniswap)
async function swapTokens(signer, tokenIn, tokenOut, amount) {
    try {
        // Replace with actual contract address and ABI
        const contractAddress = "0xUniswapContractAddress";
        const contractABI = [/* Uniswap contract ABI */];

        // Create contract instance
        const contract = new ethers.Contract(contractAddress, contractABI, signer);

        // Execute swap function (example function for Uniswap)
        const tx = await contract.swapExactTokensForTokens(
            ethers.utils.parseUnits(amount.toString(), 18), // Amount to swap
            0, // Minimum amount to receive (slippage not handled here)
            [tokenIn, tokenOut], // Path of tokens
            await signer.getAddress(), // Recipient
            Math.floor(Date.now() / 1000) + 60 * 20 // Deadline: 20 mins from now
        );

        console.log("Transaction sent:", tx.hash);
        await tx.wait(); // Wait for transaction to be mined
        console.log("Transaction confirmed:", tx.hash);
    } catch (error) {
        console.error("Error swapping tokens:", error);
    }
}

// Usage example
(async () => {
    const { provider, signer } = await connectWallet();
    const tokenIn = "0xTokenInAddress"; // Address of the token to swap from
    const tokenOut = "0xTokenOutAddress"; // Address of the token to swap to
    const amount = 1; // Amount of tokenIn to swap
    if (signer) {
        await swapTokens(signer, tokenIn, tokenOut, amount);
    }
})();
```
