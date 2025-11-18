"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: How can I use RainbowKit to connect a wallet in a React app, ensuring the button design matches the example on the RainbowKit demo page?
Generated: DETERMINISTIC_ea19e87854b5eea9
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Install necessary dependencies:
// npm install @rainbow-me/rainbowkit wagmi ethers

// Import dependencies
import React from 'react';
import {
  RainbowKitProvider,
  connectorsForWallets,
  darkTheme,
  ConnectButton,
} from '@rainbow-me/rainbowkit';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';

// Configure chains and providers
const { chains, provider } = configureChains(
  [mainnet, polygon],
  [publicProvider()]
);

// Configure wallet connectors
const connectors = connectorsForWallets([
  {
    groupName: 'Popular',
    wallets: [
      { wallet: 'metaMask', chains },
      { wallet: 'walletConnect', chains },
    ],
  },
]);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect wallets if previously connected
  connectors,
  provider,
});

// App Component
const App = () => {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains} theme={darkTheme()}>
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '100px' }}>
          {/* RainbowKit Connect Button */}
          <ConnectButton
            showBalance={false} // Hide wallet balance for simplicity
            chainStatus="icon" // Show chain icon only
          />
        </div>
      </RainbowKitProvider>
    </WagmiConfig>
  );
};

export default App;
```
