"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-phi.vercel.app
Prompt: Provide an example of how to detect and change the connected wallet in a Solana application using Phantom wallet integration.
Generated: DETERMINISTIC_b72bb04ff15e22b1
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import React, { useEffect, useState } from 'react';
import { Connection, clusterApiUrl } from '@solana/web3.js';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';

// Set the Solana cluster to connect to
const connection = new Connection(clusterApiUrl('devnet'));

// Wallet connection component
const WalletConnection = () => {
    const { wallet, connect, disconnect, connected } = useWallet();
    const [currentWallet, setCurrentWallet] = useState(null);

    // Function to handle wallet connection
    const handleConnect = async () => {
        try {
            await connect();
        } catch (error) {
            console.error("Failed to connect wallet:", error);
        }
    };

    // Function to handle wallet disconnection
    const handleDisconnect = async () => {
        try {
            await disconnect();
        } catch (error) {
            console.error("Failed to disconnect wallet:", error);
        }
    };

    // Effect to detect wallet changes
    useEffect(() => {
        if (wallet && connected) {
            setCurrentWallet(wallet.adapter.name);
        } else {
            setCurrentWallet(null);
        }
    }, [wallet, connected]);

    return (
        <div>
            <h2>Solana Wallet Connection</h2>
            <p>Current Wallet: {currentWallet ? currentWallet : 'Not connected'}</p>
            <button onClick={connected ? handleDisconnect : handleConnect}>
                {connected ? 'Disconnect Wallet' : 'Connect Wallet'}
            </button>
        </div>
    );
};

// Main application component
const App = () => {
    return (
        <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
            <WalletConnection />
        </WalletProvider>
    );
};

// Render the application
export default App;
```

### Notes:
- Make sure to install the required dependencies by running:
  ```bash
  npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom
  ```
- This code is designed to work in a React environment and integrates with the Phantom wallet to manage the connection state.
