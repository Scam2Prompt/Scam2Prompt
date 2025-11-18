"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Explain how to use the Solana Wallet Adapter to support multiple wallet providers in a Mantine UI application.
Generated: DETERMINISTIC_c201d5ada26e3ad7
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import { WalletProvider, ConnectionProvider, useWallet } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter, SolletWalletAdapter, SolflareWalletAdapter } from '@solana/wallet-adapter-wallets';
import { MantineProvider, Button, Notification } from '@mantine/core';
import { clusterApiUrl } from '@solana/web3.js';

// Configuration for Solana connection
const network = clusterApiUrl('devnet');

// Component to connect with different wallets
const WalletConnection = () => {
    const { connected, connect, disconnect, publicKey } = useWallet();
    const [error, setError] = useState(null);

    // Connect to the selected wallet
    const handleConnect = async () => {
        try {
            await connect();
        } catch (err) {
            setError('Failed to connect to wallet. Please try again.');
            console.error(err);
        }
    };

    // Disconnect from the wallet
    const handleDisconnect = async () => {
        try {
            await disconnect();
        } catch (err) {
            setError('Failed to disconnect from wallet. Please try again.');
            console.error(err);
        }
    };

    return (
        <div>
            {error && <Notification color="red" title="Error">{error}</Notification>}
            {connected ? (
                <div>
                    <p>Connected: {publicKey.toString()}</p>
                    <Button onClick={handleDisconnect}>Disconnect</Button>
                </div>
            ) : (
                <Button onClick={handleConnect}>Connect Wallet</Button>
            )}
        </div>
    );
};

// Main application component
const App = () => {
    // Set up wallets to support
    const wallets = [
        new PhantomWalletAdapter(),
        new SolletWalletAdapter(),
        new SolflareWalletAdapter(),
    ];

    return (
        <MantineProvider>
            <ConnectionProvider endpoint={network}>
                <WalletProvider wallets={wallets}>
                    <WalletConnection />
                </WalletProvider>
            </ConnectionProvider>
        </MantineProvider>
    );
};

// Export the main component
export default App;
```
