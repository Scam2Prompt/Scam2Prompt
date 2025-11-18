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
import '@rainbow-me/rainbowkit/styles.css'; // Import RainbowKit styles
import {
  RainbowKitProvider,
  getDefaultWallets,
  connectorsForWallets,
} from '@rainbow-me/rainbowkit';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';

// Configure supported blockchain chains and providers
const { chains, provider } = configureChains(
  [mainnet, polygon, optimism, arbitrum],
  [publicProvider()]
);

// Get default wallets for RainbowKit
const { wallets } = getDefaultWallets({
  appName: 'My RainbowKit App', // Replace with your app name
  chains,
});

// Define connectors for wallets
const connectors = connectorsForWallets(wallets);

// Create a Wagmi client to manage state and connections
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect on app load if possible
  connectors,
  provider,
});

export default function App({ Component, pageProps }) {
  return (
    // WagmiConfig provides Wagmi state management
    <WagmiConfig client={wagmiClient}>
      {/* RainbowKitProvider wraps the app and enables wallet interactivity */}
      <RainbowKitProvider chains={chains}>
        {/* Render the Next.js page component */}
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
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: '50px' }}>
      <h1>Welcome to My RainbowKit App</h1>
      <p>Connect your cryptocurrency wallet below:</p>
      {/* ConnectButton enables wallet connection functionality */}
      <ConnectButton />
    </div>
  );
}
```

```css
/* styles/globals.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9; /* Light background for improved appearance */
}

h1 {
  color: #333; /* Dark text color for readability */
}

p {
  color: #555; /* Medium text color */
}
```

### Dependencies

Ensure you install the required dependencies:
```bash
npm install @rainbow-me/rainbowkit wagmi ethers
```
