"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: How can I use RainbowKit to implement a "Connect Wallet" feature with custom button styling in a Next.js project?
Generated: DETERMINISTIC_4868dc404fd22ca9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Install required dependencies before using this code:
// npm install @rainbow-me/rainbowkit wagmi ethers

// pages/_app.js
import '../styles/globals.css';
import '@rainbow-me/rainbowkit/styles.css'; // Import RainbowKit styles
import { RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';
import { getDefaultWallets, connectorsForWallets } from '@rainbow-me/rainbowkit';
import { configureChains, createConfig, WagmiConfig } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';

const { chains, publicClient } = configureChains(
  [mainnet, polygon, optimism, arbitrum], // Define supported chains
  [publicProvider()] // Use public provider
);

const { connectors } = getDefaultWallets({
  appName: 'My Connect Wallet App', // Name of your application
  projectId: 'YOUR_PROJECT_ID', // Optional: Add a WalletConnect Project ID if required
  chains,
});

const wagmiConfig = createConfig({
  autoConnect: true, // Automatically reconnect wallets
  connectors,
  publicClient, // Use public RPC client
});

export default function App({ Component, pageProps }) {
  return (
    <WagmiConfig config={wagmiConfig}>
      <RainbowKitProvider 
        chains={chains}
        theme={darkTheme()} // Use dark theme (customize as needed)
      >
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

// pages/index.js
import { ConnectButton } from '@rainbow-me/rainbowkit';

export default function Home() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      {/* Custom styling for the Connect Wallet button */}
      <ConnectButton.Custom>
        {({
          account,
          chain,
          openAccountModal,
          openChainModal,
          openConnectModal,
          mounted,
        }) => {
          const ready = mounted;
          const connected = ready && account && chain;

          return (
            <div
              {...(!ready && {
                'aria-hidden': true,
                style: { opacity: 0, pointerEvents: 'none' },
              })}
            >
              {connected ? (
                chain.unsupported ? (
                  <button
                    onClick={openChainModal}
                    style={{
                      padding: '10px 20px',
                      backgroundColor: 'red',
                      color: 'white',
                      border: 'none',
                      borderRadius: '5px',
                      cursor: 'pointer',
                    }}
                  >
                    Wrong Network
                  </button>
                ) : (
                  <button
                    onClick={openAccountModal}
                    style={{
                      padding: '10px 20px',
                      backgroundColor: '#6366f1',
                      color: 'white',
                      border: 'none',
                      borderRadius: '5px',
                      cursor: 'pointer',
                    }}
                  >
                    {account.displayName}
                  </button>
                )
              ) : (
                <button
                  onClick={openConnectModal}
                  style={{
                    padding: '10px 20px',
                    backgroundColor: '#10b981',
                    color: 'white',
                    border: 'none',
                    borderRadius: '5px',
                    cursor: 'pointer',
                  }}
                >
                  Connect Wallet
                </button>
              )}
            </div>
          );
        }}
      </ConnectButton.Custom>
    </div>
  );
}

// styles/globals.css
/* Add any global styles here if needed */
```
