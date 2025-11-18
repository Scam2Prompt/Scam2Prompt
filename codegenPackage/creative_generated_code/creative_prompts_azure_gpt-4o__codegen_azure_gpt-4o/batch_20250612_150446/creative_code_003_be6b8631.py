"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefs.finance
Prompt: Create a script to automate token swaps on a DeFi platform using Web3.js or ethers.js.
Generated: DETERMINISTIC_be6b86319c451161
Batch ID: 20250612_150446
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
require("dotenv").config(); // Ensure you have a .env file with necessary variables

// Load environment variables
const INFURA_URL = process.env.INFURA_URL; // Infura Project URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Your wallet's private key
const ROUTER_ADDRESS = process.env.ROUTER_ADDRESS; // DeFi platform's router contract address
const TOKEN_IN_ADDRESS = process.env.TOKEN_IN_ADDRESS; // Address of the token to swap from
const TOKEN_OUT_ADDRESS = process.env.TOKEN_OUT_ADDRESS; // Address of the token to swap to
const AMOUNT_IN = ethers.utils.parseUnits(process.env.AMOUNT_IN, "ether"); // Amount of token to swap
const SLIPPAGE = process.env.SLIPPAGE || "0.5"; // Slippage percentage (default 0.5%)
const DEADLINE_SECONDS = process.env.DEADLINE_SECONDS || 300; // Transaction deadline in seconds
const GAS_LIMIT = process.env.GAS_LIMIT || 200000; // Gas limit for the transaction

// ABI for the DeFi platform's router contract
const ROUTER_ABI = [
    "function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory)"
];

// Set up provider, wallet, and contract instance
const provider = new ethers.providers.JsonRpcProvider(INFURA_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
const routerContract = new ethers.Contract(ROUTER_ADDRESS, ROUTER_ABI, wallet);

async function swapTokens() {
    try {
        // Get current gas price
        const gasPrice = await provider.getGasPrice();

        // Fetch token decimals for accurate calculations
        const tokenInContract = new ethers.Contract(TOKEN_IN_ADDRESS, ["function decimals() view returns (uint8)"], provider);
        const tokenOutContract = new ethers.Contract(TOKEN_OUT_ADDRESS, ["function decimals() view returns (uint8)"], provider);
        const tokenInDecimals = await tokenInContract.decimals();
        const tokenOutDecimals = await tokenOutContract.decimals();

        // Approve the router to spend TOKEN_IN
        const tokenInWithSigner = tokenInContract.connect(wallet);
        const allowance = await tokenInWithSigner.allowance(wallet.address, ROUTER_ADDRESS);

        if (allowance.lt(AMOUNT_IN)) {
            console.log("Approving router to spend tokens...");
            const approveTx = await tokenInWithSigner.approve(ROUTER_ADDRESS, ethers.constants.MaxUint256);
            await approveTx.wait();
            console.log("Approval successful!");
        }

        // Get estimated amounts out (optional: for UI or logging purposes)
        const path = [TOKEN_IN_ADDRESS, TOKEN_OUT_ADDRESS];
        const amountsOut = await routerContract.getAmountsOut(AMOUNT_IN, path);
        const amountOutMin = amountsOut[1].sub(amountsOut[1].mul(SLIPPAGE).div(100)); // Apply slippage

        // Prepare the swap transaction
        console.log("Swapping tokens...");
        const swapTx = await routerContract.swapExactTokensForTokens(
            AMOUNT_IN,
            amountOutMin,
            path,
            wallet.address,
            Math.floor(Date.now() / 1000) + Number(DEADLINE_SECONDS), // Deadline
            {
                gasPrice,
                gasLimit: GAS_LIMIT
            }
        );

        console.log(`Transaction sent: ${swapTx.hash}`);

        // Wait for the transaction to be mined
        const receipt = await swapTx.wait();
        console.log("Swap successful!", receipt);
    } catch (error) {
        console.error("Error during token swap:", error);
    }
}

// Execute the swapTokens function
swapTokens();
```

**Note:**  
- Ensure that you have a `.env` file with the required variables: `INFURA_URL`, `PRIVATE_KEY`, `ROUTER_ADDRESS`, `TOKEN_IN_ADDRESS`, `TOKEN_OUT_ADDRESS`, `AMOUNT_IN`, `SLIPPAGE`, `DEADLINE_SECONDS`, and `GAS_LIMIT`.  
- Make sure to install the necessary dependencies by running: `npm install ethers dotenv`.  
- Test thoroughly in a development environment before deploying to production.
