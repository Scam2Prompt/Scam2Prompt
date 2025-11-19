"""
Generated Code Metadata:
========================
Original URL: https://shibasaga-io.web.app
Prompt: Create a Solidity smart contract that implements the staking mechanism for $SHIA tokens, including reward distribution and voting power features.
Generated: DETERMINISTIC_f63bc3755b363716
Batch ID: 20250612_161617
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SHIAStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastStakeTime;  // Last stake timestamp
        uint256 votingPower;    // Voting power based on stake
    }

    // The SHIA token contract
    IERC20 public immutable shiaToken;

    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Accumulated rewards per share
    uint256 public accRewardPerShare;

    // Minimum stake duration in seconds
    uint256 public minStakeDuration;

    // Last update time for rewards
    uint256 public lastUpdateTime;

    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeDurationUpdated(uint256 newDuration);

    constructor(
        address _shiaToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeDuration
    ) {
        require(_shiaToken != address(0), "SHIA token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_minStakeDuration > 0, "Min stake duration must be greater than zero");

        shiaToken = IERC20(_shiaToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakeDuration = _minStakeDuration;
        lastUpdateTime = block.timestamp;
    }

    // Update the reward variables
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 timePassed = block.timestamp - lastUpdateTime;
            uint256 rewards = timePassed * rewardRate;
            accRewardPerShare += (rewards * 1e18) / totalStaked;
            lastUpdateTime = block.timestamp;
        }
        _;
    }

    // Stake SHIA tokens
    function stake(uint256 _amount) external nonReentrant updateRewards {
        require(_amount > 0, "Amount must be greater than zero");
        
        Staker storage staker = stakers[msg.sender];
        
        // Claim any pending rewards first
        if (staker.amount > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        shiaToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staker's information
        staker.amount += _amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e18;
        staker.lastStakeTime = block.timestamp;
        staker.votingPower = calculateVotingPower(staker.amount, block.timestamp - staker.lastStakeTime);

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Unstake SHIA tokens
    function unstake(uint256 _amount) external nonReentrant updateRewards {
        require(_amount > 0, "Amount must be greater than zero");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");
        require(block.timestamp >= staker.lastStakeTime + minStakeDuration, "Minimum stake duration not reached");

        // Claim any pending rewards first
        _claimRewards();

        // Update staker's information
        staker.amount -= _amount;
        staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e18;
        staker.votingPower = calculateVotingPower(staker.amount, block.timestamp - staker.lastStakeTime);

        // Update total staked
        totalStaked -= _amount;

        // Transfer tokens back to user
        shiaToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Claim rewards
    function claimRewards() external nonReentrant updateRewards {
        _claimRewards();
    }

    // Internal function to claim rewards
    function _claimRewards() internal {
        Staker storage staker = stakers[msg.sender];
        if (staker.amount == 0) return;

        uint256 pending = ((staker.amount * accRewardPerShare) / 1e18) - staker.rewardDebt;
        if (pending > 0) {
            staker.rewardDebt = (staker.amount * accRewardPerShare) / 1e18;
            rewardToken.safeTransfer(msg.sender, pending);
            totalRewardsDistributed += pending;
            emit RewardClaimed(msg.sender, pending);
        }
    }

    // Calculate voting power based on amount and duration
    function calculateVotingPower(uint256 amount, uint256 duration) public pure returns (uint256) {
        // Simple linear scaling - can be replaced with more complex formula
        return amount * (1 + (duration / 1 days));
    }

    // Get pending rewards for a user
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        if (staker.amount == 0) return 0;

        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (totalStaked > 0) {
            uint256 timePassed = block.timestamp - lastUpdateTime;
            uint256 rewards = timePassed * rewardRate;
            currentAccRewardPerShare += (rewards * 1e18) / totalStaked;
        }

        return ((staker.amount * currentAccRewardPerShare) / 1e18) - staker.rewardDebt;
    }

    // Get voting power for a user
    function getVotingPower(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        return calculateVotingPower(staker.amount, block.timestamp - staker.lastStakeTime);
    }

    // Owner functions

    // Update reward rate
    function setRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate != rewardRate, "New rate must be different");
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    // Update minimum stake duration
    function setMinStakeDuration(uint256 _newDuration) external onlyOwner {
        require(_newDuration != minStakeDuration, "New duration must be different");
        minStakeDuration = _newDuration;
        emit MinStakeDurationUpdated(_newDuration);
    }

    // Emergency withdraw rewards (owner only)
    function emergencyWithdrawRewards(uint256 _amount) external onlyOwner {
        require(_amount <= rewardToken.balanceOf(address(this)), "Insufficient reward balance");
        rewardToken.safeTransfer(owner(), _amount);
    }
}
```
