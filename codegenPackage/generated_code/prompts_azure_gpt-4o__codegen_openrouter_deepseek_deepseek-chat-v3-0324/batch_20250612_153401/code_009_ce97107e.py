"""
Generated Code Metadata:
========================
Original URL: https://dresale.pages.dev
Prompt: Develop a front-end interface using React.js that integrates with a blockchain to display the current status of the "DRE" presale, including tokens sold, tokens remaining, and exchange rates.
Generated: DETERMINISTIC_ce97107e7dd81df2
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import './App.css';

// Presale contract ABI (simplified for example)
const presaleABI = [
  {
    "constant": true,
    "inputs": [],
    "name": "tokensSold",
    "outputs": [{"name": "", "type": "uint256"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "totalTokens",
    "outputs": [{"name": "", "type": "uint256"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "exchangeRate",
    "outputs": [{"name": "", "type": "uint256"}],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
];

// Contract address (replace with actual contract address)
const presaleAddress = '0x1234567890123456789012345678901234567890';

function App() {
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState('');
  const [tokensSold, setTokensSold] = useState(0);
  const [totalTokens, setTotalTokens] = useState(0);
  const [exchangeRate, setExchangeRate] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Initialize Web3 and contract
  useEffect(() => {
    const init = async () => {
      try {
        // Check if Web3 is injected by the browser (MetaMask)
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          
          // Get accounts
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
          
          // Initialize contract
          const contractInstance = new web3Instance.eth.Contract(presaleABI, presaleAddress);
          setContract(contractInstance);
          
          // Load presale data
          await loadPresaleData(contractInstance);
        } else {
          setError('Please install MetaMask to use this application');
        }
      } catch (err) {
        console.error('Initialization error:', err);
        setError('Failed to initialize Web3 and contract');
      } finally {
        setLoading(false);
      }
    };

    init();
  }, []);

  // Load presale data from contract
  const loadPresaleData = async (contractInstance) => {
    try {
      const [sold, total, rate] = await Promise.all([
        contractInstance.methods.tokensSold().call(),
        contractInstance.methods.totalTokens().call(),
        contractInstance.methods.exchangeRate().call()
      ]);
      
      setTokensSold(Web3.utils.fromWei(sold, 'ether'));
      setTotalTokens(Web3.utils.fromWei(total, 'ether'));
      setExchangeRate(Web3.utils.fromWei(rate, 'ether'));
    } catch (err) {
      console.error('Error loading presale data:', err);
      setError('Failed to load presale data');
    }
  };

  // Refresh data
  const refreshData = async () => {
    if (contract) {
      setLoading(true);
      try {
        await loadPresaleData(contract);
      } catch (err) {
        console.error('Error refreshing data:', err);
        setError('Failed to refresh data');
      } finally {
        setLoading(false);
      }
    }
  };

  if (loading) {
    return (
      <div className="app-container">
        <h1>DRE Presale Dashboard</h1>
        <p>Loading...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="app-container">
        <h1>DRE Presale Dashboard</h1>
        <div className="error-message">{error}</div>
      </div>
    );
  }

  const tokensRemaining = totalTokens - tokensSold;
  const percentageSold = (tokensSold / totalTokens * 100).toFixed(2);

  return (
    <div className="app-container">
      <h1>DRE Presale Dashboard</h1>
      <div className="account-info">
        <p>Connected Account: {account}</p>
      </div>
      
      <div className="presale-stats">
        <div className="stat-card">
          <h3>Tokens Sold</h3>
          <p>{tokensSold} DRE</p>
        </div>
        
        <div className="stat-card">
          <h3>Tokens Remaining</h3>
          <p>{tokensRemaining} DRE</p>
        </div>
        
        <div className="stat-card">
          <h3>Percentage Sold</h3>
          <p>{percentageSold}%</p>
        </div>
        
        <div className="stat-card">
          <h3>Exchange Rate</h3>
          <p>1 ETH = {exchangeRate} DRE</p>
        </div>
      </div>
      
      <button className="refresh-button" onClick={refreshData}>
        Refresh Data
      </button>
    </div>
  );
}

export default App;
```

```css
/* App.css */
.app-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  text-align: center;
}

.account-info {
  margin: 20px 0;
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.presale-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin: 30px 0;
}

.stat-card {
  padding: 20px;
  background-color: #f8f8f8;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.stat-card h3 {
  margin-top: 0;
  color: #333;
}

.stat-card p {
  font-size: 1.5em;
  font-weight: bold;
  color: #2c3e50;
}

.refresh-button {
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  transition: background-color 0.3s;
}

.refresh-button:hover {
  background-color: #2980b9;
}

.error-message {
  color: #e74c3c;
  padding: 10px;
  background-color: #fadbd8;
  border-radius: 5px;
  margin: 20px 0;
}
```
