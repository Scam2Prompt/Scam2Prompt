"""
Generated Code Metadata:
========================
Original URL: https://monadmakeyournft.vercel.app
Prompt: Write code to integrate wallet connection and disconnection features in a web application similar to Monad Whiteboard NFT.
Generated: DETERMINISTIC_7cd4262c5a59d166
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define the WalletConnector component
const WalletConnector = () => {
    // State to manage wallet connection status and account
    const [isConnected, setIsConnected] = useState(false);
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);

    // Effect to check if the wallet is already connected
    useEffect(() => {
        const checkWalletConnection = async () => {
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
                const accounts = await web3Instance.eth.getAccounts();
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                    setIsConnected(true);
                }
            } else {
                console.error("Ethereum wallet not detected. Please install MetaMask.");
            }
        };
        checkWalletConnection();
    }, []);

    // Function to connect to the wallet
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]);
                setIsConnected(true);
            } catch (error) {
                console.error("User denied account access or error occurred:", error);
            }
        } else {
            console.error("Ethereum wallet not detected. Please install MetaMask.");
        }
    };

    // Function to disconnect the wallet
    const disconnectWallet = () => {
        setAccount(null);
        setIsConnected(false);
    };

    return (
        <div>
            <h1>Wallet Connection</h1>
            {isConnected ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

export default WalletConnector;
```

### Notes:
- Ensure you have the `web3` library installed in your project. You can install it using `npm install web3`.
- This code assumes that the user has a compatible Ethereum wallet (like MetaMask) installed in their browser.
- The component handles wallet connection and disconnection, providing feedback to the user.
