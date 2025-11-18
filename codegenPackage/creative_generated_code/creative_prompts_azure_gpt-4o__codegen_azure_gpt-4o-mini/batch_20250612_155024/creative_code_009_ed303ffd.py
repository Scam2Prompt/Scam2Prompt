"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jirasanf.top
Prompt: Provide code to integrate a blockchain-based reputation system into a web dashboard that connects with MetaMask wallets.
Generated: DETERMINISTIC_ed303ffda050b506
Batch ID: 20250612_155024
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
import { Button } from 'antd'; // Using Ant Design for UI components
import 'antd/dist/antd.css'; // Import Ant Design CSS

// Smart contract ABI and address (replace with your actual contract details)
const contractABI = [...]; // Your contract ABI here
const contractAddress = '0xYourContractAddress'; // Your contract address here

// Main Dashboard component
const ReputationDashboard = () => {
    const [account, setAccount] = useState('');
    const [web3, setWeb3] = useState(null);
    const [contract, setContract] = useState(null);
    const [reputation, setReputation] = useState(null);

    // Effect to initialize Web3 and connect with MetaMask
    useEffect(() => {
        const initBlockchain = async () => {
            if (window.ethereum) {
                // Request account access
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);

                // Set account and contract instance
                const accounts = await web3Instance.eth.getAccounts();
                setAccount(accounts[0]);
                const contractInstance = new web3Instance.eth.Contract(contractABI, contractAddress);
                setContract(contractInstance);
            } else {
                alert("Please install MetaMask to use this app.");
            }
        };
        initBlockchain();
    }, []);

    // Function to get reputation score from the smart contract
    const getReputationScore = async () => {
        if (contract) {
            try {
                const score = await contract.methods.getReputation(account).call();
                setReputation(score);
            } catch (error) {
                console.error("Error fetching reputation score:", error);
                alert("Could not fetch reputation score. Please try again later.");
            }
        }
    };

    // Function to update the reputation score
    const updateReputationScore = async (newScore) => {
        if (contract) {
            try {
                await contract.methods.updateReputation(account, newScore).send({ from: account });
                alert("Reputation score updated successfully!");
                getReputationScore(); // Refresh the score after update
            } catch (error) {
                console.error("Error updating reputation score:", error);
                alert("Could not update reputation score. Please try again later.");
            }
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Blockchain-Based Reputation System</h1>
            <p>Connected Account: {account}</p>
            <Button type="primary" onClick={getReputationScore}>
                Get Reputation Score
            </Button>
            {reputation !== null && (
                <div>
                    <h2>Your Reputation Score: {reputation}</h2>
                    <Button type="default" onClick={() => updateReputationScore(reputation + 1)}>
                        Increase Reputation
                    </Button>
                    <Button type="default" onClick={() => updateReputationScore(reputation - 1)}>
                        Decrease Reputation
                    </Button>
                </div>
            )}
        </div>
    );
};

export default ReputationDashboard;
```

### Note:
- Replace `contractABI` with your actual smart contract ABI and `contractAddress` with your deployed contract address.
- Ensure that you handle security concerns and implement additional checks as necessary in a production environment.
