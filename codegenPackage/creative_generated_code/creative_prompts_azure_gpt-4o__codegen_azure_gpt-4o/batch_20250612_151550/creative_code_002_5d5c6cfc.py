"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-staging.org
Prompt: Provide an example of how to use the Uniswap SDK to swap tokens programmatically, including error handling for failed transactions.
Generated: DETERMINISTIC_5d5c6cfc15cd1dbf
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required Dependencies:
// npm install @uniswap/sdk ethers dotenv

// Load environment variables from a .env file
require('dotenv').config();

const { ChainId, Token, TokenAmount, TradeType, Route, Trade, Fetcher } = require('@uniswap/sdk');
const { ethers } = require('ethers');

// Configuration
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID; // Replace with your Infura Project ID
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Replace with your wallet private key
const CHAIN_ID = ChainId.MAINNET; // Ethereum mainnet

// Tokens involved in the trade
const DAI = new Token(CHAIN_ID, '0x6B175474E89094C44Da98b954EedeAC495271d0F', 18, 'DAI', 'Dai Stablecoin');
const WETH = new Token(CHAIN_ID, '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 18, 'WETH', 'Wrapped Ether');

// Function to execute token swap
async function performSwap() {
  try {
    // Initialize provider and wallet
    const provider = new ethers.providers.InfuraProvider(CHAIN_ID, INFURA_PROJECT_ID);
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

    // Fetch token pair data
    const pair = await Fetcher.fetchPairData(DAI, WETH, provider);

    // Create route
    const route = new Route([pair], WETH);

    // Specify amount to trade (e.g., 1 WETH)
    const tradeAmount = ethers.utils.parseUnits('1', WETH.decimals);
    const trade = new Trade(route, new TokenAmount(WETH, tradeAmount.toString()), TradeType.EXACT_INPUT);

    // Log trade details
    console.log('Trade Execution Price:', trade.executionPrice.toSignificant(6));
    console.log('Trade Next Mid Price:', trade.nextMidPrice.toSignificant(6));

    // Generate transaction parameters
    const slippageTolerance = new ethers.BigNumber.from(50); // 0.5% slippage
    const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw.toString();
    const path = [WETH.address, DAI.address];
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from the current time
    const value = trade.inputAmount.raw.toString();

    const uniswapRouterAddress = '0xE592427A0AEce92De3Edee1F18E0157C05861564'; // Uniswap Router Address
    const uniswapRouterABI = [
      'function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) external payable',
    ];

    // Create the contract instance
    const uniswapContract = new ethers.Contract(uniswapRouterAddress, uniswapRouterABI, wallet);

    // Execute the swap
    const tx = await uniswapContract.swapExactETHForTokens(
      amountOutMin,
      path,
      wallet.address, // Recipient of the output tokens
      deadline,
      { value: trade.inputAmount.raw.toString() } // Amount to send
    );

    console.log('Transaction Hash:', tx.hash);

    // Wait for transaction to be mined
    const receipt = await tx.wait();
    console.log('Transaction was mined successfully:', receipt);
  } catch (error) {
    // Error handling
    console.error('An error occurred while executing the swap:', error);
  }
}

// Execute the swap function
performSwap();
```
