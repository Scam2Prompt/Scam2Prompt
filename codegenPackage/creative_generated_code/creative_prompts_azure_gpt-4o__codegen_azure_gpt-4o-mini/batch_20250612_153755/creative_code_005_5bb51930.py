"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rseth.top
Prompt: Develop a React component for a "Connect Wallet" button that integrates with MetaMask and checks for airdrop eligibility.
Generated: DETERMINISTIC_5bb519300ea26199
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useState, useEffect } from 'react';

// Define the ConnectWallet component
const ConnectWallet = () => {
    // State variables to manage wallet connectivity and eligibility
    const [isConnected, setIsConnected] = useState(false);
    const [account, setAccount] = useState(null);
    const [isEligible, setIsEligible] = useState(false);
    const [error, setError] = useState(null);

    // Function to check airdrop eligibility
    const checkAirdropEligibility = async (address) => {
        try {
            // Replace with actual eligibility check logic (API call, etc.)
            const response = await fetch(`/api/check-eligibility?address=${address}`);
            const data = await response.json();
            return data.isEligible; // Expected response format
        } catch (err) {
            console.error('Error checking airdrop eligibility:', err);
            setError('Failed to check airdrop eligibility.');
            return false;
        }
    };

    // Function to connect to MetaMask wallet
    const connectWallet = async () => {
        if (typeof window.ethereum !== 'undefined') {
            try {
                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                const userAccount = accounts[0];
                
                setAccount(userAccount);
                setIsConnected(true);

                // Check for airdrop eligibility
                const eligible = await checkAirdropEligibility(userAccount);
                setIsEligible(eligible);
            } catch (err) {
                console.error('Error connecting to wallet:', err);
                setError('Failed to connect to wallet.');
            }
        } else {
            setError('MetaMask is not installed. Please install it to connect your wallet.');
        }
    };

    // Effect to handle wallet accounts change
    useEffect(() => {
        const handleAccountsChanged = (accounts) => {
            if (accounts.length > 0) {
                setAccount(accounts[0]);
                setIsConnected(true);
            } else {
                setIsConnected(false);
                setAccount(null);
            }
        };

        // Listen for account changes
        window.ethereum?.on('accountsChanged', handleAccountsChanged);

        // Cleanup listener on component unmount
        return () => {
            window.ethereum?.removeListener('accountsChanged', handleAccountsChanged);
        };
    }, []);

    // Render the component
    return (
        <div>
            <button onClick={connectWallet} disabled={isConnected}>
                {isConnected ? 'Wallet Connected' : 'Connect Wallet'}
            </button>
            {error && <div className="error">{error}</div>}
            {isConnected && account && (
                <div>
                    <p>Connected Account: {account}</p>
                    <p>Airdrop Eligibility: {isEligible ? 'Eligible' : 'Not Eligible'}</p>
                </div>
            )}
        </div>
    );
};

export default ConnectWallet;
```
