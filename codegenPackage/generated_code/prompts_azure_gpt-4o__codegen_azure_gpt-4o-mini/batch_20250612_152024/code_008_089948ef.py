"""
Generated Code Metadata:
========================
Original URL: https://wallet-connect-app.productsway.com
Prompt: Generate a Next.js page that includes RainbowKit for connecting a wallet, with a focus on user-friendly design.
Generated: DETERMINISTIC_089948ef018abd83
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/_app.js
import '../styles/globals.css';
import { RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';
import { Chain, WagmiConfig, createClient } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';

// Define the supported chains
const chains = [mainnet, polygon, optimism, arbitrum];

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  provider: ({ chain }) => {
    return chain.provider;
  },
});

// Main application component
function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider chains={chains} theme={darkTheme()}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { ConnectButton } from '@rainbow-me/rainbowkit';

// Home page component
export default function Home() {
  const { isConnected } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Welcome to Wallet Connect</h1>
      <p style={styles.description}>
        {isConnected ? 'You are connected!' : 'Please connect your wallet.'}
      </p>
      <ConnectButton />
      {isConnected && (
        <button style={styles.disconnectButton} onClick={() => disconnect()}>
          Disconnect Wallet
        </button>
      )}
    </div>
  );
}

// Styles for the components
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#282c34',
    color: 'white',
  },
  title: {
    fontSize: '2rem',
    marginBottom: '1rem',
  },
  description: {
    fontSize: '1.2rem',
    marginBottom: '2rem',
  },
  disconnectButton: {
    padding: '10px 20px',
    fontSize: '1rem',
    backgroundColor: '#ff4757',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
};
```

```bash
# Install necessary dependencies
npm install next react react-dom wagmi @rainbow-me/rainbowkit
```

```json
// package.json
{
  "name": "wallet-connect-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "wagmi": "^0.8.0",
    "@rainbow-me/rainbowkit": "^0.5.0"
  }
}
```

```css
/* styles/globals.css */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #282c34;
  color: white;
}
```
