"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-curve.com
Prompt: How can I integrate the MetaMask SDK into my dapp for enhanced Web3 functionality?
Generated: DETERMINISTIC_66616ca7a74819ec
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Ensure web3 is injected by MetaMask
const MetaMaskIntegration = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  
  // Function to initialize Web3 and connect to MetaMask
  const initializeWeb3 = async () => {
    if (window.ethereum) {
      // Create a new instance of Web3 using the injected provider
      const web3Instance = new Web3(window.ethereum);
      setWeb3(web3Instance);

      try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);  // Set the first account as the current account
      } catch (error) {
        console.error("Error accessing accounts: ", error);
        alert('You need to allow MetaMask to access your accounts.');
      }
    } else {
      console.error("MetaMask is not installed.");
      alert('Please install MetaMask to use this dApp.');
    }
  };

  // Effect to initialize Web3 on component mount
  useEffect(() => {
    initializeWeb3();
  }, []);

  return (
    <div>
      <h1>MetaMask Integration</h1>
      {account ? (
        <p>Connected Account: {account}</p>
      ) : (
        <p>Please connect your MetaMask wallet.</p>
      )}
      <button onClick={initializeWeb3}>Connect to MetaMask</button>
    </div>
  );
};

export default MetaMaskIntegration;
```
