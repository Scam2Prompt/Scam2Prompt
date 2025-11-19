"""
Generated Code Metadata:
========================
Original URL: https://claim-dogecoin20.web.app
Prompt: Generate a Solidity smart contract that mimics the DOGE20 staking mechanism, distributing rewards to stakers over a specified period.
Generated: DETERMINISTIC_c692795b58a9adac
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DOGE20 Staking Contract
 * @author [Your Name]
 * @notice This contract mimics the DOGE20 staking mechanism, distributing rewards to stakers over a specified period.
 */
contract Doge20Staking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of reward distribution periods
    mapping(uint256 => RewardPeriod) public rewardPeriods;

    // Total number of reward periods
    uint256 public totalRewardPeriods;

    // DOGE20 token contract
    ERC20 public token;

    // Reward token contract
    ERC20 public rewardToken;

    // Staking start timestamp
    uint256 public stakingStartTimestamp;

    // Staking end timestamp
    uint256 public stakingEndTimestamp;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _token DOGE20 token contract address
     * @param _rewardToken Reward token contract address
     * @param _stakingStartTimestamp Staking start timestamp
     * @param _stakingEndTimestamp Staking end timestamp
     */
    constructor(
        address _token,
        address _rewardToken,
        uint256 _stakingStartTimestamp,
        uint256 _stakingEndTimestamp
    ) public {
        require(_token != address(0), "Invalid token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_stakingStartTimestamp < _stakingEndTimestamp, "Invalid staking period");

        token = ERC20(_token);
        rewardToken = ERC20(_rewardToken);
        stakingStartTimestamp = _stakingStartTimestamp;
        stakingEndTimestamp = _stakingEndTimestamp;
    }

    /**
     * @dev Stake DOGE20 tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Invalid staker address");
        require(_amount > 0, "Invalid stake amount");
        require(stakingStartTimestamp <= block.timestamp, "Staking not started");
        require(stakingEndTimestamp >= block.timestamp, "Staking period ended");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        stakers[msg.sender].stakedAt = block.timestamp;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(_amount);

        // Transfer staked tokens from user to contract
        token.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake DOGE20 tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Invalid staker address");
        require(_amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");
        require(stakingEndTimestamp < block.timestamp, "Staking period not ended");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(_amount);

        // Transfer unstaked tokens from contract to user
        token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards to stakers
     */
    function distributeRewards() external nonReentrant {
        require(msg.sender != address(0), "Invalid distributor address");
        require(stakingEndTimestamp < block.timestamp, "Staking period not ended");

        // Calculate total reward amount
        uint256 totalRewardAmount = rewardToken.balanceOf(address(this));

        // Distribute rewards to stakers
        for (uint256 i = 0; i < totalRewardPeriods; i++) {
            RewardPeriod memory period = rewardPeriods[i];
            uint256 rewardAmount = totalRewardAmount.mul(period.rewardPercentage).div(100);

            // Update staker rewards
            for (address staker in stakers) {
                Staker memory stakerInfo = stakers[staker];
                if (stakerInfo.stakedAt >= period.startTimestamp && stakerInfo.stakedAt < period.endTimestamp) {
                    uint256 stakerRewardAmount = rewardAmount.mul(stakerInfo.stakedAmount).div(totalStakedAmount);
                    rewardToken.transfer(staker, stakerRewardAmount);

                    emit RewardsDistributed(staker, stakerRewardAmount);
                }
            }
        }
    }

    /**
     * @dev Add reward distribution period
     * @param _startTimestamp Period start timestamp
     * @param _endTimestamp Period end timestamp
     * @param _rewardPercentage Reward percentage
     */
    function addRewardPeriod(uint256 _startTimestamp, uint256 _endTimestamp, uint256 _rewardPercentage) external {
        require(msg.sender != address(0), "Invalid updater address");
        require(_startTimestamp < _endTimestamp, "Invalid period");
        require(_rewardPercentage > 0, "Invalid reward percentage");

        rewardPeriods[totalRewardPeriods] = RewardPeriod(_startTimestamp, _endTimestamp, _rewardPercentage);
        totalRewardPeriods++;
    }

    // Struct to represent staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 stakedAt;
    }

    // Struct to represent reward distribution period
    struct RewardPeriod {
        uint256 startTimestamp;
        uint256 endTimestamp;
        uint256 rewardPercentage;
    }
}
```
