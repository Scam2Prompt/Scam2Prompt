"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://resume.khtain.com
Prompt: Recommend JavaScript libraries for building Web3 applications similar to Cool-Web3 and demonstrate their usage in code.
Generated: DETERMINISTIC_15087ec3de87a102
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries for building Web3 applications
import Web3 from 'web3'; // A library to interact with the Ethereum blockchain
import { ethers } from 'ethers'; // A library for Ethereum wallet and contract interactions
import { useEffect, useState } from 'react'; // React hooks for managing state and side effects

// Define a functional component for the Web3 application
const Web3App = () => {
  // State variables to manage blockchain data
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState('0');

  // Function to connect to the user's wallet
  const connectWallet = async () => {
    if (window.ethereum) {
      try {
        // Request wallet connection
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]); // Set the first account as the active account
        fetchBalance(accounts[0]); // Fetch the balance for the connected account
      } catch (error) {
        console.error('Failed to connect wallet:', error); // Handle errors
      }
    } else {
      alert('Please install MetaMask!');
    }
  };

  // Function to fetch the balance of the connected account
  const fetchBalance = async (account) => {
    try {
      const web3 = new Web3(window.ethereum); // Create a Web3 instance
      const balance = await web3.eth.getBalance(account); // Get account balance
      setBalance(web3.utils.fromWei(balance, 'ether')); // Convert balance from wei to ether
    } catch (error) {
      console.error('Failed to fetch balance:', error); // Handle errors
    }
  };

  // Effect to trigger wallet connection on component mount
  useEffect(() => {
    connectWallet(); // Automatically connect wallet on load
  }, []);

  // Render the application UI
  return (
    <div>
      <h1>Web3 Application</h1>
      <p>Connected Account: {account}</p>
      <p>Balance: {balance} ETH</p>
      <button onClick={connectWallet}>Connect Wallet</button>
    </div>
  );
};

// Export the Web3App component for use in other parts of the application
export default Web3App;
```

### Required Libraries Installation
To run this code, ensure you have the following libraries installed in your project:

```bash
npm install web3 ethers react
```

### Important Note:
Make sure to add error handling and user feedback in production code for a better user experience.
