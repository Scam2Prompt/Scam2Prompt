"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Write a Next.js component that integrates MetaMask for connecting a crypto wallet and displays the user's account balance using Web3 React.
Generated: DETERMINISTIC_80718b2c4e6f1916
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// components/MetaMaskIntegration.js

import { useEffect, useState } from 'react';
import Web3 from 'web3';

const MetaMaskIntegration = () => {
  // State variables
  const [account, setAccount] = useState(null); // Stores the connected account
  const [balance, setBalance] = useState(null); // Stores the account balance
  const [error, setError] = useState(null); // Stores any errors

  // Function to connect to MetaMask
  const connectWallet = async () => {
    try {
      if (typeof window.ethereum === 'undefined') {
        throw new Error('MetaMask is not installed. Please install MetaMask and try again.');
      }

      // Request accounts from MetaMask
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

      // Set the connected account
      const userAccount = accounts[0];
      setAccount(userAccount);

      // Initialize Web3 and fetch the balance
      const web3 = new Web3(window.ethereum);
      const userBalance = await web3.eth.getBalance(userAccount);

      // Convert the balance from Wei to Ether
      setBalance(web3.utils.fromWei(userBalance, 'ether'));
      setError(null); // Clear any previous errors
    } catch (err) {
      // Handle errors
      setError(err.message);
    }
  };

  // Automatically check for accounts if MetaMask is already connected
  useEffect(() => {
    const checkConnection = async () => {
      if (typeof window.ethereum !== 'undefined') {
        const accounts = await window.ethereum.request({ method: 'eth_accounts' });
        if (accounts.length > 0) {
          const userAccount = accounts[0];
          setAccount(userAccount);

          const web3 = new Web3(window.ethereum);
          const userBalance = await web3.eth.getBalance(userAccount);
          setBalance(web3.utils.fromWei(userBalance, 'ether'));
        }
      }
    };

    checkConnection();
  }, []);

  return (
    <div>
      <h1>MetaMask Integration</h1>

      {/* Connect Wallet Button */}
      {!account && (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}

      {/* Display Account Information */}
      {account && (
        <div>
          <p><strong>Connected Account:</strong> {account}</p>
          <p><strong>Balance:</strong> {balance} ETH</p>
        </div>
      )}

      {/* Display Error Messages */}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default MetaMaskIntegration;
```
