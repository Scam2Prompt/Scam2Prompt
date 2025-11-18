"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.com
Prompt: Write code using Reown's AppKit to integrate onchain app UX features that support scalability across 6000+ apps and 150+ chains. Include examples of connecting to multiple wallets.
Generated: DETERMINISTIC_796df09e37f8c199
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required modules from Reown's AppKit
import { AppKit } from '@reown/appkit';
import { WalletConnector } from '@reown/appkit-wallets';

// Initialize AppKit instance for scalability across 6000+ apps and 150+ chains
const app = new AppKit({
  appName: 'MyScalableOnchainApp', // Define your app name
  supportedChains: 'all', // Support all chains (150+)
  autoConnect: true, // Automatically connect to wallets on initialization
  debug: true, // Enable debugging for development; disable in production
});

// Define a method to connect to multiple wallets
async function connectWallets() {
  try {
    // Initialize WalletConnector for multi-wallet support
    const walletConnector = new WalletConnector({
      wallets: ['metaMask', 'walletConnect', 'coinbaseWallet'], // List supported wallets
      chains: 'all', // Allow connections across all chains
    });

    // Connect to all available wallets
    const connections = await walletConnector.connectAll();

    // Iterate over each wallet connection and log the connected accounts
    connections.forEach((connection) => {
      console.log(`Wallet: ${connection.walletName}`);
      console.log(`Connected Accounts: ${connection.accounts}`);
    });

    // Attach the wallet connector to the AppKit instance
    app.useWalletConnector(walletConnector);

    console.log('Successfully connected to all wallets.');
  } catch (error) {
    // Handle errors gracefully
    console.error('Error connecting to wallets:', error.message);
  }
}

// Example function showcasing a user action that interacts with the blockchain
async function performOnchainAction() {
  try {
    // Ensure the app is connected to a wallet before performing transactions
    if (!app.isConnected()) {
      throw new Error('No wallet connected. Please connect a wallet first.');
    }

    // Example: Assume we're making a transaction on a blockchain
    const tx = await app.transact({
      chainId: '1', // Example: Ethereum mainnet
      contractAddress: '0xYourContractAddressHere', // Replace with your contract address
      method: 'yourContractMethod', // Replace with the contract method
      params: { param1: 'value1', param2: 'value2' }, // Replace with method parameters
    });

    console.log('Transaction successful:', tx.transactionHash);
  } catch (error) {
    // Handle onchain interaction errors
    console.error('Error performing onchain action:', error.message);
  }
}

// Main function to bootstrap the app
async function main() {
  try {
    // Connect to wallets
    await connectWallets();

    // Perform an example onchain action
    await performOnchainAction();
  } catch (error) {
    // Handle any errors during app initialization or execution
    console.error('Error initializing app:', error.message);
  }
}

// Run the main function
main();
```
