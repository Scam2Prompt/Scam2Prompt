"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Provide a step-by-step guide to create a frontend interface using React and web3.js for minting `.linea` usernames, including wallet connection and domain selection.
Generated: DETERMINISTIC_259e8949c1cc1f0a
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Constants for the smart contract
const CONTRACT_ADDRESS = 'YOUR_CONTRACT_ADDRESS';
const ABI = [
  // Your contract ABI here
];

// Create a functional component for the app
const MintUsername = () => {
  const [account, setAccount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [domain, setDomain] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Initialize web3 and set up account on component mount
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if MetaMask is installed
        if (window.ethereum) {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Request account access
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);
        } else {
          setError('Please install MetaMask!');
        }
      } catch (err) {
        setError('Failed to connect to wallet: ' + err.message);
      }
    };

    initWeb3();
  }, []);

  // Function to handle domain selection
  const handleDomainChange = (event) => {
    setDomain(event.target.value);
  };

  // Function to mint the username
  const mintUsername = async () => {
    if (!web3) {
      setError('Web3 is not initialized.');
      return;
    }
    
    // Reset error and start loading
    setError('');
    setLoading(true);

    try {
      const contract = new web3.eth.Contract(ABI, CONTRACT_ADDRESS);
      const result = await contract.methods.mint(domain).send({ from: account });

      // Handle successful minting
      console.log('Minting successful:', result);
      alert(`Username ${domain} minted successfully!`);
    } catch (err) {
      // Catch errors during the transaction
      setError('Minting failed: ' + err.message);
    } finally {
      // Stop loading state
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Mint your .linea Username</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          <div>
            <label htmlFor="domain">Choose your username:</label>
            <input
              id="domain"
              type="text"
              value={domain}
              onChange={handleDomainChange}
              placeholder="Enter .linea username"
            />
          </div>
          <button onClick={mintUsername} disabled={!domain}>
            Mint Username
          </button>
          {account && <p>Connected account: {account}</p>}
        </>
      )}
    </div>
  );
};

// Export the component for use in other parts of the application
export default MintUsername;
```
