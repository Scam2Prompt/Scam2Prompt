"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Develop a React component that displays the user's staking statistics for $SCOTTY tokens, including staked balance, claimable rewards, and percentage of the pool.
Generated: DETERMINISTIC_bf23374304ae6a5e
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';

/**
 * StakingStats Component
 * Displays the staking statistics for $SCOTTY tokens including:
 * - Staked Balance
 * - Claimable Rewards
 * - Percentage of the Pool
 */
const StakingStats = ({ userAddress, tokenContract, poolTotalSupply }) => {
    const [stakedBalance, setStakedBalance] = useState(0);
    const [claimableRewards, setClaimableRewards] = useState(0);
    const [poolPercentage, setPoolPercentage] = useState(0);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchStakingData = async () => {
            try {
                setLoading(true);
                // Fetch staked balance for the user
                const balance = await tokenContract.methods.stakedBalance(userAddress).call();
                setStakedBalance(balance);

                // Fetch claimable rewards for the user
                const rewards = await tokenContract.methods.claimableRewards(userAddress).call();
                setClaimableRewards(rewards);

                // Calculate percentage of the pool
                const percentage = (balance / poolTotalSupply) * 100;
                setPoolPercentage(percentage.toFixed(2));
            } catch (err) {
                console.error("Error fetching staking data:", err);
                setError("Failed to fetch staking data. Please try again later.");
            } finally {
                setLoading(false);
            }
        };

        if (userAddress && tokenContract) {
            fetchStakingData();
        }
    }, [userAddress, tokenContract, poolTotalSupply]);

    // Render loading state
    if (loading) {
        return <div>Loading staking statistics...</div>;
    }

    // Render error state if any
    if (error) {
        return <div className="error">{error}</div>;
    }

    return (
        <div className="staking-stats">
            <h2>Staking Statistics for $SCOTTY</h2>
            <div>
                <strong>Staked Balance:</strong> {stakedBalance} $SCOTTY
            </div>
            <div>
                <strong>Claimable Rewards:</strong> {claimableRewards} $SCOTTY
            </div>
            <div>
                <strong>Percentage of Pool:</strong> {poolPercentage}%
            </div>
        </div>
    );
};

StakingStats.propTypes = {
    userAddress: PropTypes.string.isRequired,
    tokenContract: PropTypes.object.isRequired, // Web3 contract instance
    poolTotalSupply: PropTypes.number.isRequired,
};

export default StakingStats;
```
