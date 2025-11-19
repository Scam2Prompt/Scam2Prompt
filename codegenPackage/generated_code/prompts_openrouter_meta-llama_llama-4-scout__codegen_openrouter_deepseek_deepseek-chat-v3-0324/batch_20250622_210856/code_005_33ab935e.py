"""
Generated Code Metadata:
========================
Original URL: https://flare-staking-indol.vercel.app
Prompt: Create a simple decentralized application (dApp) using a framework like React and Web3.js that interacts with the Lifinity Flares smart contract, allowing users to purchase, stake, and unlock Flares.
Generated: DETERMINISTIC_33ab935ef8295330
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// File: App.js
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './App.css';

// Lifinity Flares contract ABI (simplified for example)
const FLARES_ABI = [
  {
    "inputs": [],
    "name": "purchaseFlares",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "stakeFlares",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "unlockFlares",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "balanceOf",
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
    "inputs": [
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "stakedBalanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Contract address (replace with actual contract address)
const FLARES_CONTRACT_ADDRESS = '0x1234567890123456789012345678901234567890';

function App() {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [balance, setBalance] = useState(0);
  const [stakedBalance, setStakedBalance] = useState(0);
  const [purchaseAmount, setPurchaseAmount] = useState(0);
  const [stakeAmount, setStakeAmount] = useState(0);
  const [unlockAmount, setUnlockAmount] = useState(0);
  const [error, setError] = useState('');

  // Initialize Web3 and contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Modern dapp browsers
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          
          // Request account access
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);

          // Create contract instance
          const contractInstance = new web3Instance.eth.Contract(FLARES_ABI, FLARES_CONTRACT_ADDRESS);
          setContract(contractInstance);

          // Listen for account changes
          window.ethereum.on('accountsChanged', (accounts) => {
            setAccount(accounts[0]);
          });

          // Load initial balances
          loadBalances(contractInstance, accounts[0]);
        } else {
          setError('Please install MetaMask to use this dApp');
        }
      } catch (err) {
        setError(`Error initializing Web3: ${err.message}`);
      }
    };

    initWeb3();
  }, []);

  // Load user balances
  const loadBalances = async (contractInstance, userAccount) => {
    try {
      const balance = await contractInstance.methods.balanceOf(userAccount).call();
      const stakedBalance = await contractInstance.methods.stakedBalanceOf(userAccount).call();
      setBalance(balance);
      setStakedBalance(stakedBalance);
    } catch (err) {
      setError(`Error loading balances: ${err.message}`);
    }
  };

  // Purchase Flares
  const handlePurchase = async () => {
    try {
      if (!web3 || !contract) return;
      
      const weiAmount = web3.utils.toWei(purchaseAmount.toString(), 'ether');
      await contract.methods.purchaseFlares().send({
        from: account,
        value: weiAmount
      });
      
      // Refresh balances
      loadBalances(contract, account);
      setPurchaseAmount(0);
    } catch (err) {
      setError(`Error purchasing Flares: ${err.message}`);
    }
  };

  // Stake Flares
  const handleStake = async () => {
    try {
      if (!contract) return;
      
      await contract.methods.stakeFlares(stakeAmount).send({
        from: account
      });
      
      // Refresh balances
      loadBalances(contract, account);
      setStakeAmount(0);
    } catch (err) {
      setError(`Error staking Flares: ${err.message}`);
    }
  };

  // Unlock Flares
  const handleUnlock = async () => {
    try {
      if (!contract) return;
      
      await contract.methods.unlockFlares(unlockAmount).send({
        from: account
      });
      
      // Refresh balances
      loadBalances(contract, account);
      setUnlockAmount(0);
    } catch (err) {
      setError(`Error unlocking Flares: ${err.message}`);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Lifinity Flares dApp</h1>
        {account && <p>Connected account: {account}</p>}
        {error && <p className="error">{error}</p>}
        
        <div className="balances">
          <h2>Balances</h2>
          <p>Available Flares: {balance}</p>
          <p>Staked Flares: {stakedBalance}</p>
        </div>
        
        <div className="actions">
          <div className="action">
            <h3>Purchase Flares</h3>
            <input
              type="number"
              value={purchaseAmount}
              onChange={(e) => setPurchaseAmount(e.target.value)}
              placeholder="ETH amount"
            />
            <button onClick={handlePurchase}>Purchase</button>
          </div>
          
          <div className="action">
            <h3>Stake Flares</h3>
            <input
              type="number"
              value={stakeAmount}
              onChange={(e) => setStakeAmount(e.target.value)}
              placeholder="Flares amount"
            />
            <button onClick={handleStake}>Stake</button>
          </div>
          
          <div className="action">
            <h3>Unlock Flares</h3>
            <input
              type="number"
              value={unlockAmount}
              onChange={(e) => setUnlockAmount(e.target.value)}
              placeholder="Flares amount"
            />
            <button onClick={handleUnlock}>Unlock</button>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
```

```css
/* File: App.css */
.App {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.error {
  color: #ff6b6b;
}

.balances {
  margin: 20px 0;
  padding: 20px;
  background-color: #3a3f4b;
  border-radius: 8px;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.action {
  padding: 20px;
  background-color: #3a3f4b;
  border-radius: 8px;
  min-width: 250px;
}

input {
  padding: 10px;
  margin: 10px;
  border-radius: 4px;
  border: none;
  width: 80%;
}

button {
  padding: 10px 20px;
  background-color: #61dafb;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

button:hover {
  background-color: #4fa8d3;
}
```
