"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrica17.vercel.app
Prompt: Provide an example of using Ethereum for login functionality in a decentralized application.
Generated: DETERMINISTIC_92eeaecff0661612
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing necessary libraries
import React, { useState } from 'react';
import Web3 from 'web3';

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// React component for the login functionality
const EthLogin = () => {
    const [account, setAccount] = useState(null);
    const [errorMessage, setErrorMessage] = useState('');

    const connectWallet = async () => {
        try {
            // Request account access from the user
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]); // Set the first account as the logged-in account
            setErrorMessage(''); // Clear any previous error messages
        } catch (error) {
            // Handle if the user rejects the request
            if (error.code === 4001) {
                setErrorMessage('User denied account access');
            } else {
                setErrorMessage('An error occurred while connecting to the wallet');
            }
        }
    };

    return (
        <div>
            <h2>Login with Ethereum</h2>
            {account ? (
                <div>
                    <p>Logged in as: {account}</p>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect Wallet</button>
            )}
            {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
        </div>
    );
};

export default EthLogin;
```

Make sure you have the `react` and `web3` libraries installed in your project. You can run this example in a React application to enable Ethereum wallet-based login functionality.
