"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Write code to create a "Connect Wallet" feature using RainbowKit and Next.js, as outlined on the Wallet Connect App page.
Generated: DETERMINISTIC_24b946cbf4dc9af4
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
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { chain, publicProvider } from 'wagmi/providers/public';

// Configure supported chains and providers
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum],
  [publicProvider()]
);

// Setup default wallets for RainbowKit
const { connectors } = getDefaultWallets({
  appName: 'My Wallet Connect App',
  chains,
});

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors,
  provider,
});

// Main application component
export default function App({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```

```javascript
// pages/index.js
import { ConnectButton } from '@rainbow-me/rainbowkit';

export default function Home() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      {/* Wallet connect button */}
      <ConnectButton />
    </div>
  );
}
```

```javascript
// styles/globals.css
/* Add basic global styles */
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background-color: #f5f5f5;
}
```

### Package Dependencies:
Ensure the following packages are installed via `npm` or `yarn`:

```bash
npm install @rainbow-me/rainbowkit wagmi ethers
```

### Note:
- The `ConnectButton` provided by RainbowKit handles wallet connection, disconnection, and state management out of the box.
- Add your own customizations (styling, chains, etc.) as needed.
```
