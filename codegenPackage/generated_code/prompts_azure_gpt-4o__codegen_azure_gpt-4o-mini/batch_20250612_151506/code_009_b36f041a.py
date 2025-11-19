"""
Generated Code Metadata:
========================
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Provide sample code for handling Ethereum transactions using Fortmatic in a JavaScript-based dApp.
Generated: DETERMINISTIC_b36f041a77b4ee31
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { useEffect, useState } from 'react';
import { create } from 'fortmatic';
import Web3 from 'web3';

// Initialize Fortmatic with your API key
const fm = create('YOUR_FORTMATIC_API_KEY');
const web3 = new Web3(fm.getProvider());

const App = () => {
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);

  // Function to connect to Fortmatic and get the user's account
  const connectWallet = async () => {
    try {
      // Request user to connect their wallet
      const accounts = await fm.user.login();
      setAccount(accounts[0]);
      await getBalance(accounts[0]);
    } catch (err) {
      setError('Failed to connect wallet: ' + err.message);
    }
  };

  // Function to get the balance of the connected account
  const getBalance = async (account) => {
    try {
      const balance = await web3.eth.getBalance(account);
      setBalance(web3.utils.fromWei(balance, 'ether'));
    } catch (err) {
      setError('Failed to fetch balance: ' + err.message);
    }
  };

  // Function to send Ether from the connected account
  const sendTransaction = async (recipient, amount) => {
    if (!account) {
      setError('Please connect your wallet first.');
      return;
    }

    try {
      const tx = {
        from: account,
        to: recipient,
        value: web3.utils.toWei(amount, 'ether'),
        gas: 21000, // Standard gas limit for a simple transfer
      };

      // Send the transaction
      const receipt = await web3.eth.sendTransaction(tx);
      console.log('Transaction successful with hash:', receipt.transactionHash);
    } catch (err) {
      setError('Transaction failed: ' + err.message);
    }
  };

  // Effect to handle account changes
  useEffect(() => {
    const checkAccount = async () => {
      const accounts = await fm.user.getAccounts();
      if (accounts.length > 0) {
        setAccount(accounts[0]);
        await getBalance(accounts[0]);
      }
    };

    checkAccount();
  }, []);

  return (
    <div>
      <h1>Ethereum Transaction with Fortmatic</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button onClick={connectWallet}>Connect Wallet</button>
      {account && (
        <div>
          <p>Connected Account: {account}</p>
          <p>Balance: {balance} ETH</p>
          <button onClick={() => sendTransaction('RECIPIENT_ADDRESS', '0.01')}>
            Send 0.01 ETH
          </button>
        </div>
      )}
    </div>
  );
};

export default App;
```

**Note:** Replace `'YOUR_FORTMATIC_API_KEY'` with your actual Fortmatic API key and `'RECIPIENT_ADDRESS'` with the address you want to send Ether to.
