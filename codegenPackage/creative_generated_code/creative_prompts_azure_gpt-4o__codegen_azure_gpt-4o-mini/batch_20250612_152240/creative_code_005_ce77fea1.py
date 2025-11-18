"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bamboomeme.pages.dev
Prompt: Develop a smart contract for a tokenized casino experience that rewards players, inspired by the `$BAMBOO` token's connection to a casino in the crypto space.
Generated: DETERMINISTIC_ce77fea195199089
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BambooCasinoToken
 * @dev ERC20 Token that represents a tokenized casino experience.
 * Players can earn rewards based on their activity within the casino.
 */
contract BambooCasinoToken is ERC20, Ownable {
    // Mapping to track player rewards
    mapping(address => uint256) private rewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed player, uint256 amount);

    // Total rewards pool for distribution
    uint256 private totalRewardsPool;

    /**
     * @dev Constructor that sets the token name and symbol, and mints initial supply to the contract owner.
     * @param initialSupply The initial supply of tokens to be minted.
     */
    constructor(uint256 initialSupply) ERC20("BambooCasinoToken", "BAMBOO") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to distribute rewards to players.
     * Only callable by the contract owner.
     * @param player The address of the player receiving rewards.
     * @param amount The amount of rewards to be distributed.
     */
    function distributeRewards(address player, uint256 amount) external onlyOwner {
        require(amount > 0, "Reward amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Insufficient balance to distribute rewards");
        
        rewards[player] += amount;
        totalRewardsPool += amount;

        emit RewardsDistributed(player, amount);
    }

    /**
     * @dev Function for players to claim their rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the player's reward balance before transferring tokens to prevent re-entrancy
        rewards[msg.sender] = 0;

        // Transfer tokens from the contract to the player
        _transfer(owner(), msg.sender, rewardAmount);
    }

    /**
     * @dev Function to check the reward balance of a player.
     * @param player The address of the player.
     * @return The amount of rewards the player has.
     */
    function getRewards(address player) external view returns (uint256) {
        return rewards[player];
    }

    /**
     * @dev Function to withdraw excess funds from the contract by the owner.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient funds to withdraw");
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Fallback function to receive Ether. 
     */
    receive() external payable {}
}
```
