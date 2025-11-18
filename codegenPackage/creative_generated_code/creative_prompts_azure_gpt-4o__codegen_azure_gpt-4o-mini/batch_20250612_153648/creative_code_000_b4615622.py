"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Write code to integrate a Solana wallet connection feature into a Next.js application for managing NFTs and streaming profits.
Generated: DETERMINISTIC_b4615622996924d7
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
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';

// Define the connection to the Solana cluster
const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

// Main component for wallet connection
const WalletConnect = () => {
    // State to hold wallet connection status and wallet address
    const [walletConnected, setWalletConnected] = useState(false);
    const [walletAddress, setWalletAddress] = useState(null);
    
    // Create a new instance of the Phantom wallet adapter
    const wallet = new PhantomWalletAdapter();

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            await wallet.connect();
            setWalletConnected(true);
            setWalletAddress(wallet.publicKey.toString());
        } catch (error) {
            console.error("Failed to connect wallet:", error);
        }
    };

    // Function to disconnect from the wallet
    const disconnectWallet = async () => {
        try {
            await wallet.disconnect();
            setWalletConnected(false);
            setWalletAddress(null);
        } catch (error) {
            console.error("Failed to disconnect wallet:", error);
        }
    };

    // Effect to handle wallet connection state
    useEffect(() => {
        if (wallet.connected) {
            setWalletConnected(true);
            setWalletAddress(wallet.publicKey.toString());
        } else {
            setWalletConnected(false);
            setWalletAddress(null);
        }

        // Cleanup function to handle wallet disconnection
        return () => {
            if (wallet.connected) {
                disconnectWallet();
            }
        };
    }, [wallet.connected]);

    return (
        <div>
            <h1>Solana Wallet Connection</h1>
            {walletConnected ? (
                <div>
                    <p>Connected Wallet Address: {walletAddress}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the WalletConnect component
export default WalletConnect;
```

### Installation Instructions
To ensure the code runs correctly, you'll need to install the required packages. You can do so by running the following command:

```bash
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom
```

### Usage
To use the `WalletConnect` component, simply import it into your Next.js pages or components where you want to enable wallet connection functionality:

```javascript
import WalletConnect from './path/to/WalletConnect';

const Home = () => {
    return (
        <div>
            <h1>Home Page</h1>
            <WalletConnect />
        </div>
    );
};

export default Home;
``` 

This completes the integration of a Solana wallet connection feature into a Next.js application. Ensure you have the Phantom wallet installed in your browser for testing.
