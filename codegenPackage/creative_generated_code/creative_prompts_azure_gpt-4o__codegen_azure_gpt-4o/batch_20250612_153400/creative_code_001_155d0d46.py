"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: Generate Solidity code for an ERC20-compliant staking contract that rewards QUBE token holders using a 5% sell tax reward pool, as described on the InQubeta platform.
Generated: DETERMINISTIC_155d0d4637310944
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the standard ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QUBEStaking is Ownable {
    // Reward token (QUBE)
    IERC20 public rewardToken;

    // Total Staked Amount
    uint256 public totalStaked;

    // Reward Pool (from 5% sell tax)
    uint256 public rewardPool;

    // Struct to represent staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    // Mapping of staker addresses to their information
    mapping(address => Staker) public stakers;

    // Last reward pool update timestamp
    uint256 public lastRewardTime;

    // Reward per token staked, scaled for precision
    uint256 public accRewardPerToken;

    // Precision factor to avoid rounding errors
    uint256 private constant PRECISION_FACTOR = 1e18;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolUpdated(uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    // Modifier to ensure reward pool is updated before actions
    modifier updateRewardPool() {
        _updateRewardPool();
        _;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external updateRewardPool {
        require(_amount > 0, "Amount must be greater than zero");

        Staker storage staker = stakers[msg.sender];
        
        // Update staker rewards
        if (staker.stakedAmount > 0) {
            uint256 pendingReward = (staker.stakedAmount * accRewardPerToken) / PRECISION_FACTOR - staker.rewardDebt;
            if (pendingReward > 0) {
                rewardToken.transfer(msg.sender, pendingReward);
                emit RewardClaimed(msg.sender, pendingReward);
            }
        }

        // Transfer the staked tokens to the contract
        rewardToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        staker.stakedAmount += _amount;
        staker.rewardDebt = (staker.stakedAmount * accRewardPerToken) / PRECISION_FACTOR;

        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external updateRewardPool {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Amount must be greater than zero");
        require(staker.stakedAmount >= _amount, "Insufficient staked amount");

        // Update staker rewards
        uint256 pendingReward = (staker.stakedAmount * accRewardPerToken) / PRECISION_FACTOR - staker.rewardDebt;
        if (pendingReward > 0) {
            rewardToken.transfer(msg.sender, pendingReward);
            emit RewardClaimed(msg.sender, pendingReward);
        }

        // Transfer the unstaked tokens back to the user
        rewardToken.transfer(msg.sender, _amount);

        // Update staker information
        staker.stakedAmount -= _amount;
        staker.rewardDebt = (staker.stakedAmount * accRewardPerToken) / PRECISION_FACTOR;

        totalStaked -= _amount;
        emit Unstaked(msg.sender, _amount);
    }

    // Function to update the reward pool (called by owner)
    function addToRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        rewardToken.transferFrom(msg.sender, address(this), _amount);
        rewardPool += _amount;
        emit RewardPoolUpdated(_amount);
    }

    // Internal function to update the reward pool distribution
    function _updateRewardPool() internal {
        if (totalStaked == 0 || rewardPool == 0 || block.timestamp <= lastRewardTime) {
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 rewardToDistribute = rewardPool;

        // Update accumulated reward per token
        accRewardPerToken += (rewardToDistribute * PRECISION_FACTOR) / totalStaked;

        // Reset reward pool
        rewardPool = 0;
        lastRewardTime = block.timestamp;
    }

    // View function to calculate pending rewards for a staker
    function pendingRewards(address _staker) external view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 pendingReward = (staker.stakedAmount * accRewardPerToken) / PRECISION_FACTOR - staker.rewardDebt;
        return pendingReward;
    }
}
```
