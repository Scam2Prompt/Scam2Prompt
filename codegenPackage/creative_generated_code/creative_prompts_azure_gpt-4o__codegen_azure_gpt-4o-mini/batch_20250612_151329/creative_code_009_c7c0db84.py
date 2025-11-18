"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lineage-ai.vercel.app
Prompt: Write code to implement a "Connect Wallet" feature in a Next.js app for managing AI model licensing transactions, as outlined on the Lineage AI site.
Generated: DETERMINISTIC_c7c0db84996a0d2b
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js
import { useEffect } from 'react';
import { useWallet, WalletProvider } from '@solana/wallet-adapter-react';
import { ConnectionProvider, WalletProvider as SolanaWalletProvider } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter, SolletWalletAdapter } from '@solana/wallet-adapter-wallets';
import '../styles/globals.css';

// Create a custom provider for connecting to the Solana network
const walletConnectors = [
    new PhantomWalletAdapter(),
    new SolletWalletAdapter()
];

function MyApp({ Component, pageProps }) {
    return (
        <ConnectionProvider>
            <SolanaWalletProvider wallets={walletConnectors}>
                <Component {...pageProps} />
            </SolanaWalletProvider>
        </ConnectionProvider>
    );
}

export default MyApp;
```

```javascript
// components/ConnectWallet.js
import { useWallet } from '@solana/wallet-adapter-react';

const ConnectWallet = () => {
    const { connected, wallet, connect, disconnect } = useWallet();

    const handleConnect = async () => {
        try {
            await connect();
        } catch (error) {
            console.error("Failed to connect wallet:", error);
        }
    };

    const handleDisconnect = async () => {
        try {
            await disconnect();
        } catch (error) {
            console.error("Failed to disconnect wallet:", error);
        }
    };

    return (
        <div>
            {connected ? (
                <div>
                    <p>Connected with {wallet.adapter.name}</p>
                    <button onClick={handleDisconnect}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={handleConnect}>Connect Wallet</button>
            )}
        </div>
    );
};

export default ConnectWallet;
```

```javascript
// pages/index.js
import Head from 'next/head';
import ConnectWallet from '../components/ConnectWallet';

const Home = () => {
    return (
        <div>
            <Head>
                <title>AI Model Licensing</title>
                <meta name="description" content="Connect your wallet to manage AI model licensing transactions." />
            </Head>
            <main>
                <h1>Welcome to Lineage AI Model Licensing</h1>
                <ConnectWallet />
            </main>
        </div>
    );
};

export default Home;
```

```javascript
// styles/globals.css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
}

main {
    padding: 20px;
    text-align: center;
}
```

```bash
# package.json dependencies
{
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "@solana/wallet-adapter-react": "^0.13.0",
    "@solana/wallet-adapter-wallets": "^0.13.0"
  }
}
```

```bash
# To install the required packages, run:
npm install next react react-dom @solana/wallet-adapter-react @solana/wallet-adapter-wallets
```
