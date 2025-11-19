"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiconnect-metamsk.pages.dev
Prompt: Generate a code example for integrating a wallet connection using Web3 Connect for a decentralized application, similar to the functionality offered by Multiconnect.
Generated: DETERMINISTIC_e0d394bc8877b1f7
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import WalletConnectProvider from '@walletconnect/web3-provider';
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider, useWeb3React } from '@web3-react/core';

// Create a Web3 provider function
function getLibrary(provider) {
    return new Web3(provider);
}

// Define a WalletConnect provider
const walletConnectProvider = new WalletConnectProvider({
    infuraId: 'YOUR_INFURA_ID', // Replace with your Infura project ID
});

// Define the injected connector for browser wallets (e.g., MetaMask)
const injectedConnector = new InjectedConnector({
    supportedChainIds: [1, 3, 4, 5, 42], // Supported Ethereum networks
});

// Main App Component
const App = () => {
    const { activate, account, library } = useWeb3React();

    // Function to connect WalletConnect
    const connectWalletConnect = async () => {
        try {
            await activate(walletConnectProvider);
            console.log('WalletConnect connected');
        } catch (error) {
            console.error('Error connecting WalletConnect:', error);
        }
    };

    // Function to connect injected wallet (MetaMask)
    const connectInjected = async () => {
        try {
            await activate(injectedConnector);
            console.log('Injected wallet connected');
        } catch (error) {
            console.error('Error connecting injected wallet:', error);
        }
    };

    return (
        <div>
            <h1>Wallet Connection Example</h1>
            {account ? (
                <p>Connected Account: {account}</p>
            ) : (
                <div>
                    <button onClick={connectWalletConnect}>
                        Connect with WalletConnect
                    </button>
                    <button onClick={connectInjected}>
                        Connect with MetaMask
                    </button>
                </div>
            )}
        </div>
    );
};

// Render the application
const Main = () => {
    return (
        <Web3ReactProvider getLibrary={getLibrary}>
            <App />
        </Web3ReactProvider>
    );
};

export default Main;
```
