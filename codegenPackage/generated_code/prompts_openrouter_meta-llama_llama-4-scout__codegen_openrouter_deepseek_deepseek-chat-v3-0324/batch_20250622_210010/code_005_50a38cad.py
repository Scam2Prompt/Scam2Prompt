"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-6h5i4lwdb-reown-com.vercel.app
Prompt: "Create a demo with sample wallets, enabling all features and randomly using Ethers or Wagmi with AppKit."
Generated: DETERMINISTIC_50a38cadea85d13a
Batch ID: 20250622_210010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import { ethers } from 'ethers';
import { WagmiConfig, createClient, configureChains, mainnet } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { WalletConnectConnector } from 'wagmi/connectors/walletConnect';
import { CoinbaseWalletConnector } from 'wagmi/connectors/coinbaseWallet';
import { AppKitProvider, useAppKit } from '@aragon/appkit-react';
import { useState, useEffect } from 'react';

// Configure chains for Wagmi
const { chains, provider, webSocketProvider } = configureChains(
  [mainnet],
  [publicProvider()]
);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors: [
    new InjectedConnector({ chains }),
    new WalletConnectConnector({
      chains,
      options: {
        qrcode: true,
      },
    }),
    new CoinbaseWalletConnector({
      chains,
      options: {
        appName: 'AppKit Demo',
      },
    }),
  ],
  provider,
  webSocketProvider,
});

// Sample wallets for Ethers.js
const sampleWallets = [
  {
    name: 'Wallet 1',
    privateKey: '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80',
  },
  {
    name: 'Wallet 2',
    privateKey: '0x59c6995e998f97a5a0044966f0945389dc9e86dae88c7a8412f4603b6b78690d',
  },
];

// Demo component
const Demo = () => {
  const [selectedWallet, setSelectedWallet] = useState<null | ethers.Wallet>(null);
  const [useWagmi, setUseWagmi] = useState(false);
  const { connection, connect, disconnect } = useAppKit();

  // Randomly select between Ethers and Wagmi
  useEffect(() => {
    setUseWagmi(Math.random() > 0.5);
  }, []);

  // Connect with Ethers.js
  const connectWithEthers = (walletIndex: number) => {
    const wallet = new ethers.Wallet(sampleWallets[walletIndex].privateKey);
    setSelectedWallet(wallet);
  };

  // Connect with AppKit
  const connectWithAppKit = async () => {
    try {
      await connect();
    } catch (error) {
      console.error('Failed to connect with AppKit:', error);
    }
  };

  // Disconnect all
  const handleDisconnect = () => {
    if (useWagmi) {
      disconnect();
    }
    setSelectedWallet(null);
  };

  return (
    <div>
      <h1>Wallet Demo</h1>
      <p>Using: {useWagmi ? 'Wagmi + AppKit' : 'Ethers.js'}</p>

      {useWagmi ? (
        <div>
          <button onClick={connectWithAppKit}>Connect with AppKit</button>
          <p>Status: {connection.status}</p>
          <p>Account: {connection.account}</p>
        </div>
      ) : (
        <div>
          <h2>Select Ethers Wallet</h2>
          {sampleWallets.map((wallet, index) => (
            <button key={index} onClick={() => connectWithEthers(index)}>
              {wallet.name}
            </button>
          ))}
          <p>Selected Wallet: {selectedWallet?.address}</p>
        </div>
      )}

      <button onClick={handleDisconnect}>Disconnect</button>
    </div>
  );
};

// Main App component
const App = () => {
  return (
    <WagmiConfig client={wagmiClient}>
      <AppKitProvider>
        <Demo />
      </AppKitProvider>
    </WagmiConfig>
  );
};

export default App;
```
