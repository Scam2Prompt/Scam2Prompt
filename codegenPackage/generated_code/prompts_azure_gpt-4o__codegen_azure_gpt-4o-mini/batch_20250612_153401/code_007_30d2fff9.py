"""
Generated Code Metadata:
========================
Original URL: https://solgotchi.vercel.app
Prompt: Provide a step-by-step guide to integrate Solana blockchain functionality into a web application for managing "Gotchis" as described on the Solgotchi site.
Generated: DETERMINISTIC_30d2fff9f7506fcb
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletAdapterNetwork } from '@solana/wallet-adapter-base';
import {
    WalletProvider,
    ConnectionProvider,
} from '@solana/wallet-adapter-react';
import {
    PhantomWalletAdapter,
    SolletWalletAdapter,
} from '@solana/wallet-adapter-wallets';
import React, { useEffect, useMemo, useState } from 'react';
import ReactDOM from 'react-dom';

// Define the network to connect to
const network = WalletAdapterNetwork.Devnet;

// Create a connection to the Solana cluster
const connection = new Connection(clusterApiUrl(network), 'confirmed');

// Define the App component
const App = () => {
    const [gotchis, setGotchis] = useState([]);

    // Fetch Gotchis from the blockchain
    const fetchGotchis = async () => {
        try {
            // Replace with the actual logic to fetch Gotchis
            const gotchiData = await connection.getParsedProgramAccounts(
                new PublicKey('YOUR_GOTCHI_PROGRAM_ID')
            );
            setGotchis(gotchiData);
        } catch (error) {
            console.error('Error fetching Gotchis:', error);
        }
    };

    // Use effect to fetch Gotchis on component mount
    useEffect(() => {
        fetchGotchis();
    }, []);

    return (
        <div>
            <h1>Gotchi Manager</h1>
            <ul>
                {gotchis.map((gotchi, index) => (
                    <li key={index}>
                        {/* Render Gotchi details */}
                        <pre>{JSON.stringify(gotchi.account.data, null, 2)}</pre>
                    </li>
                ))}
            </ul>
        </div>
    );
};

// Main entry point of the application
const Main = () => {
    // Define the wallets to be used
    const wallets = useMemo(() => [
        new PhantomWalletAdapter(),
        new SolletWalletAdapter(),
    ], []);

    return (
        <ConnectionProvider connection={connection}>
            <WalletProvider wallets={wallets} autoConnect>
                <App />
            </WalletProvider>
        </ConnectionProvider>
    );
};

// Render the application
ReactDOM.render(<Main />, document.getElementById('root'));
```

### Notes:
- Replace `'YOUR_GOTCHI_PROGRAM_ID'` with the actual program ID for the Gotchi smart contract.
- Ensure you have the necessary dependencies installed in your project:
  ```bash
  npm install @solana/web3.js @solana/wallet-adapter-react @solana/wallet-adapter-wallets
  ```
- This code assumes you have a basic React setup. Make sure to adjust the HTML file to include a root element with `id="root"`.
