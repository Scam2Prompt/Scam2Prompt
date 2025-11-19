"""
Generated Code Metadata:
========================
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Create a React component using Mantine UI that displays connected Solana wallet details using the Solana Wallet Adapter.
Generated: DETERMINISTIC_875655d60d04d811
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import { Button, Text, Container, Loader } from '@mantine/core';
import { useWallet, WalletProvider } from '@solana/wallet-adapter-react';
import { Connection, clusterApiUrl } from '@solana/web3.js';

// Define the Solana connection
const connection = new Connection(clusterApiUrl('devnet'));

// WalletDetails component to display wallet information
const WalletDetails = () => {
    const { wallet, connected, connect, disconnect } = useWallet();
    const [balance, setBalance] = useState(null);
    const [loading, setLoading] = useState(false);

    // Fetch wallet balance when connected
    useEffect(() => {
        const fetchBalance = async () => {
            if (connected && wallet) {
                setLoading(true);
                try {
                    const publicKey = wallet.publicKey;
                    const balance = await connection.getBalance(publicKey);
                    setBalance(balance / 1e9); // Convert lamports to SOL
                } catch (error) {
                    console.error('Error fetching balance:', error);
                } finally {
                    setLoading(false);
                }
            }
        };

        fetchBalance();
    }, [connected, wallet]);

    return (
        <Container>
            {loading ? (
                <Loader />
            ) : (
                <>
                    {connected ? (
                        <div>
                            <Text>Wallet Address: {wallet.publicKey.toString()}</Text>
                            <Text>Balance: {balance !== null ? `${balance} SOL` : 'N/A'}</Text>
                            <Button onClick={disconnect} color="red">Disconnect</Button>
                        </div>
                    ) : (
                        <Button onClick={connect} color="blue">Connect Wallet</Button>
                    )}
                </>
            )}
        </Container>
    );
};

// Main App component
const App = () => {
    return (
        <WalletProvider>
            <WalletDetails />
        </WalletProvider>
    );
};

export default App;
```

Make sure to install the necessary dependencies before running the code:

```bash
npm install @mantine/core @solana/wallet-adapter-react @solana/web3.js
```
