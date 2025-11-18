"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.web.app
Prompt: Write code in React to create a presale widget that allows users to connect their wallet, select a network, choose a payment currency, and purchase tokens. Include integration with the BNB Chain.
Generated: DETERMINISTIC_d6ad8c0d7dc1b4a2
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React and third-party libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define the PresaleWidget component
const PresaleWidget = () => {
  // State variables for managing wallet connection, network, currency, and amount
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [network, setNetwork] = useState('BNB Chain');
  const [currency, setCurrency] = useState('BNB');
  const [amount, setAmount] = useState('');

  // UseEffect hook to initialize Web3 instance
  useEffect(() => {
    if (window.ethereum) {
      const w3 = new Web3(window.ethereum);
      setWeb3(w3);
    } else {
      console.error("Please install MetaMask to use this app.");
    }
  }, []);

  // Function to connect wallet
  const connectWallet = async () => {
    if (web3) {
      try {
        // Request account access
        const accounts = await web3.eth.requestAccounts();
        setAccounts(accounts);
      } catch (error) {
        console.error("Failed to connect wallet:", error);
      }
    } else {
      console.error("Web3 is not initialized.");
    }
  };

  // Function to handle currency change
  const handleCurrencyChange = (event) => {
    setCurrency(event.target.value);
  };

  // Function to handle amount input change
  const handleAmountChange = (event) => {
    setAmount(event.target.value);
  };

  // Function to handle purchase action
  const handlePurchase = async () => {
    if (!amount || isNaN(amount) || parseFloat(amount) <= 0) {
      alert("Please enter a valid amount.");
      return;
    }

    if (web3 && accounts.length > 0) {
      try {
        const value = web3.utils.toWei(amount, 'ether'); // Convert amount to Wei
        // Example transaction details - adjust based on your smart contract
        const txParams = {
          from: accounts[0],
          to: 'YOUR_CONTRACT_ADDRESS', // Replace with your contract address
          value: value,
          gas: 2000000,
        };

        // Send transaction
        await web3.eth.sendTransaction(txParams);
        alert("Purchase successful!");
      } catch (error) {
        console.error("Transaction failed:", error);
        alert("Transaction failed. Please try again.");
      }
    } else {
      console.error("Wallet not connected or Web3 is not initialized.");
    }
  };

  return (
    <div>
      <h1>Presale Widget</h1>
      <button onClick={connectWallet}>
        {accounts.length > 0 ? `Connected: ${accounts[0]}` : 'Connect Wallet'}
      </button>
      <div>
        <label htmlFor="network">Select Network:</label>
        <select id="network" value={network} onChange={(e) => setNetwork(e.target.value)}>
          <option value="BNB Chain">BNB Chain</option>
          {/* Other networks can be added here */}
        </select>
      </div>
      <div>
        <label htmlFor="currency">Select Currency:</label>
        <select id="currency" value={currency} onChange={handleCurrencyChange}>
          <option value="BNB">BNB</option>
          {/* More currencies can be added here */}
        </select>
      </div>
      <div>
        <label htmlFor="amount">Amount:</label>
        <input
          type="number"
          id="amount"
          value={amount}
          onChange={handleAmountChange}
          placeholder="Enter amount"
        />
      </div>
      <button onClick={handlePurchase}>Purchase Tokens</button>
    </div>
  );
};

export default PresaleWidget;
```

Make sure to replace `'YOUR_CONTRACT_ADDRESS'` with the actual address of your smart contract. This code provides a complete presale widget that allows users to connect their wallet, select a network, choose a payment currency, and purchase tokens, specifically designed for the BNB Chain.
