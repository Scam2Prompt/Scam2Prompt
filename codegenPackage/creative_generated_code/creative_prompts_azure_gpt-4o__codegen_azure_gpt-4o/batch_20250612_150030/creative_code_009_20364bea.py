"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.vercel.app
Prompt: Generate a step-by-step guide to integrate Web3Modal into a Next.js Web3 project hosted on Vercel.
Generated: DETERMINISTIC_20364bead0d62803
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// 1. Install Required Dependencies
// Run the following command in your Next.js project:
// npm install @web3modal/react ethers @web3modal/ethereum

// 2. Create a Web3ModalProvider in `_app.js`
import { Web3Modal, Web3ModalConfig } from '@web3modal/react';
import { EthereumClient, w3mProvider, w3mConnectors } from '@web3modal/ethereum';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon } from 'wagmi/chains';

// Configure chains and providers
const chains = [mainnet, polygon];
const { provider } = configureChains(chains, [w3mProvider({ projectId: 'YOUR_PROJECT_ID' })]);

// Initialize Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors: w3mConnectors({ chains, projectId: 'YOUR_PROJECT_ID' }),
  provider,
});

// Initialize Ethereum client for Web3Modal
const ethereumClient = new EthereumClient(wagmiClient, chains);

// Web3Modal config
const web3ModalConfig = {
  projectId: 'YOUR_PROJECT_ID',
  theme: 'dark',
  accentColor: 'default',
  ethereumClient,
};

export default function App({ Component, pageProps }) {
  return (
    <Web3Modal config={web3ModalConfig}>
      <WagmiConfig client={wagmiClient}>
        <Component {...pageProps} />
      </WagmiConfig>
    </Web3Modal>
  );
}

// 3. Add a Connect Wallet Button in `index.js`
import { useAccount, useConnect, useDisconnect } from 'wagmi';

export default function Home() {
  const { address, isConnected } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Next.js + Web3Modal Integration</h1>
      {!isConnected ? (
        <div>
          {connectors.map((connector) => (
            <button
              key={connector.id}
              onClick={() => connect({ connector })}
              style={{ margin: '10px', padding: '10px' }}
            >
              Connect with {connector.name}
            </button>
          ))}
        </div>
      ) : (
        <div>
          <p>Connected to {address}</p>
          <button onClick={disconnect} style={{ padding: '10px', marginTop: '10px' }}>
            Disconnect
          </button>
        </div>
      )}
    </div>
  );
}

// 4. Environment Variables Setup
// Add your `PROJECT_ID` from Web3Modal in a `.env.local` file:
// NEXT_PUBLIC_PROJECT_ID=your_project_id

// Update the project ID in the `_app.js` file:
// Replace 'YOUR_PROJECT_ID' with `process.env.NEXT_PUBLIC_PROJECT_ID` where applicable.

// 5. Deploy to Vercel
// Push your code to GitHub, GitLab, or Bitbucket, and import the repository into Vercel.
// Ensure the `NEXT_PUBLIC_PROJECT_ID` environment variable is added in Vercel under Project Settings > Environment Variables.
// Deploy the project and test the integration.
```
