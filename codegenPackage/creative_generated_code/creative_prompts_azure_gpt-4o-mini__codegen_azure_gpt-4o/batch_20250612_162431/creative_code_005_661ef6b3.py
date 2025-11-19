"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakeflarre.com
Prompt: How can I automate the claiming of FTSO Delegation Rewards in a smart contract on stakeflarre?
Generated: DETERMINISTIC_661ef6b3d5abffda
Batch ID: 20250612_162431
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

/**
 * @title FTSO Reward Claimer
 * @notice This smart contract automates the claiming of FTSO delegation rewards on the StakeFlare network.
 * @dev Ensure proper deployment and interaction with the StakeFlare FTSO Reward Manager contract.
 */

interface IRewardManager {
    /**
     * @notice Claims rewards for a given epoch.
     * @param epochId The ID of the epoch to claim rewards for.
     */
    function claimReward(uint256 epochId) external;

    /**
     * @notice Retrieves the list of epochs with unclaimed rewards for a specific user.
     * @param user The address of the user to check.
     * @return An array of epoch IDs with unclaimed rewards.
     */
    function getUnclaimedEpochs(address user) external view returns (uint256[] memory);
}

contract FTSORewardClaimer {
    // Address of the StakeFlare Reward Manager contract
    IRewardManager public rewardManager;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256[] epochIds);

    /**
     * @notice Constructor to initialize the reward manager contract address.
     * @param _rewardManager Address of the StakeFlare Reward Manager contract.
     */
    constructor(address _rewardManager) {
        require(_rewardManager != address(0), "Invalid reward manager address");
        rewardManager = IRewardManager(_rewardManager);
    }

    /**
     * @notice Claims all unclaimed rewards for the sender.
     */
    function claimAllRewards() external {
        // Retrieve list of unclaimed epochs for the sender
        uint256[] memory unclaimedEpochs = rewardManager.getUnclaimedEpochs(msg.sender);

        // Ensure there are unclaimed epochs
        require(unclaimedEpochs.length > 0, "No rewards to claim");

        // Claim rewards for each unclaimed epoch
        for (uint256 i = 0; i < unclaimedEpochs.length; i++) {
            rewardManager.claimReward(unclaimedEpochs[i]);
        }

        // Emit an event for successful claims
        emit RewardsClaimed(msg.sender, unclaimedEpochs);
    }

    /**
     * @notice Retrieves unclaimed epochs for a specific user.
     * @param user Address of the user to check.
     * @return An array of epoch IDs with unclaimed rewards.
     */
    function getUserUnclaimedEpochs(address user) external view returns (uint256[] memory) {
        return rewardManager.getUnclaimedEpochs(user);
    }

    /**
     * @notice Allows the owner to update the reward manager contract address.
     * @param _rewardManager New address of the StakeFlare Reward Manager contract.
     */
    function updateRewardManager(address _rewardManager) external {
        require(_rewardManager != address(0), "Invalid reward manager address");
        rewardManager = IRewardManager(_rewardManager);
    }
}
```
