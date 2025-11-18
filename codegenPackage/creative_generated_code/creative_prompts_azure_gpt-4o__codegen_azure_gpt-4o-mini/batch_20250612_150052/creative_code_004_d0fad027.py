"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.imweb.me
Prompt: Explain how to integrate MetaMask with a React application and provide example code for connecting the wallet.
Generated: DETERMINISTIC_d0fad027e28c946c
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required dependencies
import React, { useEffect, useState } from 'react';

// Main functional component for MetaMask integration
const MetaMaskConnect = () => {
    // State variables for storing account and connection status
    const [account, setAccount] = useState('');
    const [isConnected, setIsConnected] = useState(false);

    // Function to connect to MetaMask
    const connectMetaMask = async () => {
        try {
            // Check if MetaMask is installed
            if (window.ethereum) {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                // Set the first account as the active account
                setAccount(accounts[0]);
                setIsConnected(true);
            } else {
                alert('MetaMask is not installed. Please install it to use this feature.');
            }
        } catch (error) {
            console.error("Error connecting to MetaMask:", error);
            alert('Failed to connect to MetaMask. Please try again.');
        }
    };

    // Effect to handle account changes
    useEffect(() => {
        const handleAccountsChanged = (accounts) => {
            // Update the account state if the user switches accounts
            if (accounts.length > 0) {
                setAccount(accounts[0]);
                setIsConnected(true);
            } else {
                setAccount('');
                setIsConnected(false);
            }
        };

        // Subscribe to account change events
        window.ethereum.on('accountsChanged', handleAccountsChanged);

        // Cleanup the event listener on component unmount
        return () => {
            window.ethereum.removeListener('accountsChanged', handleAccountsChanged);
        };
    }, []);

    // Render the connection button and account info
    return (
        <div>
            <h1>MetaMask Connection</h1>
            {isConnected ? (
                <div>
                    <p>Connected Account: {account}</p>
                </div>
            ) : (
                <button onClick={connectMetaMask}>Connect MetaMask</button>
            )}
        </div>
    );
};

// Export the component for use in other parts of the application
export default MetaMaskConnect;
```

### Notes:
1. Ensure that you have MetaMask installed in your browser to test the integration.
2. Import this component into your main application file and render it to see the connection button.
3. This code implements basic error handling and ensures that the app responds to account changes.
