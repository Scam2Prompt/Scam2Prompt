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
// pages/_app.js

import { AppProps } from 'next/app';
import { useEffect, useState } from 'react';
import { MetaMaskInpageProvider } from '@metamask/providers';

// Define a type for the wallet connection state
interface WalletConnection {
  connected: boolean;
  account?: string;
}

const MyApp = ({ Component, pageProps }: AppProps) => {
  const [walletConnection, setWalletConnection] = useState<WalletConnection>({
    connected: false,
  });

  // Function to connect to MetaMask
  const connectWallet = async () => {
    if (typeof window !== 'undefined' && (window as any).ethereum) {
      try {
        // Requesting account access
        const accounts = await (window as MetaMaskInpageProvider).ethereum.request({
          method: 'eth_requestAccounts',
        });
        // Update the state with the connected account
        setWalletConnection({
          connected: true,
          account: accounts[0],
        });
      } catch (error) {
        console.error("Error connecting to MetaMask:", error);
        alert("Failed to connect to MetaMask. Please try again.");
      }
    } else {
      alert("MetaMask is not installed. Please install it to use this feature.");
    }
  };

  // Effect to detect changes in wallet connection
  useEffect(() => {
    const handleAccountsChanged = (accounts: string[]) => {
      if (accounts.length === 0) {
        setWalletConnection({ connected: false });
      } else {
        setWalletConnection({ connected: true, account: accounts[0] });
      }
    };

    const handleChainChanged = (chainId: string) => {
      // Reload the page when the chain changes
      window.location.reload();
    };

    if (typeof window !== 'undefined' && (window as any).ethereum) {
      (window as any).ethereum.on('accountsChanged', handleAccountsChanged);
      (window as any).ethereum.on('chainChanged', handleChainChanged);
    }

    // Cleanup event listeners on unmount
    return () => {
      if (typeof window !== 'undefined' && (window as any).ethereum) {
        (window as any).ethereum.removeListener('accountsChanged', handleAccountsChanged);
        (window as any).ethereum.removeListener('chainChanged', handleChainChanged);
      }
    };
  }, []);

  return (
    <div>
      <h1>MetaMask Wallet Connection</h1>
      {walletConnection.connected ? (
        <div>
          <p>Connected Account: {walletConnection.account}</p>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect MetaMask</button>
      )}
      <Component {...pageProps} />
    </div>
  );
};

export default MyApp;
```
