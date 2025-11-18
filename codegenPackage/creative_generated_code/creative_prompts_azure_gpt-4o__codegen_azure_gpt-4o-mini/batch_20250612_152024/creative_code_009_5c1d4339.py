"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: How can I use RainbowKit in Next.js to display wallet connection status? Provide a code example.
Generated: DETERMINISTIC_5c1d43398b22a1ac
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import { useEffect } from 'react';
import { RainbowKitProvider, useWallet } from '@rainbow-me/rainbowkit';
import { chain, configureChains, createClient, WagmiConfig } from 'wagmi';
import { alchemyProvider } from 'wagmi/providers/alchemy';
import { publicProvider } from 'wagmi/providers/public';

// Configure the chains (Ethereum mainnet and testnets)
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum],
  [alchemyProvider({ apiKey: process.env.ALCHEMY_API_KEY }), publicProvider()]
);

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  provider,
});

// Main App component
export default function App({ Component, pageProps }) {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider chains={chains}>
        <WalletConnection />
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

// WalletConnection component to display wallet connection status
function WalletConnection() {
  const { account, status, connect, disconnect } = useWallet();

  // Effect for handling wallet connection updates
  useEffect(() => {
    if (status === 'connected') {
      console.log('Wallet connected:', account);
    } else if (status === 'disconnected') {
      console.log('Wallet disconnected');
    }
  }, [status, account]);

  // Function to handle connection button click
  const handleConnect = async () => {
    try {
      await connect();
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  // Function to handle disconnection button click
  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error('Error disconnecting wallet:', error);
    }
  };

  return (
    <div>
      {status === 'connected' ? (
        <div>
          <p>Connected as: {account.displayName}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnect}>Connect Wallet</button>
      )}
    </div>
  );
}
```

Make sure to set your Alchemy API key in the environment variables before running this Next.js application.
