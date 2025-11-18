"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pp8.pages.dev
Prompt: Create a React component for connecting a wallet and displaying $WATER token claim status.
Generated: DETERMINISTIC_cd1d4d2bc751eeb5
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// WalletConnect.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define constants for the token contract and network
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress'; // Replace with actual contract address
const TOKEN_ABI = [
  // Replace with the ABI of your token contract
  // Example structure: 
  // { "constant": true, "inputs": [...], "name": "methodName", "outputs": [...], ... }
];
const NETWORK_ID = '1'; // Replace with the correct network ID (e.g., '1' for Ethereum Mainnet)

const WalletConnect = () => {
  const [walletConnected, setWalletConnected] = useState(false);
  const [account, setAccount] = useState('');
  const [claimStatus, setClaimStatus] = useState('');
  const [error, setError] = useState('');

  // Initialize Web3 instance
  const web3 = new Web3(Web3.givenProvider);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error('MetaMask is not installed. Please install MetaMask to use this feature.');
      }

      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      if (accounts.length === 0) {
        throw new Error('No accounts found. Please connect your wallet.');
      }

      const networkId = await web3.eth.net.getId();
      if (networkId.toString() !== NETWORK_ID) {
        throw new Error(`Please switch to the correct network (Network ID: ${NETWORK_ID}).`);
      }

      setAccount(accounts[0]);
      setWalletConnected(true);
      setError('');
    } catch (err) {
      setError(err.message);
      setWalletConnected(false);
      setAccount('');
    }
  };

  // Function to fetch the $WATER token claim status
  const fetchClaimStatus = async () => {
    try {
      if (!walletConnected) {
        throw new Error('Wallet not connected. Please connect your wallet first.');
      }

      const tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
      const claimStatus = await tokenContract.methods.getClaimStatus(account).call();

      setClaimStatus(claimStatus ? 'Eligible to claim $WATER tokens' : 'Not eligible to claim $WATER tokens');
      setError('');
    } catch (err) {
      setError(err.message);
      setClaimStatus('');
    }
  };

  // Automatically fetch claim status when wallet is connected
  useEffect(() => {
    if (walletConnected) {
      fetchClaimStatus();
    }
  }, [walletConnected]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Wallet Connection & $WATER Token Claim Status</h1>

      {!walletConnected && (
        <button onClick={connectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Connect Wallet
        </button>
      )}

      {walletConnected && (
        <div>
          <p>
            <strong>Wallet Address:</strong> {account}
          </p>
          <p>
            <strong>Claim Status:</strong> {claimStatus || 'Fetching claim status...'}
          </p>
          <button onClick={fetchClaimStatus} style={{ padding: '10px 20px', cursor: 'pointer' }}>
            Refresh Status
          </button>
        </div>
      )}

      {error && (
        <p style={{ color: 'red' }}>
          <strong>Error:</strong> {error}
        </p>
      )}
    </div>
  );
};

export default WalletConnect;
```
