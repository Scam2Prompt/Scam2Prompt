"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Write a Next.js page that integrates RainbowKit for wallet connection, including custom button styles as demonstrated in the RainbowKit example.
Generated: DETERMINISTIC_880f42564e2b6619
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import { ConnectButton } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';
import { getDefaultWallets, RainbowKitProvider } from '@rainbow-me/rainbowkit';
import { chain, configureChains, createClient, WagmiConfig } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';

// Configure blockchain networks and providers
const { chains, provider } = configureChains(
  [chain.mainnet, chain.polygon, chain.optimism, chain.arbitrum],
  [publicProvider()]
);

// Setup default wallets with RainbowKit
const { connectors } = getDefaultWallets({
  appName: 'My RainbowKit App',
  chains,
});

// Create a Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors,
  provider,
});

// Custom styles for the RainbowKit ConnectButton
const customStyles = {
  connectButton: {
    backgroundColor: '#0070f3',
    borderRadius: '8px',
    fontSize: '16px',
    padding: '10px 20px',
    color: '#ffffff',
    border: 'none',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  },
  connectButtonHover: {
    backgroundColor: '#005bb5',
  },
};

export default function Home() {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#f0f0f0' }}>
          {/* Wrapper to control button styles */}
          <div>
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
                      style: { opacity: 0, pointerEvents: 'none', userSelect: 'none' },
                    })}
                  >
                    {connected ? (
                      chain.unsupported ? (
                        <button
                          onClick={openChainModal}
                          style={{ ...customStyles.connectButton, ...customStyles.connectButtonHover }}
                        >
                          Switch Network
                        </button>
                      ) : (
                        <button
                          onClick={openAccountModal}
                          style={customStyles.connectButton}
                          onMouseEnter={(e) => (e.target.style.backgroundColor = customStyles.connectButtonHover.backgroundColor)}
                          onMouseLeave={(e) => (e.target.style.backgroundColor = customStyles.connectButton.backgroundColor)}
                        >
                          {account.displayName}
                        </button>
                      )
                    ) : (
                      <button
                        onClick={openConnectModal}
                        style={customStyles.connectButton}
                        onMouseEnter={(e) => (e.target.style.backgroundColor = customStyles.connectButtonHover.backgroundColor)}
                        onMouseLeave={(e) => (e.target.style.backgroundColor = customStyles.connectButton.backgroundColor)}
                      >
                        Connect Wallet
                      </button>
                    )}
                  </div>
                );
              }}
            </ConnectButton.Custom>
          </div>
        </div>
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```

*Note*: Ensure you have the necessary dependencies installed for this code to work correctly. You can install them using:

```bash
npm install @rainbow-me/rainbowkit wagmi ethers
```
