"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Provide a code example for connecting MetaMask to a DApp using the methods outlined in the Dapp Starter template.
Generated: DETERMINISTIC_bc71398cb4055fdb
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

const App = () => {
  // State variables to manage the connection and account
  const [accounts, setAccounts] = useState([]);
  const [error, setError] = useState(null);
  const [web3, setWeb3] = useState(null);

  useEffect(() => {
    // Function to load Web3 and connect to MetaMask
    const loadWeb3 = async () => {
      // Check if MetaMask is installed
      if (window.ethereum) {
        // Create a new Web3 instance with the current provider
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        try {
          // Request account access
          const userAccounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccounts(userAccounts);
        } catch (err) {
          // Handle account access errors
          setError('User denied account access');
          console.error(err);
        }
      } else {
        // Handle the case when MetaMask is not installed
        setError('MetaMask is not installed. Please install it to use this DApp.');
      }
    };

    // Load Web3 on component mount
    loadWeb3();
  }, []);

  return (
    <div>
      <h1>Connect to MetaMask</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {accounts.length > 0 ? (
        <p>Connected account: {accounts[0]}</p>
      ) : (
        <button onClick={() => loadWeb3()}>Connect MetaMask</button>
      )}
    </div>
  );
};

export default App;
```
