"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kyrios.finance
Prompt: Provide an example of code that enables users to connect their MetaMask wallet to a blockchain-based app, like the one on Kyrios Finance.
Generated: DETERMINISTIC_5d8b5a3829480af1
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the required libraries
import React, { useEffect, useState } from 'react';

// MetaMask connection component
const MetaMaskConnect = () => {
    // State to hold account information
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    // Function to connect to MetaMask
    const connectMetaMask = async () => {
        if (typeof window.ethereum !== 'undefined') {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                setAccount(accounts[0]); // Set the first account
                setError(null); // Clear any previous errors
            } catch (err) {
                // Handle user rejecting the request or other errors
                console.error('Error connecting to MetaMask:', err);
                setError('Failed to connect to MetaMask. Please try again.');
            }
        } else {
            setError('MetaMask is not installed. Please install it to connect.');
        }
    };

    // Function to handle account changes
    const handleAccountChange = (accounts) => {
        if (accounts.length > 0) {
            setAccount(accounts[0]);
        } else {
            // Handle case when user disconnects
            setAccount(null);
        }
    };

    // Effect to listen for account changes
    useEffect(() => {
        // Check if MetaMask is available
        if (window.ethereum) {
            window.ethereum.on('accountsChanged', handleAccountChange);
        }

        // Cleanup listener on component unmount
        return () => {
            if (window.ethereum) {
                window.ethereum.removeListener('accountsChanged', handleAccountChange);
            }
        };
    }, []);

    return (
        <div>
            <h1>Connect to MetaMask</h1>
            <button onClick={connectMetaMask}>
                {account ? 'Connected: ' + account : 'Connect MetaMask'}
            </button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default MetaMaskConnect;
```
