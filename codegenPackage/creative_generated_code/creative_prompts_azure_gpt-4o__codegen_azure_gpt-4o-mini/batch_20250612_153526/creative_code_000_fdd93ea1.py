"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dust-box.web.app
Prompt: Write a script to connect a Phantom wallet to a Solana-based decentralized application using the Solana Web3.js library.
Generated: DETERMINISTIC_fdd93ea12b803e4e
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import { Connection, clusterApiUrl } from '@solana/web3.js';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { WalletProvider } from '@solana/wallet-adapter-react';
import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import './styles.css'; // Import your CSS styles if needed

// Create a functional component for the application
const App = () => {
    // State to hold wallet connection status and wallet instance
    const [wallet, setWallet] = useState(null);
    const [connected, setConnected] = useState(false);

    // Establish a connection to the Solana cluster
    const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

    // Function to connect to Phantom Wallet
    const connectWallet = async () => {
        try {
            const walletAdapter = new PhantomWalletAdapter();
            await walletAdapter.connect();
            setWallet(walletAdapter);
            setConnected(true);
            console.log('Connected to wallet:', walletAdapter.publicKey.toString());
        } catch (error) {
            console.error('Failed to connect wallet:', error);
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = async () => {
        if (wallet) {
            try {
                await wallet.disconnect();
                setWallet(null);
                setConnected(false);
                console.log('Disconnected from wallet');
            } catch (error) {
                console.error('Failed to disconnect wallet:', error);
            }
        }
    };

    // Attach event listeners for wallet connection status
    useEffect(() => {
        const handleWalletChange = (event) => {
            if (event.connected) {
                setConnected(true);
                setWallet(event.wallet);
            } else {
                setConnected(false);
                setWallet(null);
            }
        };

        // Listen for wallet connection events
        if (window.solana) {
            window.solana.on('connect', handleWalletChange);
            window.solana.on('disconnect', handleWalletChange);
        }

        // Cleanup event listeners on unmount
        return () => {
            if (window.solana) {
                window.solana.off('connect', handleWalletChange);
                window.solana.off('disconnect', handleWalletChange);
            }
        };
    }, []);

    return (
        <div className="App">
            <h1>Solana Phantom Wallet Connection</h1>
            {connected ? (
                <div>
                    <p>Connected: {wallet.publicKey.toString()}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect to Phantom Wallet</button>
            )}
        </div>
    );
};

// Render the application
ReactDOM.render(
    <WalletProvider wallets={[new PhantomWalletAdapter()]}>
        <App />
    </WalletProvider>,
    document.getElementById('root')
);
```

Make sure to install the required dependencies before running the code:

```bash
npm install @solana/web3.js @solana/wallet-adapter-phantom @solana/wallet-adapter-react react react-dom
```

Add an HTML file with a `<div id="root"></div>` to mount the React application.
