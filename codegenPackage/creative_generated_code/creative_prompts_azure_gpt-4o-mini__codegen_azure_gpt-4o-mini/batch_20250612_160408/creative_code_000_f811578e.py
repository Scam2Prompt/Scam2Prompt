"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-sandboxes-git-remaining-solana-ma-f4a6fe-custosprotocol.vercel.app
Prompt: How can I integrate the Phantom Wallet with my Solana application using CodeSandbox?
Generated: DETERMINISTIC_f811578e114eecee
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useEffect, useState } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { PhantomProvider, WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletProvider, ConnectionProvider, useWallet } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { Button } from '@mui/material';

// Set up the network and connection to the Solana blockchain
const network = WalletAdapterNetwork.Devnet; // Change to 'Mainnet' for production
const endpoint = clusterApiUrl(network);
const connection = new Connection(endpoint);

// Define the App component
const App = () => {
    const [balance, setBalance] = useState(0);
    const wallet = useWallet();

    // Function to fetch the wallet balance
    const fetchBalance = async () => {
        if (!wallet.connected) return;

        try {
            const publicKey = wallet.publicKey;
            const balance = await connection.getBalance(publicKey);
            setBalance(balance / 1e9); // Convert lamports to SOL
        } catch (error) {
            console.error('Error fetching balance:', error);
        }
    };

    // Effect to fetch balance when wallet is connected or updated
    useEffect(() => {
        fetchBalance();
    }, [wallet.connected]);

    // Function to connect to the Phantom wallet
    const connectWallet = async () => {
        try {
            await wallet.connect();
        } catch (error) {
            console.error('Error connecting to wallet:', error);
        }
    };

    // Render the UI
    return (
        <div>
            <h1>Phantom Wallet Integration with Solana</h1>
            <Button variant="contained" color="primary" onClick={connectWallet}>
                Connect Wallet
            </Button>
            {wallet.connected && (
                <div>
                    <p>Wallet Address: {wallet.publicKey.toString()}</p>
                    <p>Balance: {balance} SOL</p>
                </div>
            )}
        </div>
    );
};

// Main App component to wrap with providers
const MainApp = () => {
    const wallets = [new PhantomWalletAdapter()];

    return (
        <ConnectionProvider endpoint={endpoint}>
            <WalletProvider wallets={wallets} autoConnect>
                <App />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Render the application
export default MainApp;
```

### Instructions
1. Create a new React project in CodeSandbox.
2. Install the necessary dependencies:
   ```bash
   npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom @solana/wallet-adapter-base @mui/material
   ```
3. Replace the contents of `src/App.js` with the provided code.
4. Run the project to see the integration in action.
