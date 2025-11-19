"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.com
Prompt: How can I use Reown's AppKit to build a user-friendly onchain application with seamless integration across multiple wallets and chains?
Generated: DETERMINISTIC_1fad4dc9614bfa03
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { AppKit, WalletConnector, ChainSelector } from 'reown-appkit';

// Initialize AppKit with your project configuration
const appKit = new AppKit({
    apiKey: 'YOUR_API_KEY', // Replace with your actual API key
    environment: 'production', // Set environment to 'development' or 'production'
});

// Initialize wallet connector for seamless wallet integration
const walletConnector = new WalletConnector({
    supportedWallets: ['MetaMask', 'WalletConnect', 'Coinbase Wallet'], // List of supported wallets
    onConnect: handleWalletConnect, // Callback for successful connection
    onDisconnect: handleWalletDisconnect, // Callback for disconnection
});

// Setup Chain Selector for multi-chain support
const chainSelector = new ChainSelector({
    supportedChains: ['Ethereum', 'Binance Smart Chain', 'Polygon'], // List of supported chains
    onChainChange: handleChainChange, // Callback for chain change
});

// Event handler for wallet connection
function handleWalletConnect(wallet) {
    console.log(`Connected to wallet: ${wallet.name}`);
    // Perform any additional actions after connecting, such as fetching user data
    fetchUserData();
}

// Event handler for wallet disconnection
function handleWalletDisconnect() {
    console.log('Wallet disconnected');
    // Handle disconnection logic here, such as clearing user data
    clearUserData();
}

// Event handler for chain change
function handleChainChange(chain) {
    console.log(`Switched to chain: ${chain.name}`);
    // Fetch data relevant to the new chain
    fetchChainData(chain);
}

// Fetch user data from the blockchain
async function fetchUserData() {
    try {
        const userData = await appKit.getUserData();
        console.log('User Data:', userData);
        // Process user data as needed
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}

// Clear user data on wallet disconnect
function clearUserData() {
    // Logic to clear user data from the state
    console.log('User data cleared');
}

// Fetch data relevant to the selected chain
async function fetchChainData(chain) {
    try {
        const chainData = await appKit.getChainData(chain.id);
        console.log('Chain Data:', chainData);
        // Process chain data as needed
    } catch (error) {
        console.error('Error fetching chain data:', error);
    }
}

// Main function to initialize the application
async function main() {
    try {
        await appKit.initialize(); // Initialize the AppKit
        console.log('Application initialized.');

        // Attach wallet and chain selector UI components to the DOM
        document.getElementById('wallet-connect-btn').onclick = () => walletConnector.connect();
        document.getElementById('chain-selector').onchange = (event) => {
            const selectedChain = event.target.value;
            chainSelector.switchChain(selectedChain);
        };

    } catch (error) {
        console.error('Error initializing application:', error);
    }
}

// Run the main function when the document is ready
document.addEventListener('DOMContentLoaded', main);
```
