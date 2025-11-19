"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibtcfgrhknlfhnz2c5cddfnsoje4dumrc3wsyoikx2pwuf6fbcsr4.ipfs.dweb.link
Prompt: What are the key features of MetaMask that support token swaps, and how can I implement a swap function in my dApp?
Generated: DETERMINISTIC_c0f16690a9b7216a
Batch ID: 20250612_164158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: swapTokens.js
// Description: Implements a token swap function in a dApp using MetaMask APIs and best practices.
// Prerequisites: The user must have MetaMask installed and connected to their dApp.

import Web3 from 'web3';

// Ensure Web3 is initialized and connected to MetaMask
const web3 = new Web3(window.ethereum);

// Swap function to exchange one token for another using MetaMask
export async function swapTokens({
    tokenInAddress,     // Address of the token to be swapped (input)
    tokenOutAddress,    // Address of the token to receive (output)
    amountIn,           // Amount of input tokens to swap
    recipientAddress,   // Address to receive the swapped tokens
    slippage = 0.5,     // Slippage tolerance (default: 0.5%)
    dexRouterAddress    // Decentralized Exchange (DEX) router address
}) {
    try {
        // Validate input parameters
        if (!web3.utils.isAddress(tokenInAddress) || !web3.utils.isAddress(tokenOutAddress)) {
            throw new Error('Invalid token addresses provided.');
        }
        if (!web3.utils.isAddress(recipientAddress)) {
            throw new Error('Invalid recipient address provided.');
        }
        if (!web3.utils.isAddress(dexRouterAddress)) {
            throw new Error('Invalid DEX router address provided.');
        }
        if (amountIn <= 0) {
            throw new Error('Amount to swap must be greater than zero.');
        }

        // Request wallet connection if not already connected
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the connected wallet address
        const accounts = await web3.eth.getAccounts();
        const senderAddress = accounts[0];

        // ABI for the DEX router (Example: Uniswap Router)
        const dexRouterABI = [
            // Add only the relevant function signatures (e.g., `swapExactTokensForTokens`)
            {
                "inputs": [
                    { "internalType": "uint256", "name": "amountIn", "type": "uint256" },
                    { "internalType": "uint256", "name": "amountOutMin", "type": "uint256" },
                    { "internalType": "address[]", "name": "path", "type": "address[]" },
                    { "internalType": "address", "name": "to", "type": "address" },
                    { "internalType": "uint256", "name": "deadline", "type": "uint256" }
                ],
                "name": "swapExactTokensForTokens",
                "outputs": [{ "internalType": "uint256[]", "name": "amounts", "type": "uint256[]" }],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ];

        // Initialize DEX Router contract
        const dexRouter = new web3.eth.Contract(dexRouterABI, dexRouterAddress);

        // Approve the token transfer (if not already approved)
        const tokenInContractABI = [
            {
                "constant": false,
                "inputs": [
                    { "name": "_spender", "type": "address" },
                    { "name": "_value", "type": "uint256" }
                ],
                "name": "approve",
                "outputs": [{ "name": "", "type": "bool" }],
                "type": "function"
            }
        ];
        const tokenInContract = new web3.eth.Contract(tokenInContractABI, tokenInAddress);

        const allowance = await tokenInContract.methods.allowance(senderAddress, dexRouterAddress).call();
        if (parseInt(allowance) < amountIn) {
            const approveTx = await tokenInContract.methods.approve(dexRouterAddress, amountIn).send({ from: senderAddress });
            console.log('Approval transaction:', approveTx);
        }

        // Set up the swap parameters
        const path = [tokenInAddress, tokenOutAddress]; // Token swap path
        const deadline = Math.floor(Date.now() / 1000) + 60 * 10; // Transaction deadline: 10 minutes from now
        const amountsOut = await dexRouter.methods.getAmountsOut(amountIn, path).call();
        const amountOutMin = amountsOut[1] * (1 - slippage / 100); // Minimum output amount (adjusted for slippage)

        // Execute the swap transaction
        const swapTx = await dexRouter.methods.swapExactTokensForTokens(
            amountIn,
            web3.utils.toWei(amountOutMin.toString(), 'ether'), // Convert to Wei
            path,
            recipientAddress,
            deadline
        ).send({ from: senderAddress });

        console.log('Swap transaction:', swapTx);
        return swapTx;

    } catch (error) {
        console.error('Error during token swap:', error.message || error);
        throw error; // Re-throw error for further handling
    }
}
```
