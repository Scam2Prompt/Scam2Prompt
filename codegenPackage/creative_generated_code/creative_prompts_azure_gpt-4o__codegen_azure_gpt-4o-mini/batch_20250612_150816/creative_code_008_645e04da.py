"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-realio.network
Prompt: Provide an example of integrating MetaMask's card functionality to enable users to spend crypto for daily purchases directly from their wallet.
Generated: DETERMINISTIC_645e04dacd3f619b
Batch ID: 20250612_150816
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
import { ethers } from 'ethers';

// Set up the MetaMask provider
const web3 = new Web3(window.ethereum);

// Main component for integrating MetaMask functionality
const MetaMaskPayment = () => {
    // State variables
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState('0');
    const [loading, setLoading] = useState(true);

    // Function to connect to MetaMask
    const connectWallet = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
            await fetchBalance(accounts[0]);
        } catch (error) {
            console.error("Error connecting to wallet:", error);
            alert("Failed to connect to MetaMask. Please ensure MetaMask is installed and try again.");
        }
    };

    // Function to fetch the balance of the connected account
    const fetchBalance = async (account) => {
        try {
            const balance = await web3.eth.getBalance(account);
            setBalance(web3.utils.fromWei(balance, 'ether'));
        } catch (error) {
            console.error("Error fetching balance:", error);
            alert("Failed to fetch balance. Please try again later.");
        } finally {
            setLoading(false);
        }
    };

    // Function to handle payment
    const handlePayment = async (amount) => {
        if (!account) {
            alert("Please connect your wallet first!");
            return;
        }

        const amountInWei = web3.utils.toWei(amount.toString(), 'ether');
        const transactionParameters = {
            to: 'recipient-address-here', // Replace with the recipient's address
            from: account,
            value: amountInWei,
        };

        try {
            // Request sending the transaction through MetaMask
            await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });
            alert("Payment successful!");
        } catch (error) {
            console.error("Error sending transaction:", error);
            alert("Transaction failed. Please check your funds and try again.");
        }
    };

    // Effect to check if MetaMask is connected
    useEffect(() => {
        const checkIfWalletIsConnected = async () => {
            if (window.ethereum) {
                const accounts = await window.ethereum.request({ method: 'eth_accounts' });
                if (accounts.length > 0) {
                    setAccount(accounts[0]);
                    await fetchBalance(accounts[0]);
                }
                setLoading(false);
            } else {
                alert("Please install MetaMask.");
                setLoading(false);
            }
        };
        checkIfWalletIsConnected();
    }, []);

    // Render component
    return (
        <div>
            <h1>MetaMask Payment Integration</h1>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <>
                    <p>Connected Account: {account}</p>
                    <p>Balance: {balance} ETH</p>
                    <button onClick={connectWallet}>Connect Wallet</button>
                    <button onClick={() => handlePayment(0.01)}>Pay 0.01 ETH</button>
                </>
            )}
        </div>
    );
};

export default MetaMaskPayment;
```
