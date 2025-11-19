"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-n76z148gg-reown-com.vercel.app
Prompt: Create a demo using sample wallets with all features enabled in AppKit, utilizing ethers or wagmi.
Generated: DETERMINISTIC_beac035fc4f3606a
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from Ethers.js and Wagmi
import { useAccount, useConnect, useDisconnect, useEnsName } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { ethers } from 'ethers';

// Main application component
function App() {
  // Hooks for account management and connection
  const { isConnected, address } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();
  const { data: ensName } = useEnsName(address);

  // Function to handle connecting to a wallet
  const handleConnect = async (connector) => {
    try {
      await connect(connector);
    } catch (error) {
      console.error('Error connecting to wallet:', error);
    }
  };

  // Function to handle disconnection from wallet
  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  // Function to display wallet information
  const displayWalletInfo = () => {
    if (isConnected) {
      return (
        <div>
          <h2>Connected Wallet</h2>
          <p>Address: {address}</p>
          <p>ENS Name: {ensName || 'Not set'}</p>
          <button onClick={handleDisconnect}>Disconnect</button>
        </div>
      );
    } else {
      return (
        <div>
          <h2>Connect Your Wallet</h2>
          {connectors.map((connector) => (
            <button key={connector.id} onClick={() => handleConnect(connector)}>
              Connect with {connector.name}
            </button>
          ))}
        </div>
      );
    }
  };

  return (
    <div>
      <h1>Wallet Demo with Ethers and Wagmi</h1>
      {displayWalletInfo()}
    </div>
  );
}

// Main rendering function
const rootElement = document.getElementById('root');
if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <WagmiConfig>
      <App />
    </WagmiConfig>
  );
} else {
  console.error('Failed to find the root element to mount the app.');
}
```

### Note
Make sure to include the necessary imports and setup for React, ReactDOM, and WagmiConfig from the appropriate libraries to make this code runnable in a complete React application. Also, ensure you have a proper HTML structure with a root element in your index.html file.
