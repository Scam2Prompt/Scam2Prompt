"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Write a function in JavaScript to call the MetaMask wallet app for signing a transaction and returning the transaction hash, as described in the "调用MetaMask钱包App" section.
Generated: DETERMINISTIC_41f6f039a250410b
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to request MetaMask to sign a transaction and return the transaction hash.
 * @param {Object} transactionDetails - The transaction details to be signed.
 * @returns {Promise<string>} - A promise that resolves to the transaction hash.
 */
async function signTransactionWithMetaMask(transactionDetails) {
  // Ensure MetaMask is installed by checking if ethereum is available in the window object.
  if (typeof window.ethereum === 'undefined') {
    throw new Error('MetaMask is not installed. Please install MetaMask to proceed.');
  }

  try {
    // Request the user to connect their MetaMask wallet.
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    if (accounts.length === 0) {
      throw new Error('No accounts found. Please ensure MetaMask is logged in.');
    }

    // Construct the transaction request object.
    const transactionRequest = {
      from: accounts[0], // Use the first account returned by MetaMask.
      ...transactionDetails, // Spread the transactionDetails to include other necessary fields like to, value, etc.
    };

    // Request MetaMask to sign and send the transaction.
    const txHash = await window.ethereum.request({
      method: 'eth_sendTransaction',
      params: [transactionRequest],
    });

    // Return the transaction hash.
    return txHash;
  } catch (error) {
    // Handle any errors that occur during the process.
    console.error('An error occurred while signing the transaction:', error);
    throw new Error(`Failed to sign transaction: ${error.message}`);
  }
}

// Example usage:
// (Uncomment below to test the function in a browser with MetaMask installed)
// const transactionDetails = {
//   to: '0xRecipientAddressHere',
//   value: '0xAmountInWeiHere',
//   gas: '0xGasLimitHere',
// };
// signTransactionWithMetaMask(transactionDetails)
//   .then((txHash) => console.log('Transaction Hash:', txHash))
//   .catch((error) => console.error(error));

```
