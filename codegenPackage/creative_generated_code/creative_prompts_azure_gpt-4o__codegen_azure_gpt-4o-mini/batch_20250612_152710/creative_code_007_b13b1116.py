"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://temdaocom.web.app
Prompt: Create a Solana-based application that allows users to connect their wallet and view their rewards in $TNSR tokens on Tensor.
Generated: DETERMINISTIC_b13b1116cad76e12
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    WalletProvider,
    ConnectionProvider,
    useWallet,
    useConnection,
} from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { TOKEN_PROGRAM_ID, Token } from '@solana/spl-token';
import './App.css';

// Define constants
const NETWORK = WalletAdapterNetwork.Mainnet;
const TOKEN_MINT_ADDRESS = 'YOUR_TNSR_TOKEN_MINT_ADDRESS'; // Replace with actual TNSR mint address

// Main App component
function App() {
    return (
        <ConnectionProvider endpoint={clusterApiUrl(NETWORK)}>
            <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
                <RewardsViewer />
            </WalletProvider>
        </ConnectionProvider>
    );
}

// RewardsViewer component to display user rewards
function RewardsViewer() {
    const { connection } = useConnection();
    const { wallet, connected } = useWallet();
    const [rewardAmount, setRewardAmount] = useState(0);
    const [error, setError] = useState('');

    // Fetch rewards when wallet is connected
    useEffect(() => {
        const fetchRewards = async () => {
            if (connected && wallet) {
                try {
                    const tokenAccount = await Token.getAssociatedTokenAddress(
                        TOKEN_PROGRAM_ID,
                        new PublicKey(TOKEN_MINT_ADDRESS),
                        wallet.publicKey
                    );

                    // Fetch token account balance
                    const balance = await connection.getTokenAccountBalance(tokenAccount);
                    setRewardAmount(balance.value.uiAmount || 0);
                } catch (err) {
                    console.error(err);
                    setError('Failed to fetch rewards. Please try again.');
                }
            }
        };

        fetchRewards();
    }, [connected, wallet, connection]);

    return (
        <div className="App">
            <h1>TNSR Token Rewards</h1>
            {error && <p className="error">{error}</p>}
            {connected ? (
                <div>
                    <p>Wallet Address: {wallet.publicKey.toString()}</p>
                    <p>Your Rewards: {rewardAmount} $TNSR</p>
                </div>
            ) : (
                <p>Please connect your Phantom wallet to view your rewards.</p>
            )}
        </div>
    );
}

export default App;
```

Make sure to replace `'YOUR_TNSR_TOKEN_MINT_ADDRESS'` with the actual mint address of the TNSR token on the Solana blockchain before deploying the application.
