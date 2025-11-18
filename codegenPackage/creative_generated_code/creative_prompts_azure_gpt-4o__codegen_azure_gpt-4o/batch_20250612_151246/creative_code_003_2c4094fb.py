"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Generate a script using Web3.js to connect a wallet to PancakeSwap and execute a transaction to swap BNB for IQRA Tokens. Include error handling and transaction confirmation.
Generated: DETERMINISTIC_2c4094fb71d9a2ad
Batch ID: 20250612_151246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://bsc-dataseed.binance.org/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js library
const Web3 = require('web3');

// Import PancakeSwap Router ABI
const PancakeSwapRouterABI = require('./PancakeSwapRouterABI.json'); // Ensure this file contains the PancakeSwap Router ABI

// Configuration for Binance Smart Chain
const BSC_RPC_URL = 'https://bsc-dataseed.binance.org/'; // Binance Smart Chain mainnet RPC URL
const PANCAKESWAP_ROUTER_ADDRESS = '0x10ED43C718714eb63d5aA57B78B54704E256024E'; // PancakeSwap Router v2 address

// Set up web3 instance
const web3 = new Web3(new Web3.providers.HttpProvider(BSC_RPC_URL));

// User wallet details
const WALLET_ADDRESS = 'YOUR_WALLET_ADDRESS'; // Replace with your wallet address
const PRIVATE_KEY = 'YOUR_PRIVATE_KEY'; // Replace with your private key (keep this secure!)

// Token details
const IQRA_TOKEN_ADDRESS = 'IQRA_TOKEN_SMART_CONTRACT_ADDRESS'; // Replace with IQRA token contract address
const AMOUNT_TO_SWAP = web3.utils.toWei('0.01', 'ether'); // Amount of BNB to swap (converted to wei)
const SLIPPAGE = 0.01; // 1% slippage tolerance

(async () => {
  try {
    // Create contract instance for PancakeSwap Router
    const routerContract = new web3.eth.Contract(PancakeSwapRouterABI, PANCAKESWAP_ROUTER_ADDRESS);

    // Get current gas price
    const gasPrice = await web3.eth.getGasPrice();

    // Define the token swapping path: BNB -> IQRA Token
    const path = [
      '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE', // Address for BNB
      IQRA_TOKEN_ADDRESS, // Address for IQRA Token
    ];

    // Set deadline for transaction (current time + 20 minutes)
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20;

    // Estimate the minimum amount of IQRA tokens to receive (considering slippage)
    const amountsOut = await routerContract.methods.getAmountsOut(AMOUNT_TO_SWAP, path).call();
    const amountOutMin = web3.utils.toBN(amountsOut[1]).mul(web3.utils.toBN(100 - SLIPPAGE * 100)).div(web3.utils.toBN(100));

    // Prepare transaction data
    const txData = routerContract.methods.swapExactETHForTokens(
      amountOutMin.toString(),
      path,
      WALLET_ADDRESS,
      deadline
    ).encodeABI();

    // Create transaction object
    const transaction = {
      from: WALLET_ADDRESS,
      to: PANCAKESWAP_ROUTER_ADDRESS,
      value: AMOUNT_TO_SWAP, // Amount of BNB to send
      gasPrice: gasPrice,
      gas: 200000, // Set gas limit (adjust if necessary)
      data: txData,
    };

    // Sign transaction
    const signedTx = await web3.eth.accounts.signTransaction(transaction, PRIVATE_KEY);

    // Send transaction to the blockchain
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Transaction successful:', receipt);

    // Confirm transaction status
    if (receipt.status) {
      console.log('Swap completed successfully:', receipt.transactionHash);
    } else {
      console.error('Swap failed:', receipt);
    }
  } catch (error) {
    // Error handling
    console.error('Error occurred during token swap:', error.message);
  }
})();
```

### Notes:
- Replace `YOUR_WALLET_ADDRESS`, `YOUR_PRIVATE_KEY`, and `IQRA_TOKEN_SMART_CONTRACT_ADDRESS` with your actual wallet address, private key, and IQRA token contract address respectively.
- Ensure you have a `.json` file containing PancakeSwap Router ABI, or fetch it from PancakeSwap's official GitHub repository.
- Always handle your private key securely and avoid hardcoding sensitive information in production environments. Use environment variables or secret managers instead.
