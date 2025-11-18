"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Generate a Web3 React hook to listen for wallet connection events and update the UI with the connected account's balance and Chain ID.
Generated: DETERMINISTIC_3d7b6113a0c99272
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import { useEffect, useState } from 'react';
import Web3 from 'web3';

// Custom hook to manage wallet connection and balance retrieval
const useWalletConnection = () => {
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState(null);
    const [chainId, setChainId] = useState(null);
    const [error, setError] = useState(null);
    const [web3, setWeb3] = useState(null);

    useEffect(() => {
        // Initialize Web3 instance
        const initWeb3 = async () => {
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);

                try {
                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    await updateAccountAndBalance(web3Instance);
                } catch (err) {
                    setError('User denied account access');
                    console.error(err);
                }

                // Listen for account changes
                window.ethereum.on('accountsChanged', async () => {
                    await updateAccountAndBalance(web3Instance);
                });

                // Listen for chain changes
                window.ethereum.on('chainChanged', async () => {
                    await updateAccountAndBalance(web3Instance);
                });

            } else {
                setError('Please install MetaMask!');
            }
        };

        initWeb3();

        return () => {
            // Clean up listeners on unmount
            if (window.ethereum) {
                window.ethereum.removeListener('accountsChanged', () => {});
                window.ethereum.removeListener('chainChanged', () => {});
            }
        };
    }, []);

    // Function to update account and balance
    const updateAccountAndBalance = async (web3Instance) => {
        try {
            const accounts = await web3Instance.eth.getAccounts();
            if (accounts.length > 0) {
                const selectedAccount = accounts[0];
                const balanceWei = await web3Instance.eth.getBalance(selectedAccount);
                const balanceEth = web3Instance.utils.fromWei(balanceWei, 'ether');

                setAccount(selectedAccount);
                setBalance(balanceEth);
                setChainId(await web3Instance.eth.getChainId());
            } else {
                setAccount(null);
                setBalance(null);
                setChainId(null);
            }
        } catch (err) {
            setError('Failed to fetch account or balance');
            console.error(err);
        }
    };

    return { account, balance, chainId, error };
};

export default useWalletConnection;
```

### Usage
```javascript
import React from 'react';
import useWalletConnection from './useWalletConnection';

const WalletInfo = () => {
    const { account, balance, chainId, error } = useWalletConnection();

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h3>Wallet Information</h3>
            <p>Account: {account}</p>
            <p>Balance: {balance} ETH</p>
            <p>Chain ID: {chainId}</p>
        </div>
    );
};

export default WalletInfo;
```
