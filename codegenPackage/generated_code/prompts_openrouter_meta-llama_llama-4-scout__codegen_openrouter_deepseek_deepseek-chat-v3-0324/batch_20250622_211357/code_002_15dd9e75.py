"""
Generated Code Metadata:
========================
Original URL: https://bskt-staking.vercel.app
Prompt: Generate a smart contract code snippet in Solidity that implements a staking mechanism with a rewards pool, similar to the BSKT staking platform, with a time multiplier for locked tokens.
Generated: DETERMINISTIC_15dd9e75d9d9149e
Batch ID: 20250622_211357
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lockPeriod;     // Lock period in seconds
        uint256 stakeTime;      // Timestamp when tokens were staked
        bool isLocked;          // Whether tokens are locked
    }

    // Reward token and staking token interfaces
    IERC20 public rewardToken;
    IERC20 public stakingToken;

    // Staking parameters
    uint256 public rewardRate;          // Reward rate per second
    uint256 public lastUpdateTime;      // Last time rewards were calculated
    uint256 public rewardPerTokenStored; // Accumulated rewards per token
    uint256 public totalStaked;         // Total tokens staked

    // Time multiplier parameters
    uint256 public constant MAX_LOCK_PERIOD = 365 days; // Maximum lock period
    uint256 public constant MIN_LOCK_PERIOD = 7 days;   // Minimum lock period
    uint256 public constant MULTIPLIER_BASE = 1e18;     // Base for multiplier calculations

    // Mapping from staker address to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakingToken, address _rewardToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }

    // Calculate current reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored.add(
            (block.timestamp.sub(lastUpdateTime)).mul(rewardRate).mul(1e18).div(totalStaked)
        );
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Staker memory staker = stakers[account];
        uint256 currentRewardPerToken = rewardPerToken();
        return staker.amount.mul(currentRewardPerToken.sub(staker.rewardDebt)).div(1e18);
    }

    // Calculate time multiplier based on lock period
    function calculateMultiplier(uint256 lockPeriod) public pure returns (uint256) {
        require(lockPeriod >= MIN_LOCK_PERIOD && lockPeriod <= MAX_LOCK_PERIOD, "Invalid lock period");
        return MULTIPLIER_BASE.add(lockPeriod.mul(MULTIPLIER_BASE).div(MAX_LOCK_PERIOD));
    }

    // Stake tokens with optional lock period
    function stake(uint256 amount, uint256 lockPeriod) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(lockPeriod == 0 || (lockPeriod >= MIN_LOCK_PERIOD && lockPeriod <= MAX_LOCK_PERIOD), "Invalid lock period");

        Staker storage staker = stakers[msg.sender];
        
        if (staker.amount > 0) {
            claimReward();
        }

        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        staker.amount = staker.amount.add(amount);
        staker.rewardDebt = staker.amount.mul(rewardPerTokenStored).div(1e18);
        
        if (lockPeriod > 0) {
            staker.lockPeriod = lockPeriod;
            staker.stakeTime = block.timestamp;
            staker.isLocked = true;
        }

        totalStaked = totalStaked.add(amount);
        emit Staked(msg.sender, amount, lockPeriod);
    }

    // Unstake tokens
    function unstake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Cannot unstake 0");
        require(staker.amount >= amount, "Insufficient staked balance");

        if (staker.isLocked) {
            require(block.timestamp >= staker.stakeTime.add(staker.lockPeriod), "Tokens are still locked");
            staker.isLocked = false;
        }

        claimReward();

        staker.amount = staker.amount.sub(amount);
        staker.rewardDebt = staker.amount.mul(rewardPerTokenStored).div(1e18);
        totalStaked = totalStaked.sub(amount);

        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = stakers[msg.sender].amount.mul(rewardPerTokenStored).div(1e18);
            rewardToken.transfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    // Update reward rate (only callable by owner in production)
    function updateRewardRate(uint256 newRate) external updateReward(address(0)) {
        require(newRate > 0, "Reward rate must be positive");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    // Emergency withdraw without rewards (for locked tokens after lock period)
    function emergencyWithdraw() external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No tokens staked");
        require(!staker.isLocked || block.timestamp >= staker.stakeTime.add(staker.lockPeriod), "Tokens are still locked");

        uint256 amount = staker.amount;
        staker.amount = 0;
        staker.rewardDebt = 0;
        totalStaked = totalStaked.sub(amount);

        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }
}
```
