"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Write a smart contract in Solidity to handle the distribution of AirDrop rewards for "Hamster Kombat" based on player achievements and completed tasks.
Generated: DETERMINISTIC_6ebd59dbf1e3890c
Batch ID: 20250612_150347
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
 * @title HamsterKombatAirDrop
 * @dev A smart contract to manage the distribution of AirDrop rewards based on player achievements.
 */
contract HamsterKombatAirDrop {

    // Owner of the contract
    address public owner;

    // Mapping to store player achievements and rewards
    mapping(address => uint256) public playerRewards;

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed player, uint256 amount);

    // Event emitted when funds are withdrawn by the owner
    event FundsWithdrawn(uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this function");
        _;
    }

    constructor() {
        // Set the contract deployer as the owner
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute rewards to players based on their achievements.
     * @param players Array of player addresses to receive rewards.
     * @param rewards Array of reward amounts corresponding to each player.
     */
    function distributeRewards(address[] calldata players, uint256[] calldata rewards) external onlyOwner {
        require(players.length == rewards.length, "Players and rewards array length must match");

        for (uint256 i = 0; i < players.length; i++) {
            address player = players[i];
            uint256 reward = rewards[i];

            // Ensure a valid reward amount
            require(reward > 0, "Reward amount must be greater than zero");
            require(player != address(0), "Invalid player address");

            // Update player's reward balance
            playerRewards[player] += reward;

            // Emit the event
            emit RewardDistributed(player, reward);
        }
    }

    /**
     * @dev Function for players to claim their rewards.
     */
    function claimReward() external {
        uint256 rewardAmount = playerRewards[msg.sender];

        // Ensure the player has rewards to claim
        require(rewardAmount > 0, "No rewards available for this player");

        // Reset the player's reward balance
        playerRewards[msg.sender] = 0;

        // Transfer the rewards to the player
        (bool success, ) = msg.sender.call{value: rewardAmount}("");
        require(success, "Reward transfer failed");
    }

    /**
     * @dev Function to allow the contract owner to withdraw funds from the contract.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdrawal failed");

        emit FundsWithdrawn(amount);
    }

    /**
     * @dev Function to receive Ether deposits into the contract.
     * This is required to fund the rewards distribution.
     */
    receive() external payable {
        // Accept Ether deposits
    }

    /**
     * @dev Function to get the balance of the contract.
     * @return The contract's Ether balance.
     */
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
