"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-hr0b8bx2h-reown-com.vercel.app
Prompt: Create a configuration for AppKit using Wagmi without social authentication options and demonstrate how to initialize the wallet.
Generated: DETERMINISTIC_c13652c9d621abac
Batch ID: 20250612_145427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// Import required modules from Wagmi and AppKit
import { configureChains, createClient, defaultChains } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';
import { AppKitProvider, AppKitConfig } from '@aragon/appkit';

// Configure the chains and providers
const { chains, provider, webSocketProvider } = configureChains(defaultChains, [
  publicProvider(),
]);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  provider,
  webSocketProvider,
});

// AppKit configuration without social authentication
const appKitConfig: AppKitConfig = {
  wagmiClient,
  // Disable social login options
  connect: {
    walletconnect: false,
    fortmatic: false,
    portis: false,
    torus: false,
    authereum: false,
    burnerconnect: false,
    frame: false,
    walletlink: false,
  },
};

// Initialize the wallet connection
async function initializeWallet() {
  try {
    // Initialize AppKit with the configuration
    const appKit = new AppKitProvider(appKitConfig);
    
    // Connect to the wallet
    const connection = await appKit.connect();
    
    if (connection.status === 'connected') {
      console.log('Wallet connected:', connection.account);
    } else {
      console.log('Wallet connection failed');
    }
    
    return appKit;
  } catch (error) {
    console.error('Error initializing wallet:', error);
    throw error;
  }
}

// Example usage
initializeWallet().catch(console.error);
```
