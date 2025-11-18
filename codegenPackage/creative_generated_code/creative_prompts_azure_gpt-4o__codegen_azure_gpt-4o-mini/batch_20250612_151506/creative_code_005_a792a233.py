"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Explain how to use Fortmatic to manage wallet interactions in a web3 dApp and provide code examples.
Generated: DETERMINISTIC_a792a23374960dcf
Batch ID: 20250612_151506
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
import { Fortmatic } from 'fortmatic';
import Web3 from 'web3';

// Create a Fortmatic instance with your API key
const fm = new Fortmatic('YOUR_FORTMATIC_API_KEY');

// Create a Web3 instance with Fortmatic provider
const web3 = new Web3(fm.getProvider());

const App = () => {
  // State to hold the user's account and balance
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);

  // Function to connect to the user's wallet
  const connectWallet = async () => {
    try {
      // Request the user to connect their wallet
      const accounts = await fm.user.login();
      if (accounts.length > 0) {
        // Set the first account in state
        setAccount(accounts[0]);
        // Fetch and set the account's balance
        const balanceWei = await web3.eth.getBalance(accounts[0]);
        setBalance(web3.utils.fromWei(balanceWei, 'ether'));
      }
    } catch (error) {
      console.error('Error connecting to wallet:', error);
    }
  };

  // Function to disconnect the wallet
  const disconnectWallet = async () => {
    try {
      // Logout the user from Fortmatic
      await fm.user.logout();
      // Reset state
      setAccount('');
      setBalance(0);
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  // Use useEffect to automatically fetch balance when account changes
  useEffect(() => {
    const fetchBalance = async () => {
      if (account) {
        try {
          const balanceWei = await web3.eth.getBalance(account);
          setBalance(web3.utils.fromWei(balanceWei, 'ether'));
        } catch (error) {
          console.error('Error fetching balance:', error);
        }
      }
    };

    fetchBalance();
  }, [account]);

  return (
    <div>
      <h1>Wallet Interaction with Fortmatic</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Balance: {balance} ETH</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default App;
```

### Notes:
- Replace `'YOUR_FORTMATIC_API_KEY'` with your actual Fortmatic API key.
- Ensure you have the necessary packages installed in your project: `react`, `fortmatic`, and `web3`.
- This code example demonstrates a simple React component that connects to a Fortmatic wallet, fetches the user's account and balance, and allows disconnecting the wallet while handling errors appropriately.
