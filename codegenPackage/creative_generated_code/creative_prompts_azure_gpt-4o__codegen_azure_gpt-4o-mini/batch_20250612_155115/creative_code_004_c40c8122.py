"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-finac.xyz
Prompt: Implement a JavaScript function to perform an Ethereum transaction, including validation of input values and handling errors, based on the `performTransaction` function described on the webpage.
Generated: DETERMINISTIC_c40c812214922f7b
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Performs an Ethereum transaction.
 * @param {string} fromAddress - The sender's Ethereum address.
 * @param {string} toAddress - The recipient's Ethereum address.
 * @param {number} amount - The amount of Ether to send (in Wei).
 * @param {string} privateKey - The private key of the sender's wallet.
 * @returns {Promise<string>} - A promise that resolves to the transaction hash.
 * @throws {Error} Throws an error if input validation fails or transaction fails.
 */
async function performTransaction(fromAddress, toAddress, amount, privateKey) {
    // Validate input values
    if (!isValidEthereumAddress(fromAddress)) {
        throw new Error('Invalid sender address.');
    }
    if (!isValidEthereumAddress(toAddress)) {
        throw new Error('Invalid recipient address.');
    }
    if (amount <= 0) {
        throw new Error('Amount must be greater than zero.');
    }
    if (!isValidPrivateKey(privateKey)) {
        throw new Error('Invalid private key.');
    }

    // Load the Ethereum provider
    const provider = new ethers.providers.InfuraProvider('mainnet', 'YOUR_INFURA_PROJECT_ID');
    
    // Create a wallet instance
    const wallet = new ethers.Wallet(privateKey, provider);

    try {
        // Create and send the transaction
        const tx = {
            to: toAddress,
            value: ethers.utils.parseEther(amount.toString()), // Convert amount to Wei
            gasLimit: ethers.utils.hexlify(21000), // Standard gas limit for simple ETH transfer
        };

        const transactionResponse = await wallet.sendTransaction(tx);

        // Wait for the transaction to be mined
        await transactionResponse.wait();

        // Return the transaction hash
        return transactionResponse.hash;

    } catch (error) {
        // Handle errors during transaction
        throw new Error(`Transaction failed: ${error.message}`);
    }
}

/**
 * Validates an Ethereum address.
 * @param {string} address - The Ethereum address to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
function isValidEthereumAddress(address) {
    return ethers.utils.isAddress(address);
}

/**
 * Validates an Ethereum private key.
 * @param {string} privateKey - The private key to validate.
 * @returns {boolean} - True if valid, false otherwise.
 */
function isValidPrivateKey(privateKey) {
    return /^0x[a-fA-F0-9]{64}$/.test(privateKey);
}
```

**Note:** Replace `'YOUR_INFURA_PROJECT_ID'` with your actual Infura project ID for the code to function correctly. Make sure to install the `ethers` library using `npm install ethers` before running the code.
