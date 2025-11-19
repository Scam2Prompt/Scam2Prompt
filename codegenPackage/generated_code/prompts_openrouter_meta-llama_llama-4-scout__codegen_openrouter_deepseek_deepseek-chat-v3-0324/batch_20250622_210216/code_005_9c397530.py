"""
Generated Code Metadata:
========================
Original URL: https://trustpad-c0r.pages.dev
Prompt: Design a staking system for a new token, inspired by TrustPad's levels and staking requirements, and provide a high-level implementation plan.
Generated: DETERMINISTIC_9c397530d977d390
Batch ID: 20250622_210216
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

contract StakingSystem is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct StakingTier {
        string name;
        uint256 minAmount;
        uint256 allocationMultiplier; // Multiplier for allocation (e.g., 1x, 2x, etc.)
        uint256 lockDuration; // Duration in seconds
    }

    struct UserStake {
        uint256 amount;
        uint256 tierIndex;
        uint256 stakedAt;
        uint256 unlockTime;
        uint256 claimedRewards;
    }

    IERC20 public stakingToken;
    IERC20 public rewardToken;

    StakingTier[] public tiers;
    mapping(address => UserStake[]) public userStakes;
    mapping(address => uint256) public userTotalStaked;

    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;

    event Staked(address indexed user, uint256 amount, uint256 tierIndex);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TierAdded(uint256 index, string name, uint256 minAmount, uint256 multiplier, uint256 lockDuration);
    event TierUpdated(uint256 index, string name, uint256 minAmount, uint256 multiplier, uint256 lockDuration);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            _updateUserReward(account);
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    function _updateUserReward(address account) internal {
        uint256 reward = earned(account);
        if (reward > 0) {
            UserStake[] storage stakes = userStakes[account];
            for (uint256 i = 0; i < stakes.length; i++) {
                stakes[i].claimedRewards += reward;
            }
        }
    }

    function earned(address account) public view returns (uint256) {
        UserStake[] storage stakes = userStakes[account];
        uint256 totalReward = 0;
        for (uint256 i = 0; i < stakes.length; i++) {
            UserStake memory stake = stakes[i];
            uint256 stakeReward = (stake.amount * (rewardPerToken() - stake.claimedRewards)) / 1e18;
            totalReward += stakeReward;
        }
        return totalReward;
    }

    function addTier(
        string memory name,
        uint256 minAmount,
        uint256 allocationMultiplier,
        uint256 lockDuration
    ) external onlyOwner {
        tiers.push(StakingTier(name, minAmount, allocationMultiplier, lockDuration));
        emit TierAdded(tiers.length - 1, name, minAmount, allocationMultiplier, lockDuration);
    }

    function updateTier(
        uint256 index,
        string memory name,
        uint256 minAmount,
        uint256 allocationMultiplier,
        uint256 lockDuration
    ) external onlyOwner {
        require(index < tiers.length, "Invalid tier index");
        tiers[index] = StakingTier(name, minAmount, allocationMultiplier, lockDuration);
        emit TierUpdated(index, name, minAmount, allocationMultiplier, lockDuration);
    }

    function stake(uint256 amount, uint256 tierIndex) external nonReentrant updateReward(msg.sender) {
        require(tierIndex < tiers.length, "Invalid tier index");
        StakingTier memory tier = tiers[tierIndex];
        require(amount >= tier.minAmount, "Amount below minimum for tier");

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        userStakes[msg.sender].push(UserStake({
            amount: amount,
            tierIndex: tierIndex,
            stakedAt: block.timestamp,
            unlockTime: block.timestamp + tier.lockDuration,
            claimedRewards: rewardPerTokenStored
        }));

        userTotalStaked[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount, tierIndex);
    }

    function unstake(uint256 stakeIndex) external nonReentrant updateReward(msg.sender) {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        UserStake memory stakeInfo = userStakes[msg.sender][stakeIndex];
        require(block.timestamp >= stakeInfo.unlockTime, "Tokens still locked");

        uint256 amount = stakeInfo.amount;
        
        // Remove the stake from the array
        userStakes[msg.sender][stakeIndex] = userStakes[msg.sender][userStakes[msg.sender].length - 1];
        userStakes[msg.sender].pop();

        userTotalStaked[msg.sender] -= amount;
        totalStaked -= amount;

        stakingToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        require(reward > 0, "No rewards to claim");

        UserStake[] storage stakes = userStakes[msg.sender];
        for (uint256 i = 0; i < stakes.length; i++) {
            stakes[i].claimedRewards = rewardPerTokenStored;
        }

        rewardToken.safeTransfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    function withdrawRewardTokens(uint256 amount) external onlyOwner {
        rewardToken.safeTransfer(msg.sender, amount);
    }

    function getUserStakes(address user) external view returns (UserStake[] memory) {
        return userStakes[user];
    }

    function getTiers() external view returns (StakingTier[] memory) {
        return tiers;
    }
}
```
