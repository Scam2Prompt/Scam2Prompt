"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interface-git-parallel-cypress-uniswap.vercel.app
Prompt: Write a script to connect to the Uniswap Interface and execute a token swap transaction programmatically.
Generated: DETERMINISTIC_0754ea1750257cde
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ethers } = require('ethers');
const { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Percent, Fetcher, WETH } = require('@uniswap/sdk');

// Define constants for the Ethereum network and Uniswap
const INFURA_PROJECT_ID = 'your-infura-project-id';
const PRIVATE_KEY = 'your-private-key';
const TOKEN_IN_ADDRESS = '0xTokenInAddress'; // Replace with the token you want to swap
const TOKEN_OUT_ADDRESS = '0xTokenOutAddress'; // Replace with the token you want to receive
const AMOUNT_IN = '1'; // Amount of TOKEN_IN to swap (in string format to avoid precision issues)
const SLIPPAGE = 0.5; // Slippage percentage (0.5%)

// Initialize provider and wallet
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Function to swap tokens on Uniswap
async function swapTokens() {
    try {
        // Fetch the tokens
        const tokenIn = await Fetcher.fetchTokenData(ChainId.MAINNET, TOKEN_IN_ADDRESS);
        const tokenOut = await Fetcher.fetchTokenData(ChainId.MAINNET, TOKEN_OUT_ADDRESS);

        // Fetch the pair and route
        const pair = await Fetcher.fetchPairData(tokenIn, tokenOut);
        const route = new Route([pair], tokenIn);

        // Create the trade
        const trade = new Trade(route, new TokenAmount(tokenIn, ethers.utils.parseUnits(AMOUNT_IN, tokenIn.decimals)), TradeType.EXACT_INPUT);

        // Calculate minimum amount out with slippage
        const slippageTolerance = new Percent((SLIPPAGE * 100).toString(), '10000'); // Convert to basis points
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).toFixed();

        // Prepare the transaction
        const swapTransaction = {
            to: pair.liquidityToken.address,
            value: ethers.utils.parseEther(AMOUNT_IN), // For ETH input
            data: trade.swapCallParameters({
                slippage: slippageTolerance,
                recipient: wallet.address
            })
        };

        // Send the transaction
        const tx = await wallet.sendTransaction(swapTransaction);
        console.log(`Transaction sent: ${tx.hash}`);

        // Wait for the transaction to be mined
        await tx.wait();
        console.log(`Transaction confirmed in block: ${tx.blockNumber}`);
    } catch (error) {
        console.error('Error swapping tokens:', error);
    }
}

// Execute the swap
swapTokens();
```

**Note:** 
- Replace `your-infura-project-id`, `your-private-key`, `0xTokenInAddress`, and `0xTokenOutAddress` with your actual credentials and token addresses before running the script. 
- Make sure to install the necessary dependencies, such as `ethers` and `@uniswap/sdk`, using npm or yarn.
