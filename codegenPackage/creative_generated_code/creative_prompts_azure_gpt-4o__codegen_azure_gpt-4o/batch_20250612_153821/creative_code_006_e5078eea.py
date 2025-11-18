"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralisednetwork.pages.dev
Prompt: Create a staking pool smart contract that combines resources to increase staking rewards, as outlined on Decentralised Networks.
Generated: DETERMINISTIC_e5078eeaff5ef7a1
Batch ID: 20250612_153821
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
 * @title StakingPool
 * @dev This contract allows users to pool their resources for staking on decentralized networks.
 * Rewards are distributed proportionally based on individual contributions.
 */
contract StakingPool {
    // Address of the operator managing the staking pool
    address public operator;
    
    // Total amount of ETH staked in the pool
    uint256 public totalStaked;

    // Mapping to store user stakes
    mapping(address => uint256) public userStakes;

    // Events for logging activities
    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 totalRewards);

    /**
     * @dev Modifier to restrict access to the operator.
     */
    modifier onlyOperator() {
        require(msg.sender == operator, "Only operator can perform this action");
        _;
    }

    /**
     * @dev Constructor sets the initial operator as the contract deployer.
     */
    constructor() {
        operator = msg.sender;
    }

    /**
     * @dev Allows users to stake ETH in the pool.
     * The `msg.value` specifies the amount of ETH to stake.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Update user stake and total staked
        userStakes[msg.sender] += msg.value;
        totalStaked += msg.value;

        emit Stake(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to unstake their ETH from the pool.
     * Users can only withdraw the amount they have staked.
     * @param amount Amount of ETH the user wants to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Update user stake and total staked
        userStakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the unstaked amount back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        emit Unstake(msg.sender, amount);
    }

    /**
     * @dev Operator distributes staking rewards to pool participants.
     * Rewards are distributed proportionally based on individual contributions.
     * @param totalRewards Amount of ETH to distribute as rewards.
     */
    function distributeRewards(uint256 totalRewards) external payable onlyOperator {
        require(totalRewards > 0, "Reward amount must be greater than zero");
        require(msg.value == totalRewards, "Insufficient ETH sent for rewards");

        // Distribute rewards proportionally
        for (address userAddress: getAllStakers()) {
            uint256 userStake = userStakes[userAddress);
            if (userStake > 0) {
                uint256 reward = (userStake * totalRewards) / totalStaked;

                // Transfer reward to the user
                (bool success, ) = userAddress.call{value: reward}("");
                require(success, "ETH transfer failed");
            }
        }

        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Helper function to retrieve all addresses that have staked in the pool.
     * Note: This is a placeholder. Implement proper tracking for stakers.
     */
    function getAllStakers() internal view returns (address[] memory) {
        // This function needs to be implemented to track all stakers dynamically.
        // Currently, this is just a placeholder for demonstration purposes.
        address[] memory stakers;
        return stakers;
    }

    /**
     * @dev Allows the operator to update their address.
     * @param newOperator Address of the new operator.
     */
    function updateOperator(address newOperator) external onlyOperator {
        require(newOperator != address(0), "Operator address cannot be zero");
        operator = newOperator;
    }
}
```
