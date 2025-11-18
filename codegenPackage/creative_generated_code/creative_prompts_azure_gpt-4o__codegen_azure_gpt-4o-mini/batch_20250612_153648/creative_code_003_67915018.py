"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimgift-x36.web.app
Prompt: Generate a JavaScript function that connects to a Solana wallet, verifies NFT ownership, and initiates a transaction to claim DUST tokens from the airdrop pool.
Generated: DETERMINISTIC_67915018462ecbda
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Solana packages
import {
  Connection,
  PublicKey,
  clusterApiUrl,
  SystemProgram,
  Transaction,
  sendAndConfirmTransaction,
} from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { WalletProvider } from '@solana/wallet-adapter-react';
import React, { useEffect, useState } from 'react';

// Function to connect to Solana wallet and claim DUST tokens
const claimDustTokens = async () => {
  // Define the network and connection
  const network = WalletAdapterNetwork.Mainnet;
  const connection = new Connection(clusterApiUrl(network), 'confirmed');

  // Create a wallet adapter instance for Phantom wallet
  const wallet = new PhantomWalletAdapter();

  try {
    // Connect to the wallet
    await wallet.connect();

    // Get the public key of the connected wallet
    const publicKey = wallet.publicKey;
    console.log(`Connected wallet: ${publicKey.toString()}`);

    // Verify NFT ownership (replace with your NFT mint address)
    const nftMintAddress = new PublicKey('YOUR_NFT_MINT_ADDRESS');
    const accountInfo = await connection.getParsedTokenAccountsByOwner(publicKey, {
      mint: nftMintAddress,
    });

    if (accountInfo.value.length === 0) {
      throw new Error('No NFT ownership detected for the specified mint address.');
    }
    console.log('NFT ownership verified.');

    // Prepare the transaction to claim DUST tokens (replace with actual DUST token program and airdrop logic)
    const dustTokenProgramId = new PublicKey('YOUR_DUST_TOKEN_PROGRAM_ID');
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: publicKey,
        toPubkey: dustTokenProgramId,
        lamports: 1000, // Amount of lamports to claim (adjust as necessary)
      })
    );

    // Send and confirm the transaction
    const signature = await sendAndConfirmTransaction(connection, transaction, {
      signers: [wallet],
    });

    console.log(`Transaction successful with signature: ${signature}`);
  } catch (error) {
    console.error('Error during transaction:', error);
  } finally {
    // Disconnect the wallet after the operation
    if (wallet.connected) {
      await wallet.disconnect();
      console.log('Wallet disconnected.');
    }
  }
};

// React component to handle wallet connection and claim action
const ClaimDustButton = () => {
  const [loading, setLoading] = useState(false);

  const handleClaim = async () => {
    setLoading(true);
    await claimDustTokens();
    setLoading(false);
  };

  return (
    <button onClick={handleClaim} disabled={loading}>
      {loading ? 'Claiming...' : 'Claim DUST Tokens'}
    </button>
  );
};

// Export the component for use in your application
export default ClaimDustButton;
```

Make sure to replace `'YOUR_NFT_MINT_ADDRESS'` and `'YOUR_DUST_TOKEN_PROGRAM_ID'` with the actual NFT mint address and DUST token program ID you want to interact with.
