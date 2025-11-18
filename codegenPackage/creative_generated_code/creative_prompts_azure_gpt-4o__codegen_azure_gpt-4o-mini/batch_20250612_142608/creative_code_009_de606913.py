"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wap.xushuishiwu.cn
Prompt: Create a tutorial for integrating MetaMask wallet functionality into a React application, including token management and transaction execution, based on the "MetaMask钱包和imToken钱包" comparison section.
Generated: DETERMINISTIC_de606913a51e70f6
Batch ID: 20250612_142608
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and hooks
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

const App = () => {
    // State for managing wallet connection and token balance
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState(0);
    const [web3, setWeb3] = useState(null);

    // Initialize web3 and connect to MetaMask
    useEffect(() => {
        const initWeb3 = async () => {
            if (window.ethereum) {
                try {
                    // Create a new instance of Web3
                    const web3Instance = new Web3(window.ethereum);
                    setWeb3(web3Instance);

                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });

                    // Get the user's account
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);

                    // Fetch the account balance
                    fetchBalance(accounts[0], web3Instance);
                } catch (error) {
                    console.error("User denied account access or error occurred:", error);
                }
            } else {
                console.error("MetaMask is not installed!");
            }
        };

        initWeb3();
    }, []);

    // Fetch the balance of the user's account
    const fetchBalance = async (account, web3Instance) => {
        try {
            const balance = await web3Instance.eth.getBalance(account);
            setBalance(web3Instance.utils.fromWei(balance, 'ether'));
        } catch (error) {
            console.error("Error fetching balance:", error);
        }
    };

    // Function to execute a transaction
    const sendTransaction = async (recipient, amount) => {
        if (!web3 || !account) {
            console.error("Web3 or account not initialized.");
            return;
        }

        const transactionParameters = {
            to: recipient, // The address to send to
            from: account, // The user's account address
            value: web3.utils.toHex(web3.utils.toWei(amount, 'ether')), // Amount to send in wei
        };

        try {
            // Send the transaction
            await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters],
            });

            console.log("Transaction sent!");
        } catch (error) {
            console.error("Transaction failed:", error);
        }
    };

    return (
        <div>
            <h1>MetaMask Integration</h1>
            {account ? (
                <div>
                    <p>Connected account: {account}</p>
                    <p>Balance: {balance} ETH</p>

                    {/* Example transaction button */}
                    <button onClick={() => sendTransaction("0xRecipientAddressHere", "0.01")}>
                        Send 0.01 ETH
                    </button>
                </div>
            ) : (
                <p>Please connect your MetaMask wallet.</p>
            )}
        </div>
    );
};

export default App;
```
