"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-creator-seven.vercel.app
Prompt: Provide an example of integrating Solana wallet functionality into a web application, inspired by the features on the Solana Scaffold Token Creator site.
Generated: DETERMINISTIC_8b79f55d4b221e26
Batch ID: 20250612_153659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.devnet.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import { Connection, PublicKey, Transaction, sendAndConfirmTransaction } from '@solana/web3.js';
import { WalletAdapterNetwork, WalletProvider } from '@solana/wallet-adapter-base';
import { ConnectionProvider, WalletProvider as WalletAdapterProvider } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { Button, Input } from 'antd'; // Using Ant Design for UI components

// Solana connection configuration
const network = WalletAdapterNetwork.Devnet; // Change to 'Mainnet' for production
const endpoint = 'https://api.devnet.solana.com'; // RPC endpoint for Solana

// Main Application Component
const App = () => {
    // States for storing user input and wallet connection status
    const [wallet, setWallet] = useState(null);
    const [recipient, setRecipient] = useState('');
    const [amount, setAmount] = useState('');
    const [transactionStatus, setTransactionStatus] = useState('');

    // Function to handle wallet connection
    const connectWallet = async () => {
        const adapter = new PhantomWalletAdapter();
        try {
            await adapter.connect();
            setWallet(adapter);
            console.log('Wallet connected:', adapter.publicKey.toString());
        } catch (error) {
            console.error('Wallet connection error:', error);
        }
    };

    // Function to send SOL to another address
    const sendSol = async () => {
        if (!wallet || !recipient || !amount) {
            alert('Please connect your wallet and fill all fields.');
            return;
        }

        const connection = new Connection(endpoint, 'confirmed');
        const transaction = new Transaction();

        try {
            const publicKey = new PublicKey(recipient);
            const lamports = parseFloat(amount) * 1e9; // Convert SOL to lamports (1 SOL = 1e9 lamports)

            transaction.add(
                SystemProgram.transfer({
                    fromPubkey: wallet.publicKey,
                    toPubkey: publicKey,
                    lamports,
                })
            );

            // Send the transaction
            const signature = await sendAndConfirmTransaction(connection, transaction, [wallet]);
            setTransactionStatus(`Transaction successful with signature: ${signature}`);
        } catch (error) {
            console.error('Transaction error:', error);
            setTransactionStatus('Transaction failed. See console for details.');
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Solana Wallet Integration Example</h1>
            <Button onClick={connectWallet}>Connect Wallet</Button>
            {wallet && (
                <div>
                    <h3>Send SOL</h3>
                    <Input
                        placeholder="Recipient Address"
                        value={recipient}
                        onChange={(e) => setRecipient(e.target.value)}
                    />
                    <Input
                        placeholder="Amount (SOL)"
                        type="number"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                    />
                    <Button type="primary" onClick={sendSol}>Send SOL</Button>
                    {transactionStatus && <p>{transactionStatus}</p>}
                </div>
            )}
        </div>
    );
};

// Main render function for the app
const Main = () => (
    <ConnectionProvider endpoint={endpoint}>
        <WalletAdapterProvider wallets={[new PhantomWalletAdapter()]}>
            <App />
        </WalletAdapterProvider>
    </ConnectionProvider>
);

// Export Main component as default
export default Main;
```

**Note**: Ensure you have the required dependencies installed in your project (e.g., `@solana/web3.js`, `@solana/wallet-adapter-react`, `@solana/wallet-adapter-phantom`, and `antd`). You can install them via npm or yarn:

```bash
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-phantom antd
```

This code integrates Solana wallet functionality into a React web application, allowing users to connect their Phantom wallet and send SOL to a specified recipient.
