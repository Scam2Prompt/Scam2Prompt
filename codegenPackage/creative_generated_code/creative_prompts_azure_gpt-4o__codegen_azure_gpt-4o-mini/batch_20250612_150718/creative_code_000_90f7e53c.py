"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theufa.ru
Prompt: Write code to integrate WalletConnect for transferring SOL on the Solana blockchain, allowing users to select networks like Mainnet, Devnet, or Testnet.
Generated: DETERMINISTIC_90f7e53ca90ce17f
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import { WalletConnectProvider } from "@walletconnect/web3-provider";
import { Connection, clusterApiUrl, PublicKey, Transaction, SystemProgram } from "@solana/web3.js";

// Define a class for SolanaWalletConnect
class SolanaWalletConnect {
    constructor() {
        // Initialize the provider
        this.provider = new WalletConnectProvider({
            infuraId: "YOUR_INFURA_ID", // Optional: required for some networks
        });
        
        this.connection = null;
        this.selectedNetwork = null;
    }

    // Connect to the selected network
    async connect(network) {
        try {
            this.selectedNetwork = network;
            const endpoint = this.getClusterApiUrl(network);
            this.connection = new Connection(endpoint, "confirmed");

            // Enable session (triggers QR Code modal)
            await this.provider.enable();
        } catch (error) {
            console.error("Connection error: ", error);
            throw new Error("Failed to connect to wallet.");
        }
    }

    // Get cluster API URL based on the selected network
    getClusterApiUrl(network) {
        switch (network) {
            case 'mainnet':
                return clusterApiUrl('mainnet-beta');
            case 'devnet':
                return clusterApiUrl('devnet');
            case 'testnet':
                return clusterApiUrl('testnet');
            default:
                throw new Error("Invalid network selected.");
        }
    }

    // Transfer SOL to a specific address
    async transferSOL(toAddress, amount) {
        if (!this.connection) {
            throw new Error("Wallet not connected. Please connect to a wallet first.");
        }

        try {
            const fromPublicKey = new PublicKey(this.provider.accounts[0]);
            const toPublicKey = new PublicKey(toAddress);

            // Create a transaction
            const transaction = new Transaction().add(
                SystemProgram.transfer({
                    fromPubkey: fromPublicKey,
                    toPubkey: toPublicKey,
                    lamports: amount * 1e9, // Convert SOL to lamports (1 SOL = 1 billion lamports)
                })
            );

            // Send the transaction
            const signature = await this.connection.sendTransaction(transaction, [fromPublicKey]);
            await this.connection.confirmTransaction(signature, 'confirmed');
            
            console.log("Transaction successful with signature: ", signature);
        } catch (error) {
            console.error("Transaction error: ", error);
            throw new Error("Failed to transfer SOL.");
        }
    }

    // Disconnect the wallet
    async disconnect() {
        try {
            await this.provider.disconnect();
            this.connection = null;
            this.selectedNetwork = null;
        } catch (error) {
            console.error("Disconnection error: ", error);
            throw new Error("Failed to disconnect from wallet.");
        }
    }
}

// Example usage
(async () => {
    const walletConnect = new SolanaWalletConnect();

    // Connect to the Devnet
    await walletConnect.connect('devnet');

    // Transfer 0.1 SOL to a recipient address
    try {
        await walletConnect.transferSOL("RECIPIENT_PUBLIC_KEY_HERE", 0.1);
    } catch (error) {
        console.error("Error transferring SOL: ", error.message);
    }

    // Disconnect the wallet
    await walletConnect.disconnect();
})();
```

**Note:** Replace `"YOUR_INFURA_ID"` with your actual Infura ID and `"RECIPIENT_PUBLIC_KEY_HERE"` with the actual recipient's public key. This code requires installation of the `@walletconnect/web3-provider` and `@solana/web3.js` packages.
