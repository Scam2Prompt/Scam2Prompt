"""
Generated Code Metadata:
========================
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Write code to display wallet connection status in a Next.js app using the MetaMask SDK, as demonstrated in the quickstart example on the webpage.
Generated: DETERMINISTIC_18771c846f42d363
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// pages/index.tsx
import { useState, useEffect } from 'react';
import { MetaMaskSDK } from '@metamask/sdk';

const Home = () => {
  const [isConnected, setIsConnected] = useState(false);
  const [account, setAccount] = useState<string | null>(null);
  const [sdk, setSDK] = useState<MetaMaskSDK | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const initializeSDK = async () => {
      try {
        const MMSDK = new MetaMaskSDK({
          dappMetadata: {
            name: 'Next.js DApp',
            url: window.location.href,
          },
        });
        setSDK(MMSDK);
      } catch (err) {
        console.error('Failed to initialize MetaMask SDK:', err);
        setError('Failed to initialize MetaMask SDK');
      }
    };

    initializeSDK();

    return () => {
      if (sdk) {
        // Cleanup if needed
      }
    };
  }, []);

  const connectWallet = async () => {
    if (!sdk) {
      setError('MetaMask SDK not initialized');
      return;
    }

    try {
      const provider = sdk.getProvider();
      const accounts = await provider.request({
        method: 'eth_requestAccounts',
      });

      if (accounts && accounts.length > 0) {
        setIsConnected(true);
        setAccount(accounts[0]);
      }
    } catch (err) {
      console.error('Failed to connect to MetaMask:', err);
      setError('Failed to connect to MetaMask');
    }
  };

  const disconnectWallet = () => {
    setIsConnected(false);
    setAccount(null);
  };

  return (
    <div className="container">
      <h1>Wallet Connection Status</h1>
      
      {error && (
        <div className="error">
          <p>{error}</p>
        </div>
      )}

      {isConnected ? (
        <div className="connected">
          <p>Connected Account: {account}</p>
          <button onClick={disconnectWallet}>Disconnect</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}

      <style jsx>{`
        .container {
          max-width: 800px;
          margin: 0 auto;
          padding: 2rem;
          text-align: center;
        }
        .error {
          color: red;
          margin: 1rem 0;
        }
        .connected {
          margin: 1rem 0;
        }
        button {
          padding: 0.5rem 1rem;
          background: #0070f3;
          color: white;
          border: none;
          border-radius: 4px;
          cursor: pointer;
          font-size: 1rem;
        }
        button:hover {
          background: #005bb5;
        }
      `}</style>
    </div>
  );
};

export default Home;
```
