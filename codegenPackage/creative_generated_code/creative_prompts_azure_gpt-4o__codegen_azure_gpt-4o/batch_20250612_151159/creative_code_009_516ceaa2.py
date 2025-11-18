"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiroinu.pages.dev
Prompt: Generate a script using ethers.js to connect to Uniswap, swap ETH for $NEIRO tokens, and display the estimated token amount before confirming the transaction.
Generated: DETERMINISTIC_516ceaa2ba5ff1ca
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
const { ethers } = require("ethers");
const { Fetcher, Route, Trade, Token, TokenAmount, TradeType } = require("@uniswap/sdk");
require('dotenv').config(); // Load environment variables

// Configuration
const INFURA_PROJECT_ID = process.env.INFURA_PROJECT_ID; // Infura project ID for Ethereum network access
const PRIVATE_KEY = process.env.PRIVATE_KEY;            // Private key of your wallet
const NETWORK = "homestead";                            // Ethereum mainnet
const ETH_AMOUNT = "0.1";                               // Amount of ETH to swap
const NEIRO_TOKEN_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"; // Replace with the actual NEIRO token address
const SLIPPAGE_TOLERANCE = 0.005;                       // Slippage tolerance (e.g., 0.5%)

(async () => {
  try {
    // Initialize Ethereum provider
    const provider = new ethers.providers.InfuraProvider(NETWORK, INFURA_PROJECT_ID);

    // Initialize wallet
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

    // Uniswap SDK setup
    const WETH = Fetcher.fetchTokenData(1, "0xC02aaa39b223FE8D0A0e5C4F27eAD9083C756Cc2", provider); // WETH token data
    const NEIRO = Fetcher.fetchTokenData(1, NEIRO_TOKEN_ADDRESS, provider); // NEIRO token data
    const [WETH_TOKEN, NEIRO_TOKEN] = await Promise.all([WETH, NEIRO]);

    // Fetch pair data
    const pair = await Fetcher.fetchPairData(WETH_TOKEN, NEIRO_TOKEN, provider);

    // Create a trading route
    const route = new Route([pair], WETH_TOKEN);

    // Calculate trade
    const trade = new Trade(route, new TokenAmount(WETH_TOKEN, ethers.utils.parseEther(ETH_AMOUNT).toString()), TradeType.EXACT_INPUT);

    // Display estimated amount of NEIRO tokens
    const amountOut = trade.outputAmount.toSignificant(6); // 6 significant figures
    console.log(`Estimated NEIRO tokens received: ${amountOut}`);

    // Confirm transaction with user
    const confirm = require('prompt-sync')();
    const userInput = confirm(`Proceed with swapping ${ETH_AMOUNT} ETH for approximately ${amountOut} NEIRO tokens? (yes/no): `);
    if (userInput.toLowerCase() !== "yes") {
      console.log("Transaction aborted.");
      return;
    }

    // Encode transaction data for swap
    const slippageAdjustedAmountOut = trade.minimumAmountOut(SLIPPAGE_TOLERANCE).raw; // Minimum amount out accounting for slippage
    const path = [WETH_TOKEN.address, NEIRO_TOKEN.address];
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Transaction deadline: 20 minutes from now

    const uniswapRouterAddress = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"; // Uniswap V2 Router address
    const uniswapRouter = new ethers.Contract(
      uniswapRouterAddress,
      [
        "function swapExactETHForTokens(uint amountOutMin, address[] calldata path, address to, uint deadline) payable returns (uint[] memory amounts)"
      ],
      wallet
    );

    // Perform the swap
    const tx = await uniswapRouter.swapExactETHForTokens(
      ethers.BigNumber.from(slippageAdjustedAmountOut.toString()),
      path,
      wallet.address,
      deadline,
      { value: ethers.utils.parseEther(ETH_AMOUNT), gasLimit: 200000 }
    );

    console.log(`Transaction submitted. Hash: ${tx.hash}`);
    console.log("Waiting for confirmation...");

    // Wait for transaction confirmation
    const receipt = await tx.wait();
    console.log(`Transaction confirmed in block ${receipt.blockNumber}.`);
  } catch (error) {
    console.error("An error occurred:", error.message || error);
  }
})();
```
