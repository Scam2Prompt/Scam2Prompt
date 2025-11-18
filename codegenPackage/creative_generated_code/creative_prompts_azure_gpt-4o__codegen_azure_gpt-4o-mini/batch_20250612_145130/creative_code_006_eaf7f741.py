"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Create a Next.js application page that allows users to connect their Solana wallet, select input and output tokens, and submit a form to initiate value averaging deposits.
Generated: DETERMINISTIC_eaf7f7415b8ad09c
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import { useEffect, useState } from 'react';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import WalletConnect from '@solana/wallet-adapter-react';
import {
  ConnectionProvider,
  WalletProvider,
  useWallet,
} from '@solana/wallet-adapter-react';
import {
  PhantomWalletAdapter,
} from '@solana/wallet-adapter-phantom';
import '@solana/wallet-adapter-react-ui/styles.css';

// Main page component
const Home = () => {
  const { wallet, connect, disconnect, publicKey } = useWallet();
  const [inputToken, setInputToken] = useState('');
  const [outputToken, setOutputToken] = useState('');
  const [amount, setAmount] = useState(0);
  
  // Handle form submission for value averaging deposit
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!wallet || !publicKey) {
      alert('Please connect your wallet first.');
      return;
    }

    try {
      // Replace with actual logic for value averaging deposit
      console.log('Initiating deposit:', { inputToken, outputToken, amount });
      // Call smart contract function or API here

      alert('Deposit submitted successfully!');
    } catch (error) {
      console.error('Error during deposit:', error);
      alert('Failed to submit deposit. Please try again later.');
    }
  };

  return (
    <div>
      <h1>Solana Value Averaging Deposits</h1>
      <button onClick={wallet ? disconnect : connect}>
        {wallet ? 'Disconnect' : 'Connect Wallet'}
      </button>
      {wallet && publicKey && (
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="inputToken">Input Token:</label>
            <input
              id="inputToken"
              type="text"
              value={inputToken}
              onChange={(e) => setInputToken(e.target.value)}
              required
            />
          </div>
          <div>
            <label htmlFor="outputToken">Output Token:</label>
            <input
              id="outputToken"
              type="text"
              value={outputToken}
              onChange={(e) => setOutputToken(e.target.value)}
              required
            />
          </div>
          <div>
            <label htmlFor="amount">Amount:</label>
            <input
              id="amount"
              type="number"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              required
            />
          </div>
          <button type="submit">Submit Deposit</button>
        </form>
      )}
    </div>
  );
};

// Main App component wrapping the WalletProvider and ConnectionProvider
const App = () => {
  const network = clusterApiUrl('devnet'); // Change to 'mainnet-beta' for production
  const connection = new Connection(network, 'confirmed');
  
  const wallets = [
    new PhantomWalletAdapter(),
  ];

  return (
    <ConnectionProvider connection={connection}>
      <WalletProvider wallets={wallets} autoConnect>
        <Home />
      </WalletProvider>
    </ConnectionProvider>
  );
};

export default App;
```
