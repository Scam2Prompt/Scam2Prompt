"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Create a smart contract in Solidity for managing KI Token rewards based on player activity, including staking and earning mechanisms as described in Genopets.
Generated: DETERMINISTIC_0bc1fd6fa38a3725
Batch ID: 20250612_150426
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/// @title KI Token Rewards Contract
/// @notice This contract manages the staking and rewards mechanism for KI Token based on player activity.
contract KITokenRewards is Ownable, ReentrancyGuard {
    // Token interface for interacting with the KI Token
    IERC20 public kiToken;

    // Struct to hold player data
    struct Player {
        uint256 stakedAmount;
        uint256 rewardsEarned;
        uint256 lastStakedTime;
    }

    // Mapping of player addresses to their data
    mapping(address => Player) public players;

    // Reward rate in tokens per second
    uint256 public rewardRate = 1e18; // 1 token per second

    // Event emitted when a player stakes tokens
    event Staked(address indexed player, uint256 amount);

    // Event emitted when a player withdraws tokens
    event Withdrawn(address indexed player, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed player, uint256 amount);

    /// @param _kiToken Address of the KI Token contract
    constructor(address _kiToken) {
        require(_kiToken != address(0), "Invalid token address");
        kiToken = IERC20(_kiToken);
    }

    /// @notice Stakes tokens to earn rewards
    /// @param amount Amount of tokens to stake
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(kiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Player storage player = players[msg.sender];

        // Update rewards before staking
        _updateRewards(msg.sender);

        player.stakedAmount += amount;
        player.lastStakedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /// @notice Withdraws staked tokens
    /// @param amount Amount of tokens to withdraw
    function withdraw(uint256 amount) external nonReentrant {
        Player storage player = players[msg.sender];

        require(player.stakedAmount >= amount, "Insufficient staked amount");

        // Update rewards before withdrawing
        _updateRewards(msg.sender);

        player.stakedAmount -= amount;
        require(kiToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Claims earned rewards
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        Player storage player = players[msg.sender];

        uint256 rewards = player.rewardsEarned;
        require(rewards > 0, "No rewards to claim");

        player.rewardsEarned = 0;
        require(kiToken.transfer(msg.sender, rewards), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /// @notice Updates the rewards for a player
    /// @param playerAddress Address of the player
    function _updateRewards(address playerAddress) internal {
        Player storage player = players[playerAddress];

        if (player.lastStakedTime > 0) {
            uint256 timeElapsed = block.timestamp - player.lastStakedTime;
            uint256 newRewards = timeElapsed * rewardRate * player.stakedAmount / 1e18; // Adjust for rewardRate scaling
            player.rewardsEarned += newRewards;
            player.lastStakedTime = block.timestamp;
        }
    }

    /// @notice Allows the owner to update the reward rate
    /// @param newRate New reward rate in tokens per second
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    /// @notice Returns the staked balance and earned rewards of a player
    /// @param playerAddress Address of the player
    /// @return stakedAmount Amount of tokens staked
    /// @return rewardsEarned Amount of rewards earned
    function getPlayerData(address playerAddress) external view returns (uint256 stakedAmount, uint256 rewardsEarned) {
        Player storage player = players[playerAddress];
        return (player.stakedAmount, player.rewardsEarned);
    }
}
```
