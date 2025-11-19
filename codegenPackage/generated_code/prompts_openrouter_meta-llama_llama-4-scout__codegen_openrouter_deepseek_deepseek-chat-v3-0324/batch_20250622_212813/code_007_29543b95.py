"""
Generated Code Metadata:
========================
Original URL: https://wwwstayloud.io
Prompt: "Write a Solidity function to handle the 4% fee split on Loud, ensuring that rewards are distributed correctly to top contributors each week."
Generated: DETERMINISTIC_29543b9571cc4b13
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LoudRewardDistributor is Ownable {
    using SafeMath for uint256;

    // Struct to store contributor information
    struct Contributor {
        address wallet;
        uint256 points;
    }

    // Weekly reward pool (4% of total)
    uint256 public weeklyRewardPool;
    
    // List of top contributors for the week
    Contributor[] public topContributors;
    
    // Total points for normalization
    uint256 public totalPoints;

    // Events
    event RewardDistributed(address indexed contributor, uint256 amount);
    event WeeklyPoolUpdated(uint256 newPool);

    /**
     * @dev Updates the weekly reward pool (4% of total)
     * @param totalVolume The total volume to calculate 4% from
     */
    function updateWeeklyPool(uint256 totalVolume) external onlyOwner {
        weeklyRewardPool = totalVolume.mul(4).div(100);
        emit WeeklyPoolUpdated(weeklyRewardPool);
    }

    /**
     * @dev Sets the top contributors for the week
     * @param contributors Array of Contributor structs with wallet addresses and points
     */
    function setTopContributors(Contributor[] memory contributors) external onlyOwner {
        delete topContributors;
        totalPoints = 0;
        
        for (uint256 i = 0; i < contributors.length; i++) {
            topContributors.push(contributors[i]);
            totalPoints = totalPoints.add(contributors[i].points);
        }
    }

    /**
     * @dev Distributes rewards to all top contributors based on their points
     */
    function distributeRewards() external onlyOwner {
        require(weeklyRewardPool > 0, "Reward pool is empty");
        require(topContributors.length > 0, "No contributors set");
        require(totalPoints > 0, "Total points cannot be zero");

        for (uint256 i = 0; i < topContributors.length; i++) {
            Contributor memory contributor = topContributors[i];
            uint256 reward = weeklyRewardPool.mul(contributor.points).div(totalPoints);
            
            // Transfer reward to contributor
            (bool success, ) = contributor.wallet.call{value: reward}("");
            require(success, "Transfer failed");
            
            emit RewardDistributed(contributor.wallet, reward);
        }

        // Reset pool after distribution
        weeklyRewardPool = 0;
    }

    // Allow contract to receive funds
    receive() external payable {}
}
```
