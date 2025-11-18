"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-catecoin-club.pages.dev
Prompt: Generate code to integrate Catecoin staking functionality into a DApp, including features to display active and completed stakes with details like start date, amount, interest, penalty, and end date.
Generated: DETERMINISTIC_f1da43460cb3e2a6
Batch ID: 20250612_152954
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
import { ethers } from 'ethers';

// Define the contract address and ABI for Catecoin staking
const STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddressHere';
const STAKING_CONTRACT_ABI = [
    // Minimal ABI to interact with staking contract
    "function getActiveStakes(address user) view returns (tuple(uint256 startDate, uint256 amount, uint256 interest, uint256 penalty, uint256 endDate)[])",
    "function getCompletedStakes(address user) view returns (tuple(uint256 startDate, uint256 amount, uint256 interest, uint256 penalty, uint256 endDate)[])"
];

// Component to display staking information
const StakingDashboard = () => {
    const [activeStakes, setActiveStakes] = useState([]);
    const [completedStakes, setCompletedStakes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Function to fetch staking data from the blockchain
    const fetchStakes = async () => {
        try {
            // Check if the window.ethereum object is available
            if (!window.ethereum) {
                throw new Error("Ethereum provider not found. Please install MetaMask.");
            }

            // Create a new ethers provider and contract instance
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            const stakingContract = new ethers.Contract(STAKING_CONTRACT_ADDRESS, STAKING_CONTRACT_ABI, signer);

            // Get the user's Ethereum address
            const userAddress = await signer.getAddress();

            // Fetch active and completed stakes
            const active = await stakingContract.getActiveStakes(userAddress);
            const completed = await stakingContract.getCompletedStakes(userAddress);

            // Update state with fetched data
            setActiveStakes(active);
            setCompletedStakes(completed);
        } catch (err) {
            // Handle errors and update state
            setError(err.message);
        } finally {
            // Set loading to false once data fetching is complete
            setLoading(false);
        }
    };

    // UseEffect to fetch stakes when the component mounts
    useEffect(() => {
        fetchStakes();
    }, []);

    // Render the staking dashboard
    return (
        <div className="staking-dashboard">
            <h1>Catecoin Staking Dashboard</h1>
            {loading && <p>Loading stakes...</p>}
            {error && <p className="error">{error}</p>}

            <h2>Active Stakes</h2>
            {activeStakes.length === 0 ? (
                <p>No active stakes found.</p>
            ) : (
                <ul>
                    {activeStakes.map((stake, index) => (
                        <li key={index}>
                            <p>Start Date: {new Date(stake.startDate * 1000).toLocaleString()}</p>
                            <p>Amount: {ethers.utils.formatEther(stake.amount)} CATE</p>
                            <p>Interest: {stake.interest}%</p>
                            <p>Penalty: {stake.penalty}%</p>
                            <p>End Date: {new Date(stake.endDate * 1000).toLocaleString()}</p>
                        </li>
                    ))}
                </ul>
            )}

            <h2>Completed Stakes</h2>
            {completedStakes.length === 0 ? (
                <p>No completed stakes found.</p>
            ) : (
                <ul>
                    {completedStakes.map((stake, index) => (
                        <li key={index}>
                            <p>Start Date: {new Date(stake.startDate * 1000).toLocaleString()}</p>
                            <p>Amount: {ethers.utils.formatEther(stake.amount)} CATE</p>
                            <p>Interest: {stake.interest}%</p>
                            <p>Penalty: {stake.penalty}%</p>
                            <p>End Date: {new Date(stake.endDate * 1000).toLocaleString()}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default StakingDashboard;
```
