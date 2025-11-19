"""
Generated Code Metadata:
========================
Original URL: https://pushd-stores.web.app
Prompt: "Generate a Solidity code for a basic rewards program on a blockchain platform, similar to Pushd's, that incentivizes users to participate in the platform's growth."
Generated: DETERMINISTIC_0a59929b1e828aa4
Batch ID: 20250622_210057
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

/**
 * @title RewardsProgram
 * @dev A basic rewards program that incentivizes users to participate in the platform's growth.
 */
contract RewardsProgram {
    // Owner of the contract
    address public owner;

    // Mapping to store user balances (rewards points)
    mapping(address => uint256) public rewardsBalance;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when rewards are redeemed
    event RewardsRedeemed(address indexed user, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to set the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute rewards to a user.
     * @param user The address of the user to receive rewards.
     * @param amount The amount of rewards to distribute.
     */
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update the user's rewards balance
        rewardsBalance[user] += amount;

        // Emit the RewardsDistributed event
        emit RewardsDistributed(user, amount);
    }

    /**
     * @dev Function for users to redeem their rewards.
     * @param amount The amount of rewards to redeem.
     */
    function redeemRewards(uint256 amount) external {
        require(amount > 0, "Redeem amount must be greater than zero");
        require(rewardsBalance[msg.sender] >= amount, "Insufficient rewards balance");

        // Deduct the redeemed amount from the user's balance
        rewardsBalance[msg.sender] -= amount;

        // Emit the RewardsRedeemed event
        emit RewardsRedeemed(msg.sender, amount);

        // Note: In a real-world scenario, you might transfer tokens or perform other actions here.
    }

    /**
     * @dev Function to check the rewards balance of a user.
     * @param user The address of the user.
     * @return The rewards balance of the user.
     */
    function getRewardsBalance(address user) external view returns (uint256) {
        return rewardsBalance[user];
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
