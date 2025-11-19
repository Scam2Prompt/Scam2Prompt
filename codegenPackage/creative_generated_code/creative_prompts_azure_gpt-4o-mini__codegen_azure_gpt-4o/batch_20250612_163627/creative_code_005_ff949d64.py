"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-rx.pages.dev
Prompt: Provide an example of how to implement staking and harvesting of assets in a DApp using the MultiChain Protocol.
Generated: DETERMINISTIC_ff949d649fde1ed1
Batch ID: 20250612_163627
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

/// @title Staking and Harvesting Contract Example
/// @author Developer
/// @notice This contract allows users to stake assets and harvest rewards based on MultiChain protocol.
/// @dev This example assumes the use of ERC20 tokens for staking and rewards.

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingDApp is Ownable, ReentrancyGuard {
    // ERC20 token used for staking
    IERC20 public stakingToken;
    
    // ERC20 token used for rewards
    IERC20 public rewardToken;

    // Reward rate (tokens per second per staked token)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staked balance
    mapping(address => uint256) public stakedBalance;

    // Mapping of user address to last harvest timestamp
    mapping(address => uint256) public lastHarvest;

    /// @notice Constructor to initialize contract parameters
    /// @param _stakingToken Address of the staking token (ERC20)
    /// @param _rewardToken Address of the reward token (ERC20)
    /// @param _rewardRate Reward rate per second per staked token
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
    }

    /// @notice Event emitted when tokens are staked
    /// @param user Address of the user who staked tokens
    /// @param amount Amount of tokens staked
    event Staked(address indexed user, uint256 amount);

    /// @notice Event emitted when rewards are harvested
    /// @param user Address of the user who harvested rewards
    /// @param reward Amount of rewards harvested
    event Harvested(address indexed user, uint256 reward);

    /// @notice Event emitted when tokens are unstaked
    /// @param user Address of the user who unstaked tokens
    /// @param amount Amount of tokens unstaked
    event Unstaked(address indexed user, uint256 amount);

    /// @notice Stake tokens into the contract
    /// @param amount Amount of staking tokens to deposit
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");

        // Update user rewards before staking
        _harvestRewards(msg.sender);

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update staked balance and total staked amount
        stakedBalance[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /// @notice Harvest rewards for the caller
    function harvest() external nonReentrant {
        _harvestRewards(msg.sender);
    }

    /// @notice Unstake tokens and harvest rewards simultaneously
    /// @param amount Amount of staking tokens to withdraw
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");

        // Harvest rewards before unstaking
        _harvestRewards(msg.sender);

        // Update staked balance and total staked amount
        stakedBalance[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /// @notice Internal function to calculate and distribute rewards
    /// @param user Address of the user to harvest rewards for
    function _harvestRewards(address user) internal {
        uint256 staked = stakedBalance[user];
        uint256 timeElapsed = block.timestamp - lastHarvest[user];

        // Calculate rewards based on staked amount and elapsed time
        uint256 reward = staked * rewardRate * timeElapsed;

        if (reward > 0) {
            // Transfer rewards to the user
            rewardToken.transfer(user, reward);
            emit Harvested(user, reward);
        }

        // Update last harvest timestamp
        lastHarvest[user] = block.timestamp;
    }

    /// @notice Admin function to update the reward rate
    /// @param newRewardRate New reward rate per second per staked token
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /// @notice Admin function to withdraw excess reward tokens
    /// @param amount Amount of reward tokens to withdraw
    function withdrawExcessRewards(uint256 amount) external onlyOwner {
        rewardToken.transfer(owner(), amount);
    }
}
```
