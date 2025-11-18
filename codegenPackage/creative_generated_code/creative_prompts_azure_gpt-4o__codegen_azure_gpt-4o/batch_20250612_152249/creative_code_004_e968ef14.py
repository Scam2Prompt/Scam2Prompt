"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petoshi-dashboard.pages.dev
Prompt: Write a function to send a transaction using the Petoshi dashboard's "Send transaction" feature, ensuring compatibility with the `eth_signTypedData_v4` method.
Generated: DETERMINISTIC_e968ef145ae5dc58
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Sends a transaction using the Petoshi dashboard's "Send transaction" feature,
 * leveraging the `eth_signTypedData_v4` method for signing the transaction.
 * 
 * @param {Object} web3 - Web3 instance connected to the blockchain network.
 * @param {string} fromAddress - The address of the sender.
 * @param {string} toAddress - The address of the recipient.
 * @param {number} value - The amount of tokens (in wei) to send.
 * @param {string} privateKey - The sender's private key for manual signing (fallback method).
 * @returns {Promise<string>} Transaction hash on successful submission.
 */
async function sendTransaction(web3, fromAddress, toAddress, value, privateKey) {
    try {
        // Define the EIP-712 typed data structure
        const domain = {
            name: 'Petoshi',
            version: '1',
            chainId: await web3.eth.getChainId(),
            verifyingContract: '0xYourContractAddressHere' // Replace with actual contract address
        };
        
        const types = {
            Transaction: [
                { name: 'from', type: 'address' },
                { name: 'to', type: 'address' },
                { name: 'value', type: 'uint256' }
            ]
        };

        const message = {
            from: fromAddress,
            to: toAddress,
            value: value
        };

        // Prepare the typed data for signing
        const typedData = {
            domain,
            types,
            primaryType: 'Transaction',
            message
        };

        // Attempt to sign using eth_signTypedData_v4
        const signature = await web3.currentProvider.send({
            method: 'eth_signTypedData_v4',
            params: [fromAddress, JSON.stringify(typedData)],
            from: fromAddress
        });

        console.log(`Signature: ${signature.result}`);

        // Prepare the raw transaction object
        const tx = {
            from: fromAddress,
            to: toAddress,
            value: value,
            data: '0x', // Optional data payload
            gas: await web3.eth.estimateGas({ from: fromAddress, to: toAddress, value }),
            nonce: await web3.eth.getTransactionCount(fromAddress, 'latest')
        };

        // Sign the transaction manually as fallback, if signing fails
        const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);

        // Send the transaction to the network
        const txReceipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);

        console.log(`Transaction successful with hash: ${txReceipt.transactionHash}`);
        return txReceipt.transactionHash;
    } catch (error) {
        // Handle errors appropriately
        console.error('Error sending transaction:', error);
        throw new Error(`Transaction failed: ${error.message}`);
    }
}
```
