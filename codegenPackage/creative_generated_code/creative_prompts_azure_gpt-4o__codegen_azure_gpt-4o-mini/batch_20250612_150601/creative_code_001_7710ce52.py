"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maqicedao.web.app
Prompt: Generate code to connect a Solana-compatible wallet and display the wallet's balance for both the "Основной кошелек" (main wallet) and "Торговый кошелек" (trading wallet) as described on the website.
Generated: DETERMINISTIC_7710ce526734d518
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
import { Connection, clusterApiUrl, PublicKey } from '@solana/web3.js';
import { useEffect, useState } from 'react';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';

// Define the network and create a connection to the Solana cluster
const network = WalletAdapterNetwork.Devnet; // Change to Mainnet for production
const endpoint = clusterApiUrl(network);
const connection = new Connection(endpoint);

// Component to display wallet balance
const WalletBalance = () => {
    const { publicKey, connected } = useWallet(); // Get wallet info
    const [mainBalance, setMainBalance] = useState(null);
    const [tradingBalance, setTradingBalance] = useState(null);
    
    // Function to fetch the balance of a specific wallet
    const getBalance = async (walletAddress) => {
        try {
            const balance = await connection.getBalance(new PublicKey(walletAddress));
            return balance / 1e9; // Convert lamports to SOL
        } catch (error) {
            console.error("Error fetching balance:", error);
            return null;
        }
    };

    // Fetch balances for both wallets once the wallet is connected
    useEffect(() => {
        const fetchBalances = async () => {
            if (connected && publicKey) {
                // Assuming wallet addresses are hardcoded for demonstration
                const mainWalletAddress = publicKey.toString();
                const tradingWalletAddress = 'YOUR_TRADING_WALLET_ADDRESS'; // Replace with the actual trading wallet address
                
                const mainBalance = await getBalance(mainWalletAddress);
                const tradingBalance = await getBalance(tradingWalletAddress);

                setMainBalance(mainBalance);
                setTradingBalance(tradingBalance);
            }
        };

        fetchBalances();
    }, [connected, publicKey]);

    return (
        <div>
            {connected ? (
                <>
                    <h2>Wallet Balances:</h2>
                    <p>Основной кошелек: {mainBalance !== null ? `${mainBalance} SOL` : 'Loading...'}</p>
                    <p>Торговый кошелек: {tradingBalance !== null ? `${tradingBalance} SOL` : 'Loading...'}</p>
                </>
            ) : (
                <p>Please connect to your wallet.</p>
            )}
        </div>
    );
};

// Main App component
const App = () => {
    return (
        <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
            <div>
                <h1>Solana Wallet Balance</h1>
                <WalletBalance />
            </div>
        </WalletProvider>
    );
};

export default App;
```

Make sure to replace `YOUR_TRADING_WALLET_ADDRESS` with the actual address of the trading wallet when using this code. Additionally, you must install the necessary dependencies by running:

```bash
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom @solana/wallet-adapter-base
```
