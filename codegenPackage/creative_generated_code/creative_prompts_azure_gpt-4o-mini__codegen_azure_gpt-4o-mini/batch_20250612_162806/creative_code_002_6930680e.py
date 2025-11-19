"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support-metamask-com-cdn.bravesites.com
Prompt: What are the steps to perform a token swap using the MetaMask interface, and how can I customize transaction settings for better control?
Generated: DETERMINISTIC_6930680e36e2e69f
Batch ID: 20250612_162806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define the token swap function
async function swapTokens(tokenIn, tokenOut, amountIn, slippage, recipient) {
    // Initialize web3 and provider
    const web3 = new Web3(window.ethereum);
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    
    // Request account access if needed
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();
    
    // Define the router contract address and ABI (this is an example for Uniswap)
    const routerAddress = '0xYourRouterContractAddress';
    const routerABI = [
        // ABI for the swapExactTokensForTokens function (simplified)
        "function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts)",
    ];
    
    const routerContract = new ethers.Contract(routerAddress, routerABI, signer);
    
    // Prepare token swap parameters
    const amountOutMin = amountIn * (1 - slippage / 100); // Calculate minimum output based on slippage
    const path = [tokenIn, tokenOut]; // Path of the swap
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Transaction deadline (20 minutes from now)
    
    try {
        // Approve the router to spend the input tokens
        const tokenContract = new ethers.Contract(tokenIn, ['function approve(address spender, uint256 value)'], signer);
        const approvalTx = await tokenContract.approve(routerAddress, amountIn);
        await approvalTx.wait(); // Wait for the transaction to be mined
        
        // Perform the token swap
        const swapTx = await routerContract.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            recipient,
            deadline
        );
        
        const receipt = await swapTx.wait(); // Wait for the swap transaction to be confirmed
        console.log('Swap successful:', receipt);
    } catch (error) {
        console.error('Error performing token swap:', error);
    }
}

// Example usage
// Replace with appropriate token addresses and values
const tokenInAddress = '0xYourTokenInAddress';
const tokenOutAddress = '0xYourTokenOutAddress';
const amountToSwap = ethers.utils.parseUnits('1.0', 18); // Amount of tokens to swap (adjust decimals as necessary)
const slippagePercentage = 1; // Slippage percentage (1% in this example)
const recipientAddress = '0xYourRecipientAddress'; // Recipient address

// Call the swap function
swapTokens(tokenInAddress, tokenOutAddress, amountToSwap, slippagePercentage, recipientAddress);
```
