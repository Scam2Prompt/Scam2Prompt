"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Create a function in TypeScript that retrieves the user's blockchain account details and displays them, referencing the Dapp Starter's integration of Web3 React.
Generated: DETERMINISTIC_a4a22b9d124bc9cb
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Define a type for the account details
interface AccountDetails {
    address: string;
    balance: string;
}

// Create a functional component to retrieve and display blockchain account details
const AccountInfo: React.FC = () => {
    // State to hold account details
    const [accountDetails, setAccountDetails] = useState<AccountDetails | null>(null);
    const [error, setError] = useState<string | null>(null);

    // Function to fetch account details
    const fetchAccountDetails = async () => {
        try {
            // Check if Web3 is injected (e.g., by MetaMask)
            if (window.ethereum) {
                const web3 = new Web3(window.ethereum);
                
                // Request account access if needed
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                
                // Get the user's accounts
                const accounts = await web3.eth.getAccounts();
                if (accounts.length === 0) {
                    throw new Error('No accounts found. Please ensure you are logged in to your wallet.');
                }

                // Get the balance of the first account
                const balance = await web3.eth.getBalance(accounts[0]);
                
                // Update state with account details
                setAccountDetails({
                    address: accounts[0],
                    balance: web3.utils.fromWei(balance, 'ether'), // Convert balance from Wei to Ether
                });
            } else {
                throw new Error('Web3 is not injected. Please install MetaMask or another wallet provider.');
            }
        } catch (err) {
            // Handle errors and update state
            setError(err instanceof Error ? err.message : 'An unknown error occurred.');
        }
    };

    // Use effect to fetch account details on component mount
    useEffect(() => {
        fetchAccountDetails();
    }, []);

    return (
        <div>
            <h1>Account Information</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {accountDetails ? (
                <div>
                    <p><strong>Address:</strong> {accountDetails.address}</p>
                    <p><strong>Balance:</strong> {accountDetails.balance} ETH</p>
                </div>
            ) : (
                <p>Loading account details...</p>
            )}
        </div>
    );
};

export default AccountInfo;
```
