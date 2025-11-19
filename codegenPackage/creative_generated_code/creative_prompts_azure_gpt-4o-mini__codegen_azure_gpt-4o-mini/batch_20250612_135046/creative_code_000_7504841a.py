"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.foundation
Prompt: How can I implement WalletConnect in my dApp to enhance user experience and facilitate connections with multiple wallets?
Generated: DETERMINISTIC_7504841a93560983
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import { useEffect, useState } from 'react';
import WalletConnectProvider from '@walletconnect/web3-provider';
import Web3 from 'web3';

// Define the main component
const WalletConnectComponent = () => {
    // Define state variables for connected wallet information and error handling
    const [provider, setProvider] = useState(null);
    const [account, setAccount] = useState('');
    const [error, setError] = useState(null);

    // Initialize WalletConnect provider and Web3 instance
    const connectWallet = async () => {
        try {
            // Create a WalletConnect Provider
            const walletConnectProvider = new WalletConnectProvider({
                infuraId: 'YOUR_INFURA_PROJECT_ID', // Required for the provider to connect to Ethereum networks
            });

            // Enable session (triggers QR Code modal)
            await walletConnectProvider.enable();

            // Create a Web3 instance using the WalletConnect provider
            const web3 = new Web3(walletConnectProvider);

            // Get accounts and set the first account as the connected account
            const accounts = await web3.eth.getAccounts();
            setAccount(accounts[0]);

            // Set the provider in the state
            setProvider(walletConnectProvider);
        } catch (err) {
            // Log and set the error state
            console.error("Failed to connect wallet:", err);
            setError("Failed to connect wallet. Please try again.");
        }
    };

    // Disconnect wallet and clean up
    const disconnectWallet = async () => {
        if (provider) {
            await provider.disconnect(); // Disconnect the provider
            setProvider(null);           // Reset provider state
            setAccount('');              // Clear account state
        }
    };

    // Effect to handle disconnection when the component is unmounted
    useEffect(() => {
        return () => {
            if (provider) {
                disconnectWallet(); // Disconnect on cleanup
            }
        };
    }, [provider]);

    return (
        <div>
            <h1>WalletConnect Example</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Connected as: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the component as default
export default WalletConnectComponent;
```
