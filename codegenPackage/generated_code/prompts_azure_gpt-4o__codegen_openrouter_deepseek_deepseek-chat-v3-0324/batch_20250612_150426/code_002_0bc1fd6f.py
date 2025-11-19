"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Create a smart contract in Solidity for managing KI Token rewards based on player activity, including staking and earning mechanisms as described in Genopets.
Generated: DETERMINISTIC_0bc1fd6fa38a3725
Batch ID: 20250612_150426
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract KITokenRewards is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store player information
    struct Player {
        uint256 stakedAmount;
        uint256 lastClaimTime;
        uint256 accumulatedRewards;
        uint256 rewardDebt;
    }

    // The KI Token contract
    IERC20 public kiToken;

    // Reward rate per second per token staked
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Precision factor for reward calculations
    uint256 private constant PRECISION = 1e18;

    // Mapping from player address to player info
    mapping(address => Player) public players;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _kiToken, uint256 _rewardRate) {
        require(_kiToken != address(0), "Invalid token address");
        kiToken = IERC20(_kiToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake KI Tokens to start earning rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");

        Player storage player = players[msg.sender];
        _updateRewards(msg.sender);

        player.stakedAmount += amount;
        totalStaked += amount;

        kiToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake KI Tokens and claim pending rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 tokens");

        Player storage player = players[msg.sender];
        require(player.stakedAmount >= amount, "Insufficient staked amount");

        _updateRewards(msg.sender);

        player.stakedAmount -= amount;
        totalStaked -= amount;

        kiToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Player storage player = players[msg.sender];
        _updateRewards(msg.sender);

        uint256 rewardsToClaim = player.accumulatedRewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        player.accumulatedRewards = 0;
        kiToken.safeTransfer(msg.sender, rewardsToClaim);

        emit RewardClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Update reward rate (only owner)
     * @param newRate New reward rate per second per token
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Calculate pending rewards for a player
     * @param playerAddress Address of the player
     * @return Pending rewards
     */
    function pendingRewards(address playerAddress) public view returns (uint256) {
        Player storage player = players[playerAddress];
        uint256 stakedAmount = player.stakedAmount;

        if (stakedAmount == 0) {
            return player.accumulatedRewards;
        }

        uint256 timeElapsed = block.timestamp - player.lastClaimTime;
        uint256 newRewards = (stakedAmount * rewardRate * timeElapsed) / PRECISION;

        return player.accumulatedRewards + newRewards;
    }

    /**
     * @dev Internal function to update player rewards
     * @param playerAddress Address of the player
     */
    function _updateRewards(address playerAddress) internal {
        Player storage player = players[playerAddress];
        uint256 rewards = pendingRewards(playerAddress);

        player.accumulatedRewards = rewards;
        player.lastClaimTime = block.timestamp;
    }

    /**
     * @dev Emergency withdraw all tokens (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = kiToken.balanceOf(address(this));
        kiToken.safeTransfer(owner(), balance);
    }
}
```
