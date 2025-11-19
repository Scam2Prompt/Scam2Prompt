"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-react-meutas5kc-uniswap.vercel.app
Prompt: Write a React component that integrates with MetaMask to allow users to connect their wallet and select a blockchain network like Mainnet or Optimism.
Generated: DETERMINISTIC_4c106c45ccac487e
Batch ID: 20250612_135409
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary React and MetaMask dependencies
import React, { useState, useEffect } from 'react';

// Define supported networks
const supportedNetworks = {
  1: { name: 'Ethereum Mainnet', chainId: '0x1' },
  10: { name: 'Optimism', chainId: '0xa' },
};

// Create a functional React component for MetaMask integration
const MetaMaskWalletConnector = () => {
  const [isConnected, setIsConnected] = useState(false); // Track wallet connection status
  const [currentAccount, setCurrentAccount] = useState(null); // Track user's wallet address
  const [currentNetwork, setCurrentNetwork] = useState(null); // Track selected network

  // Function to check if MetaMask is installed
  const isMetaMaskInstalled = () => {
    return typeof window.ethereum !== 'undefined';
  };

  // Function to connect user's MetaMask wallet
  const connectWallet = async () => {
    if (!isMetaMaskInstalled()) {
      alert('MetaMask is not installed. Please install it to use this feature.');
      return;
    }

    try {
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setCurrentAccount(accounts[0]); // Set the first account as the connected account
      setIsConnected(true); // Update connection status
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Function to switch blockchain network
  const switchNetwork = async (chainId) => {
    if (!isMetaMaskInstalled()) {
      alert('MetaMask is not installed. Please install it to use this feature.');
      return;
    }

    try {
      await window.ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId }],
      });
      setCurrentNetwork(chainId); // Update the currently selected network
    } catch (error) {
      console.error('Error switching network:', error);
      if (error.code === 4902) {
        alert('Selected network is not supported by MetaMask.');
      } else {
        alert('Failed to switch network. Please try again.');
      }
    }
  };

  // Automatically update account and network info on wallet change
  useEffect(() => {
    if (isMetaMaskInstalled()) {
      const handleAccountsChanged = (accounts) => {
        if (accounts.length > 0) {
          setCurrentAccount(accounts[0]);
          setIsConnected(true);
        } else {
          setCurrentAccount(null);
          setIsConnected(false);
        }
      };

      const handleChainChanged = (chainId) => {
        setCurrentNetwork(chainId);
      };

      window.ethereum.on('accountsChanged', handleAccountsChanged);
      window.ethereum.on('chainChanged', handleChainChanged);

      // Cleanup event listeners on component unmount
      return () => {
        window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        window.ethereum.removeListener('chainChanged', handleChainChanged);
      };
    }
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h2>MetaMask Wallet Connector</h2>

      {/* Display connection status */}
      {isConnected ? (
        <>
          <p>
            Wallet connected: <strong>{currentAccount}</strong>
          </p>
          <p>
            Current network: <strong>{supportedNetworks[parseInt(currentNetwork, 16)]?.name || 'Unknown'}</strong>
          </p>
          <div>
            <h3>Select a Network</h3>
            {Object.entries(supportedNetworks).map(([id, { name, chainId }]) => (
              <button
                key={id}
                onClick={() => switchNetwork(chainId)}
                style={{
                  margin: '5px',
                  padding: '10px',
                  backgroundColor: '#007bff',
                  color: '#fff',
                  border: 'none',
                  borderRadius: '5px',
                  cursor: 'pointer',
                }}
              >
                {name}
              </button>
            ))}
          </div>
        </>
      ) : (
        <>
          <p>Wallet not connected.</p>
          <button
            onClick={connectWallet}
            style={{
              padding: '10px',
              backgroundColor: '#007bff',
              color: '#fff',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
            }}
          >
            Connect Wallet
          </button>
        </>
      )}
    </div>
  );
};

export default MetaMaskWalletConnector;
```
