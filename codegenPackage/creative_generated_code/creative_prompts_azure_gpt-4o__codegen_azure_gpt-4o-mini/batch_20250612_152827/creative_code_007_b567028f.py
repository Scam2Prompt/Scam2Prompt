"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://riftproject.pages.dev
Prompt: Create a React component that connects to a wallet and displays $RIFT token rewards and referral statistics from the Rift Swap platform.
Generated: DETERMINISTIC_b567028ffc3800c9
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';

// Define the RIFT token contract ABI and address (replace with actual values)
const RIFT_TOKEN_ABI = [
    // ABI details go here
];
const RIFT_TOKEN_ADDRESS = '0x...'; // Replace with actual RIFT token contract address

const WalletConnection = () => {
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState(0);
    const [referralStats, setReferralStats] = useState(null);
    const [error, setError] = useState(null);

    // Initialize Web3 or ethers provider
    const initWeb3 = async () => {
        if (window.ethereum) {
            window.web3 = new Web3(window.ethereum);
            await window.ethereum.request({ method: 'eth_requestAccounts' });
        } else {
            setError('Please install MetaMask or another wallet provider.');
        }
    };

    // Fetch RIFT token balance for the connected account
    const fetchTokenBalance = async (account) => {
        try {
            const contract = new window.web3.eth.Contract(RIFT_TOKEN_ABI, RIFT_TOKEN_ADDRESS);
            const balance = await contract.methods.balanceOf(account).call();
            setBalance(window.web3.utils.fromWei(balance, 'ether'));
        } catch (err) {
            setError('Error fetching token balance: ' + err.message);
        }
    };

    // Fetch referral statistics (replace with actual API or contract method)
    const fetchReferralStatistics = async (account) => {
        try {
            // Replace with actual logic to fetch referral statistics
            const stats = {
                totalReferrals: 10, // Dummy data
                rewardsEarned: 5,   // Dummy data
            };
            setReferralStats(stats);
        } catch (err) {
            setError('Error fetching referral statistics: ' + err.message);
        }
    };

    // Connect to wallet and fetch data
    const connectWallet = async () => {
        await initWeb3();
        const accounts = await window.web3.eth.getAccounts();
        if (accounts.length > 0) {
            setAccount(accounts[0]);
            await fetchTokenBalance(accounts[0]);
            await fetchReferralStatistics(accounts[0]);
        } else {
            setError('No accounts found. Please ensure your wallet is unlocked.');
        }
    };

    useEffect(() => {
        if (account) {
            fetchTokenBalance(account);
            fetchReferralStatistics(account);
        }
    }, [account]);

    return (
        <div>
            <h1>Rift Swap Wallet Connection</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {!account ? (
                <button onClick={connectWallet}>Connect Wallet</button>
            ) : (
                <div>
                    <p>Connected Account: {account}</p>
                    <p>RIFT Token Balance: {balance} RIFT</p>
                    {referralStats && (
                        <div>
                            <h2>Referral Statistics</h2>
                            <p>Total Referrals: {referralStats.totalReferrals}</p>
                            <p>Rewards Earned: {referralStats.rewardsEarned} RIFT</p>
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default WalletConnection;
```
