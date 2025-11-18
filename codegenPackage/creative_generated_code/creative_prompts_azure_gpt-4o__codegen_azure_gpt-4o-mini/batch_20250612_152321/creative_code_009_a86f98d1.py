"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3modal-laboratory-qix0wwvm2-walletconnect1.vercel.app
Prompt: Provide a step-by-step example for setting up a Solana wallet integration using Web3Modal's default configuration.
Generated: DETERMINISTIC_a86f98d14a53ad9e
Batch ID: 20250612_152321
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
import Web3Modal from 'web3modal';
import { Connection, clusterApiUrl, PublicKey } from '@solana/web3.js';

// Define a functional component for the wallet integration
const WalletIntegration = () => {
  // State to hold wallet connection and user address
  const [walletConnected, setWalletConnected] = useState(false);
  const [userAddress, setUserAddress] = useState('');
  
  // Create an instance of Web3Modal
  const web3Modal = new Web3Modal({
    cacheProvider: true, // Optional
    providerOptions: {} // Add provider options if needed
  });

  // Function to connect to the wallet
  const connectWallet = async () => {
    try {
      // Open the wallet connection modal
      const instance = await web3Modal.connect();
      
      // Create a Solana connection
      const connection = new Connection(clusterApiUrl('devnet'), 'confirmed');
      
      // Get the user's wallet public key
      const wallet = new PublicKey(instance.publicKey);
      setUserAddress(wallet.toString());
      
      // Set wallet connected state
      setWalletConnected(true);
      
      console.log('Wallet connected:', wallet.toString());
    } catch (error) {
      console.error('Failed to connect wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Effect to check if the wallet is already connected
  useEffect(() => {
    const checkWalletConnection = async () => {
      try {
        const provider = await web3Modal.connect();
        if (provider) {
          const wallet = new PublicKey(provider.publicKey);
          setUserAddress(wallet.toString());
          setWalletConnected(true);
          console.log('Wallet already connected:', wallet.toString());
        }
      } catch (error) {
        console.error('Error checking wallet connection:', error);
      }
    };

    // Call the function to check for existing wallet connection
    checkWalletConnection();
  }, []);

  // Render the component
  return (
    <div>
      <h1>Solana Wallet Integration</h1>
      {walletConnected ? (
        <div>
          <p>Wallet Address: {userAddress}</p>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default WalletIntegration;
```

### Notes:
- Make sure to install the required dependencies by running: 
  ```bash
  npm install web3modal @solana/web3.js
  ```
- This example uses a simple React functional component to integrate with a Solana wallet using Web3Modal. Adjust the `providerOptions` for specific wallet providers as needed.
