"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knights-of-fantom.com
Prompt: Recommend libraries or APIs for integrating wallet connection functionality in a dApp built on the Fantom network.
Generated: DETERMINISTIC_c77df7c6b0da51a8
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import Web3 from 'web3';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';
import React from 'react';
import ReactDOM from 'react-dom';

// Function to get the Web3 provider
function getLibrary(provider) {
    return new Web3(provider);
}

// Wallet connector for injected wallets (like MetaMask)
const injected = new InjectedConnector({
    supportedChainIds: [250, 4002] // Fantom mainnet and testnet chain IDs
});

// Component to connect wallet
const ConnectButton = () => {
    const { activate, active } = useWeb3React();

    // Function to handle wallet connection
    const connectWallet = async () => {
        try {
            await activate(injected);
            console.log('Wallet connected successfully.');
        } catch (error) {
            console.error('Failed to connect wallet:', error);
            alert('Connection failed. Please check console for details.');
        }
    };

    return (
        <button onClick={connectWallet} disabled={active}>
            {active ? 'Wallet Connected' : 'Connect Wallet'}
        </button>
    );
};

// Main App component
const App = () => {
    return (
        <div>
            <h1>Fantom dApp</h1>
            <ConnectButton />
        </div>
    );
};

// Render the application
ReactDOM.render(
    <Web3ReactProvider getLibrary={getLibrary}>
        <App />
    </Web3ReactProvider>,
    document.getElementById('root')
);
```
