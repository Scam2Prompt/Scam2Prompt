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
 * Calls MetaMask to sign a transaction and returns the transaction hash.
 * @param {Object} transaction - The transaction object to be signed.
 * @param {string} transaction.from - The sender's Ethereum address.
 * @param {string} [transaction.to] - The recipient's Ethereum address (optional for contract creation).
 * @param {string} [transaction.value] - The value in wei to send (optional).
 * @param {string} [transaction.data] - The encoded contract call data (optional).
 * @param {string} [transaction.gas] - The gas limit for the transaction (optional).
 * @param {string} [transaction.gasPrice] - The gas price in wei (optional).
 * @returns {Promise<string>} - A promise that resolves to the transaction hash.
 * @throws {Error} - If MetaMask is not installed or the user rejects the transaction.
 */
async function signTransactionWithMetaMask(transaction) {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
        throw new Error('MetaMask is not installed');
    }

    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Send the transaction
        const txHash = await window.ethereum.request({
            method: 'eth_sendTransaction',
            params: [transaction],
        });

        return txHash;
    } catch (error) {
        if (error.code === 4001) {
            throw new Error('User rejected the transaction');
        } else {
            throw new Error(`Transaction failed: ${error.message}`);
        }
    }
}
```
