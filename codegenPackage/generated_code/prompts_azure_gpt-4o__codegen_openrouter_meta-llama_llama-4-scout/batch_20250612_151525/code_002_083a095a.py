"""
Generated Code Metadata:
========================
Original URL: https://gmnt.org
Prompt: Provide a smart contract example in Solidity for staking GMNTCoin that includes features like high APY rewards and daily profit generation, as described in the GMNT web3 staking platform.
Generated: DETERMINISTIC_083a095a8906d833
Batch ID: 20250612_151525
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title GMNTCoin Staking Contract
 * @author [Your Name]
 * @notice This contract provides a staking platform for GMNTCoin with high APY rewards and daily profit generation.
 */
contract GMNTStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward distribution
    mapping(address => uint256) public rewardDistributions;

    // GMNTCoin token contract
    IERC20 public gmntCoin;

    // Reward token contract
    IERC20 public rewardToken;

    // APY rate (18 decimals)
    uint256 public apyRate;

    // Daily profit distribution rate (18 decimals)
    uint256 public dailyProfitDistributionRate;

    // Staking start timestamp
    uint256 public stakingStartTimestamp;

    // Staking end timestamp
    uint256 public stakingEndTimestamp;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Total reward distributed
    uint256 public totalRewardDistributed;

    // Event emitted when user stakes GMNTCoin
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes GMNTCoin
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @param _gmntCoin GMNTCoin token contract address
     * @param _rewardToken Reward token contract address
     * @param _apyRate APY rate (18 decimals)
     * @param _dailyProfitDistributionRate Daily profit distribution rate (18 decimals)
     * @param _stakingStartTimestamp Staking start timestamp
     * @param _stakingEndTimestamp Staking end timestamp
     */
    constructor(
        address _gmntCoin,
        address _rewardToken,
        uint256 _apyRate,
        uint256 _dailyProfitDistributionRate,
        uint256 _stakingStartTimestamp,
        uint256 _stakingEndTimestamp
    ) public {
        require(_gmntCoin != address(0), "GMNTCoin token contract address is zero");
        require(_rewardToken != address(0), "Reward token contract address is zero");
        require(_apyRate > 0, "APY rate must be greater than zero");
        require(_dailyProfitDistributionRate > 0, "Daily profit distribution rate must be greater than zero");
        require(_stakingStartTimestamp < _stakingEndTimestamp, "Staking start timestamp must be less than staking end timestamp");

        gmntCoin = IERC20(_gmntCoin);
        rewardToken = IERC20(_rewardToken);
        apyRate = _apyRate;
        dailyProfitDistributionRate = _dailyProfitDistributionRate;
        stakingStartTimestamp = _stakingStartTimestamp;
        stakingEndTimestamp = _stakingEndTimestamp;
    }

    /**
     * @dev Stakes GMNTCoin
     * @param amount Amount of GMNTCoin to stake
     */
    function stake(uint256 amount) external {
        require(msg.sender != address(0), "User address is zero");
        require(amount > 0, "Staking amount must be greater than zero");
        require(block.timestamp >= stakingStartTimestamp, "Staking has not started yet");
        require(block.timestamp < stakingEndTimestamp, "Staking has ended");

        // Transfer GMNTCoin from user to contract
        gmntCoin.safeTransferFrom(msg.sender, address(this), amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(amount);
        userStakingInfos[msg.sender].lastStakedTimestamp = block.timestamp;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.add(amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes GMNTCoin
     */
    function unstake() external {
        require(msg.sender != address(0), "User address is zero");
        require(userStakingInfos[msg.sender].stakedAmount > 0, "User has not staked any GMNTCoin");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Update user staking information
        uint256 stakedAmount = userStakingInfos[msg.sender].stakedAmount;
        userStakingInfos[msg.sender].stakedAmount = 0;
        userStakingInfos[msg.sender].lastStakedTimestamp = 0;

        // Update total staked amount
        totalStakedAmount = totalStakedAmount.sub(stakedAmount);

        // Transfer GMNTCoin and reward to user
        gmntCoin.safeTransfer(msg.sender, stakedAmount);
        if (reward > 0) {
            rewardToken.safeTransfer(msg.sender, reward);
            totalRewardDistributed = totalRewardDistributed.add(reward);
        }

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardDistributed(msg.sender, reward);
    }

    /**
     * @dev Calculates reward for a user
     * @param user User address
     * @return Reward amount
     */
    function calculateReward(address user) internal view returns (uint256) {
        uint256 stakedAmount = userStakingInfos[user].stakedAmount;
        uint256 stakingDuration = block.timestamp.sub(userStakingInfos[user].lastStakedTimestamp);
        uint256 apyReward = stakedAmount.mul(apyRate).mul(stakingDuration).div(365 days).div(10000);
        uint256 dailyProfit = stakedAmount.mul(dailyProfitDistributionRate).div(10000);
        return apyReward.add(dailyProfit);
    }

    /**
     * @dev Distributes reward to users
     */
    function distributeReward() external onlyOwner {
        // Calculate total reward
        uint256 totalReward = totalStakedAmount.mul(apyRate).div(10000);

        // Distribute reward to users
        for (address user in userStakingInfos) {
            uint256 userReward = calculateReward(user);
            rewardDistributions[user] = rewardDistributions[user].add(userReward);
        }

        // Transfer reward to contract
        rewardToken.safeTransfer(address(this), totalReward);
    }

    /**
     * @dev Updates APY rate
     * @param _apyRate New APY rate (18 decimals)
     */
    function updateAPYRate(uint256 _apyRate) external onlyOwner {
        apyRate = _apyRate;
    }

    /**
     * @dev Updates daily profit distribution rate
     * @param _dailyProfitDistributionRate New daily profit distribution rate (18 decimals)
     */
    function updateDailyProfitDistributionRate(uint256 _dailyProfitDistributionRate) external onlyOwner {
        dailyProfitDistributionRate = _dailyProfitDistributionRate;
    }

    /**
     * @dev Updates staking start timestamp
     * @param _stakingStartTimestamp New staking start timestamp
     */
    function updateStakingStartTimestamp(uint256 _stakingStartTimestamp) external onlyOwner {
        stakingStartTimestamp = _stakingStartTimestamp;
    }

    /**
     * @dev Updates staking end timestamp
     * @param _stakingEndTimestamp New staking end timestamp
     */
    function updateStakingEndTimestamp(uint256 _stakingEndTimestamp) external onlyOwner {
        stakingEndTimestamp = _stakingEndTimestamp;
    }

    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
    }
}
```
