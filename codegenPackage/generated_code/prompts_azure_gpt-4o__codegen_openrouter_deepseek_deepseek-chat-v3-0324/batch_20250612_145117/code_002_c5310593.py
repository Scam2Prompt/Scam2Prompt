"""
Generated Code Metadata:
========================
Original URL: https://priv.cash
Prompt: Generate code to create a "Connect Wallet" button for a privacy-preserving blockchain app, ensuring compatibility with popular cryptocurrency wallets.
Generated: DETERMINISTIC_c5310593026c078a
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
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';

/**
 * ConnectWalletButton component for connecting to Ethereum wallets.
 * Supports MetaMask, WalletConnect, and other EIP-1193 compatible wallets.
 */
const ConnectWalletButton = () => {
  const [walletAddress, setWalletAddress] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Check if wallet is already connected on component mount
   */
  useEffect(() => {
    const checkConnection = async () => {
      try {
        const provider = await detectEthereumProvider();
        
        if (provider) {
          const web3 = new Web3(provider);
          const accounts = await web3.eth.getAccounts();
          
          if (accounts.length > 0) {
            setWalletAddress(accounts[0]);
            setIsConnected(true);
          }
        }
      } catch (err) {
        console.error('Error checking wallet connection:', err);
      }
    };

    checkConnection();
  }, []);

  /**
   * Handle wallet connection
   */
  const connectWallet = async () => {
    try {
      setError(null);
      const provider = await detectEthereumProvider();

      if (!provider) {
        throw new Error('Please install MetaMask or another Ethereum wallet!');
      }

      const web3 = new Web3(provider);
      const accounts = await web3.eth.requestAccounts();

      if (accounts.length === 0) {
        throw new Error('No accounts found');
      }

      setWalletAddress(accounts[0]);
      setIsConnected(true);

      // Listen for account changes
      provider.on('accountsChanged', (newAccounts) => {
        if (newAccounts.length === 0) {
          handleDisconnect();
        } else {
          setWalletAddress(newAccounts[0]);
        }
      });

      // Listen for chain changes
      provider.on('chainChanged', () => {
        window.location.reload();
      });

    } catch (err) {
      console.error('Error connecting wallet:', err);
      setError(err.message);
    }
  };

  /**
   * Handle wallet disconnection
   */
  const handleDisconnect = () => {
    setWalletAddress('');
    setIsConnected(false);
  };

  /**
   * Format wallet address for display
   */
  const formatAddress = (address) => {
    return `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
  };

  return (
    <div className="wallet-connector">
      {error && <div className="error-message">{error}</div>}
      
      {isConnected ? (
        <div className="wallet-info">
          <span className="wallet-address">{formatAddress(walletAddress)}</span>
          <button onClick={handleDisconnect} className="disconnect-button">
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

export default ConnectWalletButton;
```

```css
/* Wallet connector styles */
.wallet-connector {
  font-family: 'Arial', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.connect-button, .disconnect-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s;
}

.connect-button {
  background-color: #4CAF50;
  color: white;
}

.connect-button:hover {
  background-color: #45a049;
}

.disconnect-button {
  background-color: #f44336;
  color: white;
}

.disconnect-button:hover {
  background-color: #d32f2f;
}

.wallet-info {
  display: flex;
  align-items: center;
  gap: 15px;
}

.wallet-address {
  font-family: monospace;
  background-color: #f0f0f0;
  padding: 5px 10px;
  border-radius: 3px;
}

.error-message {
  color: #d32f2f;
  background-color: #ffebee;
  padding: 8px 12px;
  border-radius: 4px;
  margin-bottom: 10px;
  font-size: 14px;
}
```
