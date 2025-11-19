"""
Generated Code Metadata:
========================
Original URL: https://hyperliquid.gg
Prompt: Create a Solidity-based smart contract for staking HYPE tokens on Hyperliquid, ensuring transparency and user control over rewards distribution.
Generated: DETERMINISTIC_98d6342a566486da
Batch ID: 20250612_142638
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

/**
 * @title HYPE Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake HYPE tokens and distribute rewards transparently.
 */
contract HYPEStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // HYPE token contract
    IERC20 public hypeToken;

    // Reward token contract (assuming it's different from HYPE)
    IERC20 public rewardToken;

    // Mapping of user staking balance
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebts;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward rate per second
    uint256 public rewardRate;

    // Last update timestamp
    uint256 public lastUpdateTimestamp;

    // Reward distribution start timestamp
    uint256 public rewardStartTimestamp;

    // Total staked amount
    uint256 public totalStaked;

    /**
     * @notice Constructor
     * @param _hypeToken HYPE token contract address
     * @param _rewardToken Reward token contract address
     * @param _rewardRate Reward rate per second
     * @param _rewardStartTimestamp Reward distribution start timestamp
     */
    constructor(
        address _hypeToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardStartTimestamp
    ) {
        hypeToken = IERC20(_hypeToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardStartTimestamp = _rewardStartTimestamp;
        lastUpdateTimestamp = block.timestamp;
    }

    /**
     * @notice Stake HYPE tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");

        // Update reward
        updateReward(msg.sender);

        // Transfer HYPE tokens to contract
        hypeToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staking balance and total staked amount
        stakingBalances[msg.sender] += _amount;
        totalStaked += _amount;
    }

    /**
     * @notice Unstake HYPE tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update reward
        updateReward(msg.sender);

        // Update staking balance and total staked amount
        stakingBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer HYPE tokens to user
        hypeToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Update reward
     * @param _user User address
     */
    function updateReward(address _user) internal {
        if (block.timestamp < rewardStartTimestamp) {
            return;
        }

        uint256 reward = (block.timestamp - lastUpdateTimestamp) * rewardRate;
        accRewardPerShare += reward * 1e18 / totalStaked;
        lastUpdateTimestamp = block.timestamp;

        if (_user != address(0) && stakingBalances[_user] > 0) {
            uint256 userReward = stakingBalances[_user] * (accRewardPerShare - rewardDebts[_user]) / 1e18;
            rewardDebts[_user] = accRewardPerShare;
        }
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        updateReward(msg.sender);

        uint256 reward = stakingBalances[msg.sender] * (accRewardPerShare - rewardDebts[msg.sender]) / 1e18;
        require(reward > 0, "No reward to claim");

        rewardDebts[msg.sender] = accRewardPerShare;

        // Transfer reward to user
        rewardToken.safeTransfer(msg.sender, reward);
    }

    /**
     * @notice Update reward rate
     * @param _newRewardRate New reward rate per second
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @notice Update reward distribution start timestamp
     * @param _newRewardStartTimestamp New reward distribution start timestamp
     */
    function updateRewardStartTimestamp(uint256 _newRewardStartTimestamp) external onlyOwner {
        rewardStartTimestamp = _newRewardStartTimestamp;
    }
}
```
