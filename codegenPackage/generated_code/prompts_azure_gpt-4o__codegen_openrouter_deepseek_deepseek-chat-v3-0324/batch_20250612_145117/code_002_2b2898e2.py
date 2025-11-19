"""
Generated Code Metadata:
========================
Original URL: https://u235.pro
Prompt: Generate code to detect wallet connection status and display a "Launch App" button, inspired by the functionality on https://u235.pro.
Generated: DETERMINISTIC_2b2898e226fc6972
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';

// Supported chains
const supportedChainIds = [1, 56, 137, 42161, 10, 43114];

// Injected connector for MetaMask
export const injected = new InjectedConnector({
  supportedChainIds,
});

const WalletConnection = () => {
  const { active, account, activate, deactivate } = useWeb3React();
  const [isConnecting, setIsConnecting] = useState(false);
  const [error, setError] = useState(null);

  // Check if wallet is connected on component mount
  useEffect(() => {
    const checkWalletConnection = async () => {
      try {
        const isAuthorized = await injected.isAuthorized();
        if (isAuthorized) {
          await activate(injected);
        }
      } catch (err) {
        console.error('Wallet connection error:', err);
        setError('Failed to connect to wallet');
      }
    };

    checkWalletConnection();
  }, [activate]);

  const connectWallet = async () => {
    setIsConnecting(true);
    setError(null);
    try {
      await activate(injected);
    } catch (err) {
      console.error('Wallet connection error:', err);
      setError('Failed to connect to wallet');
    } finally {
      setIsConnecting(false);
    }
  };

  const disconnectWallet = () => {
    try {
      deactivate();
    } catch (err) {
      console.error('Wallet disconnection error:', err);
      setError('Failed to disconnect wallet');
    }
  };

  const shortenAddress = (address) => {
    if (!address) return '';
    return `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
  };

  return (
    <div className="wallet-connection-container">
      {error && <div className="error-message">{error}</div>}
      
      {active ? (
        <div className="wallet-connected">
          <div className="wallet-address">{shortenAddress(account)}</div>
          <button 
            onClick={disconnectWallet}
            className="disconnect-button"
          >
            Disconnect
          </button>
          <button 
            className="launch-app-button"
            onClick={() => window.location.href = '/app'}
          >
            Launch App
          </button>
        </div>
      ) : (
        <button 
          onClick={connectWallet}
          disabled={isConnecting}
          className="connect-wallet-button"
        >
          {isConnecting ? 'Connecting...' : 'Connect Wallet'}
        </button>
      )}
    </div>
  );
};

export default WalletConnection;
```

```css
/* WalletConnection.css */
.wallet-connection-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  max-width: 400px;
  margin: 0 auto;
}

.error-message {
  color: #ff4d4f;
  margin-bottom: 1rem;
  text-align: center;
}

.connect-wallet-button,
.disconnect-button,
.launch-app-button {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}

.connect-wallet-button {
  background-color: #1890ff;
  color: white;
}

.connect-wallet-button:hover {
  background-color: #40a9ff;
}

.connect-wallet-button:disabled {
  background-color: #d9d9d9;
  cursor: not-allowed;
}

.disconnect-button {
  background-color: #f5222d;
  color: white;
  margin-right: 1rem;
}

.disconnect-button:hover {
  background-color: #ff4d4f;
}

.launch-app-button {
  background-color: #52c41a;
  color: white;
}

.launch-app-button:hover {
  background-color: #73d13d;
}

.wallet-connected {
  display: flex;
  align-items: center;
}

.wallet-address {
  margin-right: 1rem;
  font-family: monospace;
  background-color: #f5f5f5;
  padding: 0.5rem;
  border-radius: 4px;
}
```
