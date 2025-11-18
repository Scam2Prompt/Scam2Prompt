"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-sale.pages.dev
Prompt: Create a front-end widget using React that integrates with Web3 to allow users to buy OMEME tokens and display their purchased and stakeable token balances.
Generated: DETERMINISTIC_a051547cb1c71136
Batch ID: 20250612_150552
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
import TokenABI from './TokenABI.json'; // Import the token contract ABI

// Define the main component
const OmemeTokenWidget = () => {
    // State variables for user address, token balance, and transaction status
    const [account, setAccount] = useState('');
    const [balance, setBalance] = useState(0);
    const [amountToBuy, setAmountToBuy] = useState('');
    const [transactionStatus, setTransactionStatus] = useState('');
    const [provider, setProvider] = useState(null);

    // Constants for the smart contract
    const TOKEN_ADDRESS = '0xYourTokenAddressHere'; // Replace with your token contract address

    // Initialize Web3 and load account information
    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                const web3 = new Web3(window.ethereum);
                setProvider(web3);
                try {
                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3.eth.getAccounts();
                    setAccount(accounts[0]);
                } catch (error) {
                    console.error("User denied account access:", error);
                    setTransactionStatus('Account access denied');
                }
            } else {
                console.error("Please install MetaMask!");
                setTransactionStatus('MetaMask is not installed');
            }
        };

        initWeb3();
    }, []);

    // Fetch token balance
    const fetchBalance = async () => {
        if (provider && account) {
            const tokenContract = new provider.eth.Contract(TokenABI, TOKEN_ADDRESS);
            try {
                const balance = await tokenContract.methods.balanceOf(account).call();
                setBalance(balance);
            } catch (error) {
                console.error("Error fetching balance:", error);
                setTransactionStatus('Error fetching balance');
            }
        }
    };

    // Handle buy token transaction
    const buyTokens = async () => {
        if (provider && account && amountToBuy) {
            const tokenContract = new provider.eth.Contract(TokenABI, TOKEN_ADDRESS);
            try {
                // Assuming the buyTokens function of the contract takes the amount as an argument
                const response = await tokenContract.methods.buyTokens(amountToBuy).send({ from: account });
                setTransactionStatus(`Transaction successful: ${response.transactionHash}`);
                fetchBalance(); // Refresh balance after transaction
            } catch (error) {
                console.error("Transaction failed:", error);
                setTransactionStatus('Transaction failed');
            }
        } else {
            setTransactionStatus('Please enter a valid amount to buy');
        }
    };

    return (
        <div>
            <h1>OMEME Token Purchase Widget</h1>
            <div>
                <p>Connected Account: {account || 'Not connected'}</p>
                <p>Your Token Balance: {ethers.utils.formatUnits(balance, 18)} OMEME</p>
                <input
                    type="number"
                    value={amountToBuy}
                    onChange={(e) => setAmountToBuy(e.target.value)}
                    placeholder="Amount of OMEME to buy"
                />
                <button onClick={buyTokens}>Buy OMEME Tokens</button>
                <p>Status: {transactionStatus}</p>
            </div>
            <button onClick={fetchBalance}>Refresh Balance</button>
        </div>
    );
};

export default OmemeTokenWidget;
```

**Note:** Replace `'0xYourTokenAddressHere'` with your actual token contract address and ensure `TokenABI.json` contains the ABI of your ERC20 token contract. Make sure to install `web3` and `ethers` libraries before running the code.
