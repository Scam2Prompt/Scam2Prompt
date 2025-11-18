"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-usdh-mint.web.app
Prompt: Create a Solana-based minting dApp that differentiates between whitelist and public minting prices, ensuring free minting rights for eligible token holders.
Generated: DETERMINISTIC_c18af29f80ffa7ce
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
import {
  Connection,
  PublicKey,
  Transaction,
  SystemProgram,
  sendAndConfirmTransaction,
} from '@solana/web3.js';
import { useEffect, useState } from 'react';
import { useWallet } from '@solana/wallet-adapter-react';
import { toast } from 'react-toastify';

// Constants for the program and minting
const WHITELIST_PRICE = 0.1; // Price for whitelist minting in SOL
const PUBLIC_PRICE = 0.2; // Price for public minting in SOL
const WHITELISTED_ADDRESSES = []; // Add whitelist addresses here

const MintingApp = () => {
  const wallet = useWallet(); // Access the connected wallet
  const [userAddress, setUserAddress] = useState(null);
  const [isWhitelisted, setIsWhitelisted] = useState(false);
  
  // Effect to set user address and check whitelist status
  useEffect(() => {
    if (wallet.connected) {
      setUserAddress(wallet.publicKey.toString());
      checkWhitelistStatus(wallet.publicKey.toString());
    }
  }, [wallet.connected, wallet.publicKey]);

  // Function to check if the user is whitelisted
  const checkWhitelistStatus = (address) => {
    setIsWhitelisted(WHITELISTED_ADDRESSES.includes(address));
  };

  // Function to handle the minting process
  const handleMint = async () => {
    if (!wallet.connected) {
      toast.error("Please connect your wallet.");
      return;
    }

    const price = isWhitelisted ? WHITELIST_PRICE : PUBLIC_PRICE;

    // Construct minting transaction
    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: wallet.publicKey,
        toPubkey: new PublicKey("<MINTING_ADDRESS>"), // Replace with actual minting address
        lamports: price * LAMPORTS_PER_SOL, // Convert SOL to lamports
      })
    );

    try {
      // Send and confirm transaction
      const signature = await sendAndConfirmTransaction(
        new Connection("<RPC_URL>"), // Replace with actual RPC URL
        transaction,
        { signers: [wallet] }
      );
      toast.success(`Minting successful! Transaction: ${signature}`);
    } catch (error) {
      console.error("Minting failed", error);
      toast.error("Minting failed. Please try again.");
    }
  };

  return (
    <div>
      <h1>Minting dApp</h1>
      <p>Connected as: {userAddress}</p>
      <p>
        Minting Price: {isWhitelisted ? WHITELIST_PRICE : PUBLIC_PRICE} SOL
      </p>
      <button onClick={handleMint}>Mint</button>
    </div>
  );
};

export default MintingApp;
```

Make sure to replace `<MINTING_ADDRESS>` with the actual minting address and `<RPC_URL>` with the proper RPC URL for your Solana cluster.
