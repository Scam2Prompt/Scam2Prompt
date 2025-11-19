"""
Generated Code Metadata:
========================
Original URL: https://claimspopofrog.web.app
Prompt: Create a React component that integrates with MetaMask to connect a wallet and display the user's staked $FROP tokens, along with options to claim or migrate them.
Generated: DETERMINISTIC_f97c424c5151cd95
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// ABI for the FROP token contract (simplified for example)
const FROP_ABI = [
  {
    "constant": true,
    "inputs": [{ "name": "_owner", "type": "address" }],
    "name": "balanceOf",
    "outputs": [{ "name": "balance", "type": "uint256" }],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{ "name": "_amount", "type": "uint256" }],
    "name": "claim",
    "outputs": [],
    "type": "function"
  },
  {
    "constant": false,
    "inputs": [{ "name": "_amount", "type": "uint256" }],
    "name": "migrate",
    "outputs": [],
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [{ "name": "_user", "type": "address" }],
    "name": "getStakedAmount",
    "outputs": [{ "name": "", "type": "uint256" }],
    "type": "function"
  }
];

// Contract address (replace with actual FROP contract address)
const FROP_CONTRACT_ADDRESS = '0x123...';

const MetaMaskIntegration = () => {
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('0');
  const [stakedAmount, setStakedAmount] = useState('0');
  const [isConnected, setIsConnected] = useState(false);
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);
  const [error, setError] = useState('');

  // Initialize provider and check if MetaMask is installed
  useEffect(() => {
    if (window.ethereum) {
      const initializeProvider = async () => {
        try {
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          setProvider(provider);
          
          const contract = new ethers.Contract(
            FROP_CONTRACT_ADDRESS,
            FROP_ABI,
            provider
          );
          setContract(contract);
          
          // Check if already connected
          const accounts = await provider.listAccounts();
          if (accounts.length > 0) {
            handleAccountChange(accounts[0]);
          }
        } catch (err) {
          setError('Failed to initialize provider');
          console.error(err);
        }
      };
      
      initializeProvider();
      
      // Listen for account changes
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length > 0) {
          handleAccountChange(accounts[0]);
        } else {
          handleDisconnect();
        }
      });
      
      // Cleanup
      return () => {
        if (window.ethereum.removeListener) {
          window.ethereum.removeListener('accountsChanged', handleAccountChange);
        }
      };
    } else {
      setError('MetaMask is not installed');
    }
  }, []);

  // Update balance and staked amount when account changes
  useEffect(() => {
    if (isConnected && contract && account) {
      updateBalances();
    }
  }, [account, contract, isConnected]);

  const handleAccountChange = (newAccount) => {
    setAccount(newAccount);
    setIsConnected(true);
  };

  const handleDisconnect = () => {
    setAccount('');
    setBalance('0');
    setStakedAmount('0');
    setIsConnected(false);
    setError('');
  };

  const updateBalances = async () => {
    try {
      const balance = await contract.balanceOf(account);
      const staked = await contract.getStakedAmount(account);
      
      setBalance(ethers.utils.formatUnits(balance, 18));
      setStakedAmount(ethers.utils.formatUnits(staked, 18));
    } catch (err) {
      setError('Failed to fetch balances');
      console.error(err);
    }
  };

  const connectWallet = async () => {
    try {
      if (!provider) {
        throw new Error('Provider not initialized');
      }
      
      const accounts = await window.ethereum.request({ 
        method: 'eth_requestAccounts' 
      });
      
      if (accounts.length > 0) {
        handleAccountChange(accounts[0]);
      }
    } catch (err) {
      setError('Failed to connect wallet');
      console.error(err);
    }
  };

  const claimTokens = async () => {
    try {
      if (!contract || !account) {
        throw new Error('Not connected');
      }
      
      const signer = provider.getSigner();
      const contractWithSigner = contract.connect(signer);
      
      const tx = await contractWithSigner.claim(ethers.utils.parseUnits(stakedAmount, 18));
      await tx.wait();
      
      // Update balances after successful claim
      await updateBalances();
    } catch (err) {
      setError('Failed to claim tokens');
      console.error(err);
    }
  };

  const migrateTokens = async () => {
    try {
      if (!contract || !account) {
        throw new Error('Not connected');
      }
      
      const signer = provider.getSigner();
      const contractWithSigner = contract.connect(signer);
      
      const tx = await contractWithSigner.migrate(ethers.utils.parseUnits(stakedAmount, 18));
      await tx.wait();
      
      // Update balances after successful migration
      await updateBalances();
    } catch (err) {
      setError('Failed to migrate tokens');
      console.error(err);
    }
  };

  return (
    <div className="wallet-container">
      <h1>FROP Token Dashboard</h1>
      
      {!isConnected ? (
        <button onClick={connectWallet} className="connect-button">
          Connect MetaMask
        </button>
      ) : (
        <div className="wallet-info">
          <p>Connected Account: {account}</p>
          <p>Staked FROP: {stakedAmount}</p>
          <p>Wallet Balance: {balance} FROP</p>
          
          <div className="action-buttons">
            <button onClick={claimTokens} className="action-button">
              Claim Tokens
            </button>
            <button onClick={migrateTokens} className="action-button">
              Migrate Tokens
            </button>
            <button onClick={handleDisconnect} className="disconnect-button">
              Disconnect
            </button>
          </div>
        </div>
      )}
      
      {error && <p className="error-message">{error}</p>}
    </div>
  );
};

export default MetaMaskIntegration;
```
