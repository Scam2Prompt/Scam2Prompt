"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-staging.org
Prompt: How can I use the Uniswap Protocol's Javascript SDK to build a decentralized finance (DeFi) application?
Generated: DETERMINISTIC_251f53005043104a
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ChainId, Token, Fetcher, Route, Trade, TokenAmount, TradeType } from '@uniswap/sdk';
import { ethers } from 'ethers';

const UNISWAP_ROUTER_ADDRESS = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Uniswap Router address
const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID'); // Replace with your Infura Project ID
const wallet = new ethers.Wallet('YOUR_PRIVATE_KEY', provider); // Replace with your wallet's private key

/**
 * Fetches the price of a token pair from Uniswap.
 * @param {string} tokenAAddress - The contract address of token A.
 * @param {string} tokenBAddress - The contract address of token B.
 * @returns {Promise<number>} The price of token A in terms of token B.
 */
async function getPrice(tokenAAddress, tokenBAddress) {
    try {
        const tokenA = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenAAddress);
        const tokenB = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenBAddress);
        const pair = await Fetcher.fetchPairData(tokenA, tokenB);
        const route = new Route([pair], tokenA);
        return route.midPrice.toSignificant(6); // Return price with 6 significant figures
    } catch (error) {
        console.error('Error fetching price:', error);
        throw new Error('Failed to fetch the price');
    }
}

/**
 * Executes a trade on Uniswap.
 * @param {string} tokenInAddress - The contract address of the token being traded in.
 * @param {string} tokenOutAddress - The contract address of the token being traded out.
 * @param {string} amountIn - Amount of token in to trade.
 */
async function executeTrade(tokenInAddress, tokenOutAddress, amountIn) {
    try {
        const tokenIn = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenInAddress);
        const tokenOut = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenOutAddress);
        const pair = await Fetcher.fetchPairData(tokenIn, tokenOut);
        const route = new Route([pair], tokenIn);
        
        const amountInParsed = ethers.utils.parseUnits(amountIn, tokenIn.decimals);
        const trade = new Trade(route, new TokenAmount(tokenIn, amountInParsed), TradeType.EXACT_INPUT);

        // Prepare transaction
        const slippageTolerance = new ethers.BigNumber.from('50'); // 0.5% slippage
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw.toString();
        
        // Create transaction
        const uniswapRouter = new ethers.Contract(UNISWAP_ROUTER_ADDRESS, [
            'function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts)'
        ], wallet);
        
        const path = [tokenIn.address, tokenOut.address]; // Path to trade
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from now

        const tx = await uniswapRouter.swapExactTokensForTokens(
            amountInParsed,
            amountOutMin,
            path,
            wallet.address,
            deadline
        );

        console.log('Transaction sent:', tx.hash);
        await tx.wait(); // Wait for transaction confirmation
        console.log('Transaction confirmed:', tx.hash);
    } catch (error) {
        console.error('Error executing trade:', error);
        throw new Error('Trade execution failed');
    }
}

// Sample usage
(async () => {
    const DAI_ADDRESS = '0x6B175474E89094C44Da98b954EedeAC495271d0F'; // DAI token address
    const WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e6C4D5C59B14C4d8e7eE'; // WETH token address

    try {
        // Get the price of DAI in WETH
        const price = await getPrice(DAI_ADDRESS, WETH_ADDRESS);
        console.log(`Price of DAI in WETH: ${price}`);

        // Execute a trade
        await executeTrade(DAI_ADDRESS, WETH_ADDRESS, '1000000000000000000'); // Trade 1 DAI
    } catch (error) {
        console.error('Error in main execution:', error);
    }
})();
```

**Important:** Please replace `YOUR_INFURA_PROJECT_ID` and `YOUR_PRIVATE_KEY` with your actual Infura Project ID and wallet's private key. Ensure that you handle sensitive information securely and do not expose your private key in production code.
