"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a Web3 React component that displays the Chain ID, account address, and balance of a connected wallet, following the example in the Dapp Starter framework.
Generated: DETERMINISTIC_38654168b51c7887
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';

// Component to display wallet information
const WalletInfo = () => {
  // State variables to hold wallet information
  const [account, setAccount] = useState(null);
  const [chainId, setChainId] = useState(null);
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);

  // Function to connect to the wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        
        // Set account and chain ID
        setAccount(accounts[0]);
        const network = await provider.getNetwork();
        setChainId(network.chainId);

        // Fetch balance
        const balance = await provider.getBalance(accounts[0]);
        setBalance(ethers.utils.formatEther(balance));
      } catch (err) {
        setError('Failed to connect wallet: ' + err.message);
      }
    } else {
      setError('Please install MetaMask!');
    }
  };

  // Effect to handle wallet connection on component mount
  useEffect(() => {
    connectWallet();
  }, []);

  return (
    <div>
      <h2>Wallet Information</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p><strong>Account:</strong> {account ? account : 'Not connected'}</p>
      <p><strong>Chain ID:</strong> {chainId !== null ? chainId : 'Not connected'}</p>
      <p><strong>Balance:</strong> {balance !== null ? `${balance} ETH` : 'Not connected'}</p>
      <button onClick={connectWallet}>Connect Wallet</button>
    </div>
  );
};

export default WalletInfo;
```
