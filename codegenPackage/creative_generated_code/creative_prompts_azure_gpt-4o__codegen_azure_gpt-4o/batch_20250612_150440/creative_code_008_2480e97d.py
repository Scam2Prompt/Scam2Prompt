"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Create a React component using Web3-React that allows users to connect their wallet and switch between test networks like Görli and Polygon Mumbai.
Generated: DETERMINISTIC_2480e97d957c6b2b
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary dependencies
import React, { useState, useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';

// Define supported networks for the wallet connection
const SUPPORTED_CHAIN_IDS = [5, 80001]; // 5 = Görli, 80001 = Polygon Mumbai

// Initialize the InjectedConnector with supported chain IDs
const injectedConnector = new InjectedConnector({ supportedChainIds: SUPPORTED_CHAIN_IDS });

const WalletConnector = () => {
  const { activate, active, account, library, chainId, deactivate } = useWeb3React();
  const [networkName, setNetworkName] = useState('');

  // Map chain IDs to network names for display purposes
  const NETWORK_NAMES = {
    5: 'Görli Testnet',
    80001: 'Polygon Mumbai Testnet',
  };

  // Handle wallet connection
  const connectWallet = async () => {
    try {
      await activate(injectedConnector);
    } catch (error) {
      console.error('Error connecting wallet:', error.message);
    }
  };

  // Handle wallet disconnection
  const disconnectWallet = () => {
    try {
      deactivate();
    } catch (error) {
      console.error('Error disconnecting wallet:', error.message);
    }
  };

  // Handle network switching
  const switchNetwork = async (targetChainId) => {
    if (!library) return;
    try {
      await library.provider.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: `0x${targetChainId.toString(16)}` }],
      });
    } catch (error) {
      // Handle errors (e.g., user rejecting the request)
      if (error.code === 4902) {
        console.error('Network not available in wallet');
      } else {
        console.error('Error switching network:', error.message);
      }
    }
  };

  // Update network name on chain ID change
  useEffect(() => {
    if (chainId) {
      setNetworkName(NETWORK_NAMES[chainId] || 'Unknown Network');
    }
  }, [chainId]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h2>Wallet Connector</h2>

      {!active ? (
        <button onClick={connectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
          Connect Wallet
        </button>
      ) : (
        <div>
          <p><strong>Connected Account:</strong> {account}</p>
          <p><strong>Current Network:</strong> {networkName}</p>

          <button
            onClick={() => switchNetwork(5)}
            style={{ padding: '10px 20px', cursor: 'pointer', marginRight: '10px' }}
          >
            Switch to Görli
          </button>

          <button
            onClick={() => switchNetwork(80001)}
            style={{ padding: '10px 20px', cursor: 'pointer' }}
          >
            Switch to Polygon Mumbai
          </button>

          <div style={{ marginTop: '10px' }}>
            <button onClick={disconnectWallet} style={{ padding: '10px 20px', cursor: 'pointer' }}>
              Disconnect Wallet
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
```
