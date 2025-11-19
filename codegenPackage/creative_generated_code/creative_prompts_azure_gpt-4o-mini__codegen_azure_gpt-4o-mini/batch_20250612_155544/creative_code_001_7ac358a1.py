"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atocha.io
Prompt: Write a code snippet to integrate the Atocha Web App with a Polkadot JS wallet for puzzle game creation.
Generated: DETERMINISTIC_7ac358a1a5a7cdd8
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { ApiPromise, WsProvider } from '@polkadot/api';
import { web3Enable, web3FromSource } from '@polkadot/extension-dapp';

const POLKADOT_NODE_URL = 'wss://rpc.polkadot.io'; // Replace with your desired Polkadot node URL

// Main function to integrate Polkadot wallet
async function integratePolkadotWallet() {
    try {
        // Connect to the Polkadot node
        const provider = new WsProvider(POLKADOT_NODE_URL);
        const api = await ApiPromise.create({ provider });

        // Enable the Polkadot wallet
        const extensions = await web3Enable('Atocha Web App');
        if (extensions.length === 0) {
            throw new Error('No Polkadot wallet extension found. Please install it.');
        }

        // Request the user's account
        const injector = await web3FromSource(extensions[0].source);
        const accounts = await injector.accounts.get();
        const { address } = accounts[0];

        console.log(`Connected to wallet address: ${address}`);

        // Create a puzzle game
        await createPuzzleGame(api, address);

    } catch (error) {
        console.error('Error integrating Polkadot wallet:', error);
    }
}

// Function to create a puzzle game on the blockchain
async function createPuzzleGame(api, creatorAddress) {
    try {
        // Example parameters for the puzzle game creation
        const puzzleData = {
            title: 'Sample Puzzle',
            description: 'This is a sample puzzle game created on Polkadot.',
            difficulty: 'medium'
        };

        // Send a transaction to create the puzzle game
        const unsub = await api.tx.puzzleModule
            .createPuzzle(puzzleData.title, puzzleData.description, puzzleData.difficulty)
            .signAndSend(creatorAddress, { signer: injector.signer }, ({ status }) => {
                if (status.isInBlock) {
                    console.log('Puzzle game created in block:', status.asInBlock.toString());
                    unsub(); // Unsubscribe from the transaction
                } else if (status.isFinalized) {
                    console.log('Transaction finalized:', status.asFinalized.toString());
                    unsub(); // Unsubscribe from the transaction
                }
            });

    } catch (error) {
        console.error('Error creating puzzle game:', error);
    }
}

// Initialize wallet integration
integratePolkadotWallet();
```

**Note:** Make sure to replace `puzzleModule` with the actual module name used in your Polkadot blockchain for creating puzzles. Ensure the necessary permissions are set in your Polkadot wallet extension for the app to interact with it.
