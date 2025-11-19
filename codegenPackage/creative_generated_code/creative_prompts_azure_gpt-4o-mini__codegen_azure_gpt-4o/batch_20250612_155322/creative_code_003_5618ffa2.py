"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Provide an example of using RainbowKit to enable wallet connections in a Next.js application.
Generated: DETERMINISTIC_5618ffa2043d574f
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js
import "../styles/globals.css";
import "@rainbow-me/rainbowkit/styles.css";
import { getDefaultWallets, RainbowKitProvider } from "@rainbow-me/rainbowkit";
import { configureChains, createClient, WagmiConfig } from "wagmi";
import { mainnet, polygon, optimism, arbitrum } from "wagmi/chains";
import { publicProvider } from "wagmi/providers/public";

// Configure blockchain networks and providers
const { chains, provider } = configureChains(
  [mainnet, polygon, optimism, arbitrum], // Supported chains
  [publicProvider()] // Providers (public in this case)
);

// Set up default wallet options (e.g., MetaMask, WalletConnect)
const { connectors } = getDefaultWallets({
  appName: "My RainbowKit App", // Application name displayed in wallet UI
  chains,
});

// Create a Wagmi client with the configured chains and connectors
const wagmiClient = createClient({
  autoConnect: true, // Automatically reconnect to the last used wallet
  connectors,
  provider,
});

function MyApp({ Component, pageProps }) {
  return (
    // Wrap the application with WagmiConfig and RainbowKitProvider
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        {/* Render the main application */}
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { ConnectButton } from "@rainbow-me/rainbowkit";

export default function Home() {
  return (
    <div>
      <h1>Welcome to My RainbowKit App</h1>
      {/* Render the wallet connection button */}
      <ConnectButton />
    </div>
  );
}
```

```css
/* styles/globals.css */

/* Basic styles for the application */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

h1 {
  text-align: center;
  margin-top: 2rem;
}

div {
  text-align: center;
  margin-top: 1rem;
}
```

**Dependencies to install first:**
```bash
# Required dependencies
npm install @rainbow-me/rainbowkit wagmi ethers
```
