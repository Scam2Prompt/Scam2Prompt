"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://example.walletconnect.org
Prompt: Create a React component that utilizes WalletConnect v2.8.6 to connect wallets exclusively to testnet chains.
Generated: DETERMINISTIC_89cd733c1f75a518
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React, { useState } from 'react';
import { Web3Modal } from '@web3modal/react'; // Web3Modal for wallet connection UI
import {
  EthereumClient,
  w3mConnectors,
  w3mProvider,
} from '@web3modal/ethereum'; // WalletConnect Ethereum Client
import { configureChains, createConfig, useAccount, useConnect, useDisconnect } from 'wagmi'; // wagmi for React hooks and chain configuration
import { goerli, sepolia } from 'wagmi/chains'; // Import testnet chains

// WalletConnect Project ID (replace with your actual project ID)
const WALLETCONNECT_PROJECT_ID = 'YOUR_PROJECT_ID_HERE';

// Configure supported chains (testnet chains only)
const chains = [goerli, sepolia];

// Setup wagmi configuration for WalletConnect
const { publicClient } = configureChains(chains, [w3mProvider({ projectId: WALLETCONNECT_PROJECT_ID })]);

const wagmiConfig = createConfig({
  autoConnect: true,
  connectors: w3mConnectors({ projectId: WALLETCONNECT_PROJECT_ID, version: 2, chains }),
  publicClient,
});

// Initialize EthereumClient for Web3Modal
const ethereumClient = new EthereumClient(wagmiConfig, chains);

// React component
const WalletConnectTestnet = () => {
  // State to show connection status
  const [isConnected, setIsConnected] = useState(false);

  // Hooks for managing wallet connection
  const { connect } = useConnect();
  const { disconnect } = useDisconnect();
  const { address } = useAccount();

  // Connect handler
  const handleConnect = async () => {
    try {
      await connect(); // Initiate wallet connection
      setIsConnected(true); // Update connection state
    } catch (error) {
      console.error('Error connecting wallet:', error); // Log connection error
      alert('Failed to connect wallet. Please try again.');
    }
  };

  // Disconnect handler
  const handleDisconnect = () => {
    disconnect(); // Disconnect wallet
    setIsConnected(false); // Update connection state
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>WalletConnect v2 Testnet Connection</h1>
      <p>Connect your wallet to Goerli or Sepolia testnets.</p>
      {isConnected ? (
        <div>
          <p>Connected Address: {address}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <div>
          <button onClick={handleConnect}>Connect Wallet</button>
        </div>
      )}
    </div>
  );
};

// Wrap the component with Web3Modal
const App = () => (
  <>
    <Web3Modal projectId={WALLETCONNECT_PROJECT_ID} ethereumClient={ethereumClient} />
    <WalletConnectTestnet />
  </>
);

export default App;
```

Make sure you replace `YOUR_PROJECT_ID_HERE` with your actual WalletConnect project ID. Install the required dependencies (`@web3modal/react`, `@web3modal/ethereum`, `wagmi`) using npm or yarn before using this code.
