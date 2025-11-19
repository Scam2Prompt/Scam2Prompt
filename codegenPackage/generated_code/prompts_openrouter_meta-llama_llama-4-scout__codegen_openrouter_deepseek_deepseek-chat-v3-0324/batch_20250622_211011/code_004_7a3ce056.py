"""
Generated Code Metadata:
========================
Original URL: https://sol-saga-wl.web.app
Prompt: Develop a Solana Mobile Stack-based application that enables seamless onboarding onto a Solana wallet and secure transaction across dApps with ease.
Generated: DETERMINISTIC_7a3ce0569ea6e54a
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import necessary Solana Mobile Stack dependencies
import { Connection, Keypair, PublicKey, Transaction, SystemProgram, sendAndConfirmTransaction } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { Wallet } from '@solana/wallet-adapter-react';
import { useWallet } from '@solana/wallet-adapter-react';
import { WalletModalProvider, WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { SolanaMobileWalletAdapter } from '@solana-mobile/wallet-adapter-mobile';
import { clusterApiUrl } from '@solana/web3.js';
import React, { FC, ReactNode, useMemo, useState, useEffect } from 'react';
import { SnackbarProvider, useSnackbar } from 'notistack';

// Default styles for the wallet adapter
require('@solana/wallet-adapter-react-ui/styles.css');

// Main App Component
const App: FC = () => {
    return (
        <Context>
            <Content />
        </Context>
    );
};

// Context Provider for Wallet
const Context: FC<{ children: ReactNode }> = ({ children }) => {
    // Use Solana Mobile Wallet Adapter for mobile devices
    const network = WalletAdapterNetwork.Devnet;
    const endpoint = useMemo(() => clusterApiUrl(network), [network]);
    const wallets = useMemo(
        () => [
            new SolanaMobileWalletAdapter(),
        ],
        [network]
    );

    return (
        <SnackbarProvider>
            <WalletProvider wallets={wallets} autoConnect>
                <WalletModalProvider>
                    {children}
                </WalletModalProvider>
            </WalletProvider>
        </SnackbarProvider>
    );
};

// Main Content Component
const Content: FC = () => {
    const { enqueueSnackbar } = useSnackbar();
    const { publicKey, sendTransaction } = useWallet();
    const [balance, setBalance] = useState<number | null>(null);
    const [recipient, setRecipient] = useState<string>('');
    const [amount, setAmount] = useState<string>('');

    // Fetch balance when publicKey changes
    useEffect(() => {
        if (!publicKey) {
            setBalance(null);
            return;
        }

        const connection = new Connection(clusterApiUrl(WalletAdapterNetwork.Devnet));
        connection.getBalance(publicKey).then(balance => {
            setBalance(balance / 1e9); // Convert lamports to SOL
        }).catch(error => {
            enqueueSnackbar(`Error fetching balance: ${error.message}`, { variant: 'error' });
        });
    }, [publicKey, enqueueSnackbar]);

    // Handle sending SOL
    const handleSend = async () => {
        if (!publicKey || !recipient || !amount) {
            enqueueSnackbar('Please fill all fields and connect wallet', { variant: 'error' });
            return;
        }

        try {
            const recipientPubkey = new PublicKey(recipient);
            const amountInLamports = parseFloat(amount) * 1e9;

            const transaction = new Transaction().add(
                SystemProgram.transfer({
                    fromPubkey: publicKey,
                    toPubkey: recipientPubkey,
                    lamports: amountInLamports,
                })
            );

            const signature = await sendTransaction(transaction);
            enqueueSnackbar(`Transaction sent: ${signature}`, { variant: 'success' });
        } catch (error: any) {
            enqueueSnackbar(`Error sending transaction: ${error.message}`, { variant: 'error' });
        }
    };

    return (
        <div className="App">
            <div className="container">
                <div className="header">
                    <WalletMultiButton />
                </div>

                {publicKey && (
                    <div className="balance">
                        <h2>Your Balance: {balance !== null ? `${balance} SOL` : 'Loading...'}</h2>
                    </div>
                )}

                <div className="send-form">
                    <h2>Send SOL</h2>
                    <input
                        type="text"
                        placeholder="Recipient PublicKey"
                        value={recipient}
                        onChange={(e) => setRecipient(e.target.value)}
                    />
                    <input
                        type="number"
                        placeholder="Amount in SOL"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                    />
                    <button onClick={handleSend}>Send</button>
                </div>
            </div>
        </div>
    );
};

export default App;

// Error handling utility
function handleError(error: Error, enqueueSnackbar: any) {
    console.error(error);
    enqueueSnackbar(`Error: ${error.message}`, { variant: 'error' });
}

// TypeScript interfaces for props (if needed)
interface WalletProviderProps {
    wallets: Wallet[];
    autoConnect: boolean;
    children: ReactNode;
}

// Additional styles can be added via CSS-in-JS or separate stylesheet
const styles = {
    container: {
        maxWidth: '600px',
        margin: '0 auto',
        padding: '20px',
    },
    header: {
        display: 'flex',
        justifyContent: 'flex-end',
        marginBottom: '20px',
    },
    balance: {
        margin: '20px 0',
    },
    sendForm: {
        display: 'flex',
        flexDirection: 'column' as const,
        gap: '10px',
    },
};
```
