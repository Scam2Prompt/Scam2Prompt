"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-mu63br02c-reown-com.vercel.app
Prompt: How do I implement a demo with sample wallets using wagmi and ethers in AppKit?
Generated: DETERMINISTIC_a7728255c5a3e22f
Batch ID: 20250612_155422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from wagmi and ethers
import React, { useEffect } from 'react';
import { WagmiConfig, createClient, useAccount, useConnect, useDisconnect, useProvider } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { ethers } from 'ethers';

// Initialize Wagmi client
const client = createClient({
  autoConnect: true,
});

// Sample wallets for demo
const sampleWallets = [
  { name: 'MetaMask', connector: new InjectedConnector() },
  // Add more connectors as needed
];

// Main App component
const App = () => {
  return (
    <WagmiConfig client={client}>
      <WalletDemo />
    </WagmiConfig>
  );
};

// WalletDemo component for wallet connection and display
const WalletDemo = () => {
  const { isConnected, address } = useAccount();
  const { connect, disconnect } = useConnect();
  const { disconnect: disconnectWallet } = useDisconnect();
  const provider = useProvider();

  // Effect to ensure provider is set up correctly
  useEffect(() => {
    if (isConnected) {
      console.log(`Connected to wallet: ${address}`);
    }
  }, [isConnected, address]);

  // Function to connect to selected wallet
  const handleConnect = async (connector) => {
    try {
      await connect(connector);
    } catch (error) {
      console.error('Failed to connect wallet:', error);
    }
  };

  // Function to disconnect from the wallet
  const handleDisconnect = async () => {
    try {
      await disconnectWallet();
    } catch (error) {
      console.error('Failed to disconnect wallet:', error);
    }
  };

  return (
    <div>
      <h1>Wallet Demo</h1>
      {!isConnected ? (
        <div>
          <h2>Select a Wallet</h2>
          {sampleWallets.map((wallet, index) => (
            <button key={index} onClick={() => handleConnect(wallet.connector)}>
              Connect with {wallet.name}
            </button>
          ))}
        </div>
      ) : (
        <div>
          <h2>Connected Wallet</h2>
          <p>Address: {address}</p>
          <button onClick={handleDisconnect}>Disconnect</button>
        </div>
      )}
    </div>
  );
};

// Export the App component
export default App;
```
