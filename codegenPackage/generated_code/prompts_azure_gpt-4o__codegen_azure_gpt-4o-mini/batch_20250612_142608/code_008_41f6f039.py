"""
Generated Code Metadata:
========================
Original URL: https://wap.xushuishiwu.cn
Prompt: Write a function in JavaScript to call the MetaMask wallet app for signing a transaction and returning the transaction hash, as described in the "调用MetaMask钱包App" section.
Generated: DETERMINISTIC_41f6f039a250410b
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to request MetaMask to sign a transaction and return the transaction hash.
 * 
 * @param {string} to - The address to send the transaction to.
 * @param {string} value - The amount of Ether to send (in Wei).
 * @param {string} gas - The gas limit for the transaction.
 * @param {string} gasPrice - The gas price for the transaction (in Wei).
 * @returns {Promise<string>} - A promise that resolves to the transaction hash.
 * @throws {Error} - Throws an error if MetaMask is not installed or if the transaction fails.
 */
async function signTransaction(to, value, gas, gasPrice) {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error('MetaMask is not installed. Please install it to use this feature.');
    }

    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Prepare the transaction parameters
    const transactionParameters = {
        to: to, // Required: address to send the transaction to
        from: window.ethereum.selectedAddress, // Required: the user's selected address
        value: value, // Required: the amount to send in Wei
        gas: gas, // Optional: the gas limit
        gasPrice: gasPrice // Optional: the gas price in Wei
    };

    try {
        // Send the transaction and wait for the transaction hash
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });

        return txHash; // Return the transaction hash
    } catch (error) {
        // Handle errors that occur during the transaction
        throw new Error(`Transaction failed: ${error.message}`);
    }
}

// Example usage (uncomment to use):
// signTransaction('0xRecipientAddress', '1000000000000000000', '21000', '20000000000')
//     .then(txHash => console.log('Transaction Hash:', txHash))
//     .catch(error => console.error('Error:', error));
```
