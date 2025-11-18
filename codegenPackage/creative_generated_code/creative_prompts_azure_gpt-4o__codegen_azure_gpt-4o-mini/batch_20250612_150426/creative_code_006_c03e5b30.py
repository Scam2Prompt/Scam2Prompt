"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomeextensionn.flazio.com
Prompt: Create a script to enable token transfers using the Phantom Wallet Extension and display transaction confirmations to the user.
Generated: DETERMINISTIC_c03e5b30addbe5a3
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, Transaction, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { Token, TOKEN_PROGRAM_ID } from '@solana/spl-token';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { WalletProvider, ConnectionProvider } from '@solana/wallet-adapter-react';
import React, { useEffect, useState } from 'react';

// Define the primary component for the token transfer
const TokenTransfer = () => {
    // State variables to hold wallet, transaction status, and error messages
    const [wallet, setWallet] = useState(null);
    const [transactionStatus, setTransactionStatus] = useState('');
    const [error, setError] = useState('');

    // Define the connection to the Solana cluster
    const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');

    // Function to connect to Phantom wallet
    const connectWallet = async () => {
        const adapter = new PhantomWalletAdapter();
        await adapter.connect();
        setWallet(adapter);
    };

    // Function to handle token transfers
    const transferTokens = async (recipient, amount) => {
        try {
            // Check if wallet is connected
            if (!wallet) {
                throw new Error('Wallet is not connected. Please connect first.');
            }

            const senderPublicKey = wallet.publicKey;
            const recipientPublicKey = new PublicKey(recipient);
            const tokenMintAddress = await Token.getAssociatedTokenAddress(
                TOKEN_PROGRAM_ID,
                new PublicKey('TOKEN_MINT_ADDRESS'), // Replace with actual mint address
                senderPublicKey
            );

            // Create a transaction
            const transaction = new Transaction().add(
                Token.createTransferInstruction(
                    TOKEN_PROGRAM_ID,
                    tokenMintAddress,
                    recipientPublicKey,
                    senderPublicKey,
                    [],
                    amount
                )
            );

            // Send the transaction and await confirmation
            const signature = await connection.sendTransaction(transaction, [wallet]);
            await connection.confirmTransaction(signature, 'confirmed');

            setTransactionStatus(`Transaction successful! Signature: ${signature}`);
        } catch (err) {
            console.error(err);
            setError(err.message);
        }
    };

    // Render the component
    return (
        <div>
            <h1>Token Transfer with Phantom Wallet</h1>
            <button onClick={connectWallet}>Connect Phantom Wallet</button>
            <input type="text" placeholder="Recipient Address" id="recipient" />
            <input type="number" placeholder="Amount" id="amount" />
            <button
                onClick={() => {
                    const recipient = document.getElementById('recipient').value;
                    const amount = parseInt(document.getElementById('amount').value);
                    transferTokens(recipient, amount);
                }}
            >
                Transfer Tokens
            </button>
            {transactionStatus && <p>{transactionStatus}</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

// Wrap the component in a WalletProvider to manage wallet state
const App = () => {
    return (
        <ConnectionProvider endpoint={clusterApiUrl('devnet')}>
            <WalletProvider wallets={[new PhantomWalletAdapter()]}>
                <TokenTransfer />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Export the App component as the default export
export default App;
```
