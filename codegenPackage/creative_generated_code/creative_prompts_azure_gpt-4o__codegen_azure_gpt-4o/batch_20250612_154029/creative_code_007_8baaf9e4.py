"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-tokens.com
Prompt: Create a tutorial for building a PepeFarm-like staking system using Solidity, ensuring compatibility with the zero-tax tokenomics of $PEPE.
Generated: DETERMINISTIC_8baaf9e45e26b5a5
Batch ID: 20250612_154029
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
 * @title PepeFarm Staking System
 * @dev A staking system compatible with $PEPE zero-tax tokenomics.
 * Users can stake $PEPE tokens, earn rewards, and withdraw their tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PepeFarmStaking {
    // Reference to the $PEPE token contract
    IERC20 public pepeToken;

    // Structure to store staking information
    struct Staker {
        uint256 stakedAmount; // Total amount of tokens staked
        uint256 rewardDebt; // Rewards already claimed
        uint256 lastStakedTime; // Timestamp of the last staking action
    }

    // Mapping of stakers' data
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (e.g., tokens rewarded per second of staking)
    uint256 public rewardRate;

    // Contract owner
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(IERC20 _pepeToken, uint256 _rewardRate) {
        pepeToken = _pepeToken; // Assign the $PEPE token contract
        rewardRate = _rewardRate; // Set the reward rate
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Stakes a specific amount of $PEPE tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer $PEPE tokens from the user to the contract
        bool success = pepeToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Calculate pending rewards for the user
        uint256 pendingRewards = calculateRewards(msg.sender);

        Staker storage userStaker = stakers[msg.sender];
        userStaker.rewardDebt += pendingRewards; // Update reward debt
        userStaker.stakedAmount += _amount; // Update staked amount
        userStaker.lastStakedTime = block.timestamp; // Update last staked time

        totalStaked += _amount; // Update total staked amount

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstakes all the user's staked $PEPE tokens and claims rewards.
     */
    function unstake() external {
        Staker storage userStaker = stakers[msg.sender];
        require(userStaker.stakedAmount > 0, "No tokens staked");

        // Calculate pending rewards for the user
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Transfer staked tokens back to the user
        uint256 amount = userStaker.stakedAmount;
        bool success = pepeToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Transfer pending rewards to the user
        uint256 totalRewards = pendingRewards + userStaker.rewardDebt;
        bool rewardSuccess = pepeToken.transfer(msg.sender, totalRewards);
        require(rewardSuccess, "Reward transfer failed");

        // Reset user's staking data
        userStaker.stakedAmount = 0;
        userStaker.rewardDebt = 0;
        userStaker.lastStakedTime = 0;

        totalStaked -= amount; // Update total staked amount

        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Claims pending rewards without unstaking.
     */
    function claimRewards() external {
        Staker storage userStaker = stakers[msg.sender];
        require(userStaker.stakedAmount > 0, "No tokens staked");

        // Calculate pending rewards for the user
        uint256 pendingRewards = calculateRewards(msg.sender);

        // Transfer pending rewards to the user
        uint256 totalRewards = pendingRewards + userStaker.rewardDebt;
        bool success = pepeToken.transfer(msg.sender, totalRewards);
        require(success, "Reward transfer failed");

        // Reset reward debt
        userStaker.rewardDebt = 0;
        userStaker.lastStakedTime = block.timestamp; // Update last staked time

        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Calculates pending rewards for a staker.
     * @param _staker Address of the staker.
     * @return The pending reward amount.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker memory userStaker = stakers[_staker];
        if (userStaker.stakedAmount == 0) {
            return 0;
        }
        uint256 stakingDuration = block.timestamp - userStaker.lastStakedTime;
        return stakingDuration * rewardRate * userStaker.stakedAmount / 1e18;
    }

    /**
     * @dev Updates the reward rate. Only callable by the owner.
     * @param _newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Withdraws tokens from the contract (emergency use only). Only callable by the owner.
     * @param _amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        bool success = pepeToken.transfer(owner, _amount);
        require(success, "Token transfer failed");
    }
}
```
