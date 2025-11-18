"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matamesklogu.github.io
Prompt: Generate code to integrate MetaMask into a decentralized application (dApp), ensuring compatibility with its wallet features and login functionality.
Generated: DETERMINISTIC_260ead08c6421ece
Batch ID: 20250612_155037
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

// MetaMask integration component
const MetaMaskIntegration = () => {
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    // Function to check if MetaMask is installed
    const checkMetaMaskInstalled = () => {
        return typeof window.ethereum !== 'undefined';
    };

    // Function to request account access
    const requestAccount = async () => {
        if (!checkMetaMaskInstalled()) {
            setError('MetaMask is not installed. Please install it to use this dApp.');
            return;
        }

        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]); // Set the first account
        } catch (err) {
            console.error('Error requesting accounts:', err);
            setError('Failed to connect to MetaMask. Please try again.');
        }
    };

    // Function to handle account changes
    const handleAccountChange = (accounts) => {
        if (accounts.length > 0) {
            setAccount(accounts[0]);
        } else {
            setAccount(null);
            setError('Please connect to MetaMask.');
        }
    };

    // Set up event listeners for account changes
    useEffect(() => {
        if (checkMetaMaskInstalled()) {
            window.ethereum.on('accountsChanged', handleAccountChange);
            return () => {
                window.ethereum.removeListener('accountsChanged', handleAccountChange);
            };
        }
    }, []);

    return (
        <div>
            <h1>MetaMask Integration</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                </div>
            ) : (
                <button onClick={requestAccount}>Connect to MetaMask</button>
            )}
        </div>
    );
};

export default MetaMaskIntegration;
```

This code provides a React component to integrate with MetaMask, handling account connection, error messages, and ensuring compatibility with MetaMask wallet features.
