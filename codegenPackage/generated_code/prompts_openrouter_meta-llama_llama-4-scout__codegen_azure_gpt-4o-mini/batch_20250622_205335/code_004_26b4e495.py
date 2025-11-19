"""
Generated Code Metadata:
========================
Original URL: https://uniswap.arhamsoft.org
Prompt: Explain how to integrate Uniswap with a web application for token trading.
Generated: DETERMINISTIC_26b4e495b1c5c6db
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { ethers } from 'ethers';
import { ChainId, Token, TokenAmount, Pair, Route, Trade, TradeType, Fetcher } from '@uniswap/sdk';

// Define constants for the Uniswap integration
const UNISWAP_ROUTER_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Uniswap V2 Router address
const INFURA_PROJECT_ID = 'YOUR_INFURA_PROJECT_ID'; // Replace with your Infura project ID

// Initialize provider and signer
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
const signer = new ethers.Wallet('YOUR_PRIVATE_KEY', provider); // Replace with your wallet private key

// Function to fetch token details and create a trade
async function createTrade(tokenInAddress, tokenOutAddress, amountIn) {
    try {
        // Fetch token details
        const tokenIn = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenInAddress);
        const tokenOut = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenOutAddress);
        
        // Fetch pair data
        const pair = await Fetcher.fetchPairData(tokenIn, tokenOut);
        
        // Create a route and trade
        const route = new Route([pair], tokenIn);
        const trade = new Trade(route, new TokenAmount(tokenIn, amountIn.toString()), TradeType.EXACT_INPUT);
        
        return trade;
    } catch (error) {
        console.error('Error creating trade:', error);
        throw new Error('Failed to create trade');
    }
}

// Function to execute the trade
async function executeTrade(trade) {
    try {
        // Prepare transaction parameters
        const slippageTolerance = new ethers.BigNumber.from('50'); // 0.5% slippage
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).toFixed();
        const path = [trade.inputAmount.token.address, trade.outputAmount.token.address];
        const to = await signer.getAddress(); // Address to receive output tokens
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now

        // Create transaction
        const tx = {
            to: UNISWAP_ROUTER_ADDRESS,
            value: '0x0', // Set to '0x0' for token swaps
            data: trade.swapCallParameters({
                slippage: slippageTolerance,
                recipient: to,
                deadline: deadline,
            }).data,
            gasLimit: ethers.utils.hexlify(100000), // Set a gas limit
        };

        // Send transaction
        const transactionResponse = await signer.sendTransaction(tx);
        await transactionResponse.wait(); // Wait for transaction to be mined

        console.log('Trade executed successfully:', transactionResponse);
    } catch (error) {
        console.error('Error executing trade:', error);
        throw new Error('Failed to execute trade');
    }
}

// Example usage
(async () => {
    const tokenInAddress = '0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'; // USDC address
    const tokenOutAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F'; // DAI address
    const amountIn = ethers.utils.parseUnits('10', 6); // Amount of USDC to trade

    try {
        const trade = await createTrade(tokenInAddress, tokenOutAddress, amountIn);
        await executeTrade(trade);
    } catch (error) {
        console.error('Error in trading process:', error);
    }
})();
```

**Note:** Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_PRIVATE_KEY` with your actual Infura project ID and wallet private key. Ensure that you handle your private key securely and do not expose it in your code.
