"""
Generated Code Metadata:
========================
Original URL: https://react-phantom-wallet.vercel.app
Prompt: Generate a React hook for managing Phantom Wallet connection status, using the approach outlined on the React Phantom Wallet webpage.
Generated: DETERMINISTIC_e852a615adf302ab
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```jsx
import { useState, useEffect } from 'react';
import { PhantomWallet } from '@solana/phantom-wallet-adapter';

/**
 * Hook for managing Phantom Wallet connection status.
 *
 * @returns {object} - Connection status and functions to connect and disconnect.
 */
export const usePhantomWallet = () => {
  // State to store connection status
  const [isConnected, setIsConnected] = useState(false);
  const [publicKey, setPublicKey] = useState(null);
  const [phantomWallet, setPhantomWallet] = useState(null);

  // Initialize Phantom Wallet
  useEffect(() => {
    const initializePhantomWallet = async () => {
      try {
        const { default: { PhantomWallet } } = await import('@solana/phantom-wallet-adapter');
        const wallet = new PhantomWallet();
        setPhantomWallet(wallet);
      } catch (error) {
        console.error('Error initializing Phantom Wallet:', error);
      }
    };
    initializePhantomWallet();
  }, []);

  // Connect to Phantom Wallet
  const connect = async () => {
    try {
      if (phantomWallet) {
        await phantomWallet.connect();
        setIsConnected(phantomWallet.connected);
        setPublicKey(phantomWallet.publicKey);
      } else {
        console.error('Phantom Wallet not initialized');
      }
    } catch (error) {
      console.error('Error connecting to Phantom Wallet:', error);
    }
  };

  // Disconnect from Phantom Wallet
  const disconnect = async () => {
    try {
      if (phantomWallet) {
        await phantomWallet.disconnect();
        setIsConnected(false);
        setPublicKey(null);
      } else {
        console.error('Phantom Wallet not initialized');
      }
    } catch (error) {
      console.error('Error disconnecting from Phantom Wallet:', error);
    }
  };

  // Update connection status on Phantom Wallet change
  useEffect(() => {
    const handleConnect = () => {
      setIsConnected(true);
      setPublicKey(phantomWallet.publicKey);
    };

    const handleDisconnect = () => {
      setIsConnected(false);
      setPublicKey(null);
    };

    if (phantomWallet) {
      phantomWallet.on('connect', handleConnect);
      phantomWallet.on('disconnect', handleDisconnect);

      return () => {
        phantomWallet.off('connect', handleConnect);
        phantomWallet.off('disconnect', handleDisconnect);
      };
    }
  }, [phantomWallet]);

  return { isConnected, publicKey, connect, disconnect };
};
```
