"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethjxn.com
Prompt: Suggest tools or frameworks for building a mobile-friendly Ethereum dApp for managing pledges.
Generated: DETERMINISTIC_30527606695c9357
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import './App.css';

// PledgeDApp component for managing pledges
const PledgeDApp = () => {
  // State variables to manage pledges and web3 instance
  const [pledges, setPledges] = useState([]);
  const [pledgeAmount, setPledgeAmount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState('');

  // Initialize Web3 and get user account on component mount
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if MetaMask is installed
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } else {
          alert('Please install MetaMask to use this application.');
        }
      } catch (error) {
        console.error("Error initializing Web3:", error);
      }
    };

    initWeb3();
  }, []);

  // Function to handle pledging
  const handlePledge = async () => {
    if (!pledgeAmount || isNaN(pledgeAmount) || pledgeAmount <= 0) {
      alert('Please enter a valid pledge amount.');
      return;
    }

    try {
      // Placeholder for pledge transaction logic
      // TODO: Implement smart contract interaction for pledging
      console.log(`Pledged ${pledgeAmount} Ether from account ${account}`);
      // Clear pledge amount
      setPledgeAmount('');
    } catch (error) {
      console.error("Error processing pledge:", error);
    }
  };

  return (
    <div className="app-container">
      <h1>Pledge DApp</h1>
      <h2>Account: {account}</h2>
      <input
        type="number"
        value={pledgeAmount}
        onChange={(e) => setPledgeAmount(e.target.value)}
        placeholder="Enter pledge amount in Ether"
      />
      <button onClick={handlePledge}>Pledge</button>
      <h3>Your Pledges:</h3>
      <ul>
        {pledges.map((pledge, index) => (
          <li key={index}>{pledge} Ether</li>
        ))}
      </ul>
    </div>
  );
};

// Export the PledgeDApp component
export default PledgeDApp;
```

Make sure to install the required dependencies using npm:
```bash
npm install react web3 ethers
``` 

The code above will create a simple mobile-friendly Ethereum dApp that allows users to make pledges. Remember to implement the actual smart contract interaction to handle the pledge logic in place of the placeholder comments.
