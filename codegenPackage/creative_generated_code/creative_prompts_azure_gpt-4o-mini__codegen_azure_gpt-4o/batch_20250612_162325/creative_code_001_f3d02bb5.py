"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Provide a code example for integrating MetaMask with RainbowKit for wallet connection.
Generated: DETERMINISTIC_f3d02bb532b9d370
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
import { getDefaultWallets, RainbowKitProvider } from '@rainbow-me/rainbowkit';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';

// Step 1: Configure chains and providers
const { chains, provider } = configureChains(
  [mainnet, polygon, optimism, arbitrum],
  [publicProvider()]
);

// Step 2: Get default wallets (including MetaMask) with RainbowKit
const { connectors } = getDefaultWallets({
  appName: 'My RainbowKit App',
  chains,
});

// Step 3: Create the Wagmi client
const wagmiClient = createClient({
  autoConnect: true, // Automatically connect if a wallet is available
  connectors,
  provider,
});

// Step 4: Application Component
const App = () => {
  return (
    <WagmiConfig client={wagmiClient}>
      {/* Wrap the application in RainbowKitProvider */}
      <RainbowKitProvider chains={chains}>
        <MainComponent /> {/* Replace this with your actual component */}
      </RainbowKitProvider>
    </WagmiConfig>
  );
};

export default App;

// Note: To integrate with MetaMask using RainbowKit, ensure that your application
// includes the required dependencies (such as `@rainbow-me/rainbowkit` and `wagmi`)
// and follows proper setup instructions as documented by RainbowKit.
```
