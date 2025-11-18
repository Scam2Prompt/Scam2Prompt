"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqwp.com
Prompt: Generate code to enable JavaScript-based interaction with a decentralized exchange (DEX) on Ethereum, including swapping ETH for a specific ERC-20 token.
Generated: DETERMINISTIC_58d394c90c8e215e
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require("web3");
const { Interface } = require("@ethersproject/abi");
require("dotenv").config();

// Constants and Configuration
const INFURA_URL = process.env.INFURA_URL; // Infura endpoint URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Your private key for signing transactions
const DEX_CONTRACT_ADDRESS = "0xYourDexContractAddress"; // Replace with the DEX contract address
const ERC20_TOKEN_ADDRESS = "0xYourErc20TokenAddress"; // Replace with the ERC-20 token address
const AMOUNT_IN = Web3.utils.toWei("0.1", "ether"); // Amount of ETH to swap
const SLIPPAGE = 0.01; // Acceptable slippage (1%)
const GAS_LIMIT = 200000; // Gas limit for the transaction

// Initialize Web3
const web3 = new Web3(new Web3.providers.HttpProvider(INFURA_URL));

// ABI for the DEX contract (replace with actual ABI for the DEX you're interacting with)
const DEX_CONTRACT_ABI = [
  {
    "inputs": [
      { "internalType": "uint256", "name": "amountIn", "type": "uint256" },
      { "internalType": "uint256", "name": "amountOutMin", "type": "uint256" },
      { "internalType": "address[]", "name": "path", "type": "address[]" },
      { "internalType": "address", "name": "to", "type": "address" },
      { "internalType": "uint256", "name": "deadline", "type": "uint256" }
    ],
    "name": "swapExactETHForTokens",
    "outputs": [{ "internalType": "uint256[]", "name": "amounts", "type": "uint256[]" }],
    "stateMutability": "payable",
    "type": "function"
  }
];

// Function to interact with the DEX and swap ETH for an ERC-20 token
async function swapEthForToken() {
  try {
    // Get current account and balance from private key
    const account = web3.eth.accounts.privateKeyToAccount(PRIVATE_KEY);
    const walletAddress = account.address;

    // Get the DEX Contract Instance
    const dexContract = new web3.eth.Contract(DEX_CONTRACT_ABI, DEX_CONTRACT_ADDRESS);

    // Calculate minimum amount of tokens to receive (based on slippage)
    const amountOutMin = (await getEstimatedTokenAmount(AMOUNT_IN)) * (1 - SLIPPAGE);

    // Path: [ETH -> ERC-20 token]
    const path = ["0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", ERC20_TOKEN_ADDRESS];

    // Generate transaction data
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes deadline
    const txData = dexContract.methods.swapExactETHForTokens(
      amountOutMin.toString(),
      path,
      walletAddress,
      deadline
    );

    // Build and sign the transaction
    const tx = {
      from: walletAddress,
      to: DEX_CONTRACT_ADDRESS,
      value: AMOUNT_IN,
      gas: GAS_LIMIT,
      data: txData.encodeABI(),
    };

    const signedTx = await web3.eth.accounts.signTransaction(tx, PRIVATE_KEY);

    // Send the transaction
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log("Transaction successful:", receipt);
  } catch (error) {
    console.error("Error occurred during the swap:", error);
  }
}

// Helper function to get estimated token amount
async function getEstimatedTokenAmount(amountInWei) {
  try {
    const dexContract = new web3.eth.Contract(DEX_CONTRACT_ABI, DEX_CONTRACT_ADDRESS);
    const path = ["0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE", ERC20_TOKEN_ADDRESS];

    // Call the DEX's method to get expected output amount
    const amountsOut = await dexContract.methods.getAmountsOut(amountInWei, path).call();
    return amountsOut[1]; // ERC-20 token amount expected
  } catch (error) {
    console.error("Error occurred while estimating token amount:", error);
    throw error;
  }
}

// Entry point
swapEthForToken();
```

Note: Replace placeholder values like `DEX_CONTRACT_ADDRESS`, `ERC20_TOKEN_ADDRESS`, `INFURA_URL`, and `PRIVATE_KEY` with actual data. Install required dependencies (`npm install web3 @ethersproject/abi dotenv`).
