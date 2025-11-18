"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-guard.web.app
Prompt: Generate code using ethers.js to detect a wallet connection and display a confirmation message, replicating the user flow on PantherGuard.
Generated: DETERMINISTIC_894170e81c5c51ae
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import { ethers } from "ethers"; // Ethers.js for interacting with Ethereum blockchain
import React, { useEffect, useState } from "react"; // React for building UI

// Main component to handle wallet connection
const WalletConnection = () => {
    // State to manage wallet address and connection status
    const [walletAddress, setWalletAddress] = useState(null);
    const [error, setError] = useState(null);

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Check if the browser has Ethereum provider (MetaMask)
            if (!window.ethereum) {
                throw new Error("No Ethereum wallet found. Please install MetaMask.");
            }

            // Request wallet connection
            const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
            setWalletAddress(accounts[0]);
        } catch (err) {
            // Handle errors and display them to the user
            console.error(err);
            setError(err.message);
        }
    };

    // Effect to check if the wallet is already connected on component mount
    useEffect(() => {
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: "eth_accounts" });
                if (accounts.length > 0) {
                    setWalletAddress(accounts[0]);
                }
            }
        };

        checkWalletConnection();
    }, []);

    return (
        <div>
            <h1>Connect Your Wallet</h1>
            {error && <p style={{ color: "red" }}>{error}</p>}
            {walletAddress ? (
                <p>Connected as: {walletAddress}</p>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnection;
```
