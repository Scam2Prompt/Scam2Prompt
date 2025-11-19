"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-n76z148gg-reown-com.vercel.app
Prompt: Create a demo using sample wallets with all features enabled in AppKit, utilizing ethers or wagmi.
Generated: DETERMINISTIC_beac035fc4f3606a
Batch ID: 20250612_155457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries from ethers and wagmi
import { useEffect } from 'react';
import { useAccount, useConnect, useDisconnect, useProvider, useSigner } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { ethers } from 'ethers';

// Main App component
const App = () => {
  // Hooks to manage wallet connection and account state
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();
  const { isConnected, address } = useAccount();
  const provider = useProvider();
  const { data: signer } = useSigner();

  // Effect to log account changes
  useEffect(() => {
    if (isConnected) {
      console.log(`Connected to wallet: ${address}`);
    }
  }, [isConnected, address]);

  // Function to handle wallet connection
  const handleConnect = async (connector) => {
    try {
      await connect(connector);
      console.log('Wallet connected successfully');
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  // Function to handle wallet disconnection
  const handleDisconnect = async () => {
    try {
      await disconnect();
      console.log('Wallet disconnected successfully');
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  // Function to fetch the balance of the connected wallet
  const fetchBalance = async () => {
    if (!signer) return;

    try {
      const balance = await signer.getBalance();
      console.log(`Wallet balance: ${ethers.utils.formatEther(balance)} ETH`);
    } catch (error) {
      console.error('Error fetching balance:', error);
    }
  };

  // Effect to fetch balance when connected
  useEffect(() => {
    if (isConnected) {
      fetchBalance();
    }
  }, [isConnected, signer]);

  return (
    <div>
      <h1>Wallet Demo with Wagmi and Ethers</h1>
      {isConnected ? (
        <div>
          <p>Connected as: {address}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
          <button onClick={fetchBalance}>Fetch Balance</button>
        </div>
      ) : (
        <div>
          <p>No wallet connected</p>
          {connectors.map((connector) => (
            <button key={connector.id} onClick={() => handleConnect(connector)}>
              Connect with {connector.name}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default App;
```

Make sure to install the required dependencies before running the code:

```bash
npm install ethers wagmi
```

This code provides a simple wallet connection demo using the `wagmi` library for React, allowing users to connect and disconnect their wallets, as well as fetch their ETH balance.
