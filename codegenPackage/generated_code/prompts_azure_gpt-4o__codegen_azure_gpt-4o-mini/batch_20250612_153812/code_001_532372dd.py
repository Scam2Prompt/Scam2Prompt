"""
Generated Code Metadata:
========================
Original URL: https://cheemspet.web.app
Prompt: Create a web application that mimics the functionality of Cheemsverse, allowing users to connect their wallets and view token supply details, burned tokens, and current supply. Use React for the frontend and Web3.js for wallet integration.
Generated: DETERMINISTIC_532372dd7a9d91bb
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// src/App.js

import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import './App.css';

// Define the contract ABI and address (replace with actual values)
const CONTRACT_ABI = [ /* ABI goes here */ ];
const CONTRACT_ADDRESS = '0xYourContractAddress';

const App = () => {
  const [account, setAccount] = useState('');
  const [supplyDetails, setSupplyDetails] = useState({
    totalSupply: 0,
    burnedTokens: 0,
    currentSupply: 0,
  });
  const [error, setError] = useState('');

  useEffect(() => {
    // Initialize Web3 and check for wallet connection
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3 = new Web3(window.ethereum);
        try {
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);
          await fetchSupplyDetails(web3);
        } catch (err) {
          setError('Failed to connect to wallet. Please try again.');
          console.error(err);
        }
      } else {
        setError('Please install MetaMask to use this app.');
      }
    };

    initWeb3();
  }, []);

  // Fetch token supply details from the smart contract
  const fetchSupplyDetails = async (web3) => {
    try {
      const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
      const totalSupply = await contract.methods.totalSupply().call();
      const burnedTokens = await contract.methods.burnedTokens().call();
      const currentSupply = totalSupply - burnedTokens;

      setSupplyDetails({
        totalSupply: totalSupply,
        burnedTokens: burnedTokens,
        currentSupply: currentSupply,
      });
    } catch (err) {
      setError('Failed to fetch supply details. Please try again.');
      console.error(err);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cheemsverse Token Supply</h1>
        {error && <p className="error">{error}</p>}
        {account ? (
          <div>
            <p>Connected Account: {account}</p>
            <h2>Supply Details</h2>
            <p>Total Supply: {supplyDetails.totalSupply}</p>
            <p>Burned Tokens: {supplyDetails.burnedTokens}</p>
            <p>Current Supply: {supplyDetails.currentSupply}</p>
          </div>
        ) : (
          <button onClick={() => window.ethereum.request({ method: 'eth_requestAccounts' })}>
            Connect Wallet
          </button>
        )}
      </header>
    </div>
  );
};

export default App;

// src/index.js

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// src/App.css

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

.error {
  color: red;
}
```

Make sure to replace the placeholder values for `CONTRACT_ABI` and `CONTRACT_ADDRESS` with the actual ABI and address of your smart contract. Additionally, ensure that you have the necessary dependencies installed in your project:

```bash
npm install web3
```

This code provides a basic structure for a React application that connects to a wallet and fetches token supply details from a smart contract.
