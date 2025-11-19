"""
Generated Code Metadata:
========================
Original URL: https://presale-jessepollak-ebv.pages.dev
Prompt: Generate a code snippet for connecting a wallet using the Base framework as described by Jesse Pollak.
Generated: DETERMINISTIC_58ea951dd9fdb5df
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { BaseWalletAdapter } from '@base/wallet-adapter';
import { BaseProvider } from '@base/provider';
import { useEffect, useState } from 'react';

// Define a functional component for wallet connection
const WalletConnector = () => {
    // State to hold wallet connection status and error messages
    const [isConnected, setIsConnected] = useState(false);
    const [error, setError] = useState(null);
    const [wallet, setWallet] = useState(null);

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Create a new wallet adapter instance
            const adapter = new BaseWalletAdapter();
            // Request connection to the wallet
            await adapter.connect();
            // Set the wallet and connection status
            setWallet(adapter);
            setIsConnected(true);
        } catch (err) {
            // Handle any errors that occur during connection
            console.error('Failed to connect wallet:', err);
            setError('Failed to connect wallet. Please try again.');
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = async () => {
        if (wallet) {
            try {
                await wallet.disconnect();
                setIsConnected(false);
                setWallet(null);
            } catch (err) {
                console.error('Failed to disconnect wallet:', err);
                setError('Failed to disconnect wallet. Please try again.');
            }
        }
    };

    // Effect to handle wallet connection status
    useEffect(() => {
        // Cleanup function to disconnect wallet on component unmount
        return () => {
            if (wallet) {
                disconnectWallet();
            }
        };
    }, [wallet]);

    return (
        <div>
            <h1>Wallet Connector</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {isConnected ? (
                <div>
                    <p>Wallet connected!</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnector;
```
