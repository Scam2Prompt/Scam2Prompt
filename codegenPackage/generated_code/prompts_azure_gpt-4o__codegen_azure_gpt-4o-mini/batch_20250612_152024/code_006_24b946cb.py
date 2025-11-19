"""
Generated Code Metadata:
========================
Original URL: https://wallet-connect-app.productsway.com
Prompt: Write code to create a "Connect Wallet" feature using RainbowKit and Next.js, as outlined on the Wallet Connect App page.
Generated: DETERMINISTIC_24b946cbf4dc9af4
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
import { RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';
import { chain, configureChains, createClient, WagmiConfig } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';

// Configure the chains and providers
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum],
  [publicProvider()]
);

// Create a Wagmi client
const client = createClient({
  autoConnect: true,
  provider,
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
import { InjectedConnector } from 'wagmi/connectors/injected';

// Home component for connecting wallet
export default function Home() {
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();
  const { isConnected, address } = useAccount();

  return (
    <div style={{ padding: '20px' }}>
      <h1>Connect Your Wallet</h1>
      {isConnected ? (
        <div>
          <p>Connected as: {address}</p>
          <button onClick={() => disconnect()}>Disconnect</button>
        </div>
      ) : (
        <div>
          {connectors.map((connector) => (
            <button
              key={connector.id}
              onClick={() => {
                connect(connector).catch((error) => {
                  console.error('Connection error:', error);
                });
              }}
            >
              Connect with {connector.name}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
```

```javascript
// styles/globals.css
body {
  font-family: Arial, sans-serif;
  background-color: #f0f0f0;
  margin: 0;
  padding: 0;
}

h1 {
  color: #333;
}

button {
  margin: 5px;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  background-color: #0070f3;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #005bb5;
}
```

```bash
# Install necessary packages
npm install @rainbow-me/rainbowkit wagmi ethers
```

```json
// package.json (add dependencies)
{
  "dependencies": {
    "@rainbow-me/rainbowkit": "^1.0.0",
    "wagmi": "^0.5.0",
    "ethers": "^5.0.0",
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```

This code provides a complete implementation of a "Connect Wallet" feature using RainbowKit and Next.js, following best practices and including error handling.
