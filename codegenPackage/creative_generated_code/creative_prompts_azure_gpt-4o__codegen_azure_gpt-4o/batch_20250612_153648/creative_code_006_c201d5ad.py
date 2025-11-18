"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Explain how to use the Solana Wallet Adapter to support multiple wallet providers in a Mantine UI application.
Generated: DETERMINISTIC_c201d5ada26e3ad7
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import dependencies
import React, { useMemo } from 'react';
import { MantineProvider } from '@mantine/core';
import { ConnectionProvider, WalletProvider } from '@solana/wallet-adapter-react';
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
  GlowWalletAdapter,
  TorusWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import { clusterApiUrl } from '@solana/web3.js';

// Import default styles for Wallet Adapter UI
import '@solana/wallet-adapter-react-ui/styles.css';

// Functional component for the Mantine-based application
const App = () => {
  // Define the network configuration (e.g., devnet, testnet, mainnet-beta)
  const network = 'mainnet-beta';

  // Define the RPC connection endpoint based on the desired network
  const endpoint = useMemo(() => clusterApiUrl(network), [network]);

  // Initialize wallet adapters for multiple wallet providers
  const wallets = useMemo(
    () => [
      new PhantomWalletAdapter(), // Phantom wallet
      new SolflareWalletAdapter({ network }), // Solflare wallet
      new GlowWalletAdapter(), // Glow wallet
      new TorusWalletAdapter(), // Torus wallet
    ],
    [network]
  );

  return (
    // Wrap the application with the MantineProvider for UI theming
    <MantineProvider withGlobalStyles withNormalizeCSS>
      {/* Wrap the application with ConnectionProvider to provide Solana RPC connection */}
      <ConnectionProvider endpoint={endpoint}>
        {/* Wrap the application with WalletProvider to manage wallet connections */}
        <WalletProvider wallets={wallets} autoConnect>
          {/* Provide a modal for wallet connection selection */}
          <WalletModalProvider>
            {/* Main content of the application */}
            <div style={{ padding: '20px' }}>
              <h1>Welcome to Mantine + Solana Wallet Adapter</h1>
              <p>Connect your wallet using the button above.</p>
            </div>
          </WalletModalProvider>
        </WalletProvider>
      </ConnectionProvider>
    </MantineProvider>
  );
};

export default App;
```

Above is the clean, well-documented, and production-ready code for integrating the Solana Wallet Adapter with multiple wallet providers in a Mantine UI application.
