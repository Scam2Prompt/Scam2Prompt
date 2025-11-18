"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promo-ws108.github.io
Prompt: Write a script to integrate Solana wallet options (e.g., Phantom, Solflare, Ledger) into a web application, similar to the wallet connection options on the Degen Toy Machine page.
Generated: DETERMINISTIC_730e70f4857df594
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import { useEffect, useState } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { SolflareWalletAdapter } from '@solana/wallet-adapter-solflare';
import { LedgerWalletAdapter } from '@solana/wallet-adapter-ledger';

// Wallet integration options
const WALLET_OPTIONS = {
    Phantom: new PhantomWalletAdapter(),
    Solflare: new SolflareWalletAdapter(),
    Ledger: new LedgerWalletAdapter(),
};

// Solana cluster endpoint (e.g., mainnet-beta, devnet, testnet)
const SOLANA_CLUSTER = 'devnet';

// React functional component for wallet integration
function SolanaWalletIntegration() {
    const [wallet, setWallet] = useState(null);
    const [connection, setConnection] = useState(null);
    const [publicKey, setPublicKey] = useState(null);
    const [error, setError] = useState(null);

    // Initialize Solana connection
    useEffect(() => {
        const solanaConnection = new Connection(clusterApiUrl(SOLANA_CLUSTER), 'confirmed');
        setConnection(solanaConnection);
    }, []);

    // Connect wallet
    const connectWallet = async (walletName) => {
        try {
            const selectedWallet = WALLET_OPTIONS[walletName];
            if (!selectedWallet) {
                throw new Error('Wallet not supported');
            }

            await selectedWallet.connect(); // Trigger wallet connection
            setWallet(selectedWallet);
            setPublicKey(selectedWallet.publicKey);
            setError(null);
        } catch (err) {
            setError(err.message || 'Failed to connect wallet');
        }
    };

    // Disconnect wallet
    const disconnectWallet = async () => {
        try {
            if (wallet) {
                await wallet.disconnect();
                setWallet(null);
                setPublicKey(null);
                setError(null);
            }
        } catch (err) {
            setError(err.message || 'Failed to disconnect wallet');
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Solana Wallet Integration</h1>

            {/* Wallet connection options */}
            <div>
                <button onClick={() => connectWallet('Phantom')}>Connect Phantom Wallet</button>
                <button onClick={() => connectWallet('Solflare')}>Connect Solflare Wallet</button>
                <button onClick={() => connectWallet('Ledger')}>Connect Ledger Wallet</button>
                <button onClick={disconnectWallet} disabled={!wallet}>
                    Disconnect Wallet
                </button>
            </div>

            {/* Display wallet details */}
            <div style={{ marginTop: '20px' }}>
                {error && <p style={{ color: 'red' }}>Error: {error}</p>}
                {publicKey && <p>Connected Wallet: {publicKey.toString()}</p>}
            </div>
        </div>
    );
}

export default SolanaWalletIntegration;
```
