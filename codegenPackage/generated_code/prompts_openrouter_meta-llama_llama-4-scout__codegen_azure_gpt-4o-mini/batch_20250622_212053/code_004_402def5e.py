"""
Generated Code Metadata:
========================
Original URL: https://etbkwf.com
Prompt: "Create a basic example of a decentralized application (dapp) using React and Ethereum blockchain."
Generated: DETERMINISTIC_402def5e0d7e4b27
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define the DApp component
const DApp = () => {
  // State variables
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [web3, setWeb3] = useState(null);

  // Initialize Web3 and fetch account details
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

          // Fetch account balance
          const balance = await web3Instance.eth.getBalance(accounts[0]);
          setBalance(web3Instance.utils.fromWei(balance, 'ether'));
        } else {
          alert('Please install MetaMask to use this DApp.');
        }
      } catch (error) {
        console.error('Error initializing Web3:', error);
      }
    };

    initWeb3();
  }, []);

  return (
    <div style={{ padding: '20px' }}>
      <h1>My Decentralized Application (DApp)</h1>
      <h2>Account: {account}</h2>
      <h2>Balance: {balance} ETH</h2>
    </div>
  );
};

// Export the DApp component
export default DApp;
```

### Additional Setup Instructions
1. Ensure you have Node.js and npm installed.
2. Create a new React app using `npx create-react-app my-dapp`.
3. Navigate to the project directory: `cd my-dapp`.
4. Install Web3.js: `npm install web3`.
5. Replace the contents of `src/App.js` with the provided code.
6. Run the application using `npm start`.
7. Make sure you have MetaMask installed and set up in your browser.
