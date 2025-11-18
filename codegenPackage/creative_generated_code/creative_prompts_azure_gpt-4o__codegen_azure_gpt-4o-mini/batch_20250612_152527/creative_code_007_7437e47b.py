"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://register-monprotocol.pages.dev
Prompt: Create a web interface using React.js that allows users to connect their wallets and view their MON Protocol presale allocations.
Generated: DETERMINISTIC_7437e47b22510409
Batch ID: 20250612_152527
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

// Define the main App component
const App = () => {
  // State variables to hold wallet information and allocation data
  const [account, setAccount] = useState(null);
  const [allocation, setAllocation] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // Initialize Web3
  const web3 = new Web3(window.ethereum);

  // Function to connect to the user's wallet
  const connectWallet = async () => {
    try {
      setLoading(true);
      // Request account access if needed
      await window.ethereum.request({ method: 'eth_requestAccounts' });
      const accounts = await web3.eth.getAccounts();
      setAccount(accounts[0]);
      fetchAllocation(accounts[0]); // Fetch allocation for the connected account
    } catch (err) {
      setError('Failed to connect wallet. Please try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Function to fetch allocation data from the MON Protocol smart contract
  const fetchAllocation = async (account) => {
    try {
      setLoading(true);
      // Replace with the actual contract address and ABI
      const contractAddress = '0xYourContractAddressHere';
      const contractABI = [
        // Add your contract ABI here
      ];
      const contract = new web3.eth.Contract(contractABI, contractAddress);
      const result = await contract.methods.getPresaleAllocation(account).call();
      setAllocation(result);
    } catch (err) {
      setError('Failed to fetch allocation. Please check your wallet and try again.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>MON Protocol Presale Allocation</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {loading && <p>Loading...</p>}
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <h2>Connected Account: {account}</h2>
          {allocation !== null ? (
            <p>Your Presale Allocation: {allocation}</p>
          ) : (
            <p>No allocation data found.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default App;
```

### Note:
1. Replace `0xYourContractAddressHere` with the actual smart contract address.
2. Fill in the contract ABI within the `contractABI` array.
