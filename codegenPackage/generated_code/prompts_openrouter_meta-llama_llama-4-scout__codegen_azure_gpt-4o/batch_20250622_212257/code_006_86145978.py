"""
Generated Code Metadata:
========================
Original URL: https://msk-rk.ru
Prompt: Design a decentralized application (dApp) that leverages Hop Protocol for cross-chain token swaps, focusing on user experience and security.
Generated: DETERMINISTIC_86145978f55b9961
Batch ID: 20250622_212257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState } from 'react';
import Web3 from 'web3';
import { Hop } from '@hop-protocol/sdk';
import { ethers } from 'ethers';

// Constants
const SUPPORTED_CHAINS = ['ethereum', 'polygon', 'optimism', 'arbitrum']; // Supported chains for Hop Protocol
const HOP_API_KEY = 'your-hop-api-key'; // Replace with your Hop API key

// Main dApp Component
const CrossChainSwapApp = () => {
  const [web3, setWeb3] = useState(null); // Web3 instance
  const [account, setAccount] = useState(''); // User's wallet address
  const [sourceChain, setSourceChain] = useState('ethereum'); // Source chain
  const [destinationChain, setDestinationChain] = useState('polygon'); // Destination chain
  const [token, setToken] = useState('USDC'); // Token to swap
  const [amount, setAmount] = useState(''); // Amount to swap
  const [status, setStatus] = useState(''); // Status message

  // Initialize Web3 and connect wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3Instance.eth.getAccounts();
        setWeb3(web3Instance);
        setAccount(accounts[0]);
        setStatus('Wallet connected successfully.');
      } else {
        setStatus('Please install MetaMask to use this dApp.');
      }
    } catch (error) {
      console.error('Error connecting wallet:', error);
      setStatus('Failed to connect wallet.');
    }
  };

  // Perform cross-chain token swap
  const performSwap = async () => {
    try {
      if (!web3 || !account) {
        setStatus('Please connect your wallet first.');
        return;
      }

      if (!SUPPORTED_CHAINS.includes(sourceChain) || !SUPPORTED_CHAINS.includes(destinationChain)) {
        setStatus('Unsupported chain selected.');
        return;
      }

      if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
        setStatus('Please enter a valid amount.');
        return;
      }

      setStatus('Initializing swap...');

      // Initialize Hop SDK
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const hop = new Hop(HOP_API_KEY);

      // Get the bridge for the selected token
      const bridge = hop.bridge(token);

      // Perform the token transfer
      const tx = await bridge.send({
        amount: ethers.utils.parseUnits(amount, 6), // Assuming 6 decimals for USDC
        sourceChain: sourceChain,
        destinationChain: destinationChain,
        signer: provider.getSigner(),
      });

      setStatus('Transaction sent. Waiting for confirmation...');
      await tx.wait();
      setStatus('Swap completed successfully!');
    } catch (error) {
      console.error('Error performing swap:', error);
      setStatus('Swap failed. Please try again.');
    }
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Cross-Chain Token Swap</h1>
      <p>Status: {status}</p>
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected Wallet: {account}</p>
          <div>
            <label>
              Source Chain:
              <select value={sourceChain} onChange={(e) => setSourceChain(e.target.value)}>
                {SUPPORTED_CHAINS.map((chain) => (
                  <option key={chain} value={chain}>
                    {chain}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <div>
            <label>
              Destination Chain:
              <select value={destinationChain} onChange={(e) => setDestinationChain(e.target.value)}>
                {SUPPORTED_CHAINS.map((chain) => (
                  <option key={chain} value={chain}>
                    {chain}
                  </option>
                ))}
              </select>
            </label>
          </div>
          <div>
            <label>
              Token:
              <input
                type="text"
                value={token}
                onChange={(e) => setToken(e.target.value.toUpperCase())}
                placeholder="e.g., USDC"
              />
            </label>
          </div>
          <div>
            <label>
              Amount:
              <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="Enter amount"
              />
            </label>
          </div>
          <button onClick={performSwap}>Swap</button>
        </div>
      )}
    </div>
  );
};

export default CrossChainSwapApp;
```
