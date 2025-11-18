"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: How can I integrate MetaMask SDK with Wagmi in a Next.js project to manage networks and handle transactions? Provide code examples.
Generated: DETERMINISTIC_17f72f0ac4ffc521
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Install necessary dependencies before proceeding:
// npm install @wagmi/core @wagmi/connectors ethers metamask-sdk

// pages/_app.js
import { WagmiConfig, createClient, configureChains, chain } from '@wagmi/core';
import { MetaMaskConnector } from '@wagmi/connectors/metamask';
import { publicProvider } from '@wagmi/core/providers/public';

// Configure chains and providers
const { chains, provider } = configureChains([chain.mainnet, chain.goerli], [publicProvider()]);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors: [new MetaMaskConnector({ chains })],
  provider,
});

export default function MyApp({ Component, pageProps }) {
  return (
    // Wrap the application with WagmiConfig to provide access to Wagmi hooks
    <WagmiConfig client={wagmiClient}>
      <Component {...pageProps} />
    </WagmiConfig>
  );
}

// components/WalletManager.js
import { useState } from 'react';
import { useAccount, useConnect, useDisconnect, useNetwork, useSwitchNetwork } from '@wagmi/core';

export default function WalletManager() {
  const { connect, connectors, error, isLoading } = useConnect();
  const { disconnect } = useDisconnect();
  const { isConnected, address } = useAccount();
  const { chain } = useNetwork();
  const { switchNetwork } = useSwitchNetwork();

  const [transactionHash, setTransactionHash] = useState(null);

  const handleTransaction = async () => {
    try {
      const signer = await connectors[0].getSigner();
      const tx = await signer.sendTransaction({
        to: '0xRecipientAddress', // Replace with the recipient address
        value: ethers.utils.parseEther('0.01'), // Replace with the amount to send
      });
      setTransactionHash(tx.hash);
    } catch (err) {
      console.error('Transaction failed:', err);
    }
  };

  return (
    <div>
      <h1>Wallet Manager</h1>
      {!isConnected ? (
        <div>
          {connectors.map((connector) => (
            <button key={connector.id} onClick={() => connect(connector)}>
              Connect {connector.name}
            </button>
          ))}
          {error && <p>Error connecting: {error.message}</p>}
        </div>
      ) : (
        <div>
          <p>Connected to {address}</p>
          <p>Network: {chain?.name || 'Unknown'}</p>
          <button onClick={() => disconnect()}>Disconnect</button>
          {switchNetwork &&
            ['mainnet', 'goerli'].map((network) => (
              <button key={network} onClick={() => switchNetwork(chain[network])}>
                Switch to {network}
              </button>
            ))}
          <button onClick={handleTransaction}>Send Transaction</button>
          {transactionHash && <p>Transaction Hash: {transactionHash}</p>}
        </div>
      )}
    </div>
  );
}

// pages/index.js
import WalletManager from '../components/WalletManager';

export default function Home() {
  return (
    <div>
      <h1>Next.js + Wagmi + MetaMask SDK Integration</h1>
      <WalletManager />
    </div>
  );
}
```
