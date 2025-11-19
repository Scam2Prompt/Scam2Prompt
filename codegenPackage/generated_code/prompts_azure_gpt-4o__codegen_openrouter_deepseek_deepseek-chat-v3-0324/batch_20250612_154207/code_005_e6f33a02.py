"""
Generated Code Metadata:
========================
Original URL: https://jupnft.com
Prompt: Provide code examples for integrating wallet connection functionality into a decentralized application (dApp) that interacts with the Jupiverse platform.
Generated: DETERMINISTIC_e6f33a028d67a14f
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// WalletConnection.js - Handles wallet connection for dApp interacting with Jupiverse

import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
  TorusWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';
import { WalletModalProvider, WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { useMemo } from 'react';
import '@solana/wallet-adapter-react-ui/styles.css';

// Main wallet connection component
export const WalletConnection = ({ children }) => {
  // The network can be set to 'devnet', 'testnet', or 'mainnet-beta'
  const network = WalletAdapterNetwork.Devnet;
  const endpoint = useMemo(() => clusterApiUrl(network), [network]);

  const wallets = useMemo(
    () => [
      new PhantomWalletAdapter(),
      new SolflareWalletAdapter({ network }),
      new TorusWalletAdapter(),
    ],
    [network]
  );

  return (
    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={wallets} autoConnect>
        <WalletModalProvider>
          {children}
          <WalletMultiButton />
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
};

// Hook to check wallet connection status
export const useWalletConnection = () => {
  const { connected, publicKey, wallet, connect, disconnect } = useWallet();

  const connectWallet = async () => {
    try {
      await connect();
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  const disconnectWallet = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  return {
    isConnected: connected,
    walletAddress: publicKey?.toBase58(),
    wallet,
    connectWallet,
    disconnectWallet,
  };
};

// Example component using wallet connection
export const JupiverseIntegration = () => {
  const { isConnected, walletAddress, connectWallet, disconnectWallet } = useWalletConnection();

  const handleJupiverseAction = async () => {
    if (!isConnected) {
      alert('Please connect your wallet first');
      return;
    }

    try {
      // Perform Jupiverse platform interaction here
      console.log(`Performing action with wallet: ${walletAddress}`);
    } catch (error) {
      console.error('Jupiverse action failed:', error);
    }
  };

  return (
    <div>
      {isConnected ? (
        <div>
          <p>Connected: {walletAddress}</p>
          <button onClick={disconnectWallet}>Disconnect Wallet</button>
          <button onClick={handleJupiverseAction}>Perform Jupiverse Action</button>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};
```
