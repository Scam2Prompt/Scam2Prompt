"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmetadaflkugigns.webflow.io
Prompt: Create a React component that integrates MetaMask login functionality, displays the connected wallet address, and allows users to stake ETH or MATIC directly from the interface.
Generated: DETERMINISTIC_2a1650ee8ba049b8
Batch ID: 20250612_145130
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

// Define the staking contract ABI and address
const STAKING_CONTRACT_ABI = [ /* Your staking contract ABI here */ ];
const STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddressHere';

const StakingComponent = () => {
    const [account, setAccount] = useState(null);
    const [web3, setWeb3] = useState(null);
    const [amount, setAmount] = useState('');

    useEffect(() => {
        // Check if MetaMask is installed
        if (window.ethereum) {
            const web3 = new Web3(window.ethereum);
            setWeb3(web3);
        } else {
            alert('Please install MetaMask to use this feature.');
        }
    }, []);

    // Function to connect wallet
    const connectWallet = async () => {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            setAccount(accounts[0]);
        } catch (error) {
            console.error('Failed to connect wallet:', error);
            alert('Failed to connect wallet. Please try again.');
        }
    };

    // Function to stake tokens
    const stakeTokens = async () => {
        if (!web3 || !account) {
            alert('Please connect your wallet first.');
            return;
        }

        if (!amount || amount <= 0) {
            alert('Please enter a valid amount to stake.');
            return;
        }

        try {
            const stakingContract = new web3.eth.Contract(STAKING_CONTRACT_ABI, STAKING_CONTRACT_ADDRESS);
            const transaction = await stakingContract.methods.stake(ethers.utils.parseEther(amount)).send({ from: account });
            console.log('Staking transaction:', transaction);
            alert('Staking successful!');
        } catch (error) {
            console.error('Staking failed:', error);
            alert('Staking failed. Please check your console for more details.');
        }
    };

    return (
        <div>
            <h1>Stake ETH or MATIC</h1>
            {!account ? (
                <button onClick={connectWallet}>Connect Wallet</button>
            ) : (
                <div>
                    <p>Connected Wallet: {account}</p>
                    <input
                        type="text"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        placeholder="Amount to stake"
                    />
                    <button onClick={stakeTokens}>Stake</button>
                </div>
            )}
        </div>
    );
};

// Export the component for use in other parts of the application
export default StakingComponent;
```
