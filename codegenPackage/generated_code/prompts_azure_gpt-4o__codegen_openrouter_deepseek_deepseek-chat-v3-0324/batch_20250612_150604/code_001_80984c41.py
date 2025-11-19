"""
Generated Code Metadata:
========================
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Create a staking system called "Iceberg Growing" where token holders can stake their tokens and earn rewards over time, inspired by the Pingu token's staking mechanism.
Generated: DETERMINISTIC_80984c414742fdaa
Batch ID: 20250612_150604
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

contract IcebergGrowing is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The staking token
    IERC20 public immutable stakingToken;
    // The reward token
    IERC20 public immutable rewardToken;

    // Reward rate per second
    uint256 public rewardRate;
    // Duration of reward distribution in seconds
    uint256 public rewardDuration;
    // Timestamp when rewards end
    uint256 public periodFinish;
    // Last time reward was updated
    uint256 public lastUpdateTime;
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    // Total staked amount
    uint256 public totalStaked;

    // Reward per token paid for each user
    mapping(address => uint256) public userRewardPerTokenPaid;
    // Pending rewards for each user
    mapping(address => uint256) public rewards;
    // Staking details for each user
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event RewardDurationUpdated(uint256 newDuration);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _rewardDuration
    ) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        require(_rewardDuration > 0, "Reward duration must be greater than zero");

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
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
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
            rewardPerTokenStored +
            (((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalStaked);
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return
            ((stakes[account].amount * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        // Update stake details
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastStakeTime = block.timestamp;
        totalStaked += amount;

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update stake details
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    // Update reward rate (owner only)
    function setRewardRate(uint256 _rewardRate) external onlyOwner updateReward(address(0)) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        
        // Update rewards before changing rate
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        
        rewardRate = _rewardRate;
        periodFinish = block.timestamp + rewardDuration;
        
        emit RewardRateUpdated(_rewardRate);
    }

    // Update reward duration (owner only)
    function setRewardDuration(uint256 _rewardDuration) external onlyOwner {
        require(_rewardDuration > 0, "Reward duration must be greater than zero");
        require(block.timestamp > periodFinish, "Previous rewards must be completed");
        
        rewardDuration = _rewardDuration;
        emit RewardDurationUpdated(_rewardDuration);
    }

    // Recover any ERC20 tokens sent to the contract by mistake (owner only)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        require(tokenAddress != address(rewardToken) || block.timestamp > periodFinish + 30 days, 
            "Cannot withdraw reward token within 30 days after period finish");
        
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }

    // Notify reward amount (alternative to setRewardRate)
    function notifyRewardAmount(uint256 reward) external onlyOwner updateReward(address(0)) {
        require(block.timestamp >= periodFinish, "Previous rewards must be completed");
        
        uint256 balance = rewardToken.balanceOf(address(this));
        require(rewardRate <= balance / rewardDuration, "Provided reward too high");

        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        periodFinish = block.timestamp + rewardDuration;
    }
}
```
