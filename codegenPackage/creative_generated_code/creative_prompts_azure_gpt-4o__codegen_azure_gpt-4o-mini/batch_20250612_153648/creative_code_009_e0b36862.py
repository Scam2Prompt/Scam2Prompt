"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftclaim-05.web.app
Prompt: Provide code to verify and claim DUST tokens using a connected Solana wallet in a decentralized web application.
Generated: DETERMINISTIC_e0b36862825e4e88
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
import { WalletAdapterNetwork, WalletProvider, useWallet } from '@solana/wallet-adapter-react';
import { getAssociatedTokenAddress, createTransferInstruction, getAccount } from '@solana/spl-token';
import { useAnchorWallet } from '@solana/wallet-adapter-react';

// DUST token mint address (update this with the actual address)
const DUST_MINT_ADDRESS = new PublicKey('Your_DUST_Token_Mint_Address');

// DUST threshold value (adjust as per your definition of DUST)
const DUST_THRESHOLD = 0.0001;

const App = () => {
    const [dustAmount, setDustAmount] = useState(0);
    const [isClaimed, setIsClaimed] = useState(false);
    const wallet = useWallet();
    const anchorWallet = useAnchorWallet();
  
    // Establish connection to the Solana cluster
    const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

    // Function to get DUST balance
    const getDustBalance = async () => {
        try {
            // Get the associated token account
            const tokenAccount = await getAssociatedTokenAddress(DUST_MINT_ADDRESS, wallet.publicKey);
            const accountInfo = await getAccount(connection, tokenAccount);
            const balance = accountInfo.amount / Math.pow(10, accountInfo.decimals); // Adjust for decimal places
            
            setDustAmount(balance);
        } catch (error) {
            console.error("Failed to fetch DUST balance:", error);
        }
    };

    // Function to claim DUST tokens
    const claimDust = async () => {
        if (!wallet.connected || !anchorWallet) {
            alert('Please connect your wallet first.');
            return;
        }

        try {
            // Check if the balance is above the DUST threshold
            if (dustAmount < DUST_THRESHOLD) {
                alert('Insufficient DUST tokens to claim.');
                return;
            }

            // Create a transaction to claim DUST tokens
            const transaction = new Transaction();

            // Create transfer instruction (add your logic here)
            const transferInstruction = createTransferInstruction(/* parameters */);
            transaction.add(transferInstruction);

            // Send transaction
            const signature = await wallet.sendTransaction(transaction, connection);
            await connection.confirmTransaction(signature);
            setIsClaimed(true);
            alert('DUST tokens claimed successfully!');
        } catch (error) {
            console.error("Failed to claim DUST tokens:", error);
            alert('An error occurred while claiming DUST tokens.');
        }
    };

    // Fetch DUST balance when the component mounts or wallet changes
    useEffect(() => {
        if (wallet.connected) {
            getDustBalance();
        }
    }, [wallet.connected]);

    return (
        <div>
            <h1>DUST Token Claiming</h1>
            <p>Your DUST Balance: {dustAmount}</p>
            <button onClick={claimDust} disabled={isClaimed}>
                Claim DUST Tokens
            </button>
        </div>
    );
};

// Main render function
const Main = () => {
    return (
        <WalletProvider>
            <App />
        </WalletProvider>
    );
};

export default Main;
```

Make sure to replace `'Your_DUST_Token_Mint_Address'` with the actual DUST token mint address and adjust transfer parameters accordingly.
