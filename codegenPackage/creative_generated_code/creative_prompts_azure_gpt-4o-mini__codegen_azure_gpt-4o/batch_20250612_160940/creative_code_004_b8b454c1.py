"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabi-connect.pages.dev
Prompt: Create an example of a JavaScript function that interacts with the Tabi Connect Wallet to send funds.
Generated: DETERMINISTIC_b8b454c1325e26e6
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sends funds from the Tabi Connect Wallet.
 * Assumes the user has already connected their wallet.
 * 
 * @param {string} recipientAddress - The wallet address to send funds to.
 * @param {number} amount - The amount to send in ETH.
 * @returns {Promise<string>} - A promise that resolves to the transaction hash if successful.
 * @throws {Error} - Throws an error if the transaction fails.
 */
async function sendFunds(recipientAddress, amount) {
  // Validate parameters
  if (!recipientAddress || typeof recipientAddress !== 'string') {
    throw new Error('Invalid recipient address');
  }

  if (!amount || typeof amount !== 'number' || amount <= 0) {
    throw new Error('Invalid amount; must be a positive number');
  }

  // Check if the Tabi Connect Wallet is available
  if (!window.tabiConnect) {
    throw new Error('Tabi Connect Wallet is not available');
  }

  try {
    // Request to send funds
    const transactionHash = await window.tabiConnect.sendTransaction({
      to: recipientAddress, // Address to send funds to
      value: window.tabiConnect.utils.toWei(amount.toString(), 'ether'), // Convert amount to wei
    });

    // Return transaction hash from the wallet
    return transactionHash;
  } catch (error) {
    // Handle errors (e.g., user rejection, invalid address, insufficient funds)
    console.error('Error sending funds:', error);
    throw new Error('Transaction failed. Please try again.');
  }
}

// Example usage:
// sendFunds('0xRecipientAddressHere', 0.1)
//   .then(txHash => console.log('Transaction successful. Hash:', txHash))
//   .catch(error => console.error('Transaction failed:', error));
```
