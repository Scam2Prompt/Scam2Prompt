"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Show me how to use RainbowKit to connect a wallet with a personalized UI.
Generated: DETERMINISTIC_cddd3f61df06ad4e
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React from 'react';
import { RainbowKitProvider, getDefaultWallets } from '@rainbow-me/rainbowkit';
import { EthereumClient, useEthers } from '@usedapp/core';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon } from 'wagmi/chains';

// Configure chains and wallets
const { chains, provider } = configureChains(
  [mainnet, polygon],
  [publicProvider()]
);

// Get default wallets and customize if needed
const { connectors } = getDefaultWallets({
  appName: 'My RainbowKit App',
  chains,
});

// Create a Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors: () => connectors,
  provider,
});

// Custom WalletButton component
const WalletButton = () => {
  const { activateBrowserWallet, account } = useEthers();

  return (
    <button onClick={activateBrowserWallet} style={buttonStyle}>
      {account ? 'Connected: ' + account.slice(0, 6) + '...' : 'Connect Wallet'}
    </button>
  );
};

// Custom button styles
const buttonStyle = {
  padding: '10px 20px',
  backgroundColor: '#4CAF50',
  color: 'white',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
};

// Main Application Component
const App = () => {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <div style={appStyle}>
          <h1>Welcome to My Wallet Connection App</h1>
          <WalletButton />
        </div>
      </RainbowKitProvider>
    </WagmiConfig>
  );
};

// Custom application styles
const appStyle = {
  textAlign: 'center',
  marginTop: '50px',
};

// Export the App component as default
export default App;
```
