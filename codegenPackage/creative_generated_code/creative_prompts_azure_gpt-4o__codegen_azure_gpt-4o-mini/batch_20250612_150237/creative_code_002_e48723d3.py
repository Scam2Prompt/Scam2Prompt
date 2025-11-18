"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a React component that displays the user's blockchain account balance and chain ID, leveraging Web3 React as described in the Dapp Starter.
Generated: DETERMINISTIC_e48723d3f9ea58bf
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { ethers } from 'ethers';

/**
 * BlockchainAccountInfo component displays the user's blockchain account balance and chain ID.
 * It uses the Web3 React library to fetch user account details.
 */
const BlockchainAccountInfo = () => {
  const { account, library, chainId, active } = useWeb3React();
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchBalance = async () => {
      if (account && library) {
        try {
          // Fetch balance from the blockchain
          const balanceBigNumber = await library.getBalance(account);
          // Convert balance from Wei to Ether
          const balanceInEther = ethers.utils.formatEther(balanceBigNumber);
          setBalance(balanceInEther);
        } catch (err) {
          // Handle errors while fetching balance
          console.error('Error fetching balance:', err);
          setError('Failed to fetch balance. Please try again later.');
        }
      }
    };

    fetchBalance();
  }, [account, library]);

  // Render loading state or error message if applicable
  if (!active) {
    return <div>Please connect your wallet.</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h3>Account Information</h3>
      <p><strong>Account:</strong> {account}</p>
      <p><strong>Chain ID:</strong> {chainId}</p>
      <p><strong>Balance:</strong> {balance !== null ? `${balance} ETH` : 'Loading...'}</p>
    </div>
  );
};

export default BlockchainAccountInfo;
```
