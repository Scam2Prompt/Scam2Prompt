"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alik1pepe.pages.dev
Prompt: Generate a step-by-step guide in code for creating a wallet using Metamask, funding it with ETH, and connecting it to Uniswap to purchase $PEPE tokens.
Generated: DETERMINISTIC_eebfe23158d2e4ee
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import { Contract } from 'ethers';
import { ERC20_ABI } from './abis/ERC20.json'; // ABI for ERC20 tokens
import { UNISWAP_ROUTER_ABI } from './abis/UniswapRouter.json'; // ABI for Uniswap Router

// Constants
const UNISWAP_ROUTER_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Uniswap Router address
const PEPE_TOKEN_ADDRESS = '0xYourPepeTokenAddress'; // Replace with actual $PEPE token address

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Function to connect MetaMask wallet
async function connectWallet() {
    try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected to wallet:', accounts[0]);
        return accounts[0];
    } catch (error) {
        console.error('Failed to connect to wallet:', error);
        throw new Error('Wallet connection failed');
    }
}

// Function to fund the wallet with ETH (manual step)
// User must manually fund their wallet with ETH using MetaMask before proceeding.

// Function to purchase $PEPE tokens via Uniswap
async function purchasePEPETokens(amountInETH, userAddress) {
    try {
        // Set up provider and signer
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Create instances of Uniswap Router and $PEPE token contract
        const uniswapRouter = new Contract(UNISWAP_ROUTER_ADDRESS, UNISWAP_ROUTER_ABI, signer);
        const pepeToken = new Contract(PEPE_TOKEN_ADDRESS, ERC20_ABI, signer);

        // Get the amount of $PEPE tokens to purchase
        const amountOutMin = 0; // Minimum amount of tokens to receive (set to 0 for simplicity, better to calculate based on slippage)
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Transaction deadline (20 minutes)

        // Perform the swap
        const transaction = await uniswapRouter.swapExactETHForTokens(
            amountOutMin,
            [ethers.constants.AddressZero, PEPE_TOKEN_ADDRESS], // Route: ETH -> $PEPE
            userAddress,
            deadline,
            { value: ethers.utils.parseEther(amountInETH.toString()) } // Amount of ETH to swap
        );

        // Wait for transaction confirmation
        await transaction.wait();
        console.log(`Successfully purchased $PEPE tokens. Transaction Hash: ${transaction.hash}`);
        
    } catch (error) {
        console.error('Error during token purchase:', error);
        throw new Error('Token purchase failed');
    }
}

// Main function to execute the steps
async function main() {
    try {
        const userAddress = await connectWallet();
        const amountInETH = 0.1; // Amount of ETH to spend on $PEPE tokens
        
        // Call the function to purchase $PEPE tokens
        await purchasePEPETokens(amountInETH, userAddress);
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

// Execute the main function
main();
```

**Note**: Ensure that you have the correct ABI files and the actual address of the $PEPE token. This code assumes you have the necessary dependencies installed (`web3`, `ethers`, etc.) and that the user has funded their MetaMask wallet with ETH prior to running the code.
