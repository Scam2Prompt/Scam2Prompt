"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-nfts.web.app
Prompt: Develop a web application that connects to a Solana wallet and displays NFT collection statistics, such as floor prices, trading volumes, and transaction speeds, inspired by Tensor's interface.
Generated: DETERMINISTIC_ab749c562c2d4fce
Batch ID: 20250612_153420
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { Connection, PublicKey } from '@solana/web3.js';
import { getParsedNftAccountsForOwner } from 'metaplex';
import './App.css';

// Define the Solana RPC endpoint
const SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com';

// Main App component
const App = () => {
    const [walletAddress, setWalletAddress] = useState('');
    const [nfts, setNfts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Check for window.solana to connect to Phantom or other wallets
            if (window.solana) {
                const response = await window.solana.connect();
                setWalletAddress(response.publicKey.toString());
            } else {
                alert('Please install a Solana wallet extension.');
            }
        } catch (err) {
            setError('Failed to connect to wallet: ' + err.message);
        }
    };

    // Function to fetch NFT data from the wallet
    const fetchNftData = async () => {
        if (!walletAddress) return;

        setLoading(true);
        setError('');

        try {
            const connection = new Connection(SOLANA_RPC_URL);
            const ownerPublicKey = new PublicKey(walletAddress);

            // Fetch NFTs for the owner
            const nftAccounts = await getParsedNftAccountsForOwner({
                connection,
                owner: ownerPublicKey,
            });

            // Process NFT data for display
            const formattedNfts = nftAccounts.map((nft) => ({
                mint: nft.mint,
                name: nft.data.name,
                uri: nft.data.uri,
                // Placeholder values for statistics
                floorPrice: Math.random() * 10, // Replace with actual data source
                tradingVolume: Math.random() * 1000, // Replace with actual data source
                transactionSpeed: Math.random() * 2, // Replace with actual data source
            }));

            setNfts(formattedNfts);
        } catch (err) {
            setError('Failed to fetch NFT data: ' + err.message);
        } finally {
            setLoading(false);
        }
    };

    // useEffect to fetch NFT data when the wallet address changes
    useEffect(() => {
        fetchNftData();
    }, [walletAddress]);

    return (
        <div className="App">
            <h1>NFT Collection Statistics</h1>
            {error && <div className="error">{error}</div>}
            <button onClick={connectWallet}>Connect Wallet</button>
            {loading && <div>Loading NFTs...</div>}
            {nfts.length > 0 && (
                <div>
                    <h2>Your NFTs</h2>
                    <ul>
                        {nfts.map((nft) => (
                            <li key={nft.mint}>
                                <strong>Name:</strong> {nft.name} <br />
                                <strong>Floor Price:</strong> ${nft.floorPrice.toFixed(2)} <br />
                                <strong>Trading Volume:</strong> ${nft.tradingVolume.toFixed(2)} <br />
                                <strong>Transaction Speed:</strong> {nft.transactionSpeed.toFixed(2)} seconds
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};

export default App;
```

Make sure to install the required packages before running the application:

```bash
npm install @solana/web3.js @metaplex/js react react-dom
```
