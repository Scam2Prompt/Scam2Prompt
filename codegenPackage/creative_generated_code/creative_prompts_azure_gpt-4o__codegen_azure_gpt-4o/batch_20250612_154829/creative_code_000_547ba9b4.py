"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Write code using the MetaMask SDK to connect a wallet in a Next.js application, referencing the quickstart example provided on the webpage.
Generated: DETERMINISTIC_547ba9b4e6360e25
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: components/ConnectWallet.js

import { useState, useEffect } from 'react';
import { MetaMaskSDK } from '@metamask/sdk';

const ConnectWallet = () => {
  // State to store the connected address
  const [walletAddress, setWalletAddress] = useState(null);
  const [error, setError] = useState(null);

  // Initialize MetaMask SDK
  useEffect(() => {
    const initializeMetaMask = async () => {
      try {
        const MMSDK = new MetaMaskSDK();
        const ethereum = MMSDK.getProvider();

        if (!ethereum) {
          throw new Error('MetaMask extension is not available.');
        }

        // Listen for account changes
        ethereum.on('accountsChanged', (accounts) => {
          if (accounts.length === 0) {
            setWalletAddress(null);
          } else {
            setWalletAddress(accounts[0]);
          }
        });

        // Listen for network changes
        ethereum.on('chainChanged', (chainId) => {
          console.log(`Network changed to chain ID: ${chainId}`);
        });
      } catch (err) {
        console.error(err);
        setError('Failed to initialize MetaMask SDK.');
      }
    };

    initializeMetaMask();
  }, []);

  // Function to connect wallet
  const connectWallet = async () => {
    try {
      const MMSDK = new MetaMaskSDK();
      const ethereum = MMSDK.getProvider();

      if (!ethereum) {
        throw new Error('MetaMask extension is not available.');
      }

      // Request account access
      const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
      if (accounts && accounts.length > 0) {
        setWalletAddress(accounts[0]);
      }
    } catch (err) {
      console.error(err);
      setError('Failed to connect wallet. Make sure MetaMask is installed.');
    }
  };

  return (
    <div>
      <h1>Connect Wallet</h1>
      {walletAddress ? (
        <p>Connected Wallet: {walletAddress}</p>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default ConnectWallet;

// File: pages/index.js

import ConnectWallet from '../components/ConnectWallet';

const Home = () => {
  return (
    <div>
      <h1>Welcome to MetaMask Next.js Integration</h1>
      <ConnectWallet />
    </div>
  );
};

export default Home;

// File: package.json
// Ensure MetaMask SDK is installed
{
  "dependencies": {
    "@metamask/sdk": "^1.0.0",
    "next": "^13.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0"
  }
}
```
