"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-web.pages.dev
Prompt: Develop a simple web application that allows users to connect their MetaMask wallet and buy $SCOTTY tokens using ETH, BNB, MATIC, or USDT.
Generated: DETERMINISTIC_280d8acc97e1d8af
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Frontend (React with Web3.js)
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';
import './App.css';

const tokenContractAddress = '0x...'; // Replace with actual SCOTTY token contract address
const tokenABI = [...]; // Replace with actual SCOTTY token ABI
const paymentTokens = {
  ETH: { address: '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE', decimals: 18 },
  BNB: { address: '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', decimals: 18 },
  MATIC: { address: '0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0', decimals: 18 },
  USDT: { address: '0xdAC17F958D2ee523a2206206994597C13D831ec7', decimals: 6 }
};

function App() {
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [connected, setConnected] = useState(false);
  const [selectedToken, setSelectedToken] = useState('ETH');
  const [amount, setAmount] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    const init = async () => {
      const provider = await detectEthereumProvider();
      if (provider) {
        const web3Instance = new Web3(provider);
        setWeb3(web3Instance);
        window.ethereum.on('accountsChanged', (accounts) => {
          setAccounts(accounts);
        });
      } else {
        setError('Please install MetaMask!');
      }
    };
    init();
  }, []);

  const connectWallet = async () => {
    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAccounts(accounts);
      setConnected(true);
      setError('');
    } catch (err) {
      setError('Failed to connect wallet: ' + err.message);
    }
  };

  const buyTokens = async () => {
    if (!web3 || !accounts.length || !amount) {
      setError('Please connect wallet and enter amount');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const tokenContract = new web3.eth.Contract(tokenABI, tokenContractAddress);
      const paymentToken = paymentTokens[selectedToken];
      const weiAmount = web3.utils.toWei(amount, 'ether');

      if (selectedToken === 'ETH') {
        await tokenContract.methods.buyWithETH().send({
          from: accounts[0],
          value: weiAmount
        });
      } else {
        const paymentContract = new web3.eth.Contract(ERC20_ABI, paymentToken.address);
        
        // Approve token transfer
        await paymentContract.methods.approve(
          tokenContractAddress,
          weiAmount
        ).send({ from: accounts[0] });

        // Execute purchase
        await tokenContract.methods.buyWithToken(
          paymentToken.address,
          weiAmount
        ).send({ from: accounts[0] });
      }

      alert('Purchase successful!');
    } catch (err) {
      setError('Transaction failed: ' + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>SCOTTY Token Purchase</h1>
        
        {!connected ? (
          <button onClick={connectWallet}>Connect MetaMask</button>
        ) : (
          <div>
            <p>Connected: {accounts[0]}</p>
            
            <div className="form-group">
              <label>Select Payment Token:</label>
              <select 
                value={selectedToken} 
                onChange={(e) => setSelectedToken(e.target.value)}
              >
                {Object.keys(paymentTokens).map(token => (
                  <option key={token} value={token}>{token}</option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Amount:</label>
              <input 
                type="number" 
                value={amount} 
                onChange={(e) => setAmount(e.target.value)} 
                placeholder="0.0"
              />
            </div>

            <button 
              onClick={buyTokens} 
              disabled={loading}
            >
              {loading ? 'Processing...' : 'Buy SCOTTY Tokens'}
            </button>
          </div>
        )}

        {error && <p className="error">{error}</p>}
      </header>
    </div>
  );
}

export default App;

// ERC20 ABI (partial)
const ERC20_ABI = [
  {
    "constant": false,
    "inputs": [
      {
        "name": "_spender",
        "type": "address"
      },
      {
        "name": "_value",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "name": "",
        "type": "bool"
      }
    ],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [
      {
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "name": "balance",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
];
```
