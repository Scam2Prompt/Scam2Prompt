"""
Generated Code Metadata:
========================
Original URL: https://snsy-ai.pages.dev
Prompt: Create a front-end implementation in JavaScript for connecting a wallet to a blockchain-based vesting portal, inspired by Sensay's user interface.
Generated: DETERMINISTIC_2780cee1abe19039
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnector.js - Front-end implementation for connecting a wallet to a blockchain vesting portal

import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import detectEthereumProvider from '@metamask/detect-provider';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

// Supported wallet providers
const WALLET_PROVIDERS = {
  METAMASK: 'metamask',
  WALLETCONNECT: 'walletconnect',
  COINBASE: 'coinbase'
};

const WalletConnector = () => {
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [chainId, setChainId] = useState(null);
  const [isConnecting, setIsConnecting] = useState(false);
  const [activeProvider, setActiveProvider] = useState(null);

  // Initialize and check for provider
  useEffect(() => {
    const init = async () => {
      const provider = await detectEthereumProvider();
      if (provider) {
        const web3Instance = new Web3(provider);
        setWeb3(web3Instance);
        
        // Listen for account changes
        provider.on('accountsChanged', (newAccounts) => {
          setAccounts(newAccounts);
        });

        // Listen for chain changes
        provider.on('chainChanged', (newChainId) => {
          window.location.reload();
        });
      }
    };

    init();
    return () => {
      if (web3 && web3.currentProvider && web3.currentProvider.removeListener) {
        web3.currentProvider.removeListener('accountsChanged');
        web3.currentProvider.removeListener('chainChanged');
      }
    };
  }, []);

  const connectWallet = async (providerType) => {
    try {
      setIsConnecting(true);
      
      if (!window.ethereum) {
        throw new Error('No Ethereum provider found');
      }

      let provider;
      switch (providerType) {
        case WALLET_PROVIDERS.METAMASK:
          provider = window.ethereum;
          break;
        case WALLET_PROVIDERS.WALLETCONNECT:
          // WalletConnect implementation would go here
          break;
        case WALLET_PROVIDERS.COINBASE:
          // Coinbase Wallet implementation would go here
          break;
        default:
          throw new Error('Unsupported wallet provider');
      }

      // Request account access
      const accounts = await provider.request({ method: 'eth_requestAccounts' });
      const chainId = await provider.request({ method: 'eth_chainId' });

      setAccounts(accounts);
      setChainId(chainId);
      setActiveProvider(providerType);
      
      toast.success('Wallet connected successfully!');
    } catch (error) {
      console.error('Wallet connection error:', error);
      toast.error(`Failed to connect wallet: ${error.message}`);
    } finally {
      setIsConnecting(false);
    }
  };

  const disconnectWallet = () => {
    setAccounts([]);
    setChainId(null);
    setActiveProvider(null);
    toast.info('Wallet disconnected');
  };

  const formatAddress = (address) => {
    if (!address) return '';
    return `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
  };

  const getNetworkName = (id) => {
    const networks = {
      '0x1': 'Ethereum Mainnet',
      '0x5': 'Goerli Testnet',
      '0xaa36a7': 'Sepolia Testnet',
      '0x89': 'Polygon Mainnet',
      '0x13881': 'Mumbai Testnet'
    };
    return networks[id] || `Unknown Network (${id})`;
  };

  return (
    <div className="wallet-connector">
      <div className="wallet-status">
        {accounts.length > 0 ? (
          <div className="connected-wallet">
            <div className="wallet-info">
              <span className="network">{getNetworkName(chainId)}</span>
              <span className="address">{formatAddress(accounts[0])}</span>
            </div>
            <button 
              onClick={disconnectWallet}
              className="disconnect-btn"
            >
              Disconnect
            </button>
          </div>
        ) : (
          <div className="wallet-options">
            <h3>Connect your wallet</h3>
            <button
              onClick={() => connectWallet(WALLET_PROVIDERS.METAMASK)}
              disabled={isConnecting}
              className={`connect-btn ${isConnecting ? 'loading' : ''}`}
            >
              {isConnecting ? 'Connecting...' : 'MetaMask'}
            </button>
            <button
              onClick={() => connectWallet(WALLET_PROVIDERS.WALLETCONNECT)}
              disabled={isConnecting}
              className={`connect-btn ${isConnecting ? 'loading' : ''}`}
            >
              {isConnecting ? 'Connecting...' : 'WalletConnect'}
            </button>
            <button
              onClick={() => connectWallet(WALLET_PROVIDERS.COINBASE)}
              disabled={isConnecting}
              className={`connect-btn ${isConnecting ? 'loading' : ''}`}
            >
              {isConnecting ? 'Connecting...' : 'Coinbase Wallet'}
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default WalletConnector;

// CSS would typically be in a separate file, but included here for completeness
/*
.wallet-connector {
  font-family: 'Arial', sans-serif;
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  background: #f8f9fa;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.wallet-status {
  text-align: center;
}

.connected-wallet {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.wallet-info {
  display: flex;
  flex-direction: column;
  gap: 5px;
  margin-bottom: 15px;
}

.network {
  font-size: 14px;
  color: #666;
}

.address {
  font-size: 16px;
  font-weight: bold;
  word-break: break-all;
}

.connect-btn, .disconnect-btn {
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  background: #6200ee;
  color: white;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.3s;
}

.connect-btn:hover, .disconnect-btn:hover {
  background: #3700b3;
}

.connect-btn:disabled {
  background: #cccccc;
  cursor: not-allowed;
}

.connect-btn.loading {
  position: relative;
}

.connect-btn.loading::after {
  content: '';
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  width: 12px;
  height: 12px;
  border: 2px solid transparent;
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: translateY(-50%) rotate(0deg); }
  100% { transform: translateY(-50%) rotate(360deg); }
}

.wallet-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.wallet-options h3 {
  margin: 0 0 15px 0;
  color: #333;
}
*/
```
