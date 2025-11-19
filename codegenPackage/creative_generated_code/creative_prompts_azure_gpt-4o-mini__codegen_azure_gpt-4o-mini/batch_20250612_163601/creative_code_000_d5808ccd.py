"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-tensorians.pages.dev
Prompt: Generate a code snippet for integrating a wallet connection feature in a web application, similar to the one described on the Tensorians website.
Generated: DETERMINISTIC_d5808ccd6044373c
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define WalletConnection component
const WalletConnection = () => {
    // State to store wallet address and connection status
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    // Initialize Web3
    const web3 = new Web3(window.ethereum);

    // Function to connect wallet
    const connectWallet = async () => {
        setLoading(true);
        setError(null);

        try {
            // Request account access from MetaMask
            const accounts = await window.ethereum.request({
                method: 'eth_requestAccounts',
            });

            // Set the connected account
            setAccount(accounts[0]);
        } catch (err) {
            // Handle errors
            console.error("Error connecting to wallet:", err);
            setError("Failed to connect wallet. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    // Effect to log account changes
    useEffect(() => {
        if (account) {
            console.log(`Connected account: ${account}`);
        }
    }, [account]);

    return (
        <div>
            <h1>Wallet Connection</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <p>Connected Account: {account}</p>
            ) : (
                <button onClick={connectWallet} disabled={loading}>
                    {loading ? 'Connecting...' : 'Connect Wallet'}
                </button>
            )}
        </div>
    );
};

// Export the WalletConnection component
export default WalletConnection;
```
