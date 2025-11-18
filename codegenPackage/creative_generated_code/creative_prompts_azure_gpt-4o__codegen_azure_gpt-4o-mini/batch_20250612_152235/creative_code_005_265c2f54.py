"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Develop a feature in Solidity that increases an investor's tier by a percentage (e.g., +50%) based on their staking duration, as outlined in SidusPad's staking pool details.
Generated: DETERMINISTIC_265c2f54a2e0f7be
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SidusPadStaking {
    // Struct to hold investor details
    struct Investor {
        uint256 stakeAmount; // Amount staked by the investor
        uint256 tier;        // Current tier of the investor
        uint256 stakingDuration; // Duration for which the amount has been staked
        uint256 lastUpdate;  // Last time the tier was updated
    }

    // Mapping of investor addresses to their details
    mapping(address => Investor) private investors;

    // Event emitted when an investor's tier is updated
    event TierUpdated(address indexed investor, uint256 newTier);

    // Modifier to check if the caller is an investor
    modifier onlyInvestor() {
        require(investors[msg.sender].stakeAmount > 0, "Not an investor");
        _;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Update the investor's stake amount and duration
        Investor storage investor = investors[msg.sender];
        
        if (investor.stakeAmount == 0) {
            investor.lastUpdate = block.timestamp; // Set last update time only if it's the first stake
        }

        investor.stakeAmount += _amount;
        investor.stakingDuration += block.timestamp - investor.lastUpdate;
        investor.lastUpdate = block.timestamp;

        // Update tier based on staking duration
        updateTier(investor);
    }

    // Function to update an investor's tier based on their staking duration
    function updateTier(Investor storage investor) internal {
        // Calculate the additional tier based on staking duration
        uint256 percentageIncrease = (investor.stakingDuration / 30 days) * 50; // 50% increase for each 30 days
        
        // Ensure the tier does not exceed a maximum value (for example, 100)
        if (investor.tier + percentageIncrease > 100) {
            investor.tier = 100;
        } else {
            investor.tier += percentageIncrease;
        }

        emit TierUpdated(msg.sender, investor.tier);
    }

    // Function to get investor details
    function getInvestorDetails(address _investor) external view returns (uint256 stakeAmount, uint256 tier, uint256 stakingDuration) {
        Investor storage investor = investors[_investor];
        return (investor.stakeAmount, investor.tier, investor.stakingDuration);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external onlyInvestor {
        require(_amount > 0 && _amount <= investors[msg.sender].stakeAmount, "Invalid unstake amount");

        // Reduce the stake amount and reset staking duration
        investors[msg.sender].stakeAmount -= _amount;
        investors[msg.sender].stakingDuration = 0; // Reset duration on unstake
        investors[msg.sender].lastUpdate = block.timestamp; // Update last interaction time

        // Update tier after unstaking
        updateTier(investors[msg.sender]);
    }

    // Optional: Function to get the current block timestamp (for testing)
    function getCurrentTimestamp() external view returns (uint256) {
        return block.timestamp;
    }
}
```
