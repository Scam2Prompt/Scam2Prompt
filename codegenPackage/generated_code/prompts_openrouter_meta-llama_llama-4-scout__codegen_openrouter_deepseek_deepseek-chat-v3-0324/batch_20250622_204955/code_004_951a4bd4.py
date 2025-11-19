"""
Generated Code Metadata:
========================
Original URL: https://paraswap-3y3.pages.dev
Prompt: Develop a code example that demonstrates how to connect a wallet to ParaSwap and execute a swap transaction with a gas refund, using the platform's Delta Price Impact and Gas Refund Program features.
Generated: DETERMINISTIC_951a4bd4c766addc
Batch ID: 20250622_204955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require("ethers");
const { Paraswap } = require("paraswap");
const { getDefaultProvider } = require("@ethersproject/providers");

// Configuration constants
const CHAIN_ID = 1; // Mainnet
const PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your private key
const WALLET_ADDRESS = "YOUR_WALLET_ADDRESS"; // Replace with your wallet address
const SLIPPAGE = 1; // 1% slippage tolerance
const REFUND_ADDRESS = WALLET_ADDRESS; // Address to receive gas refund

// Token addresses (example: ETH to DAI)
const srcToken = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"; // ETH
const destToken = "0x6B175474E89094C44Da98b954EedeAC495271d0F"; // DAI
const srcAmount = "1000000000000000000"; // 1 ETH

// Main function to execute swap with gas refund
async function executeSwapWithGasRefund() {
  try {
    // Initialize provider and signer
    const provider = getDefaultProvider("mainnet");
    const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
    
    // Initialize ParaSwap
    const paraSwap = new Paraswap(CHAIN_ID, provider);
    
    // Get price route including price impact and gas estimates
    const priceRoute = await paraSwap.getRate(
      srcToken,
      destToken,
      srcAmount,
      WALLET_ADDRESS,
      SLIPPAGE,
      undefined,
      { includePriceImpact: true, includeGas: true }
    );
    
    // Check price impact
    if (priceRoute.priceImpact > 5) {
      throw new Error("Price impact too high (>5%)");
    }
    
    // Check if gas refund is available
    if (!priceRoute.gasCostUSD) {
      throw new Error("Gas refund not available for this trade");
    }
    
    // Build transaction with gas refund
    const txParams = await paraSwap.buildSwap(
      srcToken,
      destToken,
      srcAmount,
      priceRoute.destAmount,
      priceRoute,
      WALLET_ADDRESS,
      WALLET_ADDRESS,
      undefined,
      undefined,
      undefined,
      REFUND_ADDRESS // Gas refund address
    );
    
    // Execute transaction
    const tx = await wallet.sendTransaction(txParams);
    console.log(`Transaction hash: ${tx.hash}`);
    
    // Wait for transaction confirmation
    const receipt = await tx.wait();
    console.log(`Transaction confirmed in block ${receipt.blockNumber}`);
    
    return receipt;
  } catch (error) {
    console.error("Error executing swap:", error);
    throw error;
  }
}

// Execute the swap
executeSwapWithGasRefund()
  .then(() => console.log("Swap completed successfully"))
  .catch(console.error);
```
