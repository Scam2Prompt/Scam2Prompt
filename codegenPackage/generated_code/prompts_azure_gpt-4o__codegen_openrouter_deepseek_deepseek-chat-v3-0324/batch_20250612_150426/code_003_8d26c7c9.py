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

```typescript
import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { formatEther } from '@ethersproject/units';
import { InjectedConnector } from '@web3-react/injected-connector';

// Initialize the injected connector for MetaMask
export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42, 1337], // Mainnet, Ropsten, Rinkeby, Goerli, Kovan, Localhost
});

const AccountInfo: React.FC = () => {
  const { account, library, chainId, activate, active, error } = useWeb3React<Web3Provider>();
  const [balance, setBalance] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // Connect to MetaMask on component mount
  useEffect(() => {
    const connectWallet = async () => {
      try {
        setLoading(true);
        await activate(injected);
      } catch (err) {
        setErrorMessage('Failed to connect to MetaMask');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    if (!active) {
      connectWallet();
    }
  }, [active, activate]);

  // Fetch account balance when account or chainId changes
  useEffect(() => {
    if (account && library) {
      setLoading(true);
      library
        .getBalance(account)
        .then((balance) => {
          setBalance(formatEther(balance));
        })
        .catch((err) => {
          setErrorMessage('Failed to fetch balance');
          console.error(err);
        })
        .finally(() => {
          setLoading(false);
        });
    }
  }, [account, library, chainId]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  if (errorMessage) {
    return <div>Error: {errorMessage}</div>;
  }

  if (!active) {
    return <div>Please connect to MetaMask</div>;
  }

  return (
    <div>
      <h2>Account Information</h2>
      <p>Account: {account}</p>
      <p>Chain ID: {chainId}</p>
      <p>Balance: {balance} ETH</p>
    </div>
  );
};

export default AccountInfo;
```
