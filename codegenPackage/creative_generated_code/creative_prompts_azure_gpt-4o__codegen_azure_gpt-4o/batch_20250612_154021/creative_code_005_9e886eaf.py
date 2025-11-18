"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asteerdex.com
Prompt: Develop a smart contract in Solidity that integrates with Aster to automate staking and reward collection for supported assets.
Generated: DETERMINISTIC_9e886eaf53dfa5fa
Batch ID: 20250612_154021
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
 * @title Aster Staking Automation
 * @notice This smart contract allows users to automate staking and reward collection
 *         for supported assets on the Aster blockchain.
 */

interface IAsterStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function claimRewards() external;
    function getRewardsEarned(address user) external view returns (uint256);
}

contract AsterStakingAutomation {
    // State variables
    address public immutable stakingContract;
    address public owner;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event Staked(uint256 amount);
    event Withdrawn(uint256 amount);
    event RewardsClaimed(uint256 amount);

    // Modifiers for access control
    modifier onlyOwner() {
        require(msg.sender == owner, "AsterStakingAutomation: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor function to initialize the staking contract address and owner.
     * @param _stakingContract Address of the Aster staking contract.
     */
    constructor(address _stakingContract) {
        require(_stakingContract != address(0), "AsterStakingAutomation: Invalid staking contract address");
        stakingContract = _stakingContract;
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "AsterStakingAutomation: New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Stake a specified amount of tokens in the Aster staking contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external onlyOwner {
        require(amount > 0, "AsterStakingAutomation: Stake amount must be greater than zero");

        IAsterStaking(stakingContract).stake(amount);
        emit Staked(amount);
    }

    /**
     * @dev Withdraw a specified amount of tokens from the Aster staking contract.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "AsterStakingAutomation: Withdraw amount must be greater than zero");

        IAsterStaking(stakingContract).withdraw(amount);
        emit Withdrawn(amount);
    }

    /**
     * @dev Claim rewards from the Aster staking contract.
     */
    function claimRewards() external onlyOwner {
        uint256 rewards = IAsterStaking(stakingContract).getRewardsEarned(address(this));
        require(rewards > 0, "AsterStakingAutomation: No rewards available to claim");

        IAsterStaking(stakingContract).claimRewards();
        emit RewardsClaimed(rewards);
    }

    /**
     * @dev Get the total rewards earned by this contract in the Aster staking contract.
     * @return Total rewards earned.
     */
    function getRewardsEarned() external view returns (uint256) {
        return IAsterStaking(stakingContract).getRewardsEarned(address(this));
    }
}
```
