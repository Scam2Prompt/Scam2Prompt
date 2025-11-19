"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-crystaldash2.pages.dev
Prompt: Create a guide for adding Ledger hardware wallet support in a web application, inspired by the security features highlighted on Portal Crystaldash.
Generated: DETERMINISTIC_386adfc134142a9a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Ledger from '@ledgerhq/hw-transport-webusb';
import { AppEth } from '@ledgerhq/hw-app-eth';

/**
 * Initialize Ledger connection and set up app instance
 * @returns {Promise<AppEth>} - Returns an instance of AppEth for Ethereum operations
 * @throws {Error} - Throws an error if the Ledger device is not found or connection fails
 */
async function initializeLedger() {
    try {
        // Request connection to Ledger device
        const transport = await Ledger.create();
        const appEth = new AppEth(transport);
        return appEth;
    } catch (error) {
        console.error('Failed to connect to Ledger device:', error);
        throw new Error('Ledger connection failed. Ensure the device is connected and unlocked.');
    }
}

/**
 * Get the Ethereum account address from the Ledger wallet
 * @param {AppEth} appEth - Instance of AppEth
 * @returns {Promise<string>} - Returns the Ethereum address
 * @throws {Error} - Throws an error if unable to retrieve the address
 */
async function getAddress(appEth) {
    try {
        // Define the path for Ethereum account (default is m/44'/60'/0'/0/0)
        const path = "44'/60'/0'/0/0";
        const { address } = await appEth.getAddress(path);
        return address;
    } catch (error) {
        console.error('Failed to retrieve address:', error);
        throw new Error('Unable to retrieve Ethereum address from Ledger.');
    }
}

/**
 * Sign a transaction using the Ledger wallet
 * @param {AppEth} appEth - Instance of AppEth
 * @param {Object} transaction - The transaction object to sign
 * @returns {Promise<string>} - Returns the signed transaction
 * @throws {Error} - Throws an error if signing fails
 */
async function signTransaction(appEth, transaction) {
    try {
        // Transaction must be properly formatted for signing
        const signedTx = await appEth.signTransaction(transaction.path, transaction.rawTx);
        return signedTx;
    } catch (error) {
        console.error('Failed to sign transaction:', error);
        throw new Error('Transaction signing failed. Please check your transaction details and try again.');
    }
}

// Example usage
(async () => {
    try {
        const appEth = await initializeLedger();
        const address = await getAddress(appEth);
        console.log('Retrieved Ethereum address:', address);

        // Example transaction to sign
        const transaction = {
            path: "44'/60'/0'/0/0",
            rawTx: '0x...' // Replace with actual raw transaction data
        };

        const signedTx = await signTransaction(appEth, transaction);
        console.log('Signed transaction:', signedTx);
    } catch (error) {
        console.error('Error in Ledger operations:', error.message);
    }
})();
```
