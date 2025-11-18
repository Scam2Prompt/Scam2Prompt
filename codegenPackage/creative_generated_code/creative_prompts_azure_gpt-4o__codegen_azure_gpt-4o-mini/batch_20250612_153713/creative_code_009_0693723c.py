"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tmsrdrop.web.app
Prompt: Create a Solana-based application that allows users to connect their wallet, view their rewards in $TNSR tokens, and claim them, mimicking Tensor's reward system.
Generated: DETERMINISTIC_0693723ced071c18
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    WalletProvider,
    ConnectionProvider,
    useWallet,
} from '@solana/wallet-adapter-react';
import {
    WalletModalProvider,
    PhantomWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { TOKEN_PROGRAM_ID, getAccount, Token } from '@solana/spl-token';

// Define constants
const NETWORK = WalletAdapterNetwork.Devnet;
const TNSR_TOKEN_MINT_ADDRESS = new PublicKey('YOUR_TNSR_TOKEN_MINT_ADDRESS');

// Main Application Component
const App = () => {
    const { connected, publicKey } = useWallet();
    const [rewards, setRewards] = useState(0);
    const [error, setError] = useState(null);

    // Connection to Solana cluster
    const connection = new Connection(clusterApiUrl(NETWORK));

    // Fetch rewards when the wallet is connected
    useEffect(() => {
        const fetchRewards = async () => {
            if (connected && publicKey) {
                try {
                    const tokenAccountInfo = await getAccount(
                        connection,
                        publicKey,
                        TNSR_TOKEN_MINT_ADDRESS
                    );
                    setRewards(tokenAccountInfo.amount);
                } catch (err) {
                    setError('Failed to fetch rewards: ' + err.message);
                }
            }
        };
        fetchRewards();
    }, [connected, publicKey]);

    // Claim rewards function
    const claimRewards = async () => {
        if (!connected || !publicKey) {
            setError('Wallet not connected');
            return;
        }

        try {
            // Dummy claim function; replace with actual logic
            console.log(`Claiming rewards for ${publicKey.toBase58()}`);
            // TODO: Implement actual rewards claiming logic here
        } catch (err) {
            setError('Failed to claim rewards: ' + err.message);
        }
    };

    return (
        <div>
            <h1>TNSR Rewards Dashboard</h1>
            {error && <div style={{ color: 'red' }}>{error}</div>}
            {connected ? (
                <div>
                    <p>Your Public Key: {publicKey.toBase58()}</p>
                    <p>Your $TNSR Rewards: {rewards}</p>
                    <button onClick={claimRewards}>Claim Rewards</button>
                </div>
            ) : (
                <p>Please connect your wallet.</p>
            )}
        </div>
    );
};

// Main entry point for the application
const Main = () => {
    const wallets = [new PhantomWalletAdapter()];

    return (
        <ConnectionProvider endpoint={clusterApiUrl(NETWORK)}>
            <WalletProvider wallets={wallets} autoConnect>
                <WalletModalProvider>
                    <App />
                </WalletModalProvider>
            </WalletProvider>
        </ConnectionProvider>
    );
};

export default Main;
``` 

Make sure to replace `'YOUR_TNSR_TOKEN_MINT_ADDRESS'` with the actual mint address of the $TNSR token. Ensure that your environment is set up with the necessary dependencies, such as `@solana/web3.js`, `@solana/wallet-adapter-react`, and `@solana/spl-token`.
