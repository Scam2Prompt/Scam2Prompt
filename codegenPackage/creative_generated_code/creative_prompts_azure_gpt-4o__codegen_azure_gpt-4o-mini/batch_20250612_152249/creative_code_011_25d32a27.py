"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spores-buv.pages.dev
Prompt: Generate a code example to integrate the Spores Network staking feature into a React.js application.
Generated: DETERMINISTIC_25d32a27a905b0fc
Batch ID: 20250612_152249
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
import { SporesStakingContractAddress, SporesStakingABI } from './config'; // Adjust the path as needed

const SporesStaking = () => {
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState('');
    const [contract, setContract] = useState(null);
    const [stakeAmount, setStakeAmount] = useState('');
    const [message, setMessage] = useState('');

    // Initialize Web3 and contract
    useEffect(() => {
        const initializeWeb3 = async () => {
            if (window.ethereum) {
                const web3Instance = new Web3(window.ethereum);
                setWeb3(web3Instance);
                
                try {
                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    const accounts = await web3Instance.eth.getAccounts();
                    setAccount(accounts[0]);

                    // Create contract instance
                    const stakingContract = new web3Instance.eth.Contract(SporesStakingABI, SporesStakingContractAddress);
                    setContract(stakingContract);
                } catch (error) {
                    console.error("Error accessing Ethereum account:", error);
                    setMessage("Failed to connect to your Ethereum account. Make sure you have MetaMask installed and logged in.");
                }
            } else {
                setMessage("Please install MetaMask to use this feature.");
            }
        };

        initializeWeb3();
    }, []);

    // Function to handle staking
    const handleStake = async () => {
        if (!stakeAmount || isNaN(stakeAmount) || stakeAmount <= 0) {
            setMessage("Please enter a valid stake amount.");
            return;
        }

        if (!contract) {
            setMessage("Contract is not initialized.");
            return;
        }

        try {
            setMessage("Processing your transaction...");
            const tx = await contract.methods.stake(web3.utils.toWei(stakeAmount, 'ether')).send({ from: account });
            console.log("Transaction successful:", tx);
            setMessage(`Stake successful! Transaction Hash: ${tx.transactionHash}`);
        } catch (error) {
            console.error("Error staking:", error);
            setMessage("An error occurred while trying to stake. Please try again.");
        }
    };

    return (
        <div>
            <h2>Spores Network Staking</h2>
            {message && <p>{message}</p>}
            <input 
                type="number" 
                placeholder="Amount to stake" 
                value={stakeAmount} 
                onChange={(e) => setStakeAmount(e.target.value)} 
            />
            <button onClick={handleStake}>Stake</button>
        </div>
    );
};

export default SporesStaking;
```

### Additional Notes:
- Make sure to replace `SporesStakingContractAddress` and `SporesStakingABI` with your actual contract address and ABI.
- Ensure that MetaMask (or another Ethereum provider) is available in the user's browser for this code to run successfully.
