"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a function in TypeScript that retrieves the user's blockchain account details and displays them, referencing the Dapp Starter's integration of Web3 React.
Generated: DETERMINISTIC_a4a22b9d124bc9cb
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { useEffect, useState } from 'react';

interface AccountDetails {
  account: string | null;
  chainId: number | null;
  balance: string | null;
}

/**
 * Retrieves and displays the user's blockchain account details using Web3React.
 * @returns An object containing account details (address, chainId, balance) or null if not connected.
 */
export function useAccountDetails(): AccountDetails {
  const { account, library, chainId } = useWeb3React<Web3Provider>();
  const [balance, setBalance] = useState<string | null>(null);

  useEffect(() => {
    if (!account || !library) {
      setBalance(null);
      return;
    }

    async function fetchBalance() {
      try {
        const balance = await library.getBalance(account);
        setBalance(balance.toString());
      } catch (error) {
        console.error('Error fetching balance:', error);
        setBalance(null);
      }
    }

    fetchBalance();
  }, [account, library]);

  return {
    account: account || null,
    chainId: chainId || null,
    balance,
  };
}

/**
 * Component that displays the user's blockchain account details.
 */
export function AccountDetailsDisplay() {
  const { account, chainId, balance } = useAccountDetails();

  if (!account) {
    return <div>Not connected to a wallet</div>;
  }

  return (
    <div>
      <h2>Account Details</h2>
      <p><strong>Address:</strong> {account}</p>
      <p><strong>Chain ID:</strong> {chainId}</p>
      <p><strong>Balance:</strong> {balance ? `${balance} wei` : 'Loading...'}</p>
    </div>
  );
}
```
