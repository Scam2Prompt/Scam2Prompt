"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Generate a Solidity code snippet for a staking pool with a 180-day lock term and a 50% boost in investor tier, similar to one of the pools offered on SidusPad.
Generated: DETERMINISTIC_49473936a255710e
Batch ID: 20250622_205836
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

contract StakingPool is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Staking token
    IERC20 public stakingToken;
    
    // Reward token
    IERC20 public rewardToken;
    
    // Staking period in seconds (180 days)
    uint256 public constant LOCK_PERIOD = 180 days;
    
    // Investor tier boost (50%)
    uint256 public constant INVESTOR_BOOST = 50;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Reward rate per second
    uint256 public rewardRate;
    
    // Last update time
    uint256 public lastUpdateTime;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // Reward distribution end time
    uint256 public periodFinish;
    
    // User staking details
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 rewardPerTokenPaid;
        uint256 rewards;
        bool isInvestor;
    }
    
    // Mapping of user to their stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, bool isInvestor);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
        periodFinish = block.timestamp + LOCK_PERIOD;
    }
    
    // Update reward modifier
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakes[account].rewards = earned(account);
            stakes[account].rewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }
    
    // Get last time reward is applicable
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
            ((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) /
            totalStaked;
    }
    
    // Calculate earned rewards for account
    function earned(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        uint256 baseReward = (stake.amount *
            (rewardPerToken() - stake.rewardPerTokenPaid)) / 1e18;
        uint256 totalReward = baseReward + stake.rewards;
        
        // Apply investor boost if applicable
        if (stake.isInvestor) {
            totalReward += (baseReward * INVESTOR_BOOST) / 100;
        }
        
        return totalReward;
    }
    
    // Stake tokens
    function stake(uint256 amount, bool isInvestor) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        require(block.timestamp < periodFinish, "Staking period has ended");
        
        // Transfer tokens from user
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;
        userStake.isInvestor = isInvestor;
        
        // Update total staked
        totalStaked += amount;
        
        emit Staked(msg.sender, amount, isInvestor);
    }
    
    // Withdraw staked tokens
    function withdraw() external nonReentrant updateReward(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");
        require(
            block.timestamp >= userStake.stakedAt + LOCK_PERIOD,
            "Tokens are still locked"
        );
        
        uint256 amount = userStake.amount;
        
        // Update stake
        userStake.amount = 0;
        
        // Update total staked
        totalStaked -= amount;
        
        // Transfer tokens back to user
        stakingToken.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }
    
    // Claim rewards
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewards;
        if (reward > 0) {
            stakes[msg.sender].rewards = 0;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }
    
    // Update reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        lastUpdateTime = block.timestamp;
        emit RewardRateUpdated(newRate);
    }
    
    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(
            tokenAddress != address(stakingToken) && tokenAddress != address(rewardToken),
            "Cannot withdraw staking or reward tokens"
        );
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
