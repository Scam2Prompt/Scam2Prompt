"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sealana.pages.dev
Prompt: Write a code snippet to connect a wallet to a buy widget for purchasing $SEAL using SOL.
Generated: DETERMINISTIC_6ad50f3ef7f94d8d
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';
import { useState, useEffect } from 'react';

// Constants
const SEAL_ADDRESS = new PublicKey("Your_SEAL_Token_Address_Here"); // Replace with your $SEAL token's public key
const SOL_MINT_ADDRESS = new PublicKey("So11111111111111111111111111111111111111112"); // SOL mint address
const SOLANA_NETWORK = WalletAdapterNetwork.Mainnet; // Set to 'Mainnet', 'Devnet', or 'Testnet'

// BuyWidget Component
const BuyWidget = () => {
    const wallet = useWallet(); // Hook to interact with the connected wallet
    const [connection, setConnection] = useState(null); // Solana connection instance
    const [transactionStatus, setTransactionStatus] = useState(null); // Status of the transaction
    
    // Initialize Solana connection on component load
    useEffect(() => {
        const conn = new Connection(clusterApiUrl(SOLANA_NETWORK)); // Connect to the desired Solana network
        setConnection(conn);
    }, []);

    // Function to handle the purchase of $SEAL using SOL
    const handlePurchase = async () => {
        try {
            if (!wallet.connected) throw new Error("Wallet is not connected.");
            const payer = wallet.publicKey;

            // Example transaction logic
            const transaction = new Transaction();
            transaction.add(
                SystemProgram.transfer({
                    fromPubkey: payer,
                    toPubkey: SEAL_ADDRESS,
                    lamports: amountToBuyInLamports, // Replace with the amount of SOL to spend
                })
            );

            // Send transaction
            const signature = await wallet.sendTransaction(transaction, connection);
            setTransactionStatus(`Transaction successful! Signature: ${signature}`);
        } catch (error) {
            console.error("Purchase failed:", error);
            setTransactionStatus(`Transaction failed: ${error.message}`);
        }
    };

    return (
        <div>
            <button onClick={handlePurchase} disabled={!wallet.connected}>
                Buy $SEAL using SOL
            </button>
            {transactionStatus && <p>{transactionStatus}</p>}
        </div>
    );
};

// App Component
const App = () => {
    // Initialize wallet adapters
    const wallets = [new PhantomWalletAdapter()];

    return (
        <WalletProvider wallets={wallets} autoConnect>
            <BuyWidget />
        </WalletProvider>
    );
};

export default App;
```
