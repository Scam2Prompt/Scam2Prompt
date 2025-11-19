"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect-website.vercel.app
Prompt: How can I integrate WalletConnect into my Dapp using the Web3Modal library?
Generated: DETERMINISTIC_2c399c68aa655cfb
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { useState, useEffect } from 'react';
import Web3 from 'web3';
import Web3Modal from 'web3modal';
import WalletConnectProvider from '@walletconnect/web3-provider';

const App = () => {
  // State to manage Web3 instance and user account
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);

  // Initialize Web3Modal
  const web3Modal = new Web3Modal({
    cacheProvider: true, // Enable caching of the provider for quicker reconnects
    providerOptions: {
      /* WalletConnect provider configuration */
      walletconnect: {
        package: WalletConnectProvider, // Required
        options: {
          infuraId: 'YOUR_INFURA_PROJECT_ID', // Replace with your Infura project ID
        },
      },
    },
  });

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      // Open Web3Modal dialog to select provider
      const provider = await web3Modal.connect();

      // Create a Web3 instance with the selected provider
      const web3Instance = new Web3(provider);
      setWeb3(web3Instance);

      // Get the user's account(s)
      const accounts = await web3Instance.eth.getAccounts();
      setAccount(accounts[0]);

      // Subscribe to provider events (e.g., accounts changed)
      provider.on('accountsChanged', (accounts) => {
        setAccount(accounts[0]); // Update the account state
      });

      provider.on('disconnect', () => {
        // Clear state on disconnect
        setAccount(null);
        setWeb3(null);
      });
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Disconnect wallet and clear state
  const disconnectWallet = async () => {
    try {
      // Clear cache from Web3Modal
      web3Modal.clearCachedProvider();

      // Reset state
      setAccount(null);
      setWeb3(null);
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
      alert('Failed to disconnect wallet.');
    }
  };

  useEffect(() => {
    // Automatically reconnect if the provider was cached
    if (web3Modal.cachedProvider) {
      connectWallet();
    }
  }, []); // Run only once after initial render

  return (
    <div>
      <h1>WalletConnect Integration</h1>
      {account ? (
        <div>
          <p>Connected account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default App;
```

This code demonstrates how to integrate WalletConnect into a DApp using the Web3Modal library, along with handling wallet connection and disconnection logic.
