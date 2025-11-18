"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiazbsbbbs4ntqynyozaijhga7yzkdbfblauzwoqq6kysfzfxn2dyi.ipfs.dweb.link
Prompt: Provide an example of using MetaMask's API to connect a wallet and verify the user's account address.
Generated: DETERMINISTIC_99dc85117231c081
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import React, { useEffect, useState } from 'react';

const App = () => {
    // State variables to hold wallet connection status and user account
    const [isConnected, setIsConnected] = useState(false);
    const [userAccount, setUserAccount] = useState('');

    // Function to connect to MetaMask and retrieve the user's account
    const connectWallet = async () => {
        // Check if MetaMask is installed
        if (window.ethereum) {
            try {
                // Request account access from the user
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Set the user's account and mark as connected
                setUserAccount(accounts[0]);
                setIsConnected(true);
            } catch (error) {
                // Handle errors (e.g., user denying access)
                console.error("Error connecting to MetaMask:", error);
                alert("Failed to connect to MetaMask. Please try again.");
            }
        } else {
            // MetaMask not installed
            alert("Please install MetaMask to use this feature.");
        }
    };

    // Effect to handle account changes and connection status
    useEffect(() => {
        const checkConnection = async () => {
            if (window.ethereum) {
                // Check if user is already connected
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setUserAccount(accounts[0]);
                    setIsConnected(true);
                }
            }
        };

        checkConnection();

        // Listen for account changes
        window.ethereum.on('accountsChanged', (accounts) => {
            if (accounts.length > 0) {
                setUserAccount(accounts[0]);
            } else {
                setIsConnected(false);
                setUserAccount('');
            }
        });

        return () => {
            // Cleanup listener on component unmount
            window.ethereum.removeListener('accountsChanged', () => {});
        };
    }, []);

    return (
        <div>
            <h1>MetaMask Wallet Connection</h1>
            {isConnected ? (
                <div>
                    <p>Connected Account: {userAccount}</p>
                    <button onClick={() => setIsConnected(false)}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect MetaMask</button>
            )}
        </div>
    );
};

export default App;
```
