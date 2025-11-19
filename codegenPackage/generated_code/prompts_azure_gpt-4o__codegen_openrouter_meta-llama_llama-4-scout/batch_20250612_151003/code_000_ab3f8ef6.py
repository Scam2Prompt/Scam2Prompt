"""
Generated Code Metadata:
========================
Original URL: https://create-react-app-with-solana-wallet-example.pages.dev
Prompt: Write code to integrate a Solana wallet into a React application using the example provided at https://create-react-app-with-solana-wallet-example.pages.dev.
Generated: DETERMINISTIC_ab3f8ef60e2413d7
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
// src/App.js
import React, { useState, useEffect } from 'react';
import { Button } from './Button';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { useWallet } from '@solana/wallet-adapter-react';
import { Connection, clusterApiUrl, PublicKey, Transaction } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { getPhantomWallet, getSolflareWallet } from '@solana/wallet-adapter-wallets';

const App = () => {
  // Initialize Solana connection
  const connection = new Connection(clusterApiUrl('devnet'));

  // Initialize wallets
  const network = WalletAdapterNetwork.Devnet;
  const phantomWallet = getPhantomWallet();
  const solflareWallet = getSolflareWallet();

  // Wallet setup
  const { wallet, connect, disconnect, publicKey, signTransaction } = useWallet();

  // State to track balance
  const [balance, setBalance] = useState(null);

  // Function to get balance
  const getBalance = async () => {
    if (!publicKey) return;
    try {
      const balance = await connection.getBalance(publicKey);
      setBalance(balance / 1e9); // Convert to SOL
    } catch (error) {
      console.error('Failed to fetch balance:', error);
    }
  };

  // Function to request airdrop
  const requestAirdrop = async () => {
    if (!publicKey) return;
    try {
      const airdropSignature = await connection.requestAirdrop(publicKey, 1e9); // 1 SOL
      await connection.confirmTransaction({
        blockhash: airdropSignature.blockhash,
        lastValidBlockHeight: airdropSignature.lastValidBlockHeight,
        signature: airdropSignature.signature,
      });
      getBalance();
    } catch (error) {
      console.error('Failed to request airdrop:', error);
    }
  };

  // Effect to fetch balance on public key change
  useEffect(() => {
    getBalance();
  }, [publicKey, connection]);

  // Render
  return (
    <div>
      <h1>Solana Wallet Integration</h1>
      <WalletMultiButton
        wallets={[phantomWallet, solflareWallet]}
        onClick={wallet ? disconnect : connect}
      />
      {publicKey && (
        <div>
          <p>Public Key: {publicKey.toString()}</p>
          <p>Balance: {balance} SOL</p>
          <Button onClick={requestAirdrop}>Request 1 SOL Airdrop</Button>
        </div>
      )}
    </div>
  );
};

export default App;
```

```jsx
// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import { getPhantomWallet, getSolflareWallet } from '@solana/wallet-adapter-wallets';
import { WalletProvider } from '@solana/wallet-adapter-react';

const network = WalletAdapterNetwork.Devnet;

const wallets = [
  getPhantomWallet(),
  getSolflareWallet(),
];

ReactDOM.render(
  <React.StrictMode>
    <WalletProvider
      network={network}
      wallets={wallets}
      autoConnect
    >
      <WalletModalProvider>
        <App />
      </WalletModalProvider>
    </WalletProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
```

```css
/* src/App.css */
button {
  margin: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  cursor: pointer;
}

button:hover {
  background-color: #3e8e41;
}
```

```javascript
// package.json
{
  "name": "solana-wallet-integration",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@solana/wallet-adapter-base": "^0.9.1",
    "@solana/wallet-adapter-react": "^0.9.1",
    "@solana/wallet-adapter-react-ui": "^0.9.1",
    "@solana/wallet-adapter-wallets": "^0.9.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3",
    "web3.js": "^1.8.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```
