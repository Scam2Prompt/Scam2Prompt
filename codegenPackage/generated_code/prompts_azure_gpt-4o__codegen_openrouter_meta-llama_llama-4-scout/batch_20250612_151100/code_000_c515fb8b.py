"""
Generated Code Metadata:
========================
Original URL: https://thedogeverser.pages.dev
Prompt: Write a smart contract for staking $DOGEVERSE tokens on the Ethereum blockchain, ensuring dynamic reward rates based on the duration of staking.
Generated: DETERMINISTIC_c515fb8b191ca46c
Batch ID: 20250612_151100
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DogeverseStaking is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rate configurations
    mapping (uint256 => RewardRateConfig) public rewardRateConfigs;

    // Total staked amount
    uint256 public totalStakedAmount;

    // Number of reward rate configurations
    uint256 public numRewardRateConfigs;

    // $DOGEVERSE token contract
    ERC20 public dogeverseToken;

    // Reward token contract (assuming same as $DOGEVERSE for simplicity)
    ERC20 public rewardToken;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 stakedAt;
        uint256 lastClaimedAt;
    }

    // Struct to hold reward rate configuration
    struct RewardRateConfig {
        uint256 duration; // in seconds
        uint256 rewardRate; // in percentage (e.g., 10 for 10%)
    }

    /**
     * @dev Constructor
     * @param _dogeverseTokenAddress $DOGEVERSE token contract address
     * @param _rewardTokenAddress Reward token contract address
     */
    constructor(address _dogeverseTokenAddress, address _rewardTokenAddress) public {
        dogeverseToken = ERC20(_dogeverseTokenAddress);
        rewardToken = ERC20(_rewardTokenAddress);

        // Initialize reward rate configurations (example: 10% APY for 30 days, 20% APY for 60 days)
        rewardRateConfigs[0] = RewardRateConfig(30 days, 10);
        rewardRateConfigs[1] = RewardRateConfig(60 days, 20);
        numRewardRateConfigs = 2;
    }

    /**
     * @dev Stake $DOGEVERSE tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(dogeverseToken.transferFrom(msg.sender, address(this), _amount), "Failed to transfer tokens");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.add(_amount);
        userStakingInfo.stakedAt = block.timestamp;
        userStakingInfo.lastClaimedAt = block.timestamp;

        totalStakedAmount = totalStakedAmount.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $DOGEVERSE tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.stakedAmount = userStakingInfo.stakedAmount.sub(_amount);

        // Calculate and transfer rewards
        uint256 rewards = calculateRewards(msg.sender);
        userStakingInfo.lastClaimedAt = block.timestamp;
        require(rewardToken.transfer(msg.sender, rewards), "Failed to transfer rewards");

        // Transfer unstaked tokens
        require(dogeverseToken.transfer(msg.sender, _amount), "Failed to transfer tokens");

        totalStakedAmount = totalStakedAmount.sub(_amount);

        emit Unstaked(msg.sender, _amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        UserStakingInfo storage userStakingInfo = userStakingInfos[msg.sender];
        userStakingInfo.lastClaimedAt = block.timestamp;

        require(rewardToken.transfer(msg.sender, rewards), "Failed to transfer rewards");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate rewards for a user
     * @param _user User address
     * @return Rewards amount
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        UserStakingInfo storage userStakingInfo = userStakingInfos[_user];
        uint256 stakedDuration = block.timestamp.sub(userStakingInfo.stakedAt);
        uint256 rewardRate = getRewardRate(stakedDuration);
        uint256 rewards = userStakingInfo.stakedAmount.mul(rewardRate).div(100);

        // Only consider duration from last claim
        uint256 durationSinceLastClaim = block.timestamp.sub(userStakingInfo.lastClaimedAt);
        rewards = rewards.mul(durationSinceLastClaim).div(stakedDuration);

        return rewards;
    }

    /**
     * @dev Get reward rate based on staking duration
     * @param _stakedDuration Staking duration in seconds
     * @return Reward rate in percentage
     */
    function getRewardRate(uint256 _stakedDuration) internal view returns (uint256) {
        for (uint256 i = 0; i < numRewardRateConfigs; i++) {
            RewardRateConfig storage config = rewardRateConfigs[i];
            if (_stakedDuration >= config.duration) {
                return config.rewardRate;
            }
        }

        // Default reward rate (e.g., 5% APY)
        return 5;
    }
}
```
