"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Generate a Next.js page that includes RainbowKit for connecting a wallet, with a focus on user-friendly design.
Generated: DETERMINISTIC_089948ef018abd83
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
import { AppProps } from 'next/app';
import { RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';
import { chain, configureChains, createClient, WagmiConfig } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';

// Configure chains and providers
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.ropsten],
  [publicProvider()]
);

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  provider,
});

// Main application component
function MyApp({ Component, pageProps }: AppProps) {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider
        chains={chains}
        theme={darkTheme({
          accentColor: '#ff007a',
          accentColorForeground: 'white',
        })}
      >
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { ConnectButton } from '@rainbow-me/rainbowkit';

// Main page component
export default function Home() {
  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Welcome to the Wallet Connection App</h1>
      <p style={styles.description}>Connect your wallet to get started!</p>
      <ConnectButton style={styles.connectButton} />
    </div>
  );
}

// Inline styles for better design
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#101010',
    color: '#ffffff',
    fontFamily: 'Arial, sans-serif',
  },
  title: {
    fontSize: '2.5rem',
    marginBottom: '1rem',
  },
  description: {
    fontSize: '1.2rem',
    marginBottom: '2rem',
  },
  connectButton: {
    backgroundColor: '#ff007a',
    border: 'none',
    borderRadius: '5px',
    padding: '10px 20px',
    color: 'white',
    fontSize: '1rem',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  },
};

// Error handling for potential wallet connection issues
export function useWalletConnection() {
  const { isConnected, error } = useAccount();

  if (error) {
    console.error('Wallet connection error:', error);
    alert('Failed to connect the wallet. Please try again.');
  }

  return isConnected;
}
```

```bash
# Install necessary dependencies
npm install next react react-dom @rainbow-me/rainbowkit wagmi ethers
```

```json
// package.json (partial)
{
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "@rainbow-me/rainbowkit": "latest",
    "wagmi": "latest",
    "ethers": "latest"
  }
}
```

Ensure that you have Node.js installed and follow these steps to set up your Next.js project with the RainbowKit wallet connection:

1. Create a new Next.js project using `npx create-next-app@latest`.
2. Replace the files with the provided code.
3. Install the necessary dependencies.
4. Run your application using `npm run dev`. 

This setup is user-friendly and aligns with best practices for a production-ready application.
