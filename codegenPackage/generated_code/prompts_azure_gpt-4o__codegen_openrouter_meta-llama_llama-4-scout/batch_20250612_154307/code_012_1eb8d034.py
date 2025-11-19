"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.web.app
Prompt: Generate a Solidity contract that implements a reward distribution mechanism for $STARS holders, based on the MemeVault staking protocol.
Generated: DETERMINISTIC_1eb8d03488adfb2f
Batch ID: 20250612_154307
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StarsRewardDistribution
 * @author [Your Name]
 * @notice A contract for distributing rewards to $STARS holders based on the MemeVault staking protocol.
 */
contract StarsRewardDistribution {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping(address => uint256) public lastClaimTimestamps;

    // Reward token ($STARS)
    IERC20 public rewardToken;

    // Reward distribution rate (per second)
    uint256 public rewardRate;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // MemeVault staking protocol interface
    IMemeVault public memeVault;

    /**
     * @notice Event emitted when a user stakes tokens
     * @param user The user's address
     * @param amount The amount staked
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @notice Event emitted when a user unstakes tokens
     * @param user The user's address
     * @param amount The amount unstaked
     */
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @notice Event emitted when a user claims rewards
     * @param user The user's address
     * @param amount The amount claimed
     */
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _rewardToken The $STARS token address
     * @param _memeVault The MemeVault staking protocol address
     * @param _rewardRate The reward distribution rate (per second)
     */
    constructor(
        address _rewardToken,
        address _memeVault,
        uint256 _rewardRate
    ) {
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_memeVault != address(0), "Invalid MemeVault address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        rewardToken = IERC20(_rewardToken);
        memeVault = IMemeVault(_memeVault);
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake tokens
     * @param amount The amount to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");

        // Transfer tokens from user to contract
        rewardToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(amount);

        // Emit staked event
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens
     * @param amount The amount to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than 0");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(amount);

        // Transfer tokens from contract to user
        rewardToken.safeTransfer(msg.sender, amount);

        // Emit unstaked event
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update user's last claim timestamp
        lastClaimTimestamps[msg.sender] = block.timestamp;

        // Update total rewards distributed
        totalRewardsDistributed = totalRewardsDistributed.add(rewards);

        // Transfer rewards to user
        rewardToken.safeTransfer(msg.sender, rewards);

        // Emit rewards claimed event
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @notice Calculate rewards for a user
     * @param user The user's address
     * @return The rewards amount
     */
    function calculateRewards(address user) public view returns (uint256) {
        // Calculate time elapsed since last claim
        uint256 timeElapsed = block.timestamp.sub(lastClaimTimestamps[user]);

        // Calculate rewards
        uint256 rewards = stakingBalances[user].mul(rewardRate).mul(timeElapsed);

        return rewards;
    }
}

// MemeVault staking protocol interface
interface IMemeVault {
    // Add functions and variables as per the MemeVault staking protocol ABI
}
```
