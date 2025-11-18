"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Write Next.js code to integrate RainbowKit for cryptocurrency wallet connection, as described on the Wallet Connect App page.
Generated: DETERMINISTIC_c6f88c746e1a1217
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
import { AppProps } from 'next/app';
import { WagmiConfig, createClient } from 'wagmi';
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';

// Create a Wagmi client
const { chains, provider } = configureChains();
const { connectors } = getDefaultWallets({
  appName: 'My RainbowKit App',
  chains,
});

const wagmiClient = createClient({
  autoConnect: true,
  connectors,
  provider,
});

// Main app component
function MyApp({ Component, pageProps }: AppProps) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;

// utils/configureChains.js
import { configureChains, createClient } from 'wagmi';
import { mainnet, polygon, avalanche, optimism, celo } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';

// Configure chains and providers for Wagmi
export function configureChains() {
  const { chains, provider } = configureChains(
    [mainnet, polygon, avalanche, optimism, celo],
    [publicProvider()]
  );
  return { chains, provider };
}

// pages/index.js
import { ConnectButton } from '@rainbow-me/rainbowkit';
import { useAccount } from 'wagmi';

export default function Home() {
  const { isConnected, address } = useAccount();

  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome to My RainbowKit App</h1>
      <ConnectButton />

      {isConnected && (
        <div>
          <h2>Connected Wallet:</h2>
          <p>{address}</p>
        </div>
      )}
    </div>
  );
}
```

```bash
# Install necessary dependencies
npm install next react react-dom wagmi @rainbow-me/rainbowkit ethers
```

### Notes:
- This code assumes you have a Next.js environment set up.
- Ensure you have the appropriate versions of Next.js and related packages.
- Don't forget to adjust your styles in `globals.css` as needed for your app's design.
