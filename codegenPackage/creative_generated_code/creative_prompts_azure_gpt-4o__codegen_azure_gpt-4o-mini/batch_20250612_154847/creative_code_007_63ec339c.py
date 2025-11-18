"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-badge.vercel.app
Prompt: Demonstrate how to integrate SuiBadge functionality into a web application with wallet support.
Generated: DETERMINISTIC_63ec339cf6fcff7b
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and modules
import React, { useEffect, useState } from 'react';
import { SuiBadge, WalletProvider, useWallet } from '@sui/badge-sdk';
import { Web3Provider } from '@ethersproject/providers';
import { ethers } from 'ethers';

// App Component
const App = () => {
    // State to hold badge information
    const [badgeData, setBadgeData] = useState(null);
    const [loading, setLoading] = useState(true);
    const { wallet, connect, disconnect } = useWallet();

    // Effect to fetch badge data on mount
    useEffect(() => {
        const fetchBadgeData = async () => {
            try {
                if (wallet) {
                    const provider = new Web3Provider(wallet);
                    const badge = new SuiBadge(provider);
                    const data = await badge.getBadges(wallet.address);
                    setBadgeData(data);
                }
            } catch (error) {
                console.error("Error fetching badge data:", error);
                setBadgeData(null);
            } finally {
                setLoading(false);
            }
        };

        fetchBadgeData();
    }, [wallet]);

    // Connect wallet function
    const handleConnectWallet = async () => {
        try {
            await connect();
        } catch (error) {
            console.error("Error connecting wallet:", error);
        }
    };

    // Disconnect wallet function
    const handleDisconnectWallet = async () => {
        try {
            await disconnect();
        } catch (error) {
            console.error("Error disconnecting wallet:", error);
        }
    };

    return (
        <div>
            <h1>SuiBadge Integration</h1>
            {!wallet ? (
                <button onClick={handleConnectWallet}>Connect Wallet</button>
            ) : (
                <button onClick={handleDisconnectWallet}>Disconnect Wallet</button>
            )}
            {loading ? (
                <p>Loading badge data...</p>
            ) : badgeData ? (
                <div>
                    <h2>Your Badges:</h2>
                    <ul>
                        {badgeData.map((badge) => (
                            <li key={badge.id}>{badge.name}</li>
                        ))}
                    </ul>
                </div>
            ) : (
                <p>No badges found or there was an error.</p>
            )}
        </div>
    );
};

// Main entry point of the application
const Main = () => {
    return (
        <WalletProvider>
            <App />
        </WalletProvider>
    );
};

// Export the main component
export default Main;
```
