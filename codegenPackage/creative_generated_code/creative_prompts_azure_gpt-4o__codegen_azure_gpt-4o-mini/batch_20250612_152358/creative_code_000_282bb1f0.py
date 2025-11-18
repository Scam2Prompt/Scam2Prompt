"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://migration-dpai.pages.dev
Prompt: Write a script using JavaScript to integrate a "Connect Wallet" feature for MetaMask, WalletConnect, and Coinbase Wallet, similar to the functionality described in the DPAI Migration Tool webpage.
Generated: DETERMINISTIC_282bb1f011992fea
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for wallet integration
import Web3 from 'web3';
import WalletConnectProvider from "@walletconnect/web3-provider";
import { InjectedConnector } from '@web3-react/injected-connector';
import { Web3ReactProvider } from '@web3-react/core';

// Create a Web3 instance
let web3;

// Function to get the library instance
function getLibrary(provider) {
    return new Web3(provider);
}

// Initialize injected connector for MetaMask
const injected = new InjectedConnector({
    supportedChainIds: [1, 3, 4, 5, 42], // Ethereum mainnet and testnets
});

// WalletConnect provider configuration
const walletConnectProvider = new WalletConnectProvider({
    infuraId: "YOUR_INFURA_PROJECT_ID", // Required for WalletConnect
});

// Connect to MetaMask
async function connectMetaMask() {
    if (window.ethereum) {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            web3 = getLibrary(window.ethereum);
            console.log('MetaMask connected');
        } catch (error) {
            console.error('User denied account access or error occurred:', error);
        }
    } else {
        console.error('MetaMask is not installed. Please install it to use this feature.');
    }
}

// Connect to WalletConnect
async function connectWalletConnect() {
    try {
        // Enable session (triggers QR Code modal)
        await walletConnectProvider.enable();
        web3 = getLibrary(walletConnectProvider);
        console.log('WalletConnect connected');
    } catch (error) {
        console.error('Connection failed or user rejected:', error);
    }
}

// Connect to Coinbase Wallet (using injected connector)
async function connectCoinbaseWallet() {
    try {
        await injected.activate();
        web3 = getLibrary(injected.provider);
        console.log('Coinbase Wallet connected');
    } catch (error) {
        console.error('Coinbase Wallet connection failed:', error);
    }
}

// Main function to connect any wallet
async function connectWallet(walletType) {
    switch (walletType) {
        case 'metamask':
            await connectMetaMask();
            break;
        case 'walletconnect':
            await connectWalletConnect();
            break;
        case 'coinbase':
            await connectCoinbaseWallet();
            break;
        default:
            console.error('Unsupported wallet type:', walletType);
    }
}

// Event listeners for button clicks
document.getElementById('connect-metamask').addEventListener('click', () => connectWallet('metamask'));
document.getElementById('connect-walletconnect').addEventListener('click', () => connectWallet('walletconnect'));
document.getElementById('connect-coinbase').addEventListener('click', () => connectWallet('coinbase'));

// Export necessary functions for testing or further use
export { connectWallet, connectMetaMask, connectWalletConnect, connectCoinbaseWallet };
```

### Note:
- Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID for WalletConnect to function.
- Ensure that you have the required libraries installed (`web3`, `@walletconnect/web3-provider`, `@web3-react/core`, etc.) in your project.
- This code assumes you have buttons with IDs `connect-metamask`, `connect-walletconnect`, and `connect-coinbase` for triggering wallet connections.
