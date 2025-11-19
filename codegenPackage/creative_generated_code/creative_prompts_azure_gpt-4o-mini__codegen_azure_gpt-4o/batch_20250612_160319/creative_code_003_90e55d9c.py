"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter.productsway.com
Prompt: Generate a React component for displaying account balance in a DApp, referencing the features mentioned on the Dapp Starter site.
Generated: DETERMINISTIC_90e55d9c25ba0a2e
Batch ID: 20250612_160319
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// AccountBalance.js
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// A functional React component to display account balance in a DApp
const AccountBalance = ({ providerUrl }) => {
  // State variables for account and balance
  const [account, setAccount] = useState(null);
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);

  // Function to initialize Web3 and fetch account and balance
  const loadBlockchainData = async () => {
    try {
      // Initialize Web3 instance
      const web3 = new Web3(new Web3.providers.HttpProvider(providerUrl));

      // Get accounts from the provider
      const accounts = await web3.eth.getAccounts();
      if (accounts.length === 0) {
        throw new Error('No accounts found. Please connect your wallet.');
      }
      setAccount(accounts[0]);

      // Get balance for the first account
      const balanceWei = await web3.eth.getBalance(accounts[0]);
      const balanceEth = web3.utils.fromWei(balanceWei, 'ether');
      setBalance(balanceEth);
    } catch (err) {
      // Handle errors gracefully
      setError(err.message);
    }
  };

  // useEffect hook to load blockchain data when the component mounts
  useEffect(() => {
    loadBlockchainData();
  }, [providerUrl]);

  return (
    <div className="account-balance">
      <h2>Account Balance</h2>
      {error ? (
        // Display error message if something goes wrong
        <p style={{ color: 'red' }}>Error: {error}</p>
      ) : (
        <>
          {account && <p>Account: {account}</p>}
          {balance !== null && <p>Balance: {balance} ETH</p>}
          {!account && !balance && <p>Loading...</p>}
        </>
      )}
    </div>
  );
};

// Default export for the component
export default AccountBalance;

/*
Usage:
<AccountBalance providerUrl="https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID" />
*/
```
