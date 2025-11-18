"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom--walleth-join.webflow.io
Prompt: Write a tutorial for integrating Phantom Wallet with a Solana-based dApp, focusing on user authentication and transaction signing.
Generated: DETERMINISTIC_1ef59583cb2d8d96
Batch ID: 20250612_145218
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
import { Connection, clusterApiUrl, Keypair, PublicKey, Transaction } from '@solana/web3.js';
import { PhantomProvider } from '@solana/wallet-adapter-phantom';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';

// Endpoint for Solana cluster
const NETWORK = clusterApiUrl('devnet');

// Create a connection to the Solana cluster
const connection = new Connection(NETWORK, 'confirmed');

// Main Application Component
const App = () => {
    const [userAccount, setUserAccount] = useState(null);
    const wallet = useWallet();

    // Handle wallet connection
    const connectWallet = async () => {
        try {
            if (!wallet.connected) {
                await wallet.connect();
                // Set the user's account after connecting
                setUserAccount(wallet.publicKey.toString());
            }
        } catch (error) {
            console.error('Wallet connection failed:', error);
        }
    };

    // Handle transaction signing
    const signTransaction = async () => {
        try {
            // Create a sample transaction (this should be customized for your dApp)
            const transaction = new Transaction().add(
                // Your transaction instructions here
            );

            // Send the transaction using the wallet
            const signedTransaction = await wallet.signTransaction(transaction);
            const transactionSignature = await connection.sendRawTransaction(signedTransaction.serialize());

            // Confirm the transaction
            await connection.confirmTransaction(transactionSignature, 'confirmed');
            console.log('Transaction successful with signature:', transactionSignature);
        } catch (error) {
            console.error('Transaction signing failed:', error);
        }
    };

    // Render the UI
    return (
        <div>
            <h1>Phantom Wallet Integration with Solana dApp</h1>
            {userAccount ? (
                <div>
                    <p>Connected Account: {userAccount}</p>
                    <button onClick={signTransaction}>Sign Transaction</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Phantom Wallet</button>
            )}
        </div>
    );
};

// Main entry point
const Main = () => {
    return (
        <WalletProvider wallets={[new PhantomProvider()]}>
            <App />
        </WalletProvider>
    );
};

// Export the main component
export default Main;
```

### Note:
Make sure to install the required dependencies in your project:
```bash
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom
```
