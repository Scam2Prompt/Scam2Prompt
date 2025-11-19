"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Explain how to manage account balances in a DApp with Web3 React and MetaMask integration.
Generated: DETERMINISTIC_797a6db5c631638a
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for managing account balances in a DApp using Web3.js and Web3 React with MetaMask integration:

```javascript
// Dependencies: web3, @web3-react/core, @metamask/controllers
import { useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import Web3 from 'web3';
import { useEffect, useState } from 'react';

// Configure the Injected Connector for MetaMask
export const injectedConnector = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet, Ropsten, Rinkeby, Goerli, Kovan
});

/**
 * Custom hook for managing account balance
 * @returns {Object} - Account data and utility functions
 */
export const useAccountBalance = () => {
  const { account, library, activate, deactivate, active } = useWeb3React();
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  // Connect to MetaMask wallet
  const connect = async () => {
    try {
      setLoading(true);
      await activate(injectedConnector);
      setError(null);
    } catch (err) {
      setError(err.message || 'Failed to connect to MetaMask');
    } finally {
      setLoading(false);
    }
  };

  // Disconnect from wallet
  const disconnect = () => {
    try {
      deactivate();
      setBalance(null);
      setError(null);
    } catch (err) {
      setError('Failed to disconnect');
    }
  };

  // Fetch account balance
  const fetchBalance = async () => {
    if (!account || !library) return;

    try {
      setLoading(true);
      const web3 = new Web3(library.provider);
      const weiBalance = await web3.eth.getBalance(account);
      const etherBalance = web3.utils.fromWei(weiBalance, 'ether');
      setBalance(etherBalance);
      setError(null);
    } catch (err) {
      setError(err.message || 'Failed to fetch balance');
    } finally {
      setLoading(false);
    }
  };

  // Fetch balance when account changes
  useEffect(() => {
    if (account) {
      fetchBalance();
      
      // Set up balance subscription
      const web3 = new Web3(library?.provider);
      const subscription = web3.eth.subscribe('newBlockHeaders', (error) => {
        if (error) {
          console.error('Error subscribing to new blocks:', error);
          return;
        }
        fetchBalance();
      });

      return () => {
        if (subscription) {
          subscription.unsubscribe();
        }
      };
    }
  }, [account, library]);

  // Auto-connect on component mount
  useEffect(() => {
    const tryConnect = async () => {
      const isAuthorized = await injectedConnector.isAuthorized();
      if (isAuthorized && !active && !loading) {
        connect();
      }
    };
    
    tryConnect();
  }, []);

  return {
    account,
    balance,
    error,
    loading,
    connected: active,
    connect,
    disconnect,
    refreshBalance: fetchBalance,
  };
};

// Example component using the hook
export const AccountManager = () => {
  const {
    account,
    balance,
    connected,
    connect,
    disconnect,
    error,
    loading,
  } = useAccountBalance();

  return (
    <div className="account-manager">
      {error && <div className="error">{error}</div>}
      
      {connected ? (
        <div className="account-info">
          <p>Connected: {account}</p>
          <p>Balance: {balance || '0'} ETH</p>
          <button onClick={disconnect} disabled={loading}>
            Disconnect
          </button>
        </div>
      ) : (
        <button onClick={connect} disabled={loading}>
          {loading ? 'Connecting...' : 'Connect to MetaMask'}
        </button>
      )}
    </div>
  );
};
```
