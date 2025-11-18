"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Write a Next.js component that integrates MetaMask for connecting a crypto wallet and displays the user's account balance using Web3 React.
Generated: DETERMINISTIC_80718b2c4e6f1916
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks from React and Web3 React
import React, { useEffect } from 'react';
import { useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import { ethers } from 'ethers';

// Create an injected connector for MetaMask
const injected = new InjectedConnector({});

const WalletConnector = () => {
    const { activate, account, library, chainId, active, error } = useWeb3React();

    // Function to connect to MetaMask
    const connectWallet = async () => {
        try {
            await activate(injected);
        } catch (err) {
            console.error("Error connecting to wallet:", err);
        }
    };

    // Function to fetch the account balance
    const fetchBalance = async () => {
        if (account && library) {
            try {
                const balance = await library.getBalance(account);
                return ethers.utils.formatEther(balance); // Convert balance to Ether
            } catch (err) {
                console.error("Error fetching balance:", err);
            }
        }
        return null;
    };

    // State variable to hold the balance
    const [balance, setBalance] = React.useState(null);

    // Effect to fetch balance when account or library changes
    useEffect(() => {
        const getBalance = async () => {
            const fetchedBalance = await fetchBalance();
            setBalance(fetchedBalance);
        };
        
        if (active) {
            getBalance();
        }
    }, [active, account, library]);

    return (
        <div>
            <h1>Connect Your Wallet</h1>
            {error && <p className="error">Error: {error.message}</p>}
            {active ? (
                <>
                    <p>Connected Account: {account}</p>
                    <p>Chain ID: {chainId}</p>
                    <p>Balance: {balance ? `${balance} ETH` : 'Fetching...'}</p>
                </>
            ) : (
                <button onClick={connectWallet}>Connect MetaMask</button>
            )}
        </div>
    );
};

export default WalletConnector;
```
