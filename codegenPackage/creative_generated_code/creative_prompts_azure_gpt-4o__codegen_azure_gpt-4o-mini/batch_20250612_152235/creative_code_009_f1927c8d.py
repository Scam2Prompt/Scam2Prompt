"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchaincoin-presale.pages.dev
Prompt: Recommend tools or frameworks for building a decentralized application (dApp) that integrates wallet connection, staking, and token presale functionality, as described on the Onchain Coin presale page.
Generated: DETERMINISTIC_f1927c8de3fcead2
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';
import { ethers } from 'ethers';
import { useEffect, useState } from 'react';

// Define constants for contract addresses and ABI (replace with actual values)
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress';
const STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddress';
const TOKEN_ABI = [ /* Your Token ABI */ ];
const STAKING_ABI = [ /* Your Staking ABI */ ];

// Define the dApp component
const DApp = () => {
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState(null);
    const [tokenContract, setTokenContract] = useState(null);
    const [stakingContract, setStakingContract] = useState(null);

    // Initialize Web3 and connect wallet on component mount
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
                    
                    // Initialize contract instances
                    const token = new web3Instance.eth.Contract(TOKEN_ABI, TOKEN_CONTRACT_ADDRESS);
                    const staking = new web3Instance.eth.Contract(STAKING_ABI, STAKING_CONTRACT_ADDRESS);
                    setTokenContract(token);
                    setStakingContract(staking);
                } else {
                    alert('Please install MetaMask!');
                }
            } catch (error) {
                console.error('Error connecting to wallet:', error);
            }
        };

        initWeb3();
    }, []);

    // Function to handle token presale purchase
    const purchaseTokens = async (amount) => {
        if (!tokenContract || !account) return;

        try {
            const tx = await tokenContract.methods.purchase(amount).send({ from: account });
            console.log('Transaction successful:', tx);
        } catch (error) {
            console.error('Error purchasing tokens:', error);
        }
    };

    // Function to stake tokens
    const stakeTokens = async (amount) => {
        if (!stakingContract || !account) return;

        try {
            const tx = await stakingContract.methods.stake(amount).send({ from: account });
            console.log('Staking successful:', tx);
        } catch (error) {
            console.error('Error staking tokens:', error);
        }
    };

    return (
        <div>
            <h1>Decentralized Application (dApp)</h1>
            <p>Connected Account: {account}</p>
            {/* UI for purchasing tokens and staking would go here */}
            {/* Example buttons for actions */}
            <button onClick={() => purchaseTokens(1)}>Purchase Tokens</button>
            <button onClick={() => stakeTokens(1)}>Stake Tokens</button>
        </div>
    );
};

export default DApp;
```
