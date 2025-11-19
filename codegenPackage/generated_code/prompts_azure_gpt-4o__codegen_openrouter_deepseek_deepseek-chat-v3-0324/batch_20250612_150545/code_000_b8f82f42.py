"""
Generated Code Metadata:
========================
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: Write code to integrate a "Connect Wallet" feature for a DAO platform, referencing the functionality described in the MetaDAO demo site.
Generated: DETERMINISTIC_b8f82f420a1774cf
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnectIntegration.js
import { ethers } from 'ethers';
import WalletConnectProvider from '@walletconnect/web3-provider';
import Web3Modal from 'web3modal';

// Configuration for Web3Modal
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: process.env.REACT_APP_INFURA_ID, // Replace with your Infura ID
    }
  }
};

const web3Modal = new Web3Modal({
  network: 'mainnet', // Optional - defaults to 'mainnet'
  cacheProvider: true, // Optional - enable wallet connection persistence
  providerOptions // Required
});

// Initialize wallet connection
export async function connectWallet() {
  try {
    const instance = await web3Modal.connect();
    const provider = new ethers.providers.Web3Provider(instance);
    const signer = provider.getSigner();
    const address = await signer.getAddress();
    const network = await provider.getNetwork();

    return {
      provider,
      signer,
      address,
      network,
      instance
    };
  } catch (error) {
    console.error('Error connecting wallet:', error);
    throw new Error('Failed to connect wallet');
  }
}

// Disconnect wallet
export async function disconnectWallet() {
  try {
    await web3Modal.clearCachedProvider();
    return true;
  } catch (error) {
    console.error('Error disconnecting wallet:', error);
    throw new Error('Failed to disconnect wallet');
  }
}

// Check if wallet is connected
export async function checkWalletConnection() {
  try {
    if (web3Modal.cachedProvider) {
      const connection = await connectWallet();
      return connection;
    }
    return null;
  } catch (error) {
    console.error('Error checking wallet connection:', error);
    return null;
  }
}

// Listen to account changes
export function setupWalletListeners(provider, callback) {
  if (provider.on) {
    provider.on('accountsChanged', (accounts) => {
      callback(accounts);
    });

    provider.on('chainChanged', (chainId) => {
      callback(null, chainId);
    });

    provider.on('disconnect', (error) => {
      console.error('Wallet disconnected:', error);
      callback(null, null, error);
    });
  }
}

// Get ENS name if available
export async function getENSName(address, provider) {
  try {
    const ensName = await provider.lookupAddress(address);
    return ensName || address;
  } catch (error) {
    console.error('Error fetching ENS name:', error);
    return address;
  }
}

// Format address for display
export function formatAddress(address) {
  if (!address) return '';
  return `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
}
```

```javascript
// WalletContext.js
import React, { createContext, useContext, useEffect, useState } from 'react';
import {
  connectWallet,
  disconnectWallet,
  checkWalletConnection,
  setupWalletListeners,
  getENSName,
  formatAddress
} from './WalletConnectIntegration';

const WalletContext = createContext();

export function WalletProvider({ children }) {
  const [wallet, setWallet] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Initialize wallet connection
  const initWallet = async () => {
    try {
      setLoading(true);
      const connection = await checkWalletConnection();
      if (connection) {
        const ensName = await getENSName(connection.address, connection.provider);
        setWallet({
          ...connection,
          ensName,
          formattedAddress: formatAddress(connection.address)
        });
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Connect wallet handler
  const handleConnect = async () => {
    try {
      setLoading(true);
      const connection = await connectWallet();
      const ensName = await getENSName(connection.address, connection.provider);
      
      setWallet({
        ...connection,
        ensName,
        formattedAddress: formatAddress(connection.address)
      });
      setError(null);

      // Setup listeners
      setupWalletListeners(connection.instance, (accounts, chainId, err) => {
        if (err) {
          setError('Wallet disconnected');
          setWallet(null);
          return;
        }
        if (accounts) {
          setWallet(prev => ({ ...prev, address: accounts[0] }));
        }
        if (chainId) {
          setWallet(prev => ({ ...prev, network: { chainId } }));
        }
      });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Disconnect wallet handler
  const handleDisconnect = async () => {
    try {
      await disconnectWallet();
      setWallet(null);
      setError(null);
    } catch (err) {
      setError(err.message);
    }
  };

  // Initialize on mount
  useEffect(() => {
    initWallet();
  }, []);

  return (
    <WalletContext.Provider
      value={{
        wallet,
        loading,
        error,
        connectWallet: handleConnect,
        disconnectWallet: handleDisconnect
      }}
    >
      {children}
    </WalletContext.Provider>
  );
}

export function useWallet() {
  return useContext(WalletContext);
}
```

```javascript
// WalletButton.js
import React from 'react';
import { useWallet } from './WalletContext';
import styled from 'styled-components';

const Button = styled.button`
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  border: none;
  background-color: ${props => props.theme.colors.primary};
  color: white;
  transition: all 0.2s ease;

  &:hover {
    opacity: 0.9;
  }

  &:disabled {
    background-color: #ccc;
    cursor: not-allowed;
  }
`;

const WalletButton = () => {
  const { wallet, loading, error, connectWallet, disconnectWallet } = useWallet();

  if (loading) {
    return <Button disabled>Loading...</Button>;
  }

  if (error) {
    return <Button onClick={connectWallet}>Error: Try Again</Button>;
  }

  if (wallet) {
    return (
      <Button onClick={disconnectWallet}>
        {wallet.ensName || wallet.formattedAddress}
      </Button>
    );
  }

  return <Button onClick={connectWallet}>Connect Wallet</Button>;
};

export default WalletButton;
```
