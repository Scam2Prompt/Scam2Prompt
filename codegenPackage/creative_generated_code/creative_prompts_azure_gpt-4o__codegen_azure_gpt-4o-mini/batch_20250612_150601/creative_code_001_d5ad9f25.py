"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelth-mint.web.app
Prompt: Generate code to connect a Solana wallet and display the balance of the "Основной кошелек" (main wallet) and "Торговый кошелек" (trading wallet) as shown on the website.
Generated: DETERMINISTIC_d5ad9f254ee67d06
Batch ID: 20250612_150601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import React, { useEffect, useState } from 'react';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletProvider, ConnectionProvider, useWallet } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';

// Define constants for wallet addresses
const MAIN_WALLET_ADDRESS = 'YOUR_MAIN_WALLET_ADDRESS';
const TRADING_WALLET_ADDRESS = 'YOUR_TRADING_WALLET_ADDRESS';

// Create a connection to the Solana cluster
const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

// Component to display wallet balances
const WalletBalances = () => {
    const { connected, publicKey } = useWallet();
    const [mainWalletBalance, setMainWalletBalance] = useState(0);
    const [tradingWalletBalance, setTradingWalletBalance] = useState(0);

    // Function to fetch balance for a given wallet address
    const fetchBalance = async (walletAddress) => {
        try {
            const publicKey = new PublicKey(walletAddress);
            const balance = await connection.getBalance(publicKey);
            return balance / 1e9; // Convert lamports to SOL
        } catch (error) {
            console.error(`Error fetching balance for ${walletAddress}: `, error);
            return 0; // Return 0 in case of error
        }
    };

    // Effect to fetch balances when the component mounts or wallet connection changes
    useEffect(() => {
        if (connected) {
            const fetchWalletBalances = async () => {
                const mainBalance = await fetchBalance(MAIN_WALLET_ADDRESS);
                const tradingBalance = await fetchBalance(TRADING_WALLET_ADDRESS);
                setMainWalletBalance(mainBalance);
                setTradingWalletBalance(tradingBalance);
            };
            fetchWalletBalances();
        }
    }, [connected]);

    return (
        <div>
            {connected ? (
                <div>
                    <h2>Wallet Balances:</h2>
                    <p>Основной кошелек (Main Wallet): {mainWalletBalance} SOL</p>
                    <p>Торговый кошелек (Trading Wallet): {tradingWalletBalance} SOL</p>
                </div>
            ) : (
                <p>Please connect your wallet.</p>
            )}
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <ConnectionProvider connection={connection}>
            <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
                <WalletBalances />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Render the app
export default App;
```

**Note:** Make sure to replace `YOUR_MAIN_WALLET_ADDRESS` and `YOUR_TRADING_WALLET_ADDRESS` with actual wallet addresses. Additionally, the project should have the necessary dependencies installed, including React, @solana/web3.js, and wallet adapter libraries.
