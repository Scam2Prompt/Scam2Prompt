"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hjiihhhgg.pages.dev
Prompt: Generate code to connect a noncustodial wallet to a decentralized Dapp using Ethereum, Binance, or Polygon protocols.
Generated: DETERMINISTIC_62828c6183698f89
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import Web3 from 'web3';
import { useEffect, useState } from 'react';
import { ethers } from 'ethers';

// Define a functional component for connecting to a DApp
const DAppConnector = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [error, setError] = useState(null);

  // Function to initialize Web3
  const initWeb3 = async () => {
    // Check if MetaMask is installed
    if (window.ethereum) {
      try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        // Get the user's Ethereum account
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);
      } catch (err) {
        setError('Error connecting to wallet: ' + err.message);
      }
    } else {
      setError('Please install MetaMask to use this DApp');
    }
  };

  // Effect to set up the connection when the component mounts
  useEffect(() => {
    initWeb3();
  }, []);

  // Render the component
  return (
    <div>
      <h1>Connect to DApp</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {account ? (
        <p>Connected as: {account}</p>
      ) : (
        <button onClick={initWeb3}>Connect Wallet</button>
      )}
    </div>
  );
};

export default DAppConnector;

// Include the following CSS for better UI (optional)
// styles.css
// body {
//   font-family: Arial, sans-serif;
//   display: flex;
//   flex-direction: column;
//   align-items: center;
//   margin-top: 50px;
// }
// button {
//   background-color: #4CAF50;
//   color: white;
//   padding: 10px 20px;
//   border: none;
//   border-radius: 5px;
//   cursor: pointer;
// }
// button:hover {
//   background-color: #45a049;
// }
```
