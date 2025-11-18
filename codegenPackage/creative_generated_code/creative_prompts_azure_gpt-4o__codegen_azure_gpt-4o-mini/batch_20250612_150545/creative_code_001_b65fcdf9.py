"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfth.web.app
Prompt: Generate code to connect a Solana wallet using the wallet connection functionality described on the website, and display the wallet's balance for both the main and trading wallets.
Generated: DETERMINISTIC_b65fcdf976402917
Batch ID: 20250612_150545
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
import { Connection, clusterApiUrl, PublicKey } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    PhantomWalletAdapter,
    SolanaWalletAdapterProvider,
    useWallet,
} from '@solana/wallet-adapter-react';
import { WalletProvider } from '@solana/wallet-adapter-react';

// Set the network and connection for Solana
const network = WalletAdapterNetwork.Mainnet;
const endpoint = clusterApiUrl(network);

// WalletApp component to handle wallet connection and balance display
const WalletApp = () => {
    const { publicKey, connected } = useWallet(); // Get wallet connection details
    const [mainWalletBalance, setMainWalletBalance] = useState(null);
    const [tradingWalletBalance, setTradingWalletBalance] = useState(null);

    // Effect to fetch balance when wallet is connected
    useEffect(() => {
        const getBalances = async () => {
            if (publicKey) {
                try {
                    const connection = new Connection(endpoint, 'confirmed');

                    // Fetch main wallet balance
                    const mainBalance = await connection.getBalance(publicKey);
                    setMainWalletBalance(mainBalance / 1e9); // Convert lamports to SOL

                    // Assuming trading wallet is a known public key (replace with actual trading wallet address)
                    const tradingWalletPublicKey = new PublicKey('YOUR_TRADING_WALLET_ADDRESS');
                    const tradingBalance = await connection.getBalance(tradingWalletPublicKey);
                    setTradingWalletBalance(tradingBalance / 1e9); // Convert lamports to SOL
                } catch (error) {
                    console.error("Error fetching balances:", error);
                }
            }
        };

        getBalances();
    }, [publicKey]); // Run effect when publicKey changes

    return (
        <div>
            <h1>Solana Wallet Connection</h1>
            {connected ? (
                <div>
                    <h2>Wallet Address: {publicKey.toString()}</h2>
                    <h3>Main Wallet Balance: {mainWalletBalance !== null ? `${mainWalletBalance} SOL` : 'Loading...'}</h3>
                    <h3>Trading Wallet Balance: {tradingWalletBalance !== null ? `${tradingWalletBalance} SOL` : 'Loading...'}</h3>
                </div>
            ) : (
                <h2>Please connect your wallet</h2>
            )}
        </div>
    );
};

// Main App component to set up the wallet provider
const App = () => {
    return (
        <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
            <WalletApp />
        </WalletProvider>
    );
};

// Export the App component
export default App;
```
Note: Replace `'YOUR_TRADING_WALLET_ADDRESS'` with the actual public key of your trading wallet. Make sure you have the necessary dependencies installed, including `@solana/web3.js`, `@solana/wallet-adapter-base`, and `@solana/wallet-adapter-react`.
