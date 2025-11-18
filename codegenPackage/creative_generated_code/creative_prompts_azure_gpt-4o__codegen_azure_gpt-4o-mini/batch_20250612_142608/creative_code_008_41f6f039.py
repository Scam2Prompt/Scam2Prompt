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
 * @param {string} to - The address of the recipient.
 * @param {number} value - The amount of Ether to send (in Wei).
 * @param {string} gasPrice - The gas price for the transaction (in Wei).
 * @param {number} gasLimit - The gas limit for the transaction.
 * @returns {Promise<string>} - A promise that resolves to the transaction hash.
 * @throws {Error} - Throws an error if the transaction fails or MetaMask is not installed.
 */
async function sendTransaction(to, value, gasPrice, gasLimit) {
    // Check if MetaMask is installed
    if (!window.ethereum) {
        throw new Error('MetaMask is not installed. Please install it to use this feature.');
    }

    // Request account access if needed
    await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Prepare transaction parameters
    const transactionParameters = {
        to: to, // Required: address of the recipient
        from: window.ethereum.selectedAddress, // Required: active address of the user
        value: value.toString(16), // Required: amount in Wei (hexadecimal format)
        gasPrice: gasPrice.toString(16), // Optional: gas price in Wei (hexadecimal format)
        gas: gasLimit.toString(16), // Optional: gas limit (hexadecimal format)
    };

    try {
        // Send the transaction using MetaMask
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transactionParameters],
        });
        return txHash; // Return the transaction hash
    } catch (error) {
        // Handle errors from MetaMask
        throw new Error(`Transaction failed: ${error.message}`);
    }
}

// Example usage of the sendTransaction function
(async () => {
    try {
        const txHash = await sendTransaction('0xRecipientAddress', 1000000000000000000, 20000000000, 21000);
        console.log(`Transaction successful with hash: ${txHash}`);
    } catch (error) {
        console.error(error.message);
    }
})();
```
