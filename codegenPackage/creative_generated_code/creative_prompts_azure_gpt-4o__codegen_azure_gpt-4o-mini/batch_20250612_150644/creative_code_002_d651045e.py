"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-spark.com
Prompt: Generate code to create a walletless dapp using the MetaMask Delegation Toolkit.
Generated: DETERMINISTIC_d651045ed581646f
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries and packages
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { DelegationToolkit } from '@metamask/delegation-toolkit';

// Define the main DApp component
const WalletlessDApp = () => {
    // State variables to manage user information and error messages
    const [account, setAccount] = useState(null);
    const [error, setError] = useState(null);

    // Initialize the Delegation Toolkit
    const delegationToolkit = new DelegationToolkit();

    // Function to connect to the MetaMask Delegation Toolkit
    const connectDApp = async () => {
        try {
            // Request connection to the user's wallet using the Delegation Toolkit
            const { accounts } = await delegationToolkit.request({ method: 'wallet_requestPermissions', params: [{ eth_accounts: {} }] });

            if (accounts.length > 0) {
                setAccount(accounts[0]); // Set the connected account
            } else {
                throw new Error('No account found');
            }
        } catch (err) {
            // Handle errors and set appropriate messages
            setError(err.message);
        }
    };

    // Function to disconnect the wallet
    const disconnectDApp = () => {
        setAccount(null);
        setError(null);
    };

    // Effect hook to handle side effects and cleanup
    useEffect(() => {
        // Cleanup function on component unmount to disconnect
        return () => {
            disconnectDApp();
        };
    }, []);

    // Render the component
    return (
        <div>
            <h1>Walletless DApp using MetaMask Delegation Toolkit</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {account ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <button onClick={disconnectDApp}>Disconnect</button>
                </div>
            ) : (
                <button onClick={connectDApp}>Connect Wallet</button>
            )}
        </div>
    );
};

// Render the WalletlessDApp component to the DOM
const rootElement = document.getElementById("root");
if (rootElement) {
    ReactDOM.render(<WalletlessDApp />, rootElement);
} else {
    console.error('Root element not found');
}
```

### Instructions:
1. Ensure you have React and ethers.js as dependencies in your project.
2. Install the MetaMask Delegation Toolkit by running `npm install @metamask/delegation-toolkit`.
3. Place this code in a file (e.g., `WalletlessDApp.js`) and import it into your main application file.
4. Make sure to have a `<div id="root"></div>` in your HTML file where this React app will be mounted. 

### Error Handling:
- Error messages are displayed if there’s an issue during account connection.
- The account state resets upon disconnection and handles cleanup on component unmount.
