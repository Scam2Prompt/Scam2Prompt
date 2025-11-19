"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadot.org
Prompt: Can you provide a code example for creating a decentralized application (DApp) on the Polkadot network?
Generated: DETERMINISTIC_35f6ca6a24ebc728
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ApiPromise, WsProvider } = require('@polkadot/api');

// Define the main function to run the DApp
async function runDApp() {
    // Connect to the Polkadot network via WebSocket
    const wsProvider = new WsProvider('wss://rpc.polkadot.io');
    const api = await ApiPromise.create({ provider: wsProvider });

    // Check the connection to the network
    console.log('Connected to Polkadot network.');

    try {
        // Retrieve the latest block number
        const latestBlock = await api.derive.chain.bestNumber();
        console.log(`Latest block number: ${latestBlock.toString()}`);

        // Example: Fetch the balances of a specific account
        const accountAddress = 'YOUR_ACCOUNT_ADDRESS_HERE'; // Replace with a valid Polkadot address
        const { data: { free: freeBalance } } = await api.query.system.account(accountAddress);
        console.log(`Free balance for ${accountAddress}: ${freeBalance.toHuman()}`);

        // Example: Send a transaction (ensure you have the appropriate keypair)
        const keyring = require('@polkadot/keyring');
        const keyringInstance = new keyring.Keyring({ type: 'sr25519' });
        
        const sender = keyringInstance.addFromUri('YOUR_MNEMONIC_HERE'); // Replace with your mnemonic

        const transfer = api.tx.balances.transfer('RECIPIENT_ADDRESS_HERE', 1000000000); // Replace with the recipient address and amount to send

        // Sign and send the transaction
        const hash = await transfer.signAndSend(sender);
        console.log(`Transaction sent with hash: ${hash.toHex()}`);

    } catch (error) {
        console.error('Error occurred:', error); // Handle any errors that may occur during API calls or transactions
    } finally {
        // Optionally disconnect from the network
        await api.disconnect();
        console.log('Disconnected from Polkadot network.');
    }
}

// Run the DApp
runDApp().catch(console.error);
```

**Note**: Replace `YOUR_ACCOUNT_ADDRESS_HERE`, `YOUR_MNEMONIC_HERE`, and `RECIPIENT_ADDRESS_HERE` with appropriate values for your Polkadot account and recipient address. Make sure to install the necessary packages by running `npm install @polkadot/api @polkadot/keyring`.
