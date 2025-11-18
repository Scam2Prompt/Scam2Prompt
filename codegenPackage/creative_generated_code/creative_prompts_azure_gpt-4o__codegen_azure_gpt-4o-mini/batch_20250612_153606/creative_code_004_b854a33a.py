"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-playpixiz.vercel.app
Prompt: Develop a Solana-based application that connects a user’s wallet and automates the minting of Yetiz NFTs during the presale event.
Generated: DETERMINISTIC_b854a33a7808f25d
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useEffect, useState } from 'react';
import { Connection, clusterApiUrl, Keypair, PublicKey } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletProvider, ConnectionProvider, useWallet } from '@solana/wallet-adapter-react';
import { getToken, mintNFT } from './nftService'; // Assuming these functions are defined in nftService.js
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Define the network and connection
const network = WalletAdapterNetwork.Devnet;
const endpoint = clusterApiUrl(network);
const connection = new Connection(endpoint);

// Define the App component
const App = () => {
  const [nftData, setNftData] = useState(null);
  const wallet = useWallet();

  // Fetch NFT data (presale information)
  const fetchNFTData = async () => {
    try {
      const data = await getToken(); // Fetch NFT data from the server or blockchain
      setNftData(data);
    } catch (error) {
      console.error('Failed to fetch NFT data:', error);
      toast.error('Error fetching NFT data. Please try again.');
    }
  };

  // Function to handle minting of NFTs
  const handleMintNFT = async () => {
    if (!wallet.connected) {
      toast.warn('Wallet not connected. Please connect your wallet to mint NFT.');
      return;
    }

    try {
      const mintResult = await mintNFT(wallet.publicKey, nftData);
      if (mintResult) {
        toast.success('NFT minted successfully!');
      } else {
        toast.error('Minting failed. Please try again.');
      }
    } catch (error) {
      console.error('Minting error:', error);
      toast.error('An error occurred during minting. Please try again.');
    }
  };

  // Use effect to fetch NFT data on component mount
  useEffect(() => {
    fetchNFTData();
  }, []);

  return (
    <div>
      <h1>Yetiz NFT Presale</h1>
      {wallet.connected ? (
        <div>
          <p>Connected Wallet: {wallet.publicKey.toString()}</p>
          <button onClick={handleMintNFT}>Mint Yetiz NFT</button>
        </div>
      ) : (
        <button onClick={() => wallet.connect()}>Connect Wallet</button>
      )}
      <ToastContainer />
    </div>
  );
};

// Main component rendering
const Main = () => {
  const wallet = new PhantomWalletAdapter();

  return (
    <ConnectionProvider connection={connection}>
      <WalletProvider wallets={[wallet]} autoConnect>
        <App />
      </WalletProvider>
    </ConnectionProvider>
  );
};

// Rendering the main component
export default Main;
```

This code assumes that the `getToken` and `mintNFT` functions are defined in `nftService.js`, which handles the logic for fetching NFT data and minting the NFT on Solana, respectively. Make sure to implement these functions according to your specific backend or Solana program requirements.
