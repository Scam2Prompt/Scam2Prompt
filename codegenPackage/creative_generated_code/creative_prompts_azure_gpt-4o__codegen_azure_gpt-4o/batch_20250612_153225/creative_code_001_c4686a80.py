"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fsdffllfllllaa.web.app
Prompt: Generate code to integrate a Solana wallet connection feature into a web application, allowing users to claim rewards in $TNSR tokens based on their activity on the Tensor platform.
Generated: DETERMINISTIC_c4686a80871c1838
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required packages
import { Connection, PublicKey, Transaction, clusterApiUrl } from "@solana/web3.js";
import { useState } from "react";
import { useWallet, WalletProvider } from "@solana/wallet-adapter-react";
import { WalletModalProvider, WalletMultiButton } from "@solana/wallet-adapter-react-ui";
import { PhantomWalletAdapter } from "@solana/wallet-adapter-wallets";
import "@solana/wallet-adapter-react-ui/styles.css";

// Constants
const TOKEN_PROGRAM_ID = new PublicKey("TokenProgramAddress"); // Replace with the real token program address
const REWARD_AMOUNT = 10; // Example reward amount in $TNSR tokens
const TENSOR_PLATFORM_PUBLIC_KEY = new PublicKey("TensorPlatformPublicKey"); // Replace with Tensor's platform public key

// Main App Component
const App = () => {
    const [claimStatus, setClaimStatus] = useState(null); // Tracks reward claim status
    const wallet = useWallet(); // Wallet connection
    
    // Function to claim rewards
    const claimRewards = async () => {
        if (!wallet.connected) {
            setClaimStatus("Please connect your wallet.");
            return;
        }
        
        try {
            const connection = new Connection(clusterApiUrl("mainnet-beta")); // Connect to Solana mainnet
            const transaction = new Transaction();

            // Add instructions for token transfer (reward claim)
            transaction.add(
                // Replace with your custom instruction to transfer $TNSR rewards.
                // This is an example instruction. Use the correct token program logic.
                SystemProgram.transfer({
                    fromPubkey: TENSOR_PLATFORM_PUBLIC_KEY, // Tensor platform's public key
                    toPubkey: wallet.publicKey,             // Recipient's public key
                    lamports: REWARD_AMOUNT * LAMPORTS_PER_SOL, // Convert reward amount to lamports
                })
            );

            // Send the transaction
            const signature = await wallet.sendTransaction(transaction, connection);

            // Confirm transaction
            const confirmation = await connection.confirmTransaction(signature, "confirmed");
            if (confirmation.value.err) {
                setClaimStatus("Error while claiming rewards.");
            } else {
                setClaimStatus("Rewards successfully claimed!");
            }
        } catch (error) {
            console.error("Error during reward claim:", error);
            setClaimStatus("An error occurred while claiming rewards.");
        }
    };

    return (
        <div style={{ padding: "20px" }}>
            <h1>Tensor Platform Rewards</h1>
            <WalletMultiButton /> {/* Wallet Connection Button */}
            
            <button onClick={claimRewards} disabled={!wallet.connected}>
                Claim $TNSR Rewards
            </button>
            
            {claimStatus && <p>{claimStatus}</p>}
        </div>
    );
};

// Wrapper Component for Wallet Integration
const WalletIntegrationWrapper = () => {
    const wallets = [new PhantomWalletAdapter()]; // Add more wallets if needed

    return (
        <WalletProvider wallets={wallets} autoConnect>
            <WalletModalProvider>
                <App />
            </WalletModalProvider>
        </WalletProvider>
    );
};

export default WalletIntegrationWrapper;
```

**Note:** Replace placeholders (e.g., `TokenProgramAddress`, `TensorPlatformPublicKey`) with actual values. Confirm token program and reward logic with your Solana smart contract developer before deployment.
