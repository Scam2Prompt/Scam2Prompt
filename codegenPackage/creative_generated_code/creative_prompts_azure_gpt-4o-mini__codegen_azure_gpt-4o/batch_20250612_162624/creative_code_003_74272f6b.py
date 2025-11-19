"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana10x.com
Prompt: Generate a sample code snippet for a smart contract that manages staking rewards with a cap strategy like SOL10X's.
Generated: DETERMINISTIC_74272f6b19c2043e
Batch ID: 20250612_162624
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

/**
 * @title StakingRewards
 * @dev A smart contract that manages staking rewards with a capped strategy similar to SOL10X.
 * Users can stake tokens, earn rewards, and the contract enforces a cap on staking rewards.
 */
contract StakingRewards {
    // State variables
    address public owner;                           // Owner of the contract
    uint256 public rewardCap;                       // Maximum rewards cap (e.g., SOL10X's limit)
    uint256 public rewardRate;                      // Reward rate per second
    uint256 public totalStaked;                     // Total tokens staked in the contract

    struct Staker {
        uint256 stakedAmount;                       // Amount of tokens staked by the user
        uint256 rewardDebt;                         // Tracks rewards already paid out
        uint256 lastUpdated;                        // Last timestamp of staking activity
    }

    mapping(address => Staker) public stakers;      // Mapping of user address to staker info

    event Staked(address indexed user, uint256 amount);   // Event when a user stakes tokens
    event Withdrawn(address indexed user, uint256 amount);// Event when a user withdraws tokens
    event RewardsClaimed(address indexed user, uint256 amount);// Event when a user claims rewards

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier updateRewards(address _user) {
        if (_user != address(0)) {
            Staker storage user = stakers[_user];
            uint256 pending = calculateRewards(_user);
            user.rewardDebt += pending;
            user.lastUpdated = block.timestamp;
        }
        _;
    }

    constructor(uint256 _rewardRate, uint256 _rewardCap) {
        owner = msg.sender;
        rewardRate = _rewardRate;
        rewardCap = _rewardCap;
    }

    /**
     * @dev Allows a user to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        
        Staker storage user = stakers[msg.sender];
        user.stakedAmount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        Staker storage user = stakers[msg.sender];
        require(user.stakedAmount >= _amount, "Insufficient staked amount");

        user.stakedAmount -= _amount;
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to claim their staking rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Staker storage user = stakers[msg.sender];
        uint256 pendingRewards = user.rewardDebt;

        // Enforce the rewards cap strategy
        require(pendingRewards <= rewardCap, "Reward cap exceeded");

        user.rewardDebt = 0; // Reset rewards after claiming

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Calculates pending rewards for a user based on staked amount and time elapsed.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Staker storage user = stakers[_user];
        uint256 timeElapsed = block.timestamp - user.lastUpdated;
        return user.stakedAmount * timeElapsed * rewardRate;
    }

    /**
     * @dev Updates the reward cap. Only callable by the contract owner.
     * @param _newCap New reward cap value.
     */
    function updateRewardCap(uint256 _newCap) external onlyOwner {
        rewardCap = _newCap;
    }

    /**
     * @dev Updates the reward rate. Only callable by the contract owner.
     * @param _newRate New reward rate value.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
