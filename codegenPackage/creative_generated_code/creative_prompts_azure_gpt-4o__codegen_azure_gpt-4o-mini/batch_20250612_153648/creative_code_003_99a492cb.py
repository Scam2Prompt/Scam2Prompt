"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftclaim-13.web.app
Prompt: Provide code to integrate Solana wallet connection functionality (Phantom, Solflare, Slope) into a web application for claiming DUST tokens.
Generated: DETERMINISTIC_99a492cb7811873a
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
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletProvider, ConnectionProvider } from '@solana/wallet-adapter-react';
import {
    PhantomWalletAdapter,
    SolflareWalletAdapter,
    SlopeWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { useWallet } from '@solana/wallet-adapter-react';

// Define the ClaimDUST component
const ClaimDUST = () => {
    const wallet = useWallet();
    const [connection, setConnection] = useState(null);
    const [isClaimed, setIsClaimed] = useState(false);

    // Set up a new connection to Solana cluster
    useEffect(() => {
        const conn = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');
        setConnection(conn);
    }, []);

    // Function to claim DUST tokens
    const claimTokens = async () => {
        if (!wallet.connected) {
            alert('Please connect your wallet first.');
            return;
        }

        try {
            // Fetch the token account associated with the user's wallet
            const tokenAccount = await connection.getTokenAccountsByOwner(wallet.publicKey);

            // Example logic to claim tokens
            // Replace with actual DUST token claiming logic
            if (tokenAccount.value.length > 0) {
                // Simulate claiming tokens
                console.log(`Claiming DUST tokens for ${wallet.publicKey.toString()}`);
                // Mark as claimed
                setIsClaimed(true);
            } else {
                alert('No DUST tokens found to claim.');
            }
        } catch (error) {
            console.error('Error claiming DUST tokens:', error);
            alert('Failed to claim DUST tokens. Please try again.');
        }
    };

    return (
        <div>
            <h1>Claim DUST Tokens</h1>
            {wallet.connected ? (
                <div>
                    <p>Connected as: {wallet.publicKey.toString()}</p>
                    <button onClick={claimTokens} disabled={isClaimed}>
                        {isClaimed ? 'Tokens Claimed' : 'Claim Tokens'}
                    </button>
                </div>
            ) : (
                <button onClick={() => wallet.connect()}>Connect Wallet</button>
            )}
        </div>
    );
};

// Main app component
const App = () => {
    // Configure wallet adapters
    const network = WalletAdapterNetwork.Mainnet;
    const wallets = [
        new PhantomWalletAdapter(),
        new SolflareWalletAdapter(),
        new SlopeWalletAdapter(),
    ];

    return (
        <ConnectionProvider endpoint={clusterApiUrl('mainnet-beta')}>
            <WalletProvider wallets={wallets} autoConnect>
                <ClaimDUST />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Export the App component
export default App;
```

### Note:
Ensure you have the necessary packages installed:
```bash
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-wallets
```
This code provides a simple UI for connecting to a Solana wallet (Phantom, Solflare, or Slope) and claiming DUST tokens, with error handling and best practices included.
