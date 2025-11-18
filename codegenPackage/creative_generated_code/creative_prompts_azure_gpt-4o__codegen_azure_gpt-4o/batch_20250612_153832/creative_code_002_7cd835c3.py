"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexwin.top
Prompt: Generate a smart contract snippet for verifying wallet connections and distributing rewards, inspired by the reward claim process on the "REWARD Portal v2."
Generated: DETERMINISTIC_7cd835c3ab2b36e3
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title RewardDistributor
 * @dev A smart contract for verifying wallet connections and distributing rewards.
 */
contract RewardDistributor {
    // Mapping to track user reward claims
    mapping(address => bool) private hasClaimedReward;

    // Address of the owner (e.g., admin)
    address private owner;

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Allow users to claim their rewards.
     * @param rewardAmount The amount of reward to be distributed.
     */
    function claimReward(uint256 rewardAmount) external {
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(!hasClaimedReward[msg.sender], "Reward already claimed");

        // Check contract balance
        require(address(this).balance >= rewardAmount, "Insufficient contract balance");

        // Mark as claimed and transfer the reward
        hasClaimedReward[msg.sender] = true;
        payable(msg.sender).transfer(rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function for the owner to deposit funds into the contract.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
    }

    /**
     * @dev Retrieve the current balance of the contract.
     * @return The balance of the contract in wei.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Check if a user has already claimed their reward.
     * @param user The address of the user.
     * @return True if the user has claimed the reward, false otherwise.
     */
    function hasUserClaimedReward(address user) external view returns (bool) {
        return hasClaimedReward[user];
    }
}
```
