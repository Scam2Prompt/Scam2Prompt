"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockappsnode.com
Prompt: What are the best practices for implementing self-custodial features in a Web3 application?
Generated: DETERMINISTIC_f19f61907033db07
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Self-Custodial Features Implementation for a Web3 Application
 * This code demonstrates best practices for implementing self-custodial features, 
 * including wallet creation, private key handling, and transaction signing.
 */

const crypto = require('crypto'); // For generating secure randomness
const ethers = require('ethers'); // Popular Web3 library to interact with blockchain

/**
 * Generate a new self-custodial wallet
 * @returns {Object} Wallet object containing address and private key
 */
function createWallet() {
    try {
        // Create a new wallet using ethers.js
        const wallet = ethers.Wallet.createRandom();

        // Return wallet details (address and private key)
        return {
            address: wallet.address,
            privateKey: wallet.privateKey
        };
    } catch (error) {
        console.error('Error generating wallet:', error.message);
        throw new Error('Failed to generate wallet.');
    }
}

/**
 * Encrypt private key securely for storage
 * @param {string} privateKey - The private key to encrypt
 * @param {string} password - Password for encryption
 * @returns {string} Encrypted private key
 */
function encryptPrivateKey(privateKey, password) {
    try {
        // Use ethers.js to encrypt private key with a password
        const encryptedJSON = ethers.Wallet.fromPrivateKey(privateKey).encrypt(password);

        // Return encrypted private key JSON
        return encryptedJSON;
    } catch (error) {
        console.error('Error encrypting private key:', error.message);
        throw new Error('Failed to encrypt private key.');
    }
}

/**
 * Decrypt encrypted private key
 * @param {string} encryptedJSON - The encrypted private key JSON
 * @param {string} password - Password used during encryption
 * @returns {string} Decrypted private key
 */
async function decryptPrivateKey(encryptedJSON, password) {
    try {
        // Decrypt using ethers.js
        const wallet = await ethers.Wallet.fromEncryptedJson(encryptedJSON, password);

        // Return decrypted private key
        return wallet.privateKey;
    } catch (error) {
        console.error('Error decrypting private key:', error.message);
        throw new Error('Failed to decrypt private key.');
    }
}

/**
 * Sign a transaction using a private key
 * @param {Object} transaction - Transaction object to sign
 * @param {string} privateKey - Private key of the signer
 * @returns {string} Signed transaction
 */
function signTransaction(transaction, privateKey) {
    try {
        const wallet = new ethers.Wallet(privateKey);

        // Sign the transaction
        const signedTx = wallet.signTransaction(transaction);

        return signedTx;
    } catch (error) {
        console.error('Error signing transaction:', error.message);
        throw new Error('Failed to sign transaction.');
    }
}

/**
 * Example usage
 */
(async () => {
    try {
        // Step 1: Create a new wallet
        const wallet = createWallet();
        console.log('Wallet Address:', wallet.address);
        console.log('Private Key:', wallet.privateKey);

        // Step 2: Encrypt the private key for secure storage
        const password = 'your-secure-password';
        const encryptedKey = await encryptPrivateKey(wallet.privateKey, password);
        console.log('Encrypted Private Key:', encryptedKey);

        // Step 3: Decrypt the private key when needed
        const decryptedKey = await decryptPrivateKey(encryptedKey, password);
        console.log('Decrypted Private Key:', decryptedKey);

        // Step 4: Sign a transaction (example transaction object)
        const exampleTransaction = {
            to: '0xReceiverAddressHere',
            value: ethers.utils.parseEther('0.01'),
            gasLimit: 21000,
            gasPrice: ethers.utils.parseUnits('50', 'gwei'),
            nonce: 0,
            chainId: 1
        };
        const signedTx = await signTransaction(exampleTransaction, decryptedKey);
        console.log('Signed Transaction:', signedTx);
    } catch (error) {
        console.error('Error in self-custodial process:', error.message);
    }
})();
```
