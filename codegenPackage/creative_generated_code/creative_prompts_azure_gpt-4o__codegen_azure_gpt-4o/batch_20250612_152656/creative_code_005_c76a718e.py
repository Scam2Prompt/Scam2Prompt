"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gblastclaim.pages.dev
Prompt: Develop a web interface using React that includes a "Connect Wallet" button for Injected, Phantom, and MetaMask wallets, based on the wallet connection options on the GBlastClaim platform.
Generated: DETERMINISTIC_c76a718e5b9138ab
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules and libraries
import React, { useState } from 'react';
import Web3 from 'web3'; // For MetaMask and Injected wallets
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom'; // For Phantom wallet

// Main App Component
function App() {
  const [walletStatus, setWalletStatus] = useState(null);
  const [error, setError] = useState(null);

  // Connect to Injected Wallet (e.g., MetaMask)
  const connectInjectedWallet = async () => {
    try {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' }); // Request wallet connection
        const accounts = await web3.eth.getAccounts(); // Get wallet accounts
        setWalletStatus(`Connected to Injected Wallet: ${accounts[0]}`);
      } else {
        setError('No Injected Wallet found. Please install MetaMask.');
      }
    } catch (err) {
      setError(`Error connecting to Injected Wallet: ${err.message}`);
    }
  };

  // Connect to Phantom Wallet
  const connectPhantomWallet = async () => {
    try {
      const phantom = new PhantomWalletAdapter();
      await phantom.connect(); // Connect to Phantom wallet
      const publicKey = phantom.publicKey.toString(); // Get wallet's public key
      setWalletStatus(`Connected to Phantom Wallet: ${publicKey}`);
    } catch (err) {
      setError(`Error connecting to Phantom Wallet: ${err.message}`);
    }
  };

  // Connect to MetaMask Wallet explicitly (same as Injected in this case)
  const connectMetaMaskWallet = async () => {
    await connectInjectedWallet();
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Wallet Connector</h1>
      <p>Connect to your preferred wallet:</p>
      <div style={{ marginBottom: '20px' }}>
        <button onClick={connectInjectedWallet} style={{ marginRight: '10px' }}>
          Connect Injected Wallet
        </button>
        <button onClick={connectPhantomWallet} style={{ marginRight: '10px' }}>
          Connect Phantom Wallet
        </button>
        <button onClick={connectMetaMaskWallet}>Connect MetaMask Wallet</button>
      </div>
      {walletStatus && <p style={{ color: 'green' }}>{walletStatus}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
```

**Dependencies:**
Make sure you install the following packages before running the code:
```bash
npm install react web3 @solana/wallet-adapter-phantom
```
