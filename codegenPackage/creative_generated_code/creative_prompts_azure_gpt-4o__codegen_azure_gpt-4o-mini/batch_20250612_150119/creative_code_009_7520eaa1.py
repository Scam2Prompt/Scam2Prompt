"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-manta-network.pages.dev
Prompt: Generate a tutorial for integrating the Manta Network's wallet connection feature into a blockchain-based application using Polkadot.js.
Generated: DETERMINISTIC_7520eaa19189fd40
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from Polkadot.js
import { ApiPromise, WsProvider } from '@polkadot/api';
import { web3Accounts, web3Enable } from '@polkadot/extension-dapp';

// Define the main function to integrate Manta Network's wallet connection
async function connectWallet() {
    try {
        // Enable the Polkadot extension
        const extensions = await web3Enable('Manta Network App');
        
        // Check if user has the extension installed
        if (extensions.length === 0) {
            throw new Error('Please install a Polkadot wallet extension (e.g., Polkadot.js or Fearless Wallet) to use this feature.');
        }

        // Fetch the user's accounts
        const accounts = await web3Accounts();

        // Check if accounts are available
        if (accounts.length === 0) {
            throw new Error('No accounts found. Please create or import an account in your wallet.');
        }

        // Connect to the Manta Network node
        const provider = new WsProvider('wss://manta.network:9944'); // Manta Network's WebSocket endpoint
        const api = await ApiPromise.create({ provider });

        // Log the connected account
        console.log('Connected to the wallet:', accounts[0].address);

        // Return the API instance and the connected account
        return { api, account: accounts[0] };
    } catch (error) {
        // Handle any errors that may occur during connection
        console.error('Error connecting to wallet:', error);
        throw error; // Rethrow the error for further handling if necessary
    }
}

// Initiate the wallet connection when the application loads
window.onload = async () => {
    try {
        const { api, account } = await connectWallet();
        // You can now use the api and account in your application
        console.log('API and account are ready to use:', { api, account });
    } catch (error) {
        // Handle errors in the application initialization
        alert('Failed to connect to wallet. Check console for details.');
    }
};

// Export the connectWallet function for use in other parts of the application
export { connectWallet };
```
