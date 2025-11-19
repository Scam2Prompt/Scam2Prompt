"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapv2-ui.vercel.app
Prompt: What are the steps to integrate Uniswap V2's token swap functionality using JavaScript in a frontend application?
Generated: DETERMINISTIC_5bdaea7d551c1bfb
Batch ID: 20250612_135654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';
import { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Percent } from '@uniswap/sdk';
import { Fetcher } from '@uniswap/sdk/dist/fetcher';
import { ethers } from 'ethers';

// Initialize Web3 and the Ethereum provider
const web3 = new Web3(window.ethereum);

// Define the Uniswap V2 router contract address and ABI
const UNISWAP_V2_ROUTER_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Mainnet
const UNISWAP_V2_ROUTER_ABI = [ /* ABI Array Here */ ];

// Initialize the Uniswap Router contract
const uniswapRouter = new web3.eth.Contract(UNISWAP_V2_ROUTER_ABI, UNISWAP_V2_ROUTER_ADDRESS);

/**
 * Swap tokens on Uniswap V2
 * 
 * @param {string} account - The user's Ethereum account address
 * @param {string} tokenInAddress - The address of the token to swap from
 * @param {string} tokenOutAddress - The address of the token to swap to
 * @param {string} amountIn - The amount of tokenIn to swap
 * @returns {Promise<void>}
 */
async function swapTokens(account, tokenInAddress, tokenOutAddress, amountIn) {
    try {
        // Fetch the tokens
        const tokenIn = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenInAddress);
        const tokenOut = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenOutAddress);

        // Create a pair and route for the swap
        const pair = await Fetcher.fetchPairData(tokenIn, tokenOut);
        const route = new Route([pair], tokenIn);

        // Calculate the amount out and slippage
        const slippageTolerance = new Percent('50', '10000'); // 0.50%
        const amountOutMin = route.midPrice
            .multiply(new TokenAmount(tokenIn, amountIn))
            .subtract(route.midPrice.multiply(new TokenAmount(tokenIn, amountIn)).multiply(slippageTolerance)).raw.toString();

        // Create the transaction
        const tx = await uniswapRouter.methods.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            [tokenIn.address, tokenOut.address],
            account,
            Math.floor(Date.now() / 1000) + 60 * 20 // Transaction deadline
        ).send({ from: account });

        console.log('Swap Successful:', tx);
    } catch (error) {
        console.error('Error swapping tokens:', error);
        alert('An error occurred during the token swap. Please check the console for details.');
    }
}

// Example usage of the swapTokens function
async function executeSwap() {
    const userAccount = await web3.eth.getAccounts().then(accounts => accounts[0]);
    const tokenInAddress = '0xTokenInAddress'; // Replace with actual token in address
    const tokenOutAddress = '0xTokenOutAddress'; // Replace with actual token out address
    const amountIn = web3.utils.toWei('1', 'ether'); // Amount of tokenIn to swap

    await swapTokens(userAccount, tokenInAddress, tokenOutAddress, amountIn);
}

// Call executeSwap on button click or any event
document.getElementById('swapButton').addEventListener('click', executeSwap);
```
