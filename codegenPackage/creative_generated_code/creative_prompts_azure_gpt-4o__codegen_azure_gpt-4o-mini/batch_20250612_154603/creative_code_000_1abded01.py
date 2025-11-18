"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodechainreset.com
Prompt: Write code to create a decentralized application (Dapp) with self-custodial wallet integration and multichain support, referencing tools or libraries commonly used in Web3 development.
Generated: DETERMINISTIC_1abded01c728f61b
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // Web3.js library for interacting with Ethereum
import { ethers } from 'ethers'; // Ethers.js library for Ethereum wallet integration
import { InjectedConnector } from '@web3-react/injected-connector'; // Injected connector for wallet integration
import { Web3ReactProvider } from '@web3-react/core'; // React context for Web3
import { useEffect, useState } from 'react'; // React hooks for component state and lifecycle
import React from 'react'; // React library for building UI components
import './App.css'; // Custom styles for the application

// Initialize the web3 provider
function getLibrary(provider) {
    const library = new Web3(provider);
    library.pollingInterval = 12000; // Set polling interval for updates
    return library;
}

// Define the main application component
const App = () => {
    const [account, setAccount] = useState(null);
    const [provider, setProvider] = useState(null);
    const [chainId, setChainId] = useState(null);

    // Wallet connection function
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({
                    method: 'eth_requestAccounts',
                });
                setAccount(accounts[0]);
                const chainId = await window.ethereum.request({ method: 'eth_chainId' });
                setChainId(chainId);
                setProvider(new ethers.providers.Web3Provider(window.ethereum));
            } catch (error) {
                console.error("Error connecting to wallet:", error);
            }
        } else {
            alert('Please install a web3 wallet like MetaMask');
        }
    };

    // Effect to handle wallet changes
    useEffect(() => {
        if (provider) {
            provider.on("accountsChanged", (accounts) => {
                setAccount(accounts[0]);
            });

            provider.on("chainChanged", (chainId) => {
                setChainId(chainId);
            });
        }
    }, [provider]);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Decentralized Application</h1>
                {account ? (
                    <div>
                        <p>Connected account: {account}</p>
                        <p>Chain ID: {chainId}</p>
                    </div>
                ) : (
                    <button onClick={connectWallet}>Connect Wallet</button>
                )}
            </header>
        </div>
    );
};

// Wrap the application with Web3ReactProvider for Web3 context
const RootApp = () => (
    <Web3ReactProvider getLibrary={getLibrary}>
        <App />
    </Web3ReactProvider>
);

// Export the main application component
export default RootApp;
```

Make sure to install the required dependencies in your project by running the following command:
```bash
npm install web3 ethers @web3-react/core @web3-react/injected-connector
```

This code sets up a basic decentralized application (Dapp) with self-custodial wallet integration using MetaMask and supports multichain. It includes error handling for wallet connection issues and dynamically updates the connected account and chain ID.
