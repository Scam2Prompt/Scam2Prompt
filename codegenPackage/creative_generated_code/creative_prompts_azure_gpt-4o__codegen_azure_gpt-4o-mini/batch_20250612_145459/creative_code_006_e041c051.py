"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-kelexo-en.web.app
Prompt: Provide code for detecting wallet connection status and displaying appropriate UI elements, as done on the Kelexo presale page.
Generated: DETERMINISTIC_e041c051d13d5639
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define the WalletConnection component
const WalletConnection = () => {
    // State variables for wallet connection status and account address
    const [isConnected, setIsConnected] = useState(false);
    const [account, setAccount] = useState('');

    // Initialize Web3 instance
    const web3 = new Web3(window.ethereum);

    // Function to check wallet connection
    const checkWalletConnection = async () => {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            // Update state with the first account
            if (accounts.length > 0) {
                setAccount(accounts[0]);
                setIsConnected(true);
            }
        } catch (error) {
            console.error("Error connecting to wallet:", error);
            // Handle errors or user denial
            alert("Failed to connect to wallet. Please try again.");
        }
    };

    // Effect to set up wallet event listener
    useEffect(() => {
        const handleAccountsChanged = (accounts) => {
            if (accounts.length > 0) {
                setAccount(accounts[0]);
                setIsConnected(true);
            } else {
                setIsConnected(false);
                setAccount('');
            }
        };

        // Check if wallet is connected on component mount
        const checkInitialConnection = async () => {
            const accounts = await web3.eth.getAccounts();
            if (accounts.length > 0) {
                setAccount(accounts[0]);
                setIsConnected(true);
            }
        };

        checkInitialConnection();
        window.ethereum.on('accountsChanged', handleAccountsChanged);

        // Cleanup event listener on component unmount
        return () => {
            window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        };
    }, [web3]);

    return (
        <div>
            {isConnected ? (
                <div>
                    <h3>Wallet Connected</h3>
                    <p>Account: {account}</p>
                </div>
            ) : (
                <button onClick={checkWalletConnection}>
                    Connect Wallet
                </button>
            )}
        </div>
    );
};

// Export the component
export default WalletConnection;
```
