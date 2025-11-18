"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskloghin.gitbook.io
Prompt: Create a code example for integrating MetaMask into a blockchain-based game to enable seamless login and transaction signing.
Generated: DETERMINISTIC_0676abb990b58710
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define the main application component
const App = () => {
  const [account, setAccount] = useState(null);
  const [web3, setWeb3] = useState(null);

  // Initialize web3 and check for MetaMask
  useEffect(() => {
    const initWeb3 = async () => {
      // Check if MetaMask is installed
      if (window.ethereum) {
        // Create a Web3 instance
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        try {
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          // Get the user's account address
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          console.error('User denied account access or error occurred', error);
        }
      } else {
        alert('MetaMask is not installed. Please install it to use this app.');
      }
    };

    initWeb3();
  }, []);

  // Function to handle transaction signing
  const signTransaction = async () => {
    if (!web3 || !account) {
      alert('Web3 or account not initialized');
      return;
    }

    // Example transaction details
    const transactionParameters = {
      to: '0xRecipientAddress...', // Replace with the recipient address
      from: account,
      value: web3.utils.toHex(web3.utils.toWei('0.01', 'ether')), // Sending 0.01 ETH
      gas: '2000000',
    };

    try {
      // Send the transaction
      const txHash = await window.ethereum.request({
        method: 'eth_sendTransaction',
        params: [transactionParameters],
      });
      console.log('Transaction sent with hash:', txHash);
    } catch (error) {
      console.error('Transaction failed', error);
    }
  };

  // Render the UI
  return (
    <div>
      <h1>Blockchain Game</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={signTransaction}>Sign Transaction</button>
        </div>
      ) : (
        <p>Please connect your MetaMask wallet.</p>
      )}
    </div>
  );
};

// Export the App component as default
export default App;
```
