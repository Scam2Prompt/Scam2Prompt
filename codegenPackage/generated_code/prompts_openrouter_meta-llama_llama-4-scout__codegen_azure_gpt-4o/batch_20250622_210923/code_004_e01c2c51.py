"""
Generated Code Metadata:
========================
Original URL: https://www.zkfinance.org
Prompt: Develop a simple user interface for users to connect their wallets and access zkFinance's borrowing, lending, and swapping features, highlighting the benefits of using zkSync for fast and cheap transactions.
Generated: DETERMINISTIC_e01c2c51229a8e18
Batch ID: 20250622_210923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import { zkSyncProvider, zkSyncWallet } from 'zksync'; // Hypothetical zkSync library
import './App.css'; // Import CSS for styling

// Main App Component
function App() {
  // State variables
  const [walletConnected, setWalletConnected] = useState(false);
  const [walletAddress, setWalletAddress] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [zkSyncInstance, setZkSyncInstance] = useState(null);

  // Connect Wallet Function
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const accounts = await provider.send('eth_requestAccounts', []);
        const address = accounts[0];
        setWalletAddress(address);
        setWalletConnected(true);

        // Initialize zkSync instance
        const zkSync = await zkSyncProvider.initialize(provider);
        setZkSyncInstance(zkSync);
      } else {
        setErrorMessage('Please install MetaMask or a compatible wallet.');
      }
    } catch (error) {
      setErrorMessage(`Error connecting wallet: ${error.message}`);
    }
  };

  // Borrow Function
  const borrow = async () => {
    try {
      if (!zkSyncInstance) throw new Error('zkSync instance not initialized.');
      // Example borrow logic
      await zkSyncInstance.borrow({ amount: 100, asset: 'USDC' });
      alert('Borrowing successful!');
    } catch (error) {
      setErrorMessage(`Error borrowing: ${error.message}`);
    }
  };

  // Lend Function
  const lend = async () => {
    try {
      if (!zkSyncInstance) throw new Error('zkSync instance not initialized.');
      // Example lend logic
      await zkSyncInstance.lend({ amount: 100, asset: 'USDC' });
      alert('Lending successful!');
    } catch (error) {
      setErrorMessage(`Error lending: ${error.message}`);
    }
  };

  // Swap Function
  const swap = async () => {
    try {
      if (!zkSyncInstance) throw new Error('zkSync instance not initialized.');
      // Example swap logic
      await zkSyncInstance.swap({ fromAsset: 'ETH', toAsset: 'USDC', amount: 1 });
      alert('Swap successful!');
    } catch (error) {
      setErrorMessage(`Error swapping: ${error.message}`);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>zkFinance Interface</h1>
        <p>Fast and cheap transactions powered by zkSync.</p>
        {!walletConnected ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <p>Wallet Connected: {walletAddress}</p>
            <button onClick={borrow}>Borrow</button>
            <button onClick={lend}>Lend</button>
            <button onClick={swap}>Swap</button>
          </div>
        )}
        {errorMessage && <p className="error">{errorMessage}</p>}
      </header>
    </div>
  );
}

export default App;
```

### Notes:
- This code assumes the existence of a hypothetical `zksync` library for interacting with zkSync.
- Replace `zkSyncProvider` and `zkSyncWallet` with actual zkSync SDK methods if available.
- Ensure proper CSS styling in `App.css` for a polished UI.
