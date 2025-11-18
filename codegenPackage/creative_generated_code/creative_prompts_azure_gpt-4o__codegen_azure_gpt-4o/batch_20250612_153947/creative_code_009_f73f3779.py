"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bboop.fun
Prompt: Write a smart contract that integrates staking rewards and airdrop distribution, inspired by the cult-like ecosystem described on bboop.fun.
Generated: DETERMINISTIC_f73f3779e94d46c5
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a production-ready smart contract in Solidity for staking rewards and airdrop distribution:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingRewardsWithAirdrop
 * @dev A smart contract for staking tokens, earning rewards, and receiving airdrops.
 */
contract StakingRewardsWithAirdrop {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per second
    uint256 public airdropPool; // Pool for airdrops

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Accrued rewards
        uint256 lastUpdated; // Last time the user's stake was updated
    }

    mapping(address => StakeInfo) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);
    event AirdropDistributed(uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Modifier to ensure non-zero values
    modifier nonZero(uint256 _value) {
        require(_value > 0, "Value must be greater than zero");
        _;
    }

    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonZero(_amount) {
        StakeInfo storage userStake = stakers[msg.sender];

        // Update rewards before modifying stake amount
        claimRewards();

        userStake.amount += _amount;
        userStake.lastUpdated = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens.
     */
    function withdraw() external {
        StakeInfo storage userStake = stakers[msg.sender];
        require(userStake.amount > 0, "No staked amount to withdraw");

        claimRewards();

        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        totalStaked -= amountToWithdraw;

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() public {
        StakeInfo storage userStake = stakers[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        uint256 pendingReward = calculateRewards(msg.sender);
        userStake.rewardDebt += pendingReward;
        userStake.lastUpdated = block.timestamp;

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Calculate rewards for a staker based on time and staked amount.
     * @param _user Address of the staker.
     * @return Rewards earned by the staker.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        StakeInfo storage userStake = stakers[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        return (timeElapsed * userStake.amount * rewardRate) / 1 ether;
    }

    /**
     * @dev Distribute airdrop tokens to all stakers proportionally.
     */
    function distributeAirdrop(uint256 _amount) external onlyOwner nonZero(_amount) {
        require(totalStaked > 0, "No stakers to distribute airdrop");
        require(_amount <= airdropPool, "Insufficient airdrop pool");

        for (address staker : stakers) {
           next
