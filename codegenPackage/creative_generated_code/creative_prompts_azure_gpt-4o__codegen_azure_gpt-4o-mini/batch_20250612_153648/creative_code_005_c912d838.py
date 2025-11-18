"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neondrainer.web.app
Prompt: Provide an example of integrating a Solana wallet connection feature into a web app, similar to the "Connect Wallet" functionality described on https://neondrainer.web.app.
Generated: DETERMINISTIC_c912d83847ba9bf9
Batch ID: 20250612_153648
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
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import WalletAdapter from '@solana/wallet-adapter-react';
import { WalletProvider, ConnectionProvider } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';

// Define the main App component
const App = () => {
    // State to hold the wallet address
    const [walletAddress, setWalletAddress] = useState(null);
    const [connection, setConnection] = useState(null);

    // Create a connection to the Solana cluster
    useEffect(() => {
        const newConnection = new Connection(clusterApiUrl('devnet'), 'confirmed');
        setConnection(newConnection);
    }, []);

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Request wallet connection
            const { solana } = window;
            if (solana && solana.isPhantom) {
                const response = await solana.connect();
                setWalletAddress(response.publicKey.toString());
            } else {
                alert('Please install Phantom wallet!');
            }
        } catch (error) {
            console.error('Wallet connection failed:', error);
            alert('Failed to connect wallet. Please try again.');
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setWalletAddress(null);
    };

    return (
        <div>
            <h1>Solana Wallet Integration</h1>
            {walletAddress ? (
                <div>
                    <p>Connected Wallet: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Main entry point of the application
const Main = () => {
    // Configure wallet adapter
    const wallets = [new PhantomWalletAdapter()];

    return (
        <ConnectionProvider connection={new Connection(clusterApiUrl('devnet'), 'confirmed')}>
            <WalletProvider wallets={wallets}>
                <App />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Render the main application component
export default Main;
```

### Notes:
- Ensure you have the required packages installed: `@solana/web3.js`, `@solana/wallet-adapter-react`, and `@solana/wallet-adapter-wallets`.
- The wallet connection feature is set up for the Phantom wallet, which is a popular choice for Solana.
- This example connects to the Solana devnet. Adjust the cluster URL for mainnet or testnet as required.
