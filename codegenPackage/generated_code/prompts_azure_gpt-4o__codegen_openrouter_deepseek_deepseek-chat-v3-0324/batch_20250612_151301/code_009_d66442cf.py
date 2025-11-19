"""
Generated Code Metadata:
========================
Original URL: https://multichaingreenbitcoinapp.pages.dev
Prompt: Create a web application using React that displays the Green Bitcoin staking dashboard, including features like connecting wallets, staking tokens, and viewing rewards.
Generated: DETERMINISTIC_d66442cf4e092dae
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// App.js
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// ABI and contract address (simplified for example)
const contractABI = [
  {
    "inputs": [],
    "name": "stake",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getRewards",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "withdraw",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const contractAddress = "0x123..."; // Replace with actual contract address

function App() {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [stakedAmount, setStakedAmount] = useState(0);
  const [rewards, setRewards] = useState(0);
  const [stakingAmount, setStakingAmount] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Connect wallet
  const connectWallet = async () => {
    try {
      if (window.ethereum) {
        setLoading(true);
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        
        const contract = new ethers.Contract(contractAddress, contractABI, signer);
        
        setProvider(provider);
        setSigner(signer);
        setContract(contract);
        setAccount(address);
        setIsConnected(true);
        
        // Fetch initial data
        await fetchData(contract, address);
      } else {
        setError('Please install MetaMask!');
      }
    } catch (err) {
      setError('Error connecting wallet: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Fetch user data
  const fetchData = async (contract, address) => {
    try {
      setLoading(true);
      // These would be replaced with actual contract calls
      const balance = await provider.getBalance(address);
      const staked = await contract.getStakedAmount(address);
      const rewards = await contract.getRewards(address);
      
      setBalance(ethers.utils.formatEther(balance));
      setStakedAmount(ethers.utils.formatEther(staked));
      setRewards(ethers.utils.formatEther(rewards));
    } catch (err) {
      setError('Error fetching data: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Stake tokens
  const stakeTokens = async () => {
    try {
      if (!stakingAmount || stakingAmount <= 0) {
        setError('Please enter a valid amount');
        return;
      }
      
      setLoading(true);
      const tx = await contract.stake({
        value: ethers.utils.parseEther(stakingAmount)
      });
      await tx.wait();
      await fetchData(contract, account);
      setStakingAmount('');
    } catch (err) {
      setError('Error staking tokens: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Withdraw rewards
  const withdrawRewards = async () => {
    try {
      setLoading(true);
      const tx = await contract.withdraw();
      await tx.wait();
      await fetchData(contract, account);
    } catch (err) {
      setError('Error withdrawing rewards: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  // Refresh data
  const refreshData = async () => {
    if (isConnected) {
      await fetchData(contract, account);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Green Bitcoin Staking Dashboard</h1>
        
        {!isConnected ? (
          <button onClick={connectWallet} disabled={loading}>
            {loading ? 'Connecting...' : 'Connect Wallet'}
          </button>
        ) : (
          <div className="wallet-info">
            <p>Connected: {account.substring(0, 6)}...{account.substring(account.length - 4)}</p>
            <p>Balance: {balance} ETH</p>
          </div>
        )}
        
        {error && <div className="error">{error}</div>}
        
        {isConnected && (
          <div className="staking-container">
            <div className="stats">
              <h2>Your Stats</h2>
              <p>Staked: {stakedAmount} GBTC</p>
              <p>Rewards: {rewards} GBTC</p>
              <button onClick={refreshData} disabled={loading}>
                {loading ? 'Refreshing...' : 'Refresh'}
              </button>
            </div>
            
            <div className="staking-form">
              <h2>Stake Tokens</h2>
              <input
                type="number"
                value={stakingAmount}
                onChange={(e) => setStakingAmount(e.target.value)}
                placeholder="Amount to stake"
                disabled={loading}
              />
              <button onClick={stakeTokens} disabled={loading}>
                {loading ? 'Processing...' : 'Stake'}
              </button>
            </div>
            
            <div className="rewards-form">
              <h2>Rewards</h2>
              <button onClick={withdrawRewards} disabled={loading || rewards <= 0}>
                {loading ? 'Processing...' : 'Withdraw Rewards'}
              </button>
            </div>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
  min-height: 100vh;
  background-color: #282c34;
  color: white;
  padding: 20px;
}

.App-header {
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
}

button {
  background-color: #61dafb;
  border: none;
  color: #282c34;
  padding: 10px 20px;
  margin: 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #4fa8d3;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

input {
  padding: 10px;
  margin: 10px;
  border-radius: 5px;
  border: 1px solid #61dafb;
  font-size: 16px;
  width: 200px;
}

.staking-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  width: 100%;
  margin-top: 30px;
}

.stats, .staking-form, .rewards-form {
  background-color: #3a3f4b;
  padding: 20px;
  border-radius: 10px;
  margin: 10px;
  min-width: 250px;
}

.error {
  color: #ff6b6b;
  margin: 10px;
  padding: 10px;
  background-color: #3a3f4b;
  border-radius: 5px;
}

.wallet-info {
  background-color: #3a3f4b;
  padding: 15px;
  border-radius: 10px;
  margin-bottom: 20px;
}
```
