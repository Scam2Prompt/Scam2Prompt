"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-secret.vercel.app
Prompt: How can I create a React app that integrates with MetaMask for Ethereum transactions?
Generated: DETERMINISTIC_88f2dee773349051
Batch ID: 20250612_163950
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
import './App.css'; // Import CSS for styling

// Main App component
const App = () => {
  // State to hold account information and web3 instance
  const [account, setAccount] = useState('');
  const [web3, setWeb3] = useState(null);

  // Effect to load Web3 and request account access
  useEffect(() => {
    const loadWeb3 = async () => {
      // Check if MetaMask is installed
      if (window.ethereum) {
        try {
          // Create a new Web3 instance
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);

          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          console.error("Error accessing MetaMask accounts:", error);
        }
      } else {
        alert('MetaMask is not installed. Please install it to use this app.');
      }
    };

    loadWeb3();
  }, []);

  // Function to handle Ethereum transactions
  const sendTransaction = async () => {
    if (!web3 || !account) {
      alert('Please connect your MetaMask account first.');
      return;
    }

    // Define the transaction parameters
    const transactionParameters = {
      to: '0xRecipientAddress', // Replace with recipient address
      from: account, // Use the connected account
      value: web3.utils.toHex(web3.utils.toWei('0.01', 'ether')), // Amount in Wei
    };

    // Send the transaction
    try {
      await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParameters],
      });
      alert('Transaction sent successfully!');
    } catch (error) {
      console.error("Transaction error:", error);
      alert('Transaction failed. Check the console for details.');
    }
  };

  return (
    <div className="App">
      <h1>Ethereum Transaction App</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={sendTransaction}>Send 0.01 ETH</button>
        </div>
      ) : (
        <p>Please connect your MetaMask wallet.</p>
      )}
    </div>
  );
};

export default App;
```
