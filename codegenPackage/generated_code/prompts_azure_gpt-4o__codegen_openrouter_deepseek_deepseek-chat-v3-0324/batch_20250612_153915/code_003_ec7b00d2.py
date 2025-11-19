"""
Generated Code Metadata:
========================
Original URL: https://ton-spin.web.app
Prompt: Create a smart contract in Solidity that handles reward distribution for a gamified system like the "FREE SPIN" feature described on the TON SPIN website.
Generated: DETERMINISTIC_ec7b00d26f0a5fb4
Batch ID: 20250612_153915
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract FreeSpinRewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;

    // Reward parameters
    uint256 public constant MIN_REWARD = 1 ether; // 1 token (assuming 18 decimals)
    uint256 public constant MAX_REWARD = 10 ether; // 10 tokens
    uint256 public constant COOLDOWN_PERIOD = 1 days;

    // Player data
    struct Player {
        uint256 lastSpinTime;
        uint256 totalRewards;
        bool isWhitelisted;
    }

    mapping(address => Player) public players;

    // Events
    event RewardDistributed(address indexed player, uint256 amount);
    event PlayerWhitelisted(address indexed player);
    event PlayerRemovedFromWhitelist(address indexed player);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Whitelist a player to be eligible for rewards
     * @param player Address of the player to whitelist
     */
    function whitelistPlayer(address player) external onlyOwner {
        require(!players[player].isWhitelisted, "Player already whitelisted");
        players[player].isWhitelisted = true;
        emit PlayerWhitelisted(player);
    }

    /**
     * @dev Remove a player from the whitelist
     * @param player Address of the player to remove
     */
    function removeFromWhitelist(address player) external onlyOwner {
        require(players[player].isWhitelisted, "Player not whitelisted");
        players[player].isWhitelisted = false;
        emit PlayerRemovedFromWhitelist(player);
    }

    /**
     * @dev Distribute a random reward to the player
     */
    function spin() external nonReentrant {
        require(players[msg.sender].isWhitelisted, "Player not whitelisted");
        require(
            block.timestamp >= players[msg.sender].lastSpinTime + COOLDOWN_PERIOD,
            "Cooldown period not passed"
        );

        // Generate pseudo-random reward amount
        uint256 rewardAmount = _generateRandomReward();

        // Check contract balance
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(contractBalance >= rewardAmount, "Insufficient contract balance");

        // Update player data
        players[msg.sender].lastSpinTime = block.timestamp;
        players[msg.sender].totalRewards += rewardAmount;

        // Transfer reward
        require(rewardToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Generate a pseudo-random reward amount between MIN_REWARD and MAX_REWARD
     * @return Random reward amount
     */
    function _generateRandomReward() private view returns (uint256) {
        // This is a simple pseudo-random number generator - not suitable for production
        // In production, consider using Chainlink VRF or similar
        uint256 random = uint256(
            keccak256(
                abi.encodePacked(
                    block.difficulty,
                    block.timestamp,
                    msg.sender
                )
            )
        ) % (MAX_REWARD - MIN_REWARD + 1);

        return MIN_REWARD + random;
    }

    /**
     * @dev Withdraw tokens from the contract (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(
            rewardToken.transfer(msg.sender, amount),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Get player information
     * @param player Address of the player
     * @return lastSpinTime Last spin timestamp
     * @return totalRewards Total rewards earned
     * @return isWhitelisted Whitelist status
     */
    function getPlayerInfo(address player) external view returns (
        uint256 lastSpinTime,
        uint256 totalRewards,
        bool isWhitelisted
    ) {
        Player storage p = players[player];
        return (p.lastSpinTime, p.totalRewards, p.isWhitelisted);
    }
}
```
