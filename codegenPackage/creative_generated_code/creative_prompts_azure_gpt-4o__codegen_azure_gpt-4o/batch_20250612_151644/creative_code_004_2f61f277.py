"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-c97.pages.dev
Prompt: Write a React component that integrates wallet connection functionality and displays NFT purchase details, inspired by the nft-c97.pages.dev interface.
Generated: DETERMINISTIC_2f61f2778a40b0b0
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';

// WalletConnection Component
const WalletConnection = () => {
  const [walletAddress, setWalletAddress] = useState(null);
  const [nftDetails, setNftDetails] = useState([]);
  const [error, setError] = useState(null);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Check if MetaMask is installed
      if (!window.ethereum) {
        throw new Error('MetaMask is not installed. Please install MetaMask to continue.');
      }

      // Request wallet connection
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setWalletAddress(accounts[0]);
    } catch (err) {
      setError(err.message);
    }
  };

  // Fetch NFT purchase details (Mock API or replace with real implementation)
  const fetchNftDetails = async () => {
    try {
      // Mock data to simulate NFT purchase details
      const mockData = [
        {
          id: 1,
          name: 'NFT Alpha',
          price: '0.1 ETH',
          timestamp: '2023-10-01T12:00:00Z',
        },
        {
          id: 2,
          name: 'NFT Beta',
          price: '0.2 ETH',
          timestamp: '2023-10-02T15:30:00Z',
        },
      ];
      setNftDetails(mockData);
    } catch (err) {
      setError('Failed to fetch NFT details.');
    }
  };

  // Fetch NFT details after wallet is connected
  useEffect(() => {
    if (walletAddress) {
      fetchNftDetails();
    }
  }, [walletAddress]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>NFT Purchase Details</h1>

      {/* Wallet Connection */}
      {walletAddress ? (
        <div>
          <p>Connected Wallet: {walletAddress}</p>
        </div>
      ) : (
        <button onClick={connectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Connect Wallet
        </button>
      )}

      {/* Error Handling */}
      {error && (
        <div style={{ color: 'red', marginTop: '10px' }}>
          <strong>Error:</strong> {error}
        </div>
      )}

      {/* NFT Purchase Details */}
      {walletAddress && nftDetails.length > 0 && (
        <div style={{ marginTop: '20px' }}>
          <h2>Purchased NFTs:</h2>
          <ul>
            {nftDetails.map((nft) => (
              <li key={nft.id} style={{ marginBottom: '10px' }}>
                <strong>{nft.name}</strong> - {nft.price} - Purchased on: {new Date(nft.timestamp).toLocaleString()}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default WalletConnection;
```
