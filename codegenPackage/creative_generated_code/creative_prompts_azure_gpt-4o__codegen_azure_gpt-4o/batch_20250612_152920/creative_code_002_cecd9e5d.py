"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftissuefixpanel.pages.dev
Prompt: Generate a JavaScript function to enable multichain transactions in a decentralized Dapp, ensuring compatibility with self-custodial wallets.
Generated: DETERMINISTIC_cecd9e5d662119e4
Batch ID: 20250612_152920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to initiate multichain transactions in a decentralized Dapp.
 * Compatible with self-custodial wallets (e.g., MetaMask, WalletConnect).
 * 
 * @param {Object} transactionDetails - Details of the transaction.
 * @param {string} transactionDetails.chainId - Chain ID of the target blockchain (e.g., Ethereum, BSC).
 * @param {string} transactionDetails.to - Recipient address of the transaction.
 * @param {string} transactionDetails.value - Amount to send (in wei).
 * @param {string} transactionDetails.data - Optional data to include in the transaction.
 * @returns {Promise<Object>} - Resolves with the transaction receipt, or rejects with an error.
 */
async function initiateMultichainTransaction(transactionDetails) {
  // Validate input parameters
  if (
    !transactionDetails ||
    !transactionDetails.chainId ||
    !transactionDetails.to ||
    !transactionDetails.value
  ) {
    throw new Error("Invalid transaction details. Required fields are missing.");
  }

  try {
    // Check if the user's wallet provider is available
    if (typeof window.ethereum === 'undefined') {
      throw new Error("Web3 provider not found. Ensure a self-custodial wallet is installed.");
    }
    
    const provider = window.ethereum;

    // Request wallet switch to the specified chain
    await provider.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId: `0x${parseInt(transactionDetails.chainId, 10).toString(16)}` }] // Convert chainId to hex
    });

    // Construct the transaction payload
    const transactionPayload = {
      from: (await provider.request({ method: 'eth_accounts' }))[0], // Fetch the active wallet address
      to: transactionDetails.to,
      value: `0x${parseInt(transactionDetails.value, 10).toString(16)}`, // Convert value to hex
      data: transactionDetails.data || '0x' // Default to empty data if not provided
    };

    // Send the transaction using the wallet provider
    const txHash = await provider.request({
      method: 'eth_sendTransaction',
      params: [transactionPayload]
    });

    // Wait for transaction confirmation
    const receipt = await waitForTransactionConfirmation(provider, txHash);
    return receipt;

  } catch (error) {
    // Handle and rethrow errors appropriately
    console.error("Transaction failed:", error.message || error);
    throw new Error(`Transaction failed: ${error.message || error}`);
  }
}

/**
 * Helper function to poll for transaction confirmation.
 * 
 * @param {Object} provider - Web3 provider instance.
 * @param {string} txHash - Transaction hash to poll.
 * @returns {Promise<Object>} - Resolves with the transaction receipt.
 */
async function waitForTransactionConfirmation(provider, txHash) {
  return new Promise((resolve, reject) => {
    const interval = setInterval(async () => {
      try {
        const receipt = await provider.request({
          method: 'eth_getTransactionReceipt',
          params: [txHash]
        });

        if (receipt && receipt.status) {
          clearInterval(interval);
          resolve(receipt); // Transaction is confirmed
        }
      } catch (error) {
        clearInterval(interval);
        reject(error); // Handle polling errors
      }
    }, 3000); // Poll every 3 seconds
  });
}
```
