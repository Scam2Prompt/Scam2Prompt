"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theufa.ru
Prompt: Develop a web interface for transferring SOL with WalletConnect, including fields for recipient address, transfer amount, and network selection (Mainnet, Devnet, Testnet).
Generated: DETERMINISTIC_d766300f65a50d8d
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import { Connection, clusterApiUrl, Keypair, LAMPORTS_PER_SOL, PublicKey, Transaction, SystemProgram, sendAndConfirmTransaction } from '@solana/web3.js';
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3Modal from "web3modal";

// Define the App component
const App = () => {
    // Define state variables
    const [recipientAddress, setRecipientAddress] = useState('');
    const [transferAmount, setTransferAmount] = useState('');
    const [network, setNetwork] = useState('Mainnet');
    const [provider, setProvider] = useState(null);

    // Handle wallet connection
    const connectWallet = async () => {
        const providerOptions = {
            walletconnect: {
                package: WalletConnectProvider,
                options: {
                    qrcode: true
                }
            }
        };

        const web3Modal = new Web3Modal({
            providerOptions
        });

        const connection = await web3Modal.connect();
        setProvider(connection);
    };

    // Handle transfer of SOL
    const handleTransfer = async () => {
        if (!provider) {
            alert("Please connect your wallet first.");
            return;
        }

        try {
            const connection = new Connection(clusterApiUrl(network.toLowerCase()), 'confirmed');
            const fromWallet = provider.selectedAddress;
            const toWallet = new PublicKey(recipientAddress);
            const amount = parseFloat(transferAmount) * LAMPORTS_PER_SOL; // Convert SOL to lamports

            // Create a transaction
            const transaction = new Transaction().add(
                SystemProgram.transfer({
                    fromPubkey: new PublicKey(fromWallet),
                    toPubkey: toWallet,
                    lamports: amount,
                })
            );

            // Send and confirm the transaction
            const signature = await sendAndConfirmTransaction(connection, transaction, {skipPreflight: false});
            alert(`Transaction successful with signature: ${signature}`);
        } catch (error) {
            console.error("Transaction failed:", error);
            alert("Transaction failed. Please check the console for details.");
        }
    };

    return (
        <div>
            <h1>SOL Transfer with WalletConnect</h1>
            <button onClick={connectWallet}>Connect Wallet</button>
            <div>
                <label>
                    Recipient Address:
                    <input 
                        type="text" 
                        value={recipientAddress} 
                        onChange={(e) => setRecipientAddress(e.target.value)} 
                    />
                </label>
                <label>
                    Transfer Amount (SOL):
                    <input 
                        type="number" 
                        value={transferAmount} 
                        onChange={(e) => setTransferAmount(e.target.value)} 
                    />
                </label>
                <label>
                    Select Network:
                    <select value={network} onChange={(e) => setNetwork(e.target.value)}>
                        <option value="Mainnet">Mainnet</option>
                        <option value="Devnet">Devnet</option>
                        <option value="Testnet">Testnet</option>
                    </select>
                </label>
                <button onClick={handleTransfer}>Transfer SOL</button>
            </div>
        </div>
    );
};

export default App;
```

Please ensure you have the necessary dependencies installed in your project:

```bash
npm install @solana/web3.js web3modal @walletconnect/web3-provider
```
