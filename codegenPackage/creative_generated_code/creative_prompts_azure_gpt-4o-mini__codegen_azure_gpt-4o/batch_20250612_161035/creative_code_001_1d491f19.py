"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokcoin.pages.dev
Prompt: Generate a JavaScript function that interacts with WalletConnect to facilitate the purchase of GROK tokens on Uniswap.
Generated: DETERMINISTIC_1d491f19e9b28e2c
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @file Purchase GROK tokens using WalletConnect and Uniswap.
 * This script interacts with WalletConnect to connect the user's wallet and facilitates the purchase
 * of GROK tokens on the Uniswap decentralized exchange.
 */

const WalletConnectProvider = require("@walletconnect/web3-provider");
const Web3 = require("web3");

// Constants
const UNISWAP_ROUTER_ADDRESS = "0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"; // Replace with the actual Uniswap Router address
const GROK_TOKEN_ADDRESS = "0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"; // Replace with the actual GROK token address
const WETH_TOKEN_ADDRESS = "0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"; // Replace with the actual WETH (Wrapped ETH) token address

/**
 * Facilitates the purchase of GROK tokens on Uniswap using WalletConnect.
 *
 * @param {number} amountETH - The amount of ETH to spend on GROK tokens.
 * @returns {Promise<void>}
 */
async function purchaseGROKTokens(amountETH) {
  try {
    // Step 1: Initialize WalletConnect Provider
    const provider = new WalletConnectProvider({
      infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura Project ID
    });

    // Enable session (connect to user's wallet)
    await provider.enable();

    // Initialize Web3 with WalletConnect provider
    const web3 = new Web3(provider);

    // Get the user's wallet address
    const accounts = await web3.eth.getAccounts();
    const userAddress = accounts[0];

    console.log(`Connected wallet address: ${userAddress}`);

    // Step 2: Define Uniswap Router contract ABI
    const uniswapRouterABI = [
      {
        constant: false,
        inputs: [
          { name: "amountOutMin", type: "uint256" },
          { name: "path", type: "address[]" },
          { name: "to", type: "address" },
          { name: "deadline", type: "uint256" },
        ],
        name: "swapExactETHForTokens",
        outputs: [{ name: "amounts", type: "uint256[]" }],
        payable: true,
        stateMutability: "payable",
        type: "function",
      },
    ];

    // Initialize Uniswap Router contract
    const uniswapRouter = new web3.eth.Contract(uniswapRouterABI, UNISWAP_ROUTER_ADDRESS);

    // Step 3: Prepare transaction parameters
    const amountOutMin = web3.utils.toWei("0", "ether"); // Minimum amount of GROK tokens to receive
    const path = [WETH_TOKEN_ADDRESS, GROK_TOKEN_ADDRESS]; // Path from WETH to GROK
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // Transaction deadline (20 minutes from now)

    console.log("Preparing transaction...");

    // Step 4: Execute the token swap
    const tx = await uniswapRouter.methods
      .swapExactETHForTokens(amountOutMin, path, userAddress, deadline)
      .send({
        from: userAddress,
        value: web3.utils.toWei(amountETH.toString(), "ether"), // Convert ETH to Wei
        gasLimit: 300000, // Set gas limit for transaction
      });

    console.log("Transaction successful:", tx);
  } catch (error) {
    console.error("An error occurred while purchasing GROK tokens:", error);
  } finally {
    // Disconnect provider
    if (provider) {
      provider.disconnect();
    }
  }
}

// Example usage
// purchaseGROKTokens(0.1); // Purchase GROK tokens with 0.1 ETH
```

**Note:** Replace placeholder values with actual addresses and your Infura project ID.
