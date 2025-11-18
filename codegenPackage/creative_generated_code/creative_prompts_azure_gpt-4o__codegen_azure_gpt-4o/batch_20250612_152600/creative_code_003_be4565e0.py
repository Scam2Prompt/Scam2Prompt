"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-n76z148gg-reown-com.vercel.app
Prompt: Create a basic configuration for AppKit using Wagmi as the driving library without enabling any adapters.
Generated: DETERMINISTIC_be4565e024bbec89
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// Import necessary modules from Wagmi and AppKit
import { configureChains, createConfig } from 'wagmi';
import { mainnet } from 'wagmi/chains';
import { AppKitProvider } from '@ledgerhq/app-kit';

// Set up chains
// For this configuration, we are only using the mainnet chain for simplicity.
const { chains } = configureChains([mainnet], []); // No adapters are enabled.

// Create the Wagmi config
const wagmiConfig = createConfig({
  autoConnect: false, // Disable auto-connect to wallets
  connectors: [], // No connectors are added in this configuration
});

// Define the AppKitProvider configuration
// AppKit will use Wagmi under the hood for wallet and chain management.
const AppKitConfiguration = () => {
  return (
    <AppKitProvider wagmiConfig={wagmiConfig} supportedChains={chains}>
      {/* Add your application components here */}
    </AppKitProvider>
  );
};

// Export the configuration
export default AppKitConfiguration;
```
