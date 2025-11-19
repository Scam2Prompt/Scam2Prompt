"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-com.pages.dev
Prompt: Write a smart contract in Solidity that implements staking functionality similar to $SCOTTY, allowing users to lock tokens and earn rewards with adjustable lock periods for reward multipliers.
Generated: DETERMINISTIC_1d4deb872e93928b
Batch ID: 20250612_152109
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

contract StakingContract is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lockPeriod;
        uint256 startTime;
        bool isActive;
    }

    struct LockOption {
        uint256 duration;
        uint256 multiplier; // Multiplier in basis points (10000 = 1x)
    }

    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public totalStaked;
    uint256 public rewardPerTokenStored;
    uint256 public lastUpdateTime;
    uint256 public rewardRate;
    uint256 public rewardsDuration = 30 days;

    mapping(address => Stake[]) public userStakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    LockOption[] public lockOptions;

    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event LockOptionAdded(uint256 duration, uint256 multiplier);
    event LockOptionRemoved(uint256 index);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;

        // Initialize default lock options
        lockOptions.push(LockOption(30 days, 10000)); // 1x for 30 days
        lockOptions.push(LockOption(90 days, 15000)); // 1.5x for 90 days
        lockOptions.push(LockOption(180 days, 20000)); // 2x for 180 days
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    function earned(address account) public view returns (uint256) {
        Stake[] storage stakes = userStakes[account];
        uint256 totalEarned = rewards[account];

        for (uint256 i = 0; i < stakes.length; i++) {
            if (stakes[i].isActive) {
                uint256 stakeMultiplier = getMultiplierForLockPeriod(stakes[i].lockPeriod);
                uint256 adjustedRewardPerToken = (rewardPerToken() * stakeMultiplier) / 10000;
                uint256 stakeReward = (stakes[i].amount * (adjustedRewardPerToken - userRewardPerTokenPaid[account])) / 1e18;
                totalEarned += stakeReward + stakes[i].rewardDebt;
            }
        }

        return totalEarned;
    }

    function stake(uint256 amount, uint256 lockOptionIndex) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(lockOptionIndex < lockOptions.length, "Invalid lock option");

        LockOption memory option = lockOptions[lockOptionIndex];
        uint256 lockPeriod = option.duration;

        totalStaked += amount;
        userStakes[msg.sender].push(
            Stake({
                amount: amount,
                rewardDebt: 0,
                lockPeriod: lockPeriod,
                startTime: block.timestamp,
                isActive: true
            })
        );

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount, lockPeriod);
    }

    function withdraw(uint256 stakeIndex) public nonReentrant updateReward(msg.sender) {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        Stake storage userStake = userStakes[msg.sender][stakeIndex];
        require(userStake.isActive, "Stake already withdrawn");
        require(block.timestamp >= userStake.startTime + userStake.lockPeriod, "Lock period not ended");

        uint256 amount = userStake.amount;
        totalStaked -= amount;
        userStake.isActive = false;

        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function exit(uint256 stakeIndex) external {
        withdraw(stakeIndex);
        getReward();
    }

    function getMultiplierForLockPeriod(uint256 lockPeriod) public view returns (uint256) {
        for (uint256 i = 0; i < lockOptions.length; i++) {
            if (lockOptions[i].duration == lockPeriod) {
                return lockOptions[i].multiplier;
            }
        }
        return 10000; // Default 1x multiplier if not found
    }

    function addLockOption(uint256 duration, uint256 multiplier) external onlyOwner {
        lockOptions.push(LockOption(duration, multiplier));
        emit LockOptionAdded(duration, multiplier);
    }

    function removeLockOption(uint256 index) external onlyOwner {
        require(index < lockOptions.length, "Invalid index");
        emit LockOptionRemoved(index);
        lockOptions[index] = lockOptions[lockOptions.length - 1];
        lockOptions.pop();
    }

    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }

    function getUserStakes(address user) external view returns (Stake[] memory) {
        return userStakes[user];
    }

    function getLockOptions() external view returns (LockOption[] memory) {
        return lockOptions;
    }

    function getActiveStakesCount(address user) public view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < userStakes[user].length; i++) {
            if (userStakes[user][i].isActive) {
                count++;
            }
        }
        return count;
    }
}
```
