"""
Generated Code Metadata:
========================
Original URL: https://matrica15.vercel.app
Prompt: Generate code for displaying a dropdown menu to select a blockchain network (Solana, Ethereum, Polygon) and handle login functionality accordingly.
Generated: DETERMINISTIC_9ace554db4f88930
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState } from 'react';
import { ethers } from 'ethers';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';

/**
 * BlockchainNetworkSelector Component
 * 
 * Handles network selection and login functionality for different blockchain networks.
 */
const BlockchainNetworkSelector = () => {
  const [selectedNetwork, setSelectedNetwork] = useState('');
  const [walletAddress, setWalletAddress] = useState('');
  const [error, setError] = useState('');

  // Supported networks
  const networks = [
    { value: 'solana', label: 'Solana' },
    { value: 'ethereum', label: 'Ethereum' },
    { value: 'polygon', label: 'Polygon' }
  ];

  /**
   * Handles network selection change
   * @param {React.ChangeEvent<HTMLSelectElement>} e - The change event
   */
  const handleNetworkChange = (e) => {
    setSelectedNetwork(e.target.value);
    setWalletAddress('');
    setError('');
  };

  /**
   * Handles login based on selected network
   */
  const handleLogin = async () => {
    try {
      if (!selectedNetwork) {
        throw new Error('Please select a network');
      }

      switch (selectedNetwork) {
        case 'ethereum':
          await loginWithEthereum();
          break;
        case 'polygon':
          await loginWithPolygon();
          break;
        case 'solana':
          await loginWithSolana();
          break;
        default:
          throw new Error('Unsupported network');
      }
    } catch (err) {
      setError(err.message);
      console.error('Login error:', err);
    }
  };

  /**
   * Login with Ethereum network
   */
  const loginWithEthereum = async () => {
    if (!window.ethereum) {
      throw new Error('MetaMask not installed');
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();
    const address = await signer.getAddress();
    setWalletAddress(address);
  };

  /**
   * Login with Polygon network
   */
  const loginWithPolygon = async () => {
    if (!window.ethereum) {
      throw new Error('MetaMask not installed');
    }

    // Polygon uses the same Ethereum provider but different network
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    await provider.send("eth_requestAccounts", []);
    const signer = provider.getSigner();
    const address = await signer.getAddress();
    setWalletAddress(address);
  };

  /**
   * Login with Solana network
   */
  const loginWithSolana = async () => {
    if (!window.solana) {
      throw new Error('Phantom wallet not installed');
    }

    const connection = new Connection(clusterApiUrl(WalletAdapterNetwork.Mainnet));
    const response = await window.solana.connect();
    const publicKey = new PublicKey(response.publicKey.toString());
    setWalletAddress(publicKey.toString());
  };

  return (
    <div className="network-selector">
      <h2>Select Blockchain Network</h2>
      
      <select 
        value={selectedNetwork} 
        onChange={handleNetworkChange}
        className="network-dropdown"
      >
        <option value="">Select a network</option>
        {networks.map((network) => (
          <option key={network.value} value={network.value}>
            {network.label}
          </option>
        ))}
      </select>

      <button 
        onClick={handleLogin} 
        disabled={!selectedNetwork}
        className="login-button"
      >
        Connect Wallet
      </button>

      {walletAddress && (
        <div className="wallet-info">
          <p>Connected Wallet: {walletAddress}</p>
        </div>
      )}

      {error && (
        <div className="error-message">
          <p style={{ color: 'red' }}>{error}</p>
        </div>
      )}
    </div>
  );
};

export default BlockchainNetworkSelector;
```
