"""
Generated Code Metadata:
========================
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Create a dapp interface that allows users to connect their wallets, deposit ETH, and view their token allocation based on a conversion rate of 0.1 ETH = 99,500 tokens.
Generated: DETERMINISTIC_7c677bfb948b9fad
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import './App.css';

// Token conversion rate constants
const ETH_TO_TOKEN_RATE = 99500;
const ETH_DECIMALS = 18;
const TOKEN_DECIMALS = 18;

// App component
function App() {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('0');
  const [tokenAmount, setTokenAmount] = useState('0');
  const [depositAmount, setDepositAmount] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [error, setError] = useState('');

  // Initialize provider on component mount
  useEffect(() => {
    if (window.ethereum) {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      setProvider(provider);
    }
  }, []);

  // Connect wallet handler
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        throw new Error('Please install MetaMask or another Ethereum wallet');
      }

      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();

      setAccount(accounts[0]);
      setSigner(signer);
      setIsConnected(true);
      updateBalance(accounts[0], provider);
      
      // Listen for account changes
      window.ethereum.on('accountsChanged', (accounts) => {
        if (accounts.length === 0) {
          disconnectWallet();
        } else {
          setAccount(accounts[0]);
          updateBalance(accounts[0], provider);
        }
      });

      // Listen for chain changes
      window.ethereum.on('chainChanged', () => {
        window.location.reload();
      });

    } catch (err) {
      setError(err.message);
    }
  };

  // Disconnect wallet handler
  const disconnectWallet = () => {
    setAccount('');
    setSigner(null);
    setIsConnected(false);
    setBalance('0');
    setTokenAmount('0');
    setError('');
  };

  // Update ETH balance
  const updateBalance = async (account, provider) => {
    try {
      const balance = await provider.getBalance(account);
      const formattedBalance = ethers.utils.formatUnits(balance, ETH_DECIMALS);
      setBalance(formattedBalance);
    } catch (err) {
      setError('Failed to fetch balance');
    }
  };

  // Handle deposit amount change
  const handleDepositChange = (e) => {
    const value = e.target.value;
    if (value === '' || /^\d*\.?\d*$/.test(value)) {
      setDepositAmount(value);
      if (value) {
        const tokens = parseFloat(value) * ETH_TO_TOKEN_RATE;
        setTokenAmount(tokens.toFixed(TOKEN_DECIMALS));
      } else {
        setTokenAmount('0');
      }
    }
  };

  // Handle deposit submission
  const handleDeposit = async () => {
    try {
      if (!depositAmount || parseFloat(depositAmount) <= 0) {
        throw new Error('Please enter a valid deposit amount');
      }

      const tx = await signer.sendTransaction({
        to: '0x0000000000000000000000000000000000000000', // Replace with actual deposit address
        value: ethers.utils.parseEther(depositAmount)
      });

      await tx.wait();
      updateBalance(account, provider);
      setDepositAmount('');
      setTokenAmount('0');
      setError('');
      alert('Deposit successful!');
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Token Allocation DApp</h1>
        
        {!isConnected ? (
          <button onClick={connectWallet} className="connect-button">
            Connect Wallet
          </button>
        ) : (
          <div className="wallet-info">
            <p>Connected: {`${account.substring(0, 6)}...${account.substring(38)}`}</p>
            <p>ETH Balance: {balance}</p>
            <button onClick={disconnectWallet} className="disconnect-button">
              Disconnect
            </button>
          </div>
        )}

        {isConnected && (
          <div className="deposit-section">
            <h2>Deposit ETH</h2>
            <div className="input-group">
              <input
                type="text"
                value={depositAmount}
                onChange={handleDepositChange}
                placeholder="ETH amount"
              />
              <button onClick={handleDeposit} className="deposit-button">
                Deposit
              </button>
            </div>
            <div className="token-allocation">
              <h3>Token Allocation</h3>
              <p>{tokenAmount} Tokens</p>
              <p className="rate-info">Rate: 0.1 ETH = 99,500 Tokens</p>
            </div>
          </div>
        )}

        {error && <p className="error-message">{error}</p>}
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
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #282c34;
  color: white;
  padding: 20px;
}

.App-header {
  max-width: 800px;
  width: 100%;
  padding: 20px;
  border-radius: 10px;
  background-color: #1e2127;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.connect-button, .disconnect-button, .deposit-button {
  background-color: #61dafb;
  border: none;
  color: #282c34;
  padding: 10px 20px;
  margin: 10px;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.connect-button:hover, .disconnect-button:hover, .deposit-button:hover {
  background-color: #4fa8d3;
}

.wallet-info {
  margin-bottom: 20px;
}

.deposit-section {
  margin-top: 20px;
  padding: 20px;
  border-radius: 8px;
  background-color: #2c303a;
}

.input-group {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.input-group input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #61dafb;
  margin-right: 10px;
  width: 200px;
  font-size: 16px;
}

.token-allocation {
  margin-top: 20px;
  padding: 15px;
  border-radius: 8px;
  background-color: #3a3f4b;
}

.rate-info {
  font-size: 0.9em;
  color: #aaa;
  margin-top: 10px;
}

.error-message {
  color: #ff6b6b;
  margin-top: 20px;
}
```
