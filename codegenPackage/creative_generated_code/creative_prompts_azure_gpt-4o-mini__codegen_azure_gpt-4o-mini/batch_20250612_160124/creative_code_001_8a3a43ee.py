"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: What are the steps to enable JavaScript for using Web3Modal in a DApp?
Generated: DETERMINISTIC_8a3a43ee7ed6e804
Batch ID: 20250612_160124
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider } from '@web3-react/core';
import Web3Modal from 'web3modal';

// Initialize the Web3 provider to be used within the application
const getLibrary = (provider) => {
    const library = new Web3(provider);
    library.pollingInterval = 12000; // Set polling interval for updates
    return library;
};

// Create a new instance of Web3Modal
const web3Modal = new Web3Modal({
    cacheProvider: true, // Optional: cache provider to allow automatic connection
    providerOptions: { // Configure wallet options
        walletconnect: {
            package: WalletConnectProvider, // Required
            options: {
                infuraId: "YOUR_INFURA_ID" // Required: Replace with your Infura Project ID
            }
        },
        // Add other wallet options as needed
    }
});

// Function to connect to the selected wallet
const connectWallet = async () => {
    try {
        // Open the wallet modal for user to select a wallet
        const provider = await web3Modal.connect();
        
        // Creating a new instance of Web3 with the selected provider
        const web3 = new Web3(provider);
        
        // Optional: Subscribe to accounts change and network change
        provider.on("accountsChanged", (accounts) => {
            console.log('Accounts changed:', accounts);
        });

        provider.on("chainChanged", (chainId) => {
            console.log('Chain changed:', chainId);
        });

        provider.on("disconnect", (error) => {
            console.log('Disconnected:', error);
        });

        // Return the web3 instance for further use
        return web3;
    } catch (error) {
        console.error('Error connecting to wallet:', error);
        throw new Error('Wallet connection failed'); // Handle connection errors
    }
};

// Initialize the Web3ReactProvider to manage wallet connections
const App = () => {
    return (
        <Web3ReactProvider getLibrary={getLibrary}>
            <div>
                <h1>Connect Your Wallet</h1>
                <button onClick={connectWallet}>Connect Wallet</button>
            </div>
        </Web3ReactProvider>
    );
};

// Export the App component as the main entry point
export default App;
```
