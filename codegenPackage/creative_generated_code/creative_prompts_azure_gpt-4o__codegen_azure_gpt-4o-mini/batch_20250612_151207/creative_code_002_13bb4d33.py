"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-wat0x63.pages.dev
Prompt: Provide step-by-step instructions for integrating MetaMask with Uniswap to swap Ethereum for $WAT tokens using the contract address `0x636bd98fc13908e475f56d8a38a6e03616ec5563`. Include details about adjusting slippage and gas fees.
Generated: DETERMINISTIC_13bb4d33984bdd37
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules
import Web3 from 'web3';
import { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Percent } from '@uniswap/sdk';
import { Fetcher } from '@uniswap/sdk/dist/index';
import axios from 'axios';

// Set up the Web3 instance and provider
const web3 = new Web3(window.ethereum);

// Define the token and Uniswap router contract addresses
const WAT_TOKEN_ADDRESS = '0x636bd98fc13908e475f56d8a38a6e03616ec5563';
const UNISWAP_ROUTER_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Example address on Ethereum Mainnet

// Function to connect MetaMask
async function connectMetaMask() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        return accounts[0]; // Return the user's account address
    } catch (error) {
        console.error("Failed to connect to MetaMask:", error);
        throw new Error("User denied account access");
    }
}

// Function to get the WAT token price in ETH
async function getWATTokenPrice() {
    try {
        const token = await Fetcher.fetchTokenData(ChainId.MAINNET, WAT_TOKEN_ADDRESS);
        const pair = await Fetcher.fetchPairData(token, Token.WETH[token.chainId]);
        const route = new Route([pair], Token.WETH[token.chainId]);
        return route.midPrice.toSignificant(6); // Get the price of WAT in ETH
    } catch (error) {
        console.error("Error fetching WAT token price:", error);
        throw new Error("Failed to fetch token price");
    }
}

// Function to perform the swap
async function swapETHForWAT(amountIn, slippage = 0.5) {
    const account = await connectMetaMask();
    const amountOutMin = await calculateAmountOutMin(amountIn, slippage);
    
    const trade = new Trade(
        new Route([], Token.WETH[ChainId.MAINNET]), // Define your route based on pairs
        new TokenAmount(Token.WETH[ChainId.MAINNET], web3.utils.toWei(amountIn.toString(), 'ether')),
        TradeType.EXACT_INPUT
    );

    const transaction = {
        to: UNISWAP_ROUTER_ADDRESS,
        value: web3.utils.toHex(web3.utils.toWei(amountIn.toString(), 'ether')),
        gas: 200000, // Set gas limit (can be adjusted)
        data: trade.swapCallParameters.recipient = account, // Set recipient as user's account
    };

    try {
        const txHash = await web3.eth.sendTransaction(transaction);
        console.log("Transaction successful with hash:", txHash);
    } catch (error) {
        console.error("Transaction failed:", error);
        throw new Error("Swap failed");
    }
}

// Function to calculate minimum amount out based on slippage
async function calculateAmountOutMin(amountIn, slippage) {
    const price = await getWATTokenPrice();
    const slippageTolerance = new Percent(slippage.toString(), '100'); // Convert to percentage
    const amountOut = price * amountIn; // Calculate expected amount out
    return (amountOut * (1 - slippageTolerance.toFixed())).toString(); // Apply slippage
}

// Example usage
(async () => {
    try {
        const amountIn = 0.1; // Amount of ETH to swap
        const slippage = 0.5; // Slippage percentage
        await swapETHForWAT(amountIn, slippage);
    } catch (error) {
        console.error("Error in the swap process:", error);
    }
})();
```
