"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.net
Prompt: How can I use deBridge's developer tools to build an application that supports multi-chain liquidity transfers?
Generated: DETERMINISTIC_55dc5a4ed44f7974
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from deBridge SDK
import { deBridge, Token, TransferOptions } from '@debridge/sdk'; 

// Initialize deBridge with your API key
const deBridgeAPIKey = 'YOUR_DEBRIDGE_API_KEY'; // Replace with your actual API key
const deBridgeInstance = new deBridge(deBridgeAPIKey);

/**
 * Function to initiate a multi-chain liquidity transfer
 * @param {string} fromChain - The chain to transfer from
 * @param {string} toChain - The chain to transfer to
 * @param {string} tokenAddress - The address of the token to transfer
 * @param {string} recipientAddress - The address of the recipient on the destination chain
 * @param {number} amount - The amount of tokens to transfer
 */
async function transferTokens(fromChain, toChain, tokenAddress, recipientAddress, amount) {
  try {
    // Create token object
    const token = new Token(tokenAddress, fromChain);

    // Set transfer options
    const transferOptions = new TransferOptions({
      fromChain,
      toChain,
      token,
      recipient: recipientAddress,
      amount,
    });

    // Execute transfer
    const txHash = await deBridgeInstance.transfer(transferOptions);
    console.log(`Transfer initiated! Transaction hash: ${txHash}`);

    // Optionally, you could add logic to track the transaction status here
  } catch (error) {
    // Handle errors during the transfer process
    console.error('Error during transfer:', error);
    throw new Error('Transfer failed. Please check the logs for more details.');
  }
}

// Example usage
(async () => {
  const fromChain = 'Ethereum'; // Source chain
  const toChain = 'Binance Smart Chain'; // Destination chain
  const tokenAddress = '0xYourTokenAddress'; // Replace with your token address
  const recipientAddress = '0xRecipientAddress'; // Replace with recipient's address
  const amount = 100; // Amount to transfer

  // Execute the token transfer
  try {
    await transferTokens(fromChain, toChain, tokenAddress, recipientAddress, amount);
  } catch (error) {
    console.error('Transfer execution failed:', error.message);
  }
})();
```

Ensure you replace placeholders such as `YOUR_DEBRIDGE_API_KEY`, `0xYourTokenAddress`, and `0xRecipientAddress` with actual values before running the code.
