"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a Web3 React component that displays the Chain ID, account address, and balance of a connected wallet, following the example in the Dapp Starter framework.
Generated: DETERMINISTIC_38654168b51c7887
Batch ID: 20250612_154226
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
import { injected } from '../connectors';

interface WalletInfoProps {
  className?: string;
}

const WalletInfo: React.FC<WalletInfoProps> = ({ className }) => {
  const { account, active, chainId, library, activate, deactivate } = useWeb3React<Web3Provider>();
  const [balance, setBalance] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (active && account && library) {
      library
        .getBalance(account)
        .then((balance) => {
          setBalance(formatEther(balance));
          setError(null);
        })
        .catch((err) => {
          console.error('Error fetching balance:', err);
          setError('Failed to fetch balance');
        });
    } else {
      setBalance(null);
    }
  }, [account, active, library]);

  const connectWallet = async () => {
    try {
      await activate(injected);
      setError(null);
    } catch (err) {
      console.error('Error connecting wallet:', err);
      setError('Failed to connect wallet');
    }
  };

  const disconnectWallet = () => {
    try {
      deactivate();
      setError(null);
    } catch (err) {
      console.error('Error disconnecting wallet:', err);
      setError('Failed to disconnect wallet');
    }
  };

  return (
    <div className={`wallet-info ${className || ''}`}>
      {error && <div className="error-message">{error}</div>}
      
      {active ? (
        <div className="wallet-connected">
          <div className="wallet-detail">
            <span className="label">Chain ID:</span>
            <span className="value">{chainId}</span>
          </div>
          <div className="wallet-detail">
            <span className="label">Account:</span>
            <span className="value">{account}</span>
          </div>
          {balance && (
            <div className="wallet-detail">
              <span className="label">Balance:</span>
              <span className="value">{balance} ETH</span>
            </div>
          )}
          <button onClick={disconnectWallet} className="disconnect-button">
            Disconnect
          </button>
        </div>
      ) : (
        <button onClick={connectWallet} className="connect-button">
          Connect Wallet
        </button>
      )}
    </div>
  );
};

export default WalletInfo;
```
