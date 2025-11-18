"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Write code to display a list of supported Solana wallets using Mantine UI and the Solana Wallet Adapter.
Generated: DETERMINISTIC_d603a69ee0db1db2
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary dependencies
import React from 'react';
import { Button, Stack, Title } from '@mantine/core'; // Mantine UI components
import {
  WalletModalProvider,
  WalletMultiButton,
} from '@solana/wallet-adapter-react-ui'; // Solana Wallet Adapter UI
import {
  ConnectionProvider,
  WalletProvider,
} from '@solana/wallet-adapter-react'; // Solana Wallet Adapter Core
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
  BackpackWalletAdapter,
  GlowWalletAdapter,
} from '@solana/wallet-adapter-wallets'; // Import supported wallets
import { clusterApiUrl } from '@solana/web3.js'; // Import cluster utilities

// Default Solana cluster endpoint
const NETWORK = clusterApiUrl('mainnet-beta');

// Main application component
const WalletListApp = () => {
  // Initialize wallet adapters
  const wallets = [
    new PhantomWalletAdapter(),
    new SolflareWalletAdapter(),
    new BackpackWalletAdapter(),
    new GlowWalletAdapter(),
  ];

  return (
    <ConnectionProvider endpoint={NETWORK}>
      <WalletProvider wallets={wallets} autoConnect={false}>
        <WalletModalProvider>
          <Stack spacing="lg" align="center" mt="xl">
            {/* Application Title */}
            <Title order={2}>Supported Solana Wallets</Title>

            {/* Wallet Connect Button (Handles all wallets) */}
            <WalletMultiButton />

            {/* List of Supported Wallets */}
            <Stack>
              {wallets.map((wallet, index) => (
                <Button key={index} variant="light" color="blue">
                  {wallet.name}
                </Button>
              ))}
            </Stack>
          </Stack>
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
};

export default WalletListApp;
```

Note: Ensure you install all dependencies:
```bash
npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-wallets @solana/wallet-adapter-react-ui @mantine/core
```
