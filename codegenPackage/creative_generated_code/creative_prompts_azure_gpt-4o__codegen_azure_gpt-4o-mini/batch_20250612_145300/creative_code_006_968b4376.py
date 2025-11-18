"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Generate code to integrate a cryptocurrency wallet connection feature into a web application, similar to the "Connect Wallet" functionality on the $MPEPE website.
Generated: DETERMINISTIC_968b43760b35003a
Batch ID: 20250612_145300
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

// Define the WalletConnect component
const WalletConnect = () => {
    // State variables for web3 and account management
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        // Check if window.ethereum is available (MetaMask)
        const loadWeb3 = async () => {
            if (window.ethereum) {
                // Create a new Web3 instance
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
            } else {
                setError("Please install MetaMask!");
            }
        };
        loadWeb3();
    }, []);

    // Function to connect to the wallet
    const connectWallet = async () => {
        try {
            // Request account access from the user
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            if (accounts.length > 0) {
                setAccount(accounts[0]); // Set the first account as the connected account
            } else {
                setError("No accounts found. Please ensure you are logged into MetaMask.");
            }
        } catch (err) {
            // Handle errors while connecting
            setError(err.message || "An error occurred while connecting to wallet.");
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setAccount(null); // Clear the connected account
    };

    return (
        <div>
            <h2>Connect Your Wallet</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>} {/* Display error messages */}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnect;
```

### Additional Notes
- Ensure that you have the `web3` library installed in your project (`npm install web3`).
- This code assumes that the user has a compatible wallet (such as MetaMask) installed in their browser.
- The code handles connection errors and provides user feedback through error messages.
