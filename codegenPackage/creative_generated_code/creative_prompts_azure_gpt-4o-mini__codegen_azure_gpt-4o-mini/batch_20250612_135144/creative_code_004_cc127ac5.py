"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disperse-starknet.vercel.app
Prompt: Explain the process of connecting a wallet with the Disperse Starknet GitHub documentation.
Generated: DETERMINISTIC_cc127ac5247615d6
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Wallet, Provider, Contract } from 'starknet';

// Define constants
const DISPERSE_CONTRACT_ADDRESS = '0xYourDisperseContractAddress'; // Replace with the actual contract address
const INFURA_PROJECT_ID = 'YourInfuraProjectID'; // Replace with your Infura project ID

/**
 * Connects to a Starknet wallet and initializes the Disperse contract.
 */
async function connectWallet() {
    try {
        // Check if wallet provider is available
        if (!window.starknet) {
            throw new Error('Starknet wallet not found. Please install a wallet like Argent or Braavos.');
        }

        // Request wallet connection
        const accounts = await window.starknet.enable();
        const address = accounts[0];

        console.log(`Wallet connected: ${address}`);

        // Initialize provider with Infura
        const provider = new Provider({
            network: 'goerli', // or other networks as needed
            infura: INFURA_PROJECT_ID,
        });

        // Initialize contract
        const disperseContract = new Contract(DISPERSE_CONTRACT_ADDRESS, provider);

        console.log('Disperse contract initialized.');

        return { address, disperseContract };

    } catch (error) {
        console.error('Error connecting wallet or initializing contract:', error);
        alert(error.message); // Alert the user in case of an error
    }
}

// Example usage
connectWallet().then(({ address, disperseContract }) => {
    if (address) {
        console.log(`Successfully connected to wallet: ${address}`);
        // Further interaction with the disperseContract can be done here
    }
});
```
