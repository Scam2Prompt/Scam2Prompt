"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-widget-e94wzx722-toraverse.vercel.app
Prompt: Write code to integrate the Tegro Swap widget into a React application, ensuring compatibility with MetaMask and WalletConnect for wallet connections.
Generated: DETERMINISTIC_14121aff417b3d4a
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import WalletConnectProvider from "@walletconnect/web3-provider";
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';

// Create a provider function for Web3
function getLibrary(provider) {
    const library = new Web3(provider);
    library.pollingInterval = 12000; // Set polling interval for the provider
    return library;
}

// Component to integrate the Tegro Swap widget
const TegroSwapWidget = () => {
    const { activate, account, library } = useWeb3React();
    const [error, setError] = useState(null);

    // Connector for MetaMask
    const injected = new InjectedConnector({ supportedChainIds: [1, 3, 4, 5, 42] });

    // Function to connect with MetaMask
    const connectMetaMask = async () => {
        try {
            await activate(injected);
        } catch (err) {
            console.error('MetaMask connection error:', err);
            setError('Failed to connect to MetaMask.');
        }
    };

    // Function to connect with WalletConnect
    const connectWalletConnect = async () => {
        // Create a WalletConnect Provider
        const provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Replace with your Infura ID
        });

        // Enable session (triggers QR Code modal)
        await provider.enable();

        // Activate the provider
        try {
            await activate(provider);
        } catch (err) {
            console.error('WalletConnect connection error:', err);
            setError('Failed to connect to WalletConnect.');
        }
    };

    // Effect to handle account changes
    useEffect(() => {
        if (account) {
            console.log('Connected account:', account);
        }
    }, [account]);

    return (
        <div>
            <h1>Tegro Swap Widget</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <button onClick={connectMetaMask}>Connect MetaMask</button>
            <button onClick={connectWalletConnect}>Connect WalletConnect</button>
            {/* Insert Tegro Swap widget here, using the connected account and library if available */}
            {account && library && (
                <div>
                    <p>Connected as: {account}</p>
                    {/* Tegro Swap widget integration code goes here */}
                </div>
            )}
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <Web3ReactProvider getLibrary={getLibrary}>
            <TegroSwapWidget />
        </Web3ReactProvider>
    );
};

export default App;
```

Make sure you replace `"YOUR_INFURA_ID"` with your actual Infura ID. This script provides a basic implementation for integrating the Tegro Swap widget with wallet connection support via MetaMask and WalletConnect.
