"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-hop.com
Prompt: Generate a sample transaction that demonstrates how to swap ETH for USDC using Hop Exchange's cross-chain capabilities.
Generated: DETERMINISTIC_79e213d92858dc1e
Batch ID: 20250612_155607
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const ethers = require("ethers"); // Ethereum library for interacting with the blockchain
const hop = require("@hop-protocol/sdk"); // Hop Protocol SDK for cross-chain swaps

// Configuration
const INFURA_API_KEY = "your-infura-api-key"; // Replace with your Infura API Key
const PRIVATE_KEY = "your-private-key"; // Replace with your private wallet key
const ETH_NETWORK = "homestead"; // Ethereum mainnet
const USDC_TOKEN_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0CE3606eb48"; // USDC contract address on Ethereum
const HOP_CHAIN = "polygon"; // Target cross-chain destination (e.g., Polygon)
const HOP_BRIDGE_TOKEN = "USDC"; // Bridge token name (USDC in this example)

// Initialize provider and signer
const provider = new ethers.providers.InfuraProvider(ETH_NETWORK, INFURA_API_KEY);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Initialize Hop SDK
const hopSdk = new hop.SDK({ chain: ETH_NETWORK });

// Swap ETH for USDC using Hop Exchange cross-chain capability
async function swapEthForUSDC(amountInEth) {
  try {
    // Step 1: Convert ETH amount to Wei (smallest denomination)
    const amountInWei = ethers.utils.parseEther(amountInEth.toString());

    // Step 2: Get Hop Bridge instance for the USDC token
    const bridge = hopSdk.bridge(HOP_BRIDGE_TOKEN);

    // Step 3: Calculate the estimated amount of USDC to receive
    const amountOutUSDC = await bridge.getQuote({
      amountIn: amountInWei,
      fromChain: ETH_NETWORK,
      toChain: HOP_CHAIN,
    });

    console.log("Estimated USDC amount:", ethers.utils.formatUnits(amountOutUSDC, 6));

    // Step 4: Perform the token swap
    const tx = await bridge.send({
      amount: amountInWei, // Amount of ETH to swap
      fromChain: ETH_NETWORK, // Source chain (Ethereum in this case)
      toChain: HOP_CHAIN, // Destination chain (Polygon)
      recipient: wallet.address, // Receiver address (your wallet)
    });

    console.log("Transaction submitted:", tx.hash);

    // Step 5: Wait for transaction confirmation
    const receipt = await tx.wait();
    console.log("Transaction confirmed:", receipt.transactionHash);

    console.log("Swap completed successfully!");
  } catch (error) {
    console.error("Error during swap:", error.message);
    throw new Error("Swap failed. See error details above.");
  }
}

// Example usage: Swap 0.1 ETH for USDC
swapEthForUSDC(0.1);
```

Note: Replace `your-infura-api-key` and `your-private-key` with appropriate credentials. Make sure the Hop Protocol SDK is installed (`npm install @hop-protocol/sdk`) and the script is executed in a secure environment.
