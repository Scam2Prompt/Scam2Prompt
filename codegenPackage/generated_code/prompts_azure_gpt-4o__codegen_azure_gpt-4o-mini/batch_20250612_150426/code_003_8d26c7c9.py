"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter.productsway.com
Prompt: Write code to display a user's account balance and chain ID in a DApp using Web3 React and MetaMask, referencing the Dapp Starter framework.
Generated: DETERMINISTIC_8d26c7c906ba6f65
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { useWeb3React } from '@web3-react/core';
import { injected } from './connectors'; // Ensure you have a connector for MetaMask

const AccountBalance = () => {
  const { account, library, activate, chainId } = useWeb3React();
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);

  // Function to fetch account balance
  const fetchBalance = async () => {
    if (account && library) {
      try {
        // Fetch balance in Wei and convert to Ether
        const balanceInWei = await library.eth.getBalance(account);
        const balanceInEther = library.utils.fromWei(balanceInWei, 'ether');
        setBalance(balanceInEther);
      } catch (err) {
        console.error('Error fetching balance:', err);
        setError('Failed to fetch balance. Please try again later.');
      }
    }
  };

  // Effect to fetch balance when account or library changes
  useEffect(() => {
    fetchBalance();
  }, [account, library]);

  // Function to connect to MetaMask
  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (err) {
      console.error('Error connecting to wallet:', err);
      setError('Failed to connect to wallet. Please try again.');
    }
  };

  return (
    <div>
      <h1>User Account Information</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button onClick={connectWallet}>Connect Wallet</button>
      {account ? (
        <div>
          <p>
            <strong>Account:</strong> {account}
          </p>
          <p>
            <strong>Chain ID:</strong> {chainId}
          </p>
          <p>
            <strong>Balance:</strong> {balance !== null ? `${balance} ETH` : 'Loading...'}
          </p>
        </div>
      ) : (
        <p>Please connect your wallet to see your account information.</p>
      )}
    </div>
  );
};

export default AccountBalance;
```

Make sure to install the necessary dependencies and set up the `injected` connector for MetaMask in your project.
