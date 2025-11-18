"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: Create a JavaScript function to enable USDC token swaps on a DeFi platform using the Uniswap API.
Generated: DETERMINISTIC_1be278214fb445ac
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to enable USDC token swaps on a DeFi platform using the Uniswap API
 * 
 * @param {string} fromToken - The token to swap from (should be USDC)
 * @param {string} toToken - The token to swap to
 * @param {number} amount - The amount of tokens to swap (in USDC)
 * @param {string} walletAddress - The user's wallet address
 * @param {Object} provider - The Ethereum provider instance (e.g., ethers.js provider)
 * @returns {Promise<void>} - A promise that resolves when the swap is complete
 * @throws {Error} - Throws an error if swap fails
 */
async function swapUSDC(fromToken, toToken, amount, walletAddress, provider) {
    // Validate input parameters
    if (fromToken !== 'USDC') {
        throw new Error('Invalid fromToken. Only USDC swaps are allowed.');
    }
    if (amount <= 0) {
        throw new Error('Amount must be greater than zero.');
    }
    
    // Import necessary libraries (ensure you have ethers.js and @uniswap/sdk installed)
    const { ethers } = require('ethers');
    const { ChainId, Token, Fetcher, Route, Trade, TokenAmount, TradeType, Percent } = require('@uniswap/sdk');

    // Set up the provider and wallet
    const signer = provider.getSigner(walletAddress);

    // Fetch token data from Uniswap
    const usdc = new Token(ChainId.MAINNET, '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', 6); // USDC token address
    const toTokenData = await Fetcher.fetchTokenData(ChainId.MAINNET, toToken);
    
    // Create a pair and route for the trade
    const pair = await Fetcher.fetchPairData(usdc, toTokenData);
    const route = new Route([pair], new TokenAmount(usdc, ethers.utils.parseUnits(amount.toString(), 6)));

    // Create trade instance
    const trade = new Trade(route, new TokenAmount(usdc, ethers.utils.parseUnits(amount.toString(), 6)), TradeType.EXACT_INPUT);
    
    // Get slippage tolerance
    const slippageTolerance = new Percent('50', '10000'); // 0.5% slippage

    // Prepare transaction parameters
    const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw; // Minimum amount of tokens to receive
    const path = [usdc.address, toTokenData.address];
    const to = walletAddress;
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from the current time

    // Set up the contract and transaction
    const uniswapRouterAddress = '0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6'; // Uniswap V2 Router address
    const routerContract = new ethers.Contract(uniswapRouterAddress, [
        // ABI of the swapExactTokensForTokens
        "function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts)"
    ], signer);

    // Approve the router to spend USDC
    const usdcContract = new ethers.Contract(usdc.address, [
        "function approve(address spender, uint256 value) public returns (bool)"
    ], signer);

    const approvalTx = await usdcContract.approve(uniswapRouterAddress, ethers.utils.parseUnits(amount.toString(), 6));
    await approvalTx.wait(); // Wait for transaction confirmation

    // Execute the swap
    try {
        const swapTx = await routerContract.swapExactTokensForTokens(
            ethers.utils.parseUnits(amount.toString(), 6),
            amountOutMin.toString(),
            path,
            to,
            deadline
        );
        await swapTx.wait(); // Wait for transaction confirmation
        console.log(`Swap successful! Transaction hash: ${swapTx.hash}`);
    } catch (error) {
        throw new Error(`Swap failed: ${error.message}`);
    }
}

// Example usage (uncomment and replace with actual parameters)
// swapUSDC('USDC', 'DAI', 100, '0xYourWalletAddress', provider).catch(console.error);
```
