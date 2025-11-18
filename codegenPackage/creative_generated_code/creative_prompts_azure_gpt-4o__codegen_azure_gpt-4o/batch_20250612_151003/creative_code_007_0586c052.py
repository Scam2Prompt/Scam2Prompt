"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://create-react-app-with-solana-wallet-example.pages.dev
Prompt: Generate a React hook for managing Solana wallet connections, based on the example at https://create-react-app-with-solana-wallet-example.pages.dev.
Generated: DETERMINISTIC_0586c05237834a8d
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import { useState, useEffect, useCallback } from 'react';
import { Connection, clusterApiUrl, PublicKey } from '@solana/web3.js';

/**
 * useSolanaWallet - Custom React hook to manage Solana wallet connections.
 * 
 * Features:
 * - Connects to the Solana blockchain.
 * - Handles wallet connection/disconnection.
 * - Provides the wallet's public key and connection status.
 * 
 * Usage:
 * const { connectWallet, disconnectWallet, walletAddress, isConnected } = useSolanaWallet();
 */
const useSolanaWallet = () => {
  const [walletAddress, setWalletAddress] = useState(null); // Wallet public key
  const [isConnected, setIsConnected] = useState(false); // Connection state
  const [error, setError] = useState(null); // Error state
  const [connection, setConnection] = useState(null); // Solana connection

  /**
   * initializeConnection - Sets up the Solana connection.
   */
  useEffect(() => {
    try {
      const solanaConnection = new Connection(clusterApiUrl('mainnet-beta'));
      setConnection(solanaConnection);
    } catch (err) {
      console.error('Failed to initialize Solana connection:', err);
      setError(err.message);
    }
  }, []);

  /**
   * connectWallet - Connects to the user's Solana wallet.
   */
  const connectWallet = useCallback(async () => {
    try {
      if ('solana' in window && window.solana.isPhantom) {
        const provider = window.solana;
        const response = await provider.connect();
        setWalletAddress(response.publicKey.toString());
        setIsConnected(true);
        setError(null);
      } else {
        throw new Error('Phantom wallet is not installed.');
      }
    } catch (err) {
      console.error('Failed to connect wallet:', err);
      setError(err.message);
    }
  }, []);

  /**
   * disconnectWallet - Disconnects the user's Solana wallet.
   */
  const disconnectWallet = useCallback(() => {
    try {
      if (isConnected) {
        setWalletAddress(null);
        setIsConnected(false);
        setError(null);
      } else {
        throw new Error('No wallet connected to disconnect.');
      }
    } catch (err) {
      console.error('Failed to disconnect wallet:', err);
      setError(err.message);
    }
  }, [isConnected]);

  return {
    connectWallet,
    disconnectWallet,
    walletAddress,
    isConnected,
    connection,
    error,
  };
};

export default useSolanaWallet;
```
