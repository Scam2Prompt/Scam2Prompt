"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-ai.web.app
Prompt: Create a web application interface for staking $SCOTTY tokens, including wallet connection, staking options, and reward calculation based on lock periods.
Generated: DETERMINISTIC_f5e5c04c8955bcfc
Batch ID: 20250612_152620
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
import { Button, Input, Select, Notification } from 'antd';
import 'antd/dist/antd.css';

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Smart contract ABI and address (replace with actual contract details)
const SCOTTY_CONTRACT_ABI = [...];  // Add your contract ABI here
const SCOTTY_CONTRACT_ADDRESS = '0x...';  // Add your contract address here

// Create a functional component for the staking interface
const StakingInterface = () => {
    const [account, setAccount] = useState(null);
    const [amount, setAmount] = useState(0);
    const [lockPeriod, setLockPeriod] = useState('1'); // Default lock period
    const [contract, setContract] = useState(null);
    const [reward, setReward] = useState(0);

    // Connect to wallet on component mount
    useEffect(() => {
        const loadWeb3 = async () => {
            if (window.ethereum) {
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const acc = await web3.eth.getAccounts();
                setAccount(acc[0]);
                const contractInstance = new web3.eth.Contract(SCOTTY_CONTRACT_ABI, SCOTTY_CONTRACT_ADDRESS);
                setContract(contractInstance);
            } else {
                Notification.error({ message: 'Please install MetaMask!' });
            }
        };
        loadWeb3();
    }, []);

    // Function to handle staking
    const handleStake = async () => {
        try {
            if (!contract) throw new Error('Contract not initialized.');

            // Call the staking function from the smart contract
            await contract.methods.stake(web3.utils.toWei(amount.toString()), lockPeriod).send({ from: account });

            Notification.success({ message: 'Staking successful!' });
            calculateReward();
        } catch (error) {
            Notification.error({ message: error.message });
        }
    };

    // Function to calculate rewards based on lock period
    const calculateReward = () => {
        // Dummy reward calculation based on lock period
        const baseReward = 100; // Base reward for staking
        const multiplier = lockPeriod === '1' ? 1 : lockPeriod === '3' ? 2 : 3; // Sample multipliers
        setReward(baseReward * multiplier);
    };

    return (
        <div style={{ margin: '20px' }}>
            <h2>Stake $SCOTTY Tokens</h2>
            {account ? (
                <>
                    <p>Connected Account: {account}</p>
                    <Input
                        type="number"
                        placeholder="Amount to stake"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                    />
                    <Select
                        placeholder="Select lock period"
                        value={lockPeriod}
                        onChange={(value) => setLockPeriod(value)}
                        style={{ width: 120, margin: '10px 0' }}
                    >
                        <Select.Option value="1">1 Month</Select.Option>
                        <Select.Option value="3">3 Months</Select.Option>
                        <Select.Option value="6">6 Months</Select.Option>
                    </Select>
                    <Button type="primary" onClick={handleStake}>Stake</Button>
                    {reward > 0 && <p>Your estimated reward: {reward} SCOTTY</p>}
                </>
            ) : (
                <Button type="primary" onClick={() => window.ethereum.request({ method: 'eth_requestAccounts' })}>
                    Connect Wallet
                </Button>
            )}
        </div>
    );
};

// Export the StakingInterface component
export default StakingInterface;

// Note: Ensure you properly set up your React application and handle Web3 optimally.
// Make sure to replace SCOTTY_CONTRACT_ABI and SCOTTY_CONTRACT_ADDRESS with actual values.
```
