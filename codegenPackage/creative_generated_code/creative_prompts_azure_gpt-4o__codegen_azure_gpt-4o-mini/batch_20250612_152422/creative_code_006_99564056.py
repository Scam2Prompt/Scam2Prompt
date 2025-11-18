"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spyro-vip.pages.dev
Prompt: Explain how to use the $SPYRO token address with Metamask and Uniswap to perform a token swap, including handling slippage during market volatility.
Generated: DETERMINISTIC_99564056b7aca56a
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const Web3 = require('web3');
const { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Percent } = require('@uniswap/sdk');
const { ethers } = require('ethers');

// Initialize web3 and set up Metamask provider
const web3 = new Web3(window.ethereum);

// Constants
const SPYRO_ADDRESS = 'INSERT_SPYRO_TOKEN_ADDRESS_HERE';
const WETH_ADDRESS = 'INSERT_WETH_TOKEN_ADDRESS_HERE'; // WETH token address
const SLIPPAGE_TOLERANCE = new Percent('50', '10000'); // 0.5%

// Function to swap tokens
async function swapTokens(amountIn, amountOutMin) {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Create ERC20 token objects for SPYRO and WETH
        const spyroToken = new Token(ChainId.MAINNET, SPYRO_ADDRESS, 18); // Assuming 18 decimals
        const wethToken = new Token(ChainId.MAINNET, WETH_ADDRESS, 18); // Assuming 18 decimals

        // Create a pair and fetch reserves
        const pair = await Pair.fetchData(spyroToken, wethToken);
        const route = new Route([pair], wethToken);
        
        // Create a trade object
        const trade = new Trade(route, new TokenAmount(wethToken, amountIn), TradeType.EXACT_INPUT);
        
        // Calculate minimum amount out considering slippage
        const minimumAmountOut = trade.minimumAmountOut(SLIPPAGE_TOLERANCE).toExact();

        // Create the transaction data
        const txData = {
            from: userAddress,
            to: pair.liquidityToken.address,
            value: web3.utils.toWei(amountIn.toString(), 'ether'),
            gas: 2000000,
            data: trade.swapCallParameters({ slippage: SLIPPAGE_TOLERANCE })
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(txData);
        
        console.log(`Transaction successful with hash: ${txHash.transactionHash}`);
    } catch (error) {
        console.error('Error in swapping tokens:', error);
        alert('Transaction failed. Please check console for details.');
    }
}

// Example usage: Swap 0.1 WETH for SPYRO
swapTokens(0.1, 0); // amountIn is in WETH, amountOutMin is optional for user-defined minimum
```

> Note: Replace `'INSERT_SPYRO_TOKEN_ADDRESS_HERE'` and `'INSERT_WETH_TOKEN_ADDRESS_HERE'` with actual token addresses.
