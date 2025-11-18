"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: How do I configure RainbowKit in Next.js to support multiple wallet providers?
Generated: DETERMINISTIC_21e4cb1ecc213459
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js
import '../styles/globals.css';
import '@rainbow-me/rainbowkit/styles.css';
import { RainbowKitProvider, getDefaultWallets, connectorsForWallets } from '@rainbow-me/rainbowkit';
import { configureChains, createConfig, WagmiConfig } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';

export default function App({ Component, pageProps }) {
  // Configure chains to support multiple networks
  const { chains, publicClient } = configureChains(
    [mainnet, polygon, optimism, arbitrum], // Add chains here
    [publicProvider()] // Use public provider for simplicity
  );

  // Get default wallet connectors (e.g., MetaMask, WalletConnect)
  const { wallets } = getDefaultWallets({
    appName: 'Your RainbowKit App',
    chains,
  });

  // Create custom connectors for demonstration purposes (if needed)
  const connectors = connectorsForWallets([
    ...wallets,
    // Add additional wallets if desired
  ]);

  // Create Wagmi config for RainbowKit
  const wagmiConfig = createConfig({
    autoConnect: true, // Automatically connect to saved wallets
    connectors,
    publicClient,
  });

  return (
    <WagmiConfig config={wagmiConfig}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```
