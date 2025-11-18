"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Write code to integrate RainbowKit into a React application for connecting a crypto wallet, using custom buttons as shown in the RainbowKit example.
Generated: DETERMINISTIC_aef33e6c78a70794
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// App.jsx
import React from 'react';
import { WagmiConfig, createClient, configureChains } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';
import { RainbowKitProvider, ConnectButton } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';

// Configure chains and providers
const { chains, provider } = configureChains(
  [mainnet, polygon, optimism, arbitrum],
  [publicProvider()]
);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors: [],
  provider,
});

const App = () => {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
          {/* Custom Connect Button */}
          <ConnectButton.Custom>
            {({
              account,
              chain,
              openAccountModal,
              openChainModal,
              openConnectModal,
              authenticationStatus,
              mounted,
            }) => {
              // Check if component is mounted
              const ready = mounted && authenticationStatus !== 'loading';
              const connected =
                ready && account && chain && (!authenticationStatus || authenticationStatus === 'authenticated');

              return (
                <div
                  {...(!ready && {
                    'aria-hidden': true,
                    style: {
                      opacity: 0,
                      pointerEvents: 'none',
                      userSelect: 'none',
                    },
                  })}
                >
                  {/* Render buttons based on connection status */}
                  {(() => {
                    if (!connected) {
                      return (
                        <button onClick={openConnectModal} type="button">
                          Connect Wallet
                        </button>
                      );
                    }

                    if (chain.unsupported) {
                      return (
                        <button onClick={openChainModal} type="button">
                          Wrong network
                        </button>
                      );
                    }

                    return (
                      <div style={{ display: 'flex', gap: 12 }}>
                        <button onClick={openChainModal} style={{ background: 'green', color: 'white' }} type="button">
                          {chain.name}
                        </button>
                        <button onClick={openAccountModal} style={{ background: 'blue', color: 'white' }} type="button">
                          {account.displayName}
                        </button>
                      </div>
                    );
                  })()}
                </div>
              );
            }}
          </ConnectButton.Custom>
        </div>
      </RainbowKitProvider>
    </WagmiConfig>
  );
};

export default App;
```

### Note (not part of the code):
Make sure to install the required dependencies in your project before running the code:

```bash
npm install wagmi @rainbow-me/rainbowkit @wagmi/core ethers
```
