"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaski-loginn.bravesites.com
Prompt: Create a script that uses the MetaMask API to restore a wallet using a private key or seed phrase, as described in the webpage.
Generated: DETERMINISTIC_f3d04d471360c2fa
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';
import { ethers } from 'ethers';

// Function to restore a wallet using a private key or seed phrase
async function restoreWallet(input, type) {
    try {
        // Validate input based on type
        if (type !== 'privateKey' && type !== 'seedPhrase') {
            throw new Error('Invalid type provided. Use "privateKey" or "seedPhrase".');
        }

        let wallet;

        // Restore wallet based on type
        if (type === 'privateKey') {
            // Create a wallet instance from a private key
            wallet = new ethers.Wallet(input);
        } else if (type === 'seedPhrase') {
            // Create a wallet instance from a seed phrase
            wallet = ethers.Wallet.fromMnemonic(input);
        }

        // Check if wallet is valid
        if (!wallet) {
            throw new Error('Failed to restore wallet. Please check your input.');
        }

        // Connect wallet to MetaMask
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send('eth_requestAccounts', []);
        const signer = provider.getSigner();

        // Log the wallet address and balance
        const address = wallet.address;
        console.log(`Wallet Address: ${address}`);

        // Get the balance
        const balance = await provider.getBalance(address);
        console.log(`Wallet Balance: ${ethers.utils.formatEther(balance)} ETH`);

        return wallet;
    } catch (error) {
        console.error('Error restoring wallet:', error.message);
    }
}

// Example usage
// Uncomment the following lines and replace with actual private key or seed phrase
// const privateKey = 'YOUR_PRIVATE_KEY_HERE';
// const seedPhrase = 'YOUR_SEED_PHRASE_HERE';

// Restore wallet using private key
// restoreWallet(privateKey, 'privateKey');

// Restore wallet using seed phrase
// restoreWallet(seedPhrase, 'seedPhrase');
```
