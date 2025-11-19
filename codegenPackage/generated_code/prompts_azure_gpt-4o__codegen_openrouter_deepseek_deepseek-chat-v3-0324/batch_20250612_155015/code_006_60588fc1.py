"""
Generated Code Metadata:
========================
Original URL: https://pythweb.com
Prompt: Create a JavaScript-based front-end application that interacts with Pyth Network's price feed oracles for smart contract data.
Generated: DETERMINISTIC_60588fc1af25155e
Batch ID: 20250612_155015
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
import axios from 'axios';
import Web3 from 'web3';

// Pyth Network contract ABI (simplified for price feed interaction)
const PYTH_ORACLE_ABI = [
  {
    "inputs": [],
    "name": "getPrice",
    "outputs": [
      {
        "internalType": "int64",
        "name": "price",
        "type": "int64"
      },
      {
        "internalType": "uint64",
        "name": "conf",
        "type": "uint64"
      },
      {
        "internalType": "int32",
        "name": "expo",
        "type": "int32"
      },
      {
        "internalType": "uint64",
        "name": "publishTime",
        "type": "uint64"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Default Pyth Network contract address (example for ETH/USD)
const DEFAULT_PYTH_CONTRACT = '0x4305FB66699C3B2702D4d05CF36551390A4c69C6';

// Component for interacting with Pyth Network price feeds
const PythPriceFeed = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');
  const [priceData, setPriceData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [contractAddress, setContractAddress] = useState(DEFAULT_PYTH_CONTRACT);
  const [network, setNetwork] = useState('mainnet');

  // Initialize Web3 and connect to wallet
  const initWeb3 = async () => {
    try {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        await window.ethereum.enable();
        setWeb3(web3Instance);
        
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);
      } else {
        throw new Error('Please install MetaMask or another Web3 provider');
      }
    } catch (err) {
      setError(err.message);
    }
  };

  // Fetch price data from Pyth Network oracle
  const fetchPriceData = async () => {
    if (!web3) {
      setError('Web3 not initialized');
      return;
    }

    setLoading(true);
    setError(null);

    try {
      const contract = new web3.eth.Contract(PYTH_ORACLE_ABI, contractAddress);
      const result = await contract.methods.getPrice().call();
      
      // Convert price to human-readable format
      const price = parseFloat(result.price) * Math.pow(10, result.expo);
      const confidence = parseFloat(result.conf) * Math.pow(10, result.expo);
      
      setPriceData({
        price,
        confidence,
        exponent: result.expo,
        publishTime: new Date(parseInt(result.publishTime) * 1000).toLocaleString()
      });
    } catch (err) {
      setError(`Failed to fetch price data: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Handle contract address change
  const handleAddressChange = (e) => {
    setContractAddress(e.target.value);
  };

  // Handle network change
  const handleNetworkChange = (e) => {
    setNetwork(e.target.value);
  };

  // Format price for display
  const formatPrice = (price) => {
    if (!price) return 'N/A';
    return price.toLocaleString(undefined, {
      minimumFractionDigits: 2,
      maximumFractionDigits: 6
    });
  };

  return (
    <div className="pyth-price-feed">
      <h1>Pyth Network Price Feed</h1>
      
      {!web3 ? (
        <button onClick={initWeb3}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected account: {account}</p>
          
          <div className="input-group">
            <label htmlFor="network">Network:</label>
            <select id="network" value={network} onChange={handleNetworkChange}>
              <option value="mainnet">Mainnet</option>
              <option value="testnet">Testnet</option>
            </select>
          </div>
          
          <div className="input-group">
            <label htmlFor="contract">Contract Address:</label>
            <input
              id="contract"
              type="text"
              value={contractAddress}
              onChange={handleAddressChange}
              placeholder="Enter Pyth contract address"
            />
          </div>
          
          <button onClick={fetchPriceData} disabled={loading}>
            {loading ? 'Loading...' : 'Fetch Price Data'}
          </button>
          
          {error && <div className="error">{error}</div>}
          
          {priceData && (
            <div className="price-data">
              <h2>Price Information</h2>
              <p><strong>Price:</strong> {formatPrice(priceData.price)}</p>
              <p><strong>Confidence:</strong> ±{formatPrice(priceData.confidence)}</p>
              <p><strong>Last Updated:</strong> {priceData.publishTime}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default PythPriceFeed;
```
