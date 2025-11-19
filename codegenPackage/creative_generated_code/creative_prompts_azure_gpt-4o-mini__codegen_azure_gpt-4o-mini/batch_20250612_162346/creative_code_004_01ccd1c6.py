"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-srunexyz.pages.dev
Prompt: Illustrate how to implement a wallet connection feature in a DApp for users to buy $SRUNE tokens during the presale.
Generated: DETERMINISTIC_01ccd1c60dca287f
Batch ID: 20250612_162346
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
import Web3 from 'web3';

// Contract ABI and Address
const CONTRACT_ABI = [/* ABI goes here */];
const CONTRACT_ADDRESS = '0xYourContractAddressHere';

// Wallet Connection Component
const WalletConnect = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [contract, setContract] = useState(null);
    const [amount, setAmount] = useState(0);
    const [error, setError] = useState('');

    // Initialize Web3 instance and contract
    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                try {
                    // Request account access if needed
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const web3Instance = new Web3(window.ethereum);
                    const contractInstance = new web3Instance.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
                    
                    setWeb3(web3Instance);
                    setContract(contractInstance);
                    
                    // Get current account
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                } catch (error) {
                    setError('Failed to connect to wallet. Please install MetaMask.');
                }
            } else {
                setError('Ethereum wallet not found. Please install MetaMask.');
            }
        };

        initWeb3();
    }, []);

    // Function to buy $SRUNE tokens
    const buyTokens = async () => {
        if (!contract || !account) {
            setError('Wallet not connected or contract not initialized.');
            return;
        }

        try {
            const value = web3.utils.toWei(amount.toString(), 'ether'); // Convert amount to wei
            await contract.methods.buyTokens().send({ from: account, value });
            alert('Tokens purchased successfully!');
        } catch (error) {
            setError('Transaction failed. Please try again.');
            console.error(error);
        }
    };

    return (
        <div>
            <h1>Buy $SRUNE Tokens</h1>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <div>
                <strong>Connected Account: </strong>{account || 'Not connected'}
            </div>
            <input
                type="number"
                placeholder="Enter amount in ETH"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
            />
            <button onClick={buyTokens}>Buy Tokens</button>
        </div>
    );
};

export default WalletConnect;
```

This code snippet provides a simple React component that connects to an Ethereum wallet, allowing users to buy $SRUNE tokens during a presale. Please replace placeholders with actual ABI and contract address and ensure that proper testing and security practices are followed before deployment.
