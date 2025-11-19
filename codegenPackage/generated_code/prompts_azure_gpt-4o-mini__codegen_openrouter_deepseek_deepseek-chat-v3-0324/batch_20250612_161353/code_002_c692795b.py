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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DOGE20Staking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Struct to represent a staker
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastStakeTime;  // Last time tokens were staked
    }

    // Staking token (DOGE20)
    IERC20 public stakingToken;
    
    // Reward token (could be same as staking token)
    IERC20 public rewardToken;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Duration of reward distribution period (in seconds)
    uint256 public rewardDuration;
    
    // Timestamp when rewards end
    uint256 public periodFinish;
    
    // Last time reward was updated
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Mapping of staker addresses to their info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardAdded(uint256 reward);
    event RewardDurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardDuration
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_rewardDuration > 0, "Reward duration must be greater than 0");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        rewardDuration = _rewardDuration;
    }

    // Update reward variables
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
            stakers[account].lastStakeTime = block.timestamp;
        }
        _;
    }

    // Get the last time reward is applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < periodFinish ? block.timestamp : periodFinish;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored.add(
                lastTimeRewardApplicable()
                    .sub(lastUpdateTime)
                    .mul(rewardRate)
                    .mul(1e18)
                    .div(totalStaked)
            );
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return
            stakers[account]
                .amount
                .mul(rewardPerToken().sub(stakers[account].rewardDebt))
                .div(1e18)
                .add(stakers[account].rewardDebt);
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        stakers[msg.sender].amount = stakers[msg.sender].amount.add(amount);
        totalStaked = totalStaked.add(amount);
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakers[msg.sender].amount >= amount, "Insufficient balance");
        
        stakers[msg.sender].amount = stakers[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(stakers[msg.sender].amount);
        getReward();
    }

    // Notify reward amount to extend or start new reward period
    function notifyRewardAmount(uint256 reward) external updateReward(address(0)) {
        require(reward > 0, "No reward");
        
        if (block.timestamp >= periodFinish) {
            rewardRate = reward.div(rewardDuration);
        } else {
            uint256 remaining = periodFinish.sub(block.timestamp);
            uint256 leftover = remaining.mul(rewardRate);
            rewardRate = reward.add(leftover).div(rewardDuration);
        }

        // Ensure the provided reward amount is not more than the balance
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardRate <= balance.div(rewardDuration), "Reward too high");

        lastUpdateTime = block.timestamp;
        periodFinish = block.timestamp.add(rewardDuration);
        emit RewardAdded(reward);
    }

    // Update reward duration (only callable by owner in a real implementation)
    function setRewardDuration(uint256 _rewardDuration) external {
        require(block.timestamp > periodFinish, "Previous rewards not complete");
        require(_rewardDuration > 0, "Duration must be > 0");
        
        rewardDuration = _rewardDuration;
        emit RewardDurationUpdated(_rewardDuration);
    }

    // Get staked amount for an account
    function balanceOf(address account) external view returns (uint256) {
        return stakers[account].amount;
    }
}
```
