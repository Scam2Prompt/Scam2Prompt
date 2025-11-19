"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: "Design a simple staking system in Solidity for $MTE token holders to earn rewards from a staking rewards pool funded by trading tax, with a percentage of tax revenue allocated to the pool."
Generated: DETERMINISTIC_151fccaf0706caed
Batch ID: 20250622_210806
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

contract MTEStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Staking token (MTE)
    IERC20 public stakingToken;
    
    // Reward token (MTE)
    IERC20 public rewardToken;
    
    // Staking period in seconds (e.g., 30 days)
    uint256 public stakingPeriod;
    
    // Reward rate (percentage of pool distributed per staking period)
    uint256 public rewardRate;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Total rewards distributed
    uint256 public totalRewardsDistributed;
    
    // Staking pool balance
    uint256 public stakingPoolBalance;
    
    // Last update timestamp
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // User staking info
    struct Staker {
        uint256 balance;
        uint256 rewards;
        uint256 rewardPerTokenPaid;
        uint256 stakingStartTime;
    }
    
    // Mapping of user to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardPoolFunded(uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event StakingPeriodUpdated(uint256 newPeriod);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingPeriod,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_stakingPeriod > 0, "Staking period must be greater than 0");
        require(_rewardRate > 0 && _rewardRate <= 100, "Reward rate must be between 1 and 100");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        stakingPeriod = _stakingPeriod;
        rewardRate = _rewardRate;
    }

    // Update reward for a given account
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        
        if (account != address(0)) {
            stakers[account].rewards = earned(account);
            stakers[account].rewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / stakingPeriod / 100
        );
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Staker memory staker = stakers[account];
        return staker.balance * (rewardPerToken() - staker.rewardPerTokenPaid) / 1e18 + staker.rewards;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        Staker storage staker = stakers[msg.sender];
        staker.balance += amount;
        staker.stakingStartTime = block.timestamp;
        totalStaked += amount;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.balance >= amount, "Insufficient balance");
        require(block.timestamp >= staker.stakingStartTime + stakingPeriod, "Staking period not completed");

        staker.balance -= amount;
        totalStaked -= amount;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakers[msg.sender].rewards;
        require(reward > 0, "No rewards to claim");
        
        stakers[msg.sender].rewards = 0;
        totalRewardsDistributed += reward;
        stakingPoolBalance -= reward;
        
        rewardToken.safeTransfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Fund the staking pool (can be called by tax contract)
    function fundRewardPool(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        stakingPoolBalance += amount;
        rewardToken.safeTransferFrom(msg.sender, address(this), amount);
        emit RewardPoolFunded(amount);
    }

    // Set reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0 && _rewardRate <= 100, "Reward rate must be between 1 and 100");
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Set staking period (only owner)
    function setStakingPeriod(uint256 _stakingPeriod) external onlyOwner {
        require(_stakingPeriod > 0, "Staking period must be greater than 0");
        stakingPeriod = _stakingPeriod;
        emit StakingPeriodUpdated(_stakingPeriod);
    }

    // Withdraw any ERC20 tokens (only owner, for emergency)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken), 
            "Cannot withdraw staking or reward tokens");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
