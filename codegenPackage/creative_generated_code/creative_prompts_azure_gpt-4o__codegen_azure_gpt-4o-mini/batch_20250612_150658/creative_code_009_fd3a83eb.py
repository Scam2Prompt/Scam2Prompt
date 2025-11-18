"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-ether.com
Prompt: Explain how to use MetaMask's SDK to build a secure dashboard for managing multiple crypto accounts and assets in a web application.
Generated: DETERMINISTIC_fd3a83eba977d323
Batch ID: 20250612_150658
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
import Web3 from 'web3'; // Web3.js for Ethereum integration
import MetaMaskOnboarding from '@metamask/onboarding'; // MetaMask onboarding package

// Define constants
const ONBOARDING_V2 = 'Onboarding'; // Onboarding variable for MetaMask
const ACCOUNT_CHANGE_EVENT = 'accountsChanged'; // Event for account changes
const NETWORK_CHANGE_EVENT = 'chainChanged'; // Event for network changes

const App = () => {
    // State variables for managing account and balance
    const [accounts, setAccounts] = useState([]);
    const [balance, setBalance] = useState('0');
    const [loading, setLoading] = useState(true);
    const [web3, setWeb3] = useState(null);

    // Effect to initialize MetaMask onboarding
    useEffect(() => {
        const onboarding = new MetaMaskOnboarding();
        
        // Check if MetaMask is installed
        if (MetaMaskOnboarding.isMetaMaskInstalled()) {
            // Initialize Web3 instance
            const web3Instance = new Web3(window.ethereum);
            setWeb3(web3Instance);
            loadAccountData(web3Instance);
            
            // Add event listeners for account and network changes
            window.ethereum.on(ACCOUNT_CHANGE_EVENT, () => loadAccountData(web3Instance));
            window.ethereum.on(NETWORK_CHANGE_EVENT, () => loadAccountData(web3Instance));
        } else {
            // Start onboarding process if MetaMask is not installed
            onboarding.startOnboarding();
        }
    }, []);
    
    // Function to load account data
    const loadAccountData = async (web3Instance) => {
        try {
            setLoading(true);
            // Fetch accounts
            const userAccounts = await web3Instance.eth.getAccounts();
            setAccounts(userAccounts);

            // Fetch balance for the first account
            if (userAccounts.length > 0) {
                const balanceWei = await web3Instance.eth.getBalance(userAccounts[0]);
                setBalance(web3Instance.utils.fromWei(balanceWei, 'ether'));
            } else {
                setBalance('0');
            }
        } catch (error) {
            console.error('Error loading account data:', error);
            alert('An error occurred while loading account data. Please check the console for more details.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Crypto Dashboard</h1>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <div>
                    <h2>Your Accounts:</h2>
                    <ul>
                        {accounts.map((account, index) => (
                            <li key={index}>{account}</li>
                        ))}
                    </ul>
                    <h3>Balance: {balance} ETH</h3>
                </div>
            )}
        </div>
    );
};

export default App;
```
