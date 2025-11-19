"""
Generated Code Metadata:
========================
Original URL: https://notion817.tistory.com
Prompt: Generate code for a wallet connection toolbar, similar to the "티스토리툴바 guardconnect" feature described on https://notion817.tistory.com.
Generated: DETERMINISTIC_4b20ef8d4a1362a7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';

/**
 * WalletConnectionToolbar Component
 * Provides UI for connecting/disconnecting wallets and displays wallet status
 */
const WalletConnectionToolbar = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState('');
  const [provider, setProvider] = useState(null);
  const [error, setError] = useState(null);

  // Check if wallet is connected on component mount
  useEffect(() => {
    const checkWalletConnection = async () => {
      try {
        const detectedProvider = await detectEthereumProvider();
        
        if (detectedProvider) {
          setProvider(detectedProvider);
          
          const web3 = new Web3(detectedProvider);
          const accounts = await web3.eth.getAccounts();
          
          if (accounts.length > 0) {
            setIsConnected(true);
            setAccount(accounts[0]);
          }
        }
      } catch (err) {
        console.error('Error checking wallet connection:', err);
        setError('Failed to check wallet connection');
      }
    };

    checkWalletConnection();
  }, []);

  // Handle account changes
  useEffect(() => {
    if (!provider) return;

    const handleAccountsChanged = (accounts) => {
      if (accounts.length === 0) {
        setIsConnected(false);
        setAccount('');
      } else {
        setAccount(accounts[0]);
      }
    };

    provider.on('accountsChanged', handleAccountsChanged);

    return () => {
      provider.removeListener('accountsChanged', handleAccountsChanged);
    };
  }, [provider]);

  // Handle chain changes
  useEffect(() => {
    if (!provider) return;

    const handleChainChanged = () => {
      window.location.reload();
    };

    provider.on('chainChanged', handleChainChanged);

    return () => {
      provider.removeListener('chainChanged', handleChainChanged);
    };
  }, [provider]);

  /**
   * Connect wallet handler
   */
  const connectWallet = async () => {
    try {
      if (!provider) {
        throw new Error('No Ethereum provider detected');
      }

      const accounts = await provider.request({ method: 'eth_requestAccounts' });
      
      if (accounts.length > 0) {
        setIsConnected(true);
        setAccount(accounts[0]);
      }
    } catch (err) {
      console.error('Error connecting wallet:', err);
      setError('Failed to connect wallet');
    }
  };

  /**
   * Disconnect wallet handler
   */
  const disconnectWallet = () => {
    setIsConnected(false);
    setAccount('');
    setError(null);
  };

  /**
   * Format wallet address for display
   */
  const formatAddress = (addr) => {
    if (!addr) return '';
    return `${addr.substring(0, 6)}...${addr.substring(addr.length - 4)}`;
  };

  return (
    <div className="wallet-toolbar">
      <div className="toolbar-content">
        {error && (
          <div className="error-message">
            {error}
            <button onClick={() => setError(null)}>×</button>
          </div>
        )}

        {isConnected ? (
          <div className="wallet-info">
            <span className="wallet-address">{formatAddress(account)}</span>
            <button className="disconnect-btn" onClick={disconnectWallet}>
              Disconnect
            </button>
          </div>
        ) : (
          <button className="connect-btn" onClick={connectWallet}>
            Connect Wallet
          </button>
        )}
      </div>

      <style jsx>{`
        .wallet-toolbar {
          position: fixed;
          bottom: 20px;
          right: 20px;
          z-index: 1000;
          background: rgba(255, 255, 255, 0.9);
          border-radius: 8px;
          padding: 10px 15px;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          font-family: Arial, sans-serif;
        }
        
        .toolbar-content {
          display: flex;
          align-items: center;
          gap: 10px;
        }
        
        .error-message {
          background: #ffebee;
          color: #c62828;
          padding: 8px 12px;
          border-radius: 4px;
          display: flex;
          align-items: center;
          gap: 8px;
          margin-right: 10px;
        }
        
        .error-message button {
          background: none;
          border: none;
          color: #c62828;
          cursor: pointer;
          font-size: 16px;
          padding: 0;
        }
        
        .wallet-info {
          display: flex;
          align-items: center;
          gap: 10px;
        }
        
        .wallet-address {
          font-family: monospace;
          background: #f5f5f5;
          padding: 5px 10px;
          border-radius: 4px;
        }
        
        button {
          padding: 8px 16px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-weight: 500;
          transition: background 0.2s;
        }
        
        .connect-btn {
          background: #4caf50;
          color: white;
        }
        
        .connect-btn:hover {
          background: #3d8b40;
        }
        
        .disconnect-btn {
          background: #f44336;
          color: white;
        }
        
        .disconnect-btn:hover {
          background: #d32f2f;
        }
      `}</style>
    </div>
  );
};

export default WalletConnectionToolbar;
```
