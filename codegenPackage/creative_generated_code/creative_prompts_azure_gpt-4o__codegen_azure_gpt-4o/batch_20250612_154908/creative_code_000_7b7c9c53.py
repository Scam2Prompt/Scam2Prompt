"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap3.vercel.app
Prompt: Write a script using the Uniswap v3 SDK to swap ETH for USDC on the Ethereum blockchain.
Generated: DETERMINISTIC_7b7c9c53bbaa7728
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies and modules
require('dotenv').config(); // For loading environment variables
const { ethers } = require('ethers'); // Ethereum library
const { Pool, Route, Trade, Token, TokenAmount, TradeType } = require('@uniswap/v3-sdk'); // Uniswap v3 SDK
const { AlphaRouter } = require('@uniswap/smart-order-router'); // Smart order router
const { Percent } = require('@uniswap/sdk-core'); // SDK Utils

// Load environment variables
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID;
const PRIVATE_KEY = process.env.PRIVATE_KEY;
const UNISWAP_ROUTER_ADDRESS = process.env.UNISWAP_ROUTER_ADDRESS;

// Check required environment variables
if (!INFURA_PROJECT_ID || !PRIVATE_KEY || !UNISWAP_ROUTER_ADDRESS) {
  throw new Error('Missing required environment variables');
}

// Set up Ethereum provider
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);

// Set up wallet
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Define token details (USDC and WETH9)
const USDC = new Token(
  1, // Chain ID (Ethereum mainnet)
  '0xA0b86991c6218b36c1d19d4a2e9Eb0CE3606EB48', // USDC contract address
  6, // Decimals
  'USDC', // Symbol
  'USD Coin' // Name
);

const WETH = new Token(
  1, // Chain ID (Ethereum mainnet)
  '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', // WETH contract address
  18, // Decimals
  'WETH', // Symbol
  'Wrapped Ether' // Name
);

// Create AlphaRouter instance
const alphaRouter = new AlphaRouter({ chainId: 1, provider });

// Function to perform the swap
async function swapETHForUSDC(amountInETH) {
  try {
    // Convert ETH input to WETH TokenAmount
    const amountIn = ethers.utils.parseEther(amountInETH.toString());

    // Fetch USDC pool data and construct pool
    const poolData = await alphaRouter.fetchPoolData(WETH, USDC);
    const pool = new Pool(
      WETH,
      USDC,
      poolData.fee,
      poolData.sqrtPriceX96,
      poolData.liquidity,
      poolData.tickCurrent
    );

    // Define a route through the pool
    const route = new Route([pool], WETH, USDC);

    // Create a trade
    const trade = new Trade(route, new TokenAmount(WETH, amountIn.toString()), TradeType.EXACT_INPUT);

    // Define slippage tolerance (1%)
    const slippageTolerance = new Percent('1', '100');

    // Approximate output amount
    const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw.toString();

    // Generate calldata for the swap transaction
    const { calldata, value } = await alphaRouter.swapCallParameters(trade, {
      recipient: wallet.address, // Address receiving the swapped tokens
      slippageTolerance,
      deadline: Math.floor(Date.now() / 1000) + 60 * 10, // 10 min deadline
    });

    // Send transaction
    const tx = await wallet.sendTransaction({
      to: UNISWAP_ROUTER_ADDRESS,
      data: calldata,
      value: ethers.BigNumber.from(value),
    });

    console.log('Transaction sent:', tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log('Transaction confirmed:', receipt.transactionHash);
  } catch (error) {
    console.error('Error during swap:', error);
  }
}

// Execute the swap with 0.1 ETH as an example input
swapETHForUSDC(0.1);
```

Make sure the `.env` file has the following values set:
```plaintext
INFURA_PROJECT_ID=your_infura_project_id
PRIVATE_KEY=your_wallet_private_key
UNISWAP_ROUTER_ADDRESS=0xE592427A0AEce92De3Edee1F18E0157C05861564
```
