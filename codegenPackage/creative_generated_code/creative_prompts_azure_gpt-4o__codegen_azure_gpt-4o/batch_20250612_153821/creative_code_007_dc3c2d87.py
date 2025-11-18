"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-git-felipe-draftwebrefetchsolanabalancesonsw-00ef87-uniswap.vercel.app
Prompt: Using ethers.js, create a script to connect to the Uniswap platform and execute a token trade programmatically.
Generated: DETERMINISTIC_dc3c2d87ee89940c
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const { ethers } = require("ethers");
const { abi: IUniswapV2Router02ABI } = require("@uniswap/v2-periphery/build/IUniswapV2Router02.json");
const { abi: ERC20ABI } = require("@openzeppelin/contracts/build/contracts/ERC20.json");

// Configure the script
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura Project ID
const WALLET_PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const UNISWAP_ROUTER_ADDRESS = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D"; // Uniswap V2 Router address
const TOKEN_IN_ADDRESS = "0x..."; // Replace with the address of the input token
const TOKEN_OUT_ADDRESS = "0x..."; // Replace with the address of the output token
const AMOUNT_IN = ethers.utils.parseUnits("1", 18); // Replace with the amount to trade (in input token units)
const AMOUNT_OUT_MIN = ethers.utils.parseUnits("0.1", 18); // Replace with the minimum amount of output token to receive
const SLIPPAGE_TOLERANCE = 0.5; // Slippage tolerance percentage (e.g., 0.5 for 0.5%)
const DEADLINE = Math.floor(Date.now() / 1000) + 60 * 5; // 5 minutes from now

// Initialize the provider
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);

// Initialize the wallet
const wallet = new ethers.Wallet(WALLET_PRIVATE_KEY, provider);

// Initialize the Uniswap Router contract
const uniswapRouter = new ethers.Contract(
  UNISWAP_ROUTER_ADDRESS,
  IUniswapV2Router02ABI,
  wallet
);

// Initialize the token contracts
const tokenIn = new ethers.Contract(TOKEN_IN_ADDRESS, ERC20ABI, wallet);
const tokenOut = new ethers.Contract(TOKEN_OUT_ADDRESS, ERC20ABI, wallet);

async function executeTrade() {
  try {
    console.log("Starting trade...");

    // Approve the Uniswap Router to spend the input token
    console.log("Approving token...");
    const approveTx = await tokenIn.approve(UNISWAP_ROUTER_ADDRESS, AMOUNT_IN);
    await approveTx.wait();
    console.log("Token approved successfully.");

    // Get the current token balance
    const tokenInBalance = await tokenIn.balanceOf(wallet.address);
    console.log(`Current token balance: ${ethers.utils.formatUnits(tokenInBalance, 18)} ${TOKEN_IN_ADDRESS}`);

    if (tokenInBalance.lt(AMOUNT_IN)) {
      throw new Error("Insufficient token balance for the trade.");
    }

    // Execute the swap on Uniswap
    console.log("Executing trade...");
    const swapTx = await uniswapRouter.swapExactTokensForTokens(
      AMOUNT_IN,
      AMOUNT_OUT_MIN,
      [TOKEN_IN_ADDRESS, TOKEN_OUT_ADDRESS], // Token path
      wallet.address, // Recipient address
      DEADLINE, // Deadline
      { gasLimit: 300000 } // Set a gas limit
    );
    console.log(`Transaction hash: ${swapTx.hash}`);
    await swapTx.wait();
    console.log("Trade executed successfully.");

    // Get the new token balances after the trade
    const newTokenOutBalance = await tokenOut.balanceOf(wallet.address);
    console.log(`New ${TOKEN_OUT_ADDRESS} balance: ${ethers.utils.formatUnits(newTokenOutBalance, 18)}`);

  } catch (error) {
    console.error("Error executing trade:", error.message);
  }
}

// Run the script
executeTrade();
```

**Note:** Replace placeholders (`YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, etc.) with your actual details. Also, install the required dependencies using:
```
npm install ethers @uniswap/v2-periphery @openzeppelin/contracts
```
