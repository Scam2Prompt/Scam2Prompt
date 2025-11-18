"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fastyield.app
Prompt: Suggest best practices for building a "Connect Wallet" functionality for a blockchain application similar to FastYield.
Generated: DETERMINISTIC_9145875dc89b5e23
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';
import { useState, useEffect } from 'react';

// Custom hook to handle wallet connection
const useWalletConnection = () => {
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);
    const [web3, setWeb3] = useState(null);

    // Function to connect to the wallet
    const connectWallet = async () => {
        if (window.ethereum) {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Set the first account from the returned array
                setAccount(accounts[0]);
                // Initialize web3 instance
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
            } catch (err) {
                // Handle error during wallet connection
                setError('Could not connect to wallet. Please ensure wallet is installed and accessible.');
                console.error(err);
            }
        } else {
            // Handle case where Ethereum provider is not available
            setError('MetaMask is not installed. Please install it to use this feature.');
        }
    };

    // Function to disconnect wallet
    const disconnectWallet = () => {
        setAccount(null);
        setWeb3(null);
    };

    // Effect to handle wallet disconnection
    useEffect(() => {
        const handleAccountsChanged = (accounts) => {
            if (accounts.length === 0) {
                disconnectWallet();
            } else {
                setAccount(accounts[0]);
            }
        };

        // Add listener for account changes
        window.ethereum?.on('accountsChanged', handleAccountsChanged);

        // Cleanup listener on component unmount
        return () => {
            window.ethereum?.removeListener('accountsChanged', handleAccountsChanged);
        };
    }, []);

    return {
        account,
        connectWallet,
        disconnectWallet,
        error,
        web3,
    };
};

// React component to render the Connect Wallet button
const ConnectWalletButton = () => {
    const { account, connectWallet, disconnectWallet, error } = useWalletConnection();

    return (
        <div>
            {error && <div style={{ color: 'red' }}>{error}</div>}
            {account ? (
                <div>
                    <p>Connected: {account}</p>
                    <button onClick={disconnectWallet}>Disconnect Wallet</button>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
        </div>
    );
};

// Export the ConnectWalletButton component for use in the application
export default ConnectWalletButton;
```
