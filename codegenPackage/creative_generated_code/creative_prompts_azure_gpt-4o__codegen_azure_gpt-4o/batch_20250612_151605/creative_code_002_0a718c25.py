"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://de-agent.com
Prompt: Generate code for an Ethereum-based prize pool system in Solidity, where users can claim rewards using their EVM-compatible wallets.
Generated: DETERMINISTIC_0a718c2523711506
Batch ID: 20250612_151605
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
 * @title PrizePool
 * @dev This contract allows users to deposit funds and claim rewards.
 * Rewards are distributed periodically, and users can claim them using their wallets.
 */
contract PrizePool {
    // Events
    event Deposit(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event FundsWithdrawn(address indexed owner, uint256 amount);

    // Owner of the contract
    address public owner;

    // Total pool balance
    uint256 public poolBalance;

    // Mapping to track user deposits
    mapping(address => uint256) public userDeposits;

    // Mapping to track user rewards
    mapping(address => uint256) public userRewards;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to deposit Ether into the prize pool.
     * Emits a Deposit event.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user deposit and pool balance
        userDeposits[msg.sender] += msg.value;
        poolBalance += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Allows the contract owner to distribute rewards to a user.
     * @param user The address of the user to reward.
     * @param rewardAmount The amount of reward to distribute.
     */
    function distributeReward(address user, uint256 rewardAmount) external onlyOwner {
        require(userDeposits[user] > 0, "User has no deposits");
        require(rewardAmount > 0, "Reward amount must be greater than zero");
        require(rewardAmount <= poolBalance, "Insufficient pool balance");

        // Update rewards and pool balance
        userRewards[user] += rewardAmount;
        poolBalance -= rewardAmount;
    }

    /**
     * @dev Allows users to claim their rewards.
     * Emits a RewardClaimed event.
     */
    function claimReward() external {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset user rewards before transfer to prevent reentrancy
        userRewards[msg.sender] = 0;

        // Transfer reward to user
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Failed to transfer reward");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the contract owner to withdraw all remaining funds.
     * Emits a FundsWithdrawn event.
     */
    function withdrawFunds() external onlyOwner {
        require(poolBalance > 0, "No funds available to withdraw");

        uint256 amount = poolBalance;

        // Reset pool balance before transfer to prevent reentrancy
        poolBalance = 0;

        // Transfer funds to owner
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Failed to withdraw funds");

        emit FundsWithdrawn(owner, amount);
    }

    /**
     * @dev Fallback function to reject incoming Ether to non-payable functions.
     */
    fallback() external payable {
        revert("Fallback function does not accept Ether");
    }

    /**
     * @dev Receive function to accept direct Ether transfers to the contract.
     */
    receive() external payable {
        poolBalance += msg.value;
    }
}
```
