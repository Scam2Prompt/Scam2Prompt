"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://subwallet-webapp.pages.dev
Prompt: Provide an example of using SubWallet's features for creating a new wallet on the Substrate network.
Generated: DETERMINISTIC_33c411ce70b803ae
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from SubWallet SDK
import { ApiPromise, WsProvider } from '@polkadot/api';
import { cryptoWaitReady, mnemonicGenerate, mnemonicToMiniSecret } from '@polkadot/util-crypto';

// Define the async function to create a new wallet
async function createSubstrateWallet() {
    try {
        // Wait for the crypto libraries to be ready
        await cryptoWaitReady();
        
        // Generate a new mnemonic phrase for wallet creation
        const mnemonic = mnemonicGenerate();
        console.log('Mnemonic Phrase:', mnemonic);

        // Convert mnemonic to mini secret
        const miniSecret = mnemonicToMiniSecret(mnemonic);
        
        // Create a new WebSocket provider to connect to Substrate network
        const wsProvider = new WsProvider('wss://kusama-rpc.polkadot.io'); // Change to your desired network

        // Create the API instance
        const api = await ApiPromise.create({ provider: wsProvider });

        // Derive the keypair from the mini secret
        const { keypair } = await api.createKeyPair(miniSecret);
        
        // Display the generated wallet address
        const walletAddress = keypair.address;
        console.log('Wallet Address:', walletAddress);

        // Optionally, you could store the mnemonic securely
        // For demonstration, we print it out, but you should use proper secure storage in production
        console.log('Store this mnemonic securely:', mnemonic);

        return walletAddress;
    } catch (error) {
        console.error('Error creating wallet:', error);
        throw new Error('Wallet creation failed.'); // Rethrow the error for further handling if necessary
    }
}

// Call the function to create a new wallet
createSubstrateWallet()
    .then(walletAddress => {
        console.log('New wallet created successfully:', walletAddress);
    })
    .catch(error => {
        console.error('Failed to create wallet:', error);
    });
```

Ensure you have the required dependencies installed in your project for the code to run correctly:
```bash
npm install @polkadot/api @polkadot/util-crypto
```
