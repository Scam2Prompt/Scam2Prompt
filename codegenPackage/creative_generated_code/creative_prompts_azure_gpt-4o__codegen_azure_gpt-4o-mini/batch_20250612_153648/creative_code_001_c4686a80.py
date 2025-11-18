"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-daor.web.app
Prompt: Generate code to integrate a Solana wallet connection feature into a web application, allowing users to claim rewards in $TNSR tokens based on their activity on the Tensor platform.
Generated: DETERMINISTIC_c4686a80871c1838
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
import React, { useState, useEffect } from 'react';
import { Connection, PublicKey, Transaction, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { ConnectionProvider, WalletProvider } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Solana network configuration
const network = WalletAdapterNetwork.Mainnet; // Change to Devnet or Testnet as needed
const endpoint = clusterApiUrl(network);

// Component for Wallet Connection and Reward Claiming
const WalletConnector = () => {
    // State to hold the connected wallet and user activity data
    const [wallet, setWallet] = useState(null);
    const [userActivity, setUserActivity] = useState({}); // Example object structure
    
    // Function to connect wallet
    const connectWallet = async () => {
        if (wallet) {
            try {
                await wallet.connect();
                toast.success("Wallet connected successfully!");
            } catch (error) {
                toast.error("Failed to connect wallet. Please try again.");
                console.error("Wallet connection error:", error);
            }
        }
    };

    // Function to claim rewards
    const claimRewards = async () => {
        if (!wallet) {
            toast.warn("Please connect your wallet first.");
            return;
        }

        try {
            // Assuming the reward claiming logic is implemented in this function
            const connection = new Connection(endpoint, 'confirmed');
            const publicKey = wallet.publicKey;

            // Example: Create a transaction to claim rewards
            const transaction = new Transaction().add(
                // Add your instruction here to claim $TNSR based on user activity
            );

            // Send transaction and await confirmation
            const signature = await wallet.sendTransaction(transaction, connection);
            await connection.confirmTransaction(signature, 'processed');
            toast.success("Rewards claimed successfully!");

        } catch (error) {
            toast.error("Failed to claim rewards. Please try again.");
            console.error("Reward claiming error:", error);
        }
    };

    // Effect to set up wallet connection
    useEffect(() => {
        const adapter = new PhantomWalletAdapter();
        setWallet(adapter);
        
        // Auto connect if wallet is already connected
        (async () => {
            if (adapter.connected) {
                await connectWallet();
            }
        })();
    }, []);

    return (
        <div>
            <h1>Solana Wallet Connector</h1>
            <button onClick={connectWallet}>Connect Wallet</button>
            <button onClick={claimRewards}>Claim Rewards</button>
            <ToastContainer />
        </div>
    );
};

// Main App component to provide Wallet context
const App = () => {
    return (
        <ConnectionProvider endpoint={endpoint}>
            <WalletProvider wallets={[new PhantomWalletAdapter()]}>
                <WalletConnector />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Export the App component as default
export default App;
```

### Notes:
- Ensure to install the required dependencies: `@solana/web3.js`, `@solana/wallet-adapter-react`, `@solana/wallet-adapter-phantom`, and `react-toastify` via NPM.
- Customize the transaction logic in `claimRewards` function based on how you intend to claim $TNSR tokens on the Tensor platform.
- Make sure to handle user activity data accordingly to adjust reward claims as necessary.
