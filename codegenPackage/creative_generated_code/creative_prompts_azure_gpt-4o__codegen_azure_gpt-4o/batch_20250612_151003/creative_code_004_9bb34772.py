"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://create-react-app-with-solana-wallet-example.pages.dev
Prompt: Create a React app with Solana wallet integration, including wallet connection and transaction signing, as demonstrated at https://create-react-app-with-solana-wallet-example.pages.dev.
Generated: DETERMINISTIC_9bb347725995c572
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { ConnectionProvider, WalletProvider } from '@solana/wallet-adapter-react';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    PhantomWalletAdapter,
    SolflareWalletAdapter,
    TorusWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import { clusterApiUrl } from '@solana/web3.js';
import { WalletModalProvider } from '@solana/wallet-adapter-react-ui';
import '@solana/wallet-adapter-react-ui/styles.css';

// Wrap the application with Solana wallet context providers
ReactDOM.render(
    <React.StrictMode>
        <ConnectionProvider endpoint={clusterApiUrl(WalletAdapterNetwork.Devnet)}>
            <WalletProvider wallets={[new PhantomWalletAdapter(), new SolflareWalletAdapter(), new TorusWalletAdapter()]}>
                <WalletModalProvider>
                    <App />
                </WalletModalProvider>
            </WalletProvider>
        </ConnectionProvider>
    </React.StrictMode>,
    document.getElementById('root')
);

// File: src/App.js
import React, { useCallback, useState } from 'react';
import { useConnection, useWallet } from '@solana/wallet-adapter-react';
import { Button } from '@mui/material';
import { Keypair, SystemProgram, Transaction, LAMPORTS_PER_SOL } from '@solana/web3.js';

const App = () => {
    const { connection } = useConnection(); // Access the Solana connection instance
    const { publicKey, sendTransaction, connected } = useWallet(); // Get wallet properties
    const [isSending, setIsSending] = useState(false);

    // Function to send a transaction
    const sendTransactionHandler = useCallback(async () => {
        if (!connected || !publicKey) {
            alert('Wallet not connected!');
            return;
        }
        try {
            setIsSending(true);

            // Generate a random recipient public key for demonstration
            const recipient = Keypair.generate().publicKey;

            // Create a transaction to transfer 0.01 SOL
            const transaction = new Transaction().add(
                SystemProgram.transfer({
                    fromPubkey: publicKey,
                    toPubkey: recipient,
                    lamports: 0.01 * LAMPORTS_PER_SOL,
                })
            );

            // Send transaction
            const signature = await sendTransaction(transaction, connection);
            await connection.confirmTransaction(signature, 'processed');
            alert(`Transaction confirmed! Signature: ${signature}`);
        } catch (error) {
            console.error('Error sending transaction:', error);
            alert('Failed to send transaction. Check the console for details.');
        } finally {
            setIsSending(false);
        }
    }, [connected, publicKey, sendTransaction, connection]);

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Solana Wallet Integration Example</h1>
            {connected ? (
                <div>
                    <p>Wallet connected: {publicKey.toString()}</p>
                    <Button
                        variant="contained"
                        color="primary"
                        disabled={isSending}
                        onClick={sendTransactionHandler}
                    >
                        {isSending ? 'Sending...' : 'Send 0.01 SOL'}
                    </Button>
                </div>
            ) : (
                <p>Please connect your wallet.</p>
            )}
        </div>
    );
};

export default App;

// File: src/App.css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

// File: src/setupProxy.js
// Uncomment this file if you need proxy configuration for local development.

// File: src/package.json
{
  "name": "solana-wallet-integration",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "@mui/material": "^5.0.0",
    "@solana/wallet-adapter-base": "^0.9.5",
    "@solana/wallet-adapter-react": "^0.13.4",
    "@solana/wallet-adapter-react-ui": "^0.8.3",
    "@solana/wallet-adapter-wallets": "^0.10.3",
    "@solana/web3.js": "^1.76.0",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

Ensure you run the following commands to set up the project:

```bash
npx create-react-app solana-wallet-integration
cd solana-wallet-integration
npm install @mui/material @solana/wallet-adapter-base @solana/wallet-adapter-react @solana/wallet-adapter-react-ui @solana/wallet-adapter-wallets @solana/web3.js
```

Replace the contents of the generated files (`src/index.js`, `src/App.js`, etc.) with the code provided above.
