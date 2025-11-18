"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-es.web.app
Prompt: Develop a web interface using React.js for users to connect their wallets, buy $PEPU tokens, and stake them directly for maximum rewards.
Generated: DETERMINISTIC_cf44a79ab2e926b5
Batch ID: 20250612_145144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.js
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import './App.css';

// Constants
const TOKEN_CONTRACT_ADDRESS = 'YOUR_TOKEN_CONTRACT_ADDRESS';
const STAKING_CONTRACT_ADDRESS = 'YOUR_STAKING_CONTRACT_ADDRESS';
const TOKEN_ABI = [];  // Provide your token ABI here
const STAKING_ABI = []; // Provide your staking ABI here

function App() {
  const [account, setAccount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [amount, setAmount] = useState(0);
  const [isConnected, setIsConnected] = useState(false);

  // Initialize web3 instance and connect to wallet
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        
        // Request wallet connection
        try {
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);
          setIsConnected(true);
        } catch (error) {
          console.error('User denied wallet connection:', error);
        }
      } else {
        console.error('Ethereum wallet not detected');
      }
    };
    initWeb3();
  }, []);

  // Handle token purchase
  const buyTokens = async () => {
    if (!web3) return alert('Web3 not initialized');
    if (!amount || amount <= 0) return alert('Please enter a valid amount');

    const tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
    const value = web3.utils.toWei(amount.toString(), 'ether');

    try {
      await tokenContract.methods.buyTokens().send({ from: account, value });
      alert('Tokens purchased successfully!');
    } catch (error) {
      console.error('Error purchasing tokens:', error);
      alert('Token purchase failed. Check console for details.');
    }
  };

  // Handle staking tokens
  const stakeTokens = async () => {
    if (!web3) return alert('Web3 not initialized');
    if (!amount || amount <= 0) return alert('Please enter a valid amount');

    const stakingContract = new web3.eth.Contract(STAKING_ABI, STAKING_CONTRACT_ADDRESS);

    try {
      const tokenContract = new web3.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
      await tokenContract.methods.approve(STAKING_CONTRACT_ADDRESS, web3.utils.toWei(amount.toString(), 'ether')).send({ from: account });

      await stakingContract.methods.stakeTokens(web3.utils.toWei(amount.toString(), 'ether')).send({ from: account });
      alert('Tokens staked successfully!');
    } catch (error) {
      console.error('Error staking tokens:', error);
      alert('Token staking failed. Check console for details.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>PEPU Token Interface</h1>
        {isConnected ? (
          <div>
            <p>Connected Account: {account}</p>
            <input
              type="number"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              placeholder="Amount in ETH"
            />
            <button onClick={buyTokens}>Buy $PEPU Tokens</button>
            <button onClick={stakeTokens}>Stake $PEPU Tokens</button>
          </div>
        ) : (
          <p>Please connect your wallet</p>
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

input {
  margin: 10px;
  padding: 10px;
  border: none;
  border-radius: 5px;
}

button {
  margin: 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #61dafb;
  color: black;
  cursor: pointer;
}

button:hover {
  background-color: #21a1f1;
}
```

### Note:
- Replace `YOUR_TOKEN_CONTRACT_ADDRESS` and `YOUR_STAKING_CONTRACT_ADDRESS` with the actual contract addresses.
- You need to provide the ABI for your token and staking contracts in the `TOKEN_ABI` and `STAKING_ABI` constants.
