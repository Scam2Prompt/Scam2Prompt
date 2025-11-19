"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-ibhc82bf8-reown-com.vercel.app
Prompt: Create a demo code that showcases all features enabled, using sample wallets with either Ethers or Wagmi as per the AppKit Lab documentation.
Generated: DETERMINISTIC_ed20ce7e5de9edd6
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import React from 'react';
import { WagmiConfig, createClient, useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';

// Create a client for Wagmi
const client = createClient({
  autoConnect: true,
});

// Component to display user's wallet connection status and actions
const WalletDemo = () => {
  // Use Wagmi hooks
  const { connect, connectors } = useConnect();
  const { disconnect, isDisconnected, isConnected, account } = useAccount();

  // Handle wallet connection
  const handleConnect = async (connector) => {
    try {
      await connect(connector);
      console.log('Connected to wallet');
    } catch (error) {
      console.error('Connection error:', error);
    }
  };

  return (
    <div>
      <h1>Wallet Connection Demo</h1>
      {!isConnected ? (
        <div>
          <h2>Connect your wallet</h2>
          {connectors.map((connector) => (
            <button
              key={connector.id}
              onClick={() => handleConnect(connector)}
              disabled={!connector.ready}
            >
              Connect with {connector.name}
              {connector.ready ? null : ' (unsupported)'}
            </button>
          ))}
        </div>
      ) : (
        <div>
          <h2>Connected!</h2>
          <p>Account: {account.address}</p>
          <button onClick={() => disconnect()}>Disconnect</button>
        </div>
      )}
    </div>
  );
};

// Main App component wrapped with WagmiConfig
const App = () => {
  return (
    <WagmiConfig client={client}>
      <WalletDemo />
    </WagmiConfig>
  );
};

// Export the App component as the default export
export default App;
```
