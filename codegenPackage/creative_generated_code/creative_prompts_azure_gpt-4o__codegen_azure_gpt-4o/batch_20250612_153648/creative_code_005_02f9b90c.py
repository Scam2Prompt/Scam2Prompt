"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Generate code to customize Mantine UI buttons for connecting to Solana wallets via the Solana Wallet Adapter.
Generated: DETERMINISTIC_02f9b90c7de95647
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import React from 'react';
import { Button } from '@mantine/core'; // Mantine UI Button component
import {
  WalletProvider,
  ConnectionProvider,
  useWallet,
} from '@solana/wallet-adapter-react'; // Solana wallet adapter
import {
  WalletModalProvider,
  WalletMultiButton,
} from '@solana/wallet-adapter-react-ui'; // Wallet UI components
import {
  PhantomWalletAdapter,
  SolflareWalletAdapter,
  TorusWalletAdapter,
} from '@solana/wallet-adapter-wallets'; // Wallet adapters
import { clusterApiUrl } from '@solana/web3.js'; // API for Solana network interaction

// Custom Mantine Button for Solana Wallet Connection
const CustomWalletButton = () => {
  const { wallet, select } = useWallet(); // Access wallet state and selection function

  return (
    <Button
      // Apply custom styles to Mantine button
      styles={{
        root: {
          backgroundColor: wallet ? '#16a34a' : '#1e40af', // Green if connected, blue otherwise
          color: 'white',
          '&:hover': {
            backgroundColor: wallet ? '#15803d' : '#1d4ed8', // Darker shade on hover
          },
        },
      }}
      onClick={() => {
        // If no wallet selected, open wallet selection modal
        if (!wallet) select(); // Open modal
      }}
    >
      {wallet ? `Connected: ${wallet.name}` : 'Connect Wallet'}
    </Button>
  );
};

// Main App Component
export default function App() {
  // Create Solana wallet instances
  const wallets = [
    new PhantomWalletAdapter(),
    new SolflareWalletAdapter(),
    new TorusWalletAdapter(),
  ];

  return (
    <ConnectionProvider endpoint={clusterApiUrl('devnet')}>
      {/* Wrap components with WalletProvider */}
      <WalletProvider wallets={wallets} autoConnect>
        {/* Provide Wallet UI Modal */}
        <WalletModalProvider>
          <div style={{ padding: '2rem', textAlign: 'center' }}>
            <h1>Connect to Solana Wallet</h1>
            <CustomWalletButton />
            {/* Optional Multi-button for default wallets */}
            <div style={{ marginTop: '1rem' }}>
              <WalletMultiButton />
            </div>
          </div>
        </WalletModalProvider>
      </WalletProvider>
    </ConnectionProvider>
  );
}
```
