"""
Generated Code Metadata:
========================
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Generate code to connect a Solana wallet with a Mantine UI component using the Solana Wallet Adapter.
Generated: DETERMINISTIC_9f119032c3f2d1d6
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and components
import React, { useMemo } from 'react';
import { WalletProvider, ConnectionProvider } from '@solana/wallet-adapter-react';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import {
    PhantomWalletAdapter,
    SolflareWalletAdapter,
    TorusWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { clusterApiUrl } from '@solana/web3.js';
import { Button } from '@mantine/core';

// Import styles for the wallet adapter modal
require('@solana/wallet-adapter-react-ui/styles.css');

// Main component to connect Solana wallet
const SolanaWalletConnector = () => {
    // Define the network (e.g., 'mainnet-beta', 'testnet', 'devnet')
    const network = 'devnet';

    // Create a connection endpoint based on the selected network
    const endpoint = useMemo(() => clusterApiUrl(network), [network]);

    // Initialize wallet adapters
    const wallets = useMemo(
        () => [
            new PhantomWalletAdapter(),
            new SolflareWalletAdapter({ network }),
            new TorusWalletAdapter(),
        ],
        [network]
    );

    return (
        <ConnectionProvider endpoint={endpoint}>
            <WalletProvider wallets={wallets} autoConnect>
                <WalletModalProvider>
                    {/* Mantine UI Button to trigger wallet connection */}
                    <Button
                        onClick={() => {
                            const modal = document.querySelector('.wallet-adapter-modal-button');
                            if (modal) modal.click(); // Trigger the wallet modal
                        }}
                        variant="outline"
                        color="blue"
                    >
                        Connect Wallet
                    </Button>
                </WalletModalProvider>
            </WalletProvider>
        </ConnectionProvider>
    );
};

export default SolanaWalletConnector;
```
