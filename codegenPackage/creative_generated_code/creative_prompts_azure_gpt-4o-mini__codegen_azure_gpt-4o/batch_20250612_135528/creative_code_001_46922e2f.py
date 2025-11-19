"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-multisig.vercel.app
Prompt: What are the steps to sign a transaction with Starsign using ArgentX or Braavos wallets?
Generated: DETERMINISTIC_46922e2f8c3b0739
Batch ID: 20250612_135528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, well-documented, and production-ready code for signing a transaction with Starsign using ArgentX or Braavos wallets:

```javascript
// Import necessary libraries
// Ensure you have installed starknet.js via npm or yarn before running this code
const { ec, hash, encode, defaultProvider } = require('starknet');

// Configuration for interacting with ArgentX or Braavos wallets
// Make sure you are using the correct network (e.g., testnet or mainnet)
const NETWORK = 'testnet'; // Change to 'mainnet' if needed

async function signTransactionWithWallet(walletType, transactionData) {
    try {
        // Validate the input
        if (!['ArgentX', 'Braavos'].includes(walletType)) {
            throw new Error('Invalid wallet type. Supported wallets: ArgentX, Braavos.');
        }

        if (!transactionData || typeof transactionData !== 'object') {
            throw new Error('Invalid transaction data. Must provide an object with transaction details.');
        }

        // Initialize wallet connection
        // For ArgentX and Braavos, the wallet injects a provider into the browser's window object
        const walletProvider = window.starknet;
        if (!walletProvider) {
            throw new Error(`${walletType} wallet not detected. Ensure it is installed and enabled.`);
        }

        // Enable the wallet (trigger the wallet connection dialog if not already connected)
        await walletProvider.enable({ network: NETWORK });

        // Get account details
        const account = walletProvider.account;
        if (!account) {
            throw new Error('Failed to retrieve account details from the wallet.');
        }

        // Construct the transaction payload
        const { to, method, parameters } = transactionData;
        if (!to || !method || !Array.isArray(parameters)) {
            throw new Error('Transaction data must include "to", "method", and "parameters".');
        }

        // Prepare the transaction invocation
        const invocation = {
            contractAddress: to,
            entrypoint: method,
            calldata: parameters,
        };

        // Sign the transaction using the connected wallet
        const signature = await walletProvider.signTransaction(invocation);

        // Verify the signature
        if (!signature || signature.length === 0) {
            throw new Error('Failed to sign the transaction.');
        }

        // Optionally: Submit the signed transaction to the StarkNet network
        const response = await account.execute(invocation);

        // Return the transaction response
        return {
            status: 'success',
            message: 'Transaction signed and submitted successfully.',
            transactionHash: response.transaction_hash,
        };
    } catch (error) {
        // Handle any errors that occur during the process
        console.error('Error signing transaction:', error.message);
        return {
            status: 'error',
            message: error.message,
        };
    }
}

// Example usage
(async () => {
    const walletType = 'ArgentX'; // Or 'Braavos'
    const transactionData = {
        to: '0x0123456789abcdef', // Target contract address
        method: 'transfer', // Example method name
        parameters: ['0x0987654321abcdef', '100'], // Example parameters
    };

    const result = await signTransactionWithWallet(walletType, transactionData);
    console.log(result); // Print the result
})();
```

_Key Notes:_
- Replace the `NETWORK` variable with your desired network (e.g., 'mainnet' or 'testnet').
- Ensure the `transactionData` matches the specific contract and method you're interacting with.
- Install any required dependencies, such as `starknet.js`, using `npm install starknet`.
