"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a React component that displays the user's blockchain account balance and chain ID, leveraging Web3 React as described in the Dapp Starter.
Generated: DETERMINISTIC_e48723d3f9ea58bf
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { formatEther } from '@ethersproject/units';

/**
 * Displays the user's blockchain account balance and chain ID
 */
const AccountInfo = () => {
  const { account, library, chainId } = useWeb3React<Web3Provider>();
  const [balance, setBalance] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!account || !library) {
      setBalance(null);
      return;
    }

    let stale = false;

    async function fetchBalance() {
      try {
        const balance = await library.getBalance(account);
        if (!stale) {
          setBalance(formatEther(balance));
        }
      } catch (err) {
        if (!stale) {
          setError('Failed to fetch balance');
          console.error('Error fetching balance:', err);
        }
      }
    }

    fetchBalance();

    // Create a cleanup function to avoid state updates after unmount
    return () => {
      stale = true;
      setBalance(null);
    };
  }, [account, library]);

  if (!account) {
    return <div>Please connect your wallet</div>;
  }

  return (
    <div>
      <div>
        <strong>Account:</strong> {account}
      </div>
      <div>
        <strong>Chain ID:</strong> {chainId}
      </div>
      <div>
        <strong>Balance:</strong> {balance ? `${balance} ETH` : 'Loading...'}
      </div>
      {error && (
        <div style={{ color: 'red' }}>
          <strong>Error:</strong> {error}
        </div>
      )}
    </div>
  );
};

export default AccountInfo;
```
