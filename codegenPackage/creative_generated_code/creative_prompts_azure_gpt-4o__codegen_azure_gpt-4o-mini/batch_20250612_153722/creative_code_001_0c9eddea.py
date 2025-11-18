"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pengwu.io
Prompt: Create a decentralized exchange (DEX) interface for trading PENGWU tokens, incorporating features like PENGWUSwap mentioned on the website.
Generated: DETERMINISTIC_0c9eddeab9d52a7e
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { PENGWU_ABI, PENGWU_ADDRESS, DEX_ABI, DEX_ADDRESS } from './config'; // Assume ABI and addresses are defined in config file

const PENGWUSwap = () => {
    // State variables
    const [account, setAccount] = useState('');
    const [web3, setWeb3] = useState(null);
    const [tokenAmount, setTokenAmount] = useState(0);
    const [ethAmount, setEthAmount] = useState(0);
    const [exchangeRate, setExchangeRate] = useState(0);

    // Initialize web3 and set the current account
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Check if MetaMask is installed
                if (window.ethereum) {
                    const web3Instance = new Web3(window.ethereum);
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);
                    setWeb3(web3Instance);
                } else {
                    alert('Please install MetaMask!');
                }
            } catch (error) {
                console.error("Could not connect to wallet:", error);
            }
        };
        initWeb3();
    }, []);

    // Fetch the current exchange rate
    const fetchExchangeRate = async () => {
        try {
            const dexContract = new web3.eth.Contract(DEX_ABI, DEX_ADDRESS);
            const rate = await dexContract.methods.getExchangeRate(PENGWU_ADDRESS).call();
            setExchangeRate(rate);
        } catch (error) {
            console.error("Error fetching exchange rate:", error);
        }
    };

    // Handle token amount change
    const handleTokenAmountChange = (event) => {
        setTokenAmount(event.target.value);
        setEthAmount(event.target.value * exchangeRate); // Update ETH amount based on exchange rate
    };

    // Handle ETH amount change
    const handleEthAmountChange = (event) => {
        setEthAmount(event.target.value);
        setTokenAmount(event.target.value / exchangeRate); // Update token amount based on exchange rate
    };

    // Swap function to exchange tokens
    const swapTokens = async () => {
        try {
            const dexContract = new web3.eth.Contract(DEX_ABI, DEX_ADDRESS);
            const pengwuContract = new web3.eth.Contract(PENGWU_ABI, PENGWU_ADDRESS);

            // Approve the DEX to spend PENGWU tokens
            await pengwuContract.methods.approve(DEX_ADDRESS, web3.utils.toWei(tokenAmount.toString(), 'ether')).send({ from: account });

            // Execute the swap
            await dexContract.methods.swapTokens(PENGWU_ADDRESS, web3.utils.toWei(tokenAmount.toString(), 'ether')).send({ from: account, value: web3.utils.toWei(ethAmount.toString(), 'ether') });

            alert('Swap successful!');
        } catch (error) {
            console.error("Error during the swap:", error);
            alert('Swap failed! Check console for details.');
        }
    };

    return (
        <div>
            <h1>PENGWU Swap</h1>
            <p>Account: {account}</p>
            <p>Current Exchange Rate: {exchangeRate}</p>
            <div>
                <input
                    type="number"
                    value={tokenAmount}
                    onChange={handleTokenAmountChange}
                    placeholder="Amount of PENGWU"
                />
                <input
                    type="number"
                    value={ethAmount}
                    onChange={handleEthAmountChange}
                    placeholder="Amount of ETH"
                />
                <button onClick={fetchExchangeRate}>Refresh Rate</button>
                <button onClick={swapTokens}>Swap Tokens</button>
            </div>
        </div>
    );
};

export default PENGWUSwap;
```
