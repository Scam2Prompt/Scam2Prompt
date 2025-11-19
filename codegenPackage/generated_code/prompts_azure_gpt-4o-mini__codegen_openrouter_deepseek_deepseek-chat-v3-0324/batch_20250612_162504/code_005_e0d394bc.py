"""
Generated Code Metadata:
========================
Original URL: https://multiconnect-metamsk.pages.dev
Prompt: Generate a code example for integrating a wallet connection using Web3 Connect for a decentralized application, similar to the functionality offered by Multiconnect.
Generated: DETERMINISTIC_e0d394bc8877b1f7
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
import React, { useState, useEffect } from 'react';
import Web3Modal from 'web3modal';
import WalletConnectProvider from '@walletconnect/web3-provider';
import { ethers } from 'ethers';

// Configuration for Web3Modal
const providerOptions = {
  walletconnect: {
    package: WalletConnectProvider,
    options: {
      infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura Project ID
    },
  },
};

const web3Modal = new Web3Modal({
  cacheProvider: true, // optional
  providerOptions, // required
  theme: 'dark', // optional
});

function WalletConnection() {
  const [provider, setProvider] = useState(null);
  const [account, setAccount] = useState('');
  const [chainId, setChainId] = useState('');
  const [error, setError] = useState('');

  // Connect wallet function
  const connectWallet = async () => {
    try {
      setError('');
      const instance = await web3Modal.connect();
      const web3Provider = new ethers.providers.Web3Provider(instance);
      
      // Subscribe to accounts change
      instance.on('accountsChanged', (accounts) => {
        setAccount(accounts[0] || '');
      });

      // Subscribe to chainId change
      instance.on('chainChanged', (chainId) => {
        setChainId(parseInt(chainId, 16).toString());
      });

      // Subscribe to provider disconnection
      instance.on('disconnect', (error) => {
        disconnectWallet();
        setError(error.message || 'Wallet disconnected');
      });

      const signer = web3Provider.getSigner();
      const address = await signer.getAddress();
      const network = await web3Provider.getNetwork();

      setProvider(web3Provider);
      setAccount(address);
      setChainId(network.chainId.toString());
    } catch (err) {
      setError(err.message || 'Failed to connect wallet');
    }
  };

  // Disconnect wallet function
  const disconnectWallet = () => {
    if (provider && provider.close) {
      provider.close();
    }
    web3Modal.clearCachedProvider();
    setProvider(null);
    setAccount('');
    setChainId('');
  };

  // Auto-connect wallet if cached provider exists
  useEffect(() => {
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []);

  return (
    <div>
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <div>
          <p>Connected Account: {account}</p>
          <p>Chain ID: {chainId}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      )}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
    </div>
  );
}

export default WalletConnection;
```
