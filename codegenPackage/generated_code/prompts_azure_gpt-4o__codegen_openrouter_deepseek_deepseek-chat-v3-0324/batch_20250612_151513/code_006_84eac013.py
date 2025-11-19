"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Generate code for a staking rewards system in a blockchain gaming platform, aligning with MetaLeagues' roadmap Phase 2 goals. Include functionality for calculating and distributing rewards based on player activity.
Generated: DETERMINISTIC_84eac013323324ea
Batch ID: 20250612_151513
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MetaLeagues Staking Rewards System
 * @dev Implements a staking rewards mechanism for the MetaLeagues gaming platform
 */
contract MetaLeaguesStaking is Ownable, ReentrancyGuard {
    IERC20 public rewardsToken;
    IERC20 public stakingToken;

    // Staking period in seconds (e.g., 30 days = 2592000 seconds)
    uint256 public stakingPeriod = 2592000;
    
    // Reward rate per second (calculated based on total rewards and staking period)
    uint256 public rewardRate;
    
    // Timestamp when rewards finish
    uint256 public finishAt;
    
    // Last time reward was updated
    uint256 public updatedAt;
    
    // Reward per token stored
    uint256 public rewardPerTokenStored;
    
    // Total staked amount
    uint256 public totalStaked;
    
    // Player activity multiplier (1x base, up to 3x for active players)
    uint256 public constant MAX_ACTIVITY_MULTIPLIER = 3;
    
    // Minimum stake amount
    uint256 public constant MIN_STAKE_AMOUNT = 100 ether;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimedAt;
        uint256 rewardPerTokenPaid;
        uint256 rewards;
        uint256 activityScore;
    }

    mapping(address => Stake) public stakes;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event ActivityUpdated(address indexed user, uint256 newScore);
    event RewardsSet(uint256 amount, uint256 duration);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the token used for staking
     * @param _rewardsToken Address of the token used for rewards
     */
    constructor(address _stakingToken, address _rewardsToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardsToken);
    }

    /**
     * @dev Updates the reward calculation parameters
     */
    modifier updateReward(address _account) {
        rewardPerTokenStored = rewardPerToken();
        updatedAt = lastTimeRewardApplicable();
        
        if (_account != address(0)) {
            stakes[_account].rewards = earned(_account);
            stakes[_account].rewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Returns the last time reward was applicable
     */
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < finishAt ? block.timestamp : finishAt;
    }

    /**
     * @dev Calculates reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        
        return rewardPerTokenStored + 
            (rewardRate * (lastTimeRewardApplicable() - updatedAt) * 1e18) / totalStaked;
    }

    /**
     * @dev Calculates earned rewards for an account
     * @param _account Address of the staker
     */
    function earned(address _account) public view returns (uint256) {
        Stake memory stake = stakes[_account];
        
        return ((stake.amount * (rewardPerToken() - stake.rewardPerTokenPaid)) / 1e18) 
            + stake.rewards;
    }

    /**
     * @dev Sets the reward parameters
     * @param _amount Total reward amount
     * @param _duration Duration of the reward period in seconds
     */
    function setRewards(uint256 _amount, uint256 _duration) external onlyOwner updateReward(address(0)) {
        require(_duration > 0, "Duration must be positive");
        
        if (block.timestamp >= finishAt) {
            rewardRate = _amount / _duration;
        } else {
            uint256 remainingRewards = (finishAt - block.timestamp) * rewardRate;
            rewardRate = (_amount + remainingRewards) / _duration;
        }
        
        require(rewardRate > 0, "Reward rate must be positive");
        require(
            rewardRate * _duration <= rewardsToken.balanceOf(address(this)),
            "Reward amount exceeds balance"
        );
        
        finishAt = block.timestamp + _duration;
        updatedAt = block.timestamp;
        
        emit RewardsSet(_amount, _duration);
    }

    /**
     * @dev Stakes tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(stakes[msg.sender].amount == 0, "Already staked");
        
        stakes[msg.sender] = Stake({
            amount: _amount,
            stakedAt: block.timestamp,
            lastClaimedAt: block.timestamp,
            rewardPerTokenPaid: rewardPerTokenStored,
            rewards: 0,
            activityScore: 1 // Start with base multiplier
        });
        
        totalStaked += _amount;
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes tokens and claims rewards
     */
    function unstake() external nonReentrant updateReward(msg.sender) {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");
        require(block.timestamp >= userStake.stakedAt + stakingPeriod, "Staking period not ended");
        
        uint256 amount = userStake.amount;
        uint256 reward = userStake.rewards;
        
        totalStaked -= amount;
        delete stakes[msg.sender];
        
        if (reward > 0) {
            rewardsToken.transfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
        
        stakingToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims rewards without unstaking
     */
    function claimReward() external nonReentrant updateReward(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        
        uint256 reward = userStake.rewards;
        require(reward > 0, "No rewards to claim");
        
        userStake.rewards = 0;
        userStake.lastClaimedAt = block.timestamp;
        
        rewardsToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Updates player activity score (called by game backend)
     * @param _player Address of the player
     * @param _score New activity score (1-3)
     */
    function updateActivityScore(address _player, uint256 _score) external onlyOwner updateReward(_player) {
        require(_score >= 1 && _score <= MAX_ACTIVITY_MULTIPLIER, "Invalid activity score");
        require(stakes[_player].amount > 0, "Player not staking");
        
        stakes[_player].activityScore = _score;
        emit ActivityUpdated(_player, _score);
    }

    /**
     * @dev Calculates rewards with activity multiplier applied
     * @param _account Address of the staker
     */
    function earnedWithMultiplier(address _account) public view returns (uint256) {
        uint256 baseReward = earned(_account);
        uint256 multiplier = stakes[_account].activityScore;
        return baseReward * multiplier;
    }

    /**
     * @dev Emergency withdrawal of rewards tokens (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardsToken.balanceOf(address(this));
        rewardsToken.transfer(owner(), balance);
    }
}
```
