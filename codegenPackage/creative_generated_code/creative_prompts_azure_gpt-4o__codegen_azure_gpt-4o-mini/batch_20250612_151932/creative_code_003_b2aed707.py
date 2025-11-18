"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-dapp.vercel.app
Prompt: Generate code to enable wallet connection in a StarkNet dApp, ensuring compatibility with popular wallets like Argent.
Generated: DETERMINISTIC_b2aed707b767cbe8
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import libraries
import { Provider, Contract, utils } from 'starknet';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import React, { useEffect, useState } from 'react';

// Define a function to get the library (web3 provider)
function getLibrary(provider) {
    return new Provider(provider);
}

// Create a wallet connection component
const WalletConnect = () => {
    const { activate, account, active, library } = useWeb3React();
    const [error, setError] = useState(null);

    // Function to connect to the wallet
    const connectWallet = async () => {
        const injected = new InjectedConnector({ supportedChainIds: [1, 42] }); // Add your supported chain IDs
        try {
            await activate(injected);
        } catch (err) {
            console.error('Wallet connection error:', err);
            setError('Failed to connect wallet.');
        }
    };

    // Function to disconnect from the wallet
    const disconnectWallet = () => {
        // Reset the state or perform any cleanup
        setError(null);
    };

    useEffect(() => {
        if (active) {
            console.log(`Connected account: ${account}`);
            // Optionally, load your contracts or perform additional logic here
        }
    }, [active, account]);

    return (
        <div>
            {active ? (
                <div>
                    <p>Connected account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <Web3ReactProvider getLibrary={getLibrary}>
            <h1>StarkNet dApp Wallet Connection</h1>
            <WalletConnect />
        </Web3ReactProvider>
    );
};

// Render the App component to the DOM
export default App;
```

Make sure to install the necessary libraries by running:

```bash
npm install @web3-react/core @web3-react/injected-connector starknet
```
