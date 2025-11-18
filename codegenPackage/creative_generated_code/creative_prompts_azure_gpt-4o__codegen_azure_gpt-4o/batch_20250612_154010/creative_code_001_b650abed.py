"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peaptoken.fun
Prompt: Generate Solidity code for a staking smart contract compatible with the PEPE Ascension Layer 2 blockchain that incorporates double rewards programs as described in the presale phase.
Generated: DETERMINISTIC_b650abedce3a02f2
Batch ID: 20250612_154010
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
 * @title StakingContract
 * @dev A staking smart contract for PEPE Ascension Layer 2 that supports double rewards programs.
 */
contract StakingContract {
    // User stake structure to track staked amount and rewards.
    struct UserStake {
        uint256 stakedAmount;
        uint256 rewardA; // Reward program A
        uint256 rewardB; // Reward program B
        uint256 lastStakeTime;
    }

    // State variables
    address public owner;
    uint256 public totalStaked;
    uint256 public rewardRateA; // Reward rate for program A (in percentage)
    uint256 public rewardRateB; // Reward rate for program B (in percentage)
    uint256 public minStakeAmount;

    mapping(address => UserStake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ClaimedRewards(address indexed user, uint256 rewardA, uint256 rewardB);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].stakedAmount > 0, "No active stake found.");
        _;
    }

    constructor(uint256 _rewardRateA, uint256 _rewardRateB, uint256 _minStakeAmount) {
        require(_rewardRateA > 0 && _rewardRateB > 0, "Invalid reward rates.");
        require(_minStakeAmount > 0, "Minimum stake amount must be greater than zero.");

        owner = msg.sender;
        rewardRateA = _rewardRateA;
        rewardRateB = _rewardRateB;
        minStakeAmount = _minStakeAmount;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external payable {
        require(_amount >= minStakeAmount, "Amount below minimum stake.");
        require(msg.value == _amount, "Incorrect staking amount sent.");

        UserStake storage userStake = stakes[msg.sender];

        // Calculate pending rewards before updating staked amount
        if (userStake.stakedAmount > 0) {
            uint256 rewardA = calculateReward(userStake.stakedAmount, rewardRateA, userStake.lastStakeTime);
            uint256 rewardB = calculateReward(userStake.stakedAmount, rewardRateB, userStake.lastStakeTime);

            userStake.rewardA += rewardA;
            userStake.rewardB += rewardB;
        }

        // Update user's stake
        userStake.stakedAmount += _amount;
        userStake.lastStakeTime = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        UserStake storage userStake = stakes[msg.sender];

        uint256 stakedAmount = userStake.stakedAmount;
        uint256 rewardA = calculateReward(stakedAmount, rewardRateA, userStake.lastStakeTime) + userStake.rewardA;
        uint256 rewardB = calculateReward(stakedAmount, rewardRateB, userStake.lastStakeTime) + userStake.rewardB;

        // Reset user stake
        userStake.stakedAmount = 0;
        userStake.rewardA = 0;
        userStake.rewardB = 0;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked amount and rewards to user
        payable(msg.sender).transfer(stakedAmount + rewardA + rewardB);

        emit Unstaked(msg.sender, stakedAmount);
        emit ClaimedRewards(msg.sender, rewardA, rewardB);
    }

    /**
     * @dev Claim rewards without unstaking.
     */
    function claimRewards() external hasStake(msg.sender) {
        UserStake storage userStake = stakes[msg.sender];

        uint256 rewardA = calculateReward(userStake.stakedAmount, rewardRateA, userStake.lastStakeTime) + userStake.rewardA;
        uint256 rewardB = calculateReward(userStake.stakedAmount, rewardRateB, userStake.lastStakeTime) + userStake.rewardB;

        // Reset rewards
        userStake.rewardA = 0;
        userStake.rewardB = 0;
        userStake.lastStakeTime = block.timestamp;

        // Transfer rewards to user
        payable(msg.sender).transfer(rewardA + rewardB);

        emit ClaimedRewards(msg.sender, rewardA, rewardB);
    }

    /**
     * @dev Calculate rewards based on stake, rate, and duration.
     * @param _amount Amount staked.
     * @param _rate Reward rate (percentage).
     * @param _lastStakeTime Timestamp of the last stake.
     * @return Calculated reward.
     */
    function calculateReward(
        uint256 _amount,
        uint256 _rate,
        uint256 _lastStakeTime
    ) internal view returns (uint256) {
        uint256 duration = block.timestamp - _lastStakeTime;
        return (_amount * _rate * duration) / (100 * 365 days);
    }

    /**
     * @dev Update reward rates for staking programs.
     * @param _rewardRateA New reward rate for program A.
     * @param _rewardRateB New reward rate for program B.
     */
    function updateRewardRates(uint256 _rewardRateA, uint256 _rewardRateB) external onlyOwner {
        require(_rewardRateA > 0 && _rewardRateB > 0, "Invalid reward rates.");
        rewardRateA = _rewardRateA;
        rewardRateB = _rewardRateB;
    }

    /**
     * @dev Update minimum staking amount.
     * @param _minStakeAmount New minimum staking amount.
     */
    function updateMinStakeAmount(uint256 _minStakeAmount) external onlyOwner {
        require(_minStakeAmount > 0, "Minimum stake amount must be greater than zero.");
        minStakeAmount = _minStakeAmount;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers not allowed.");
    }

    receive() external payable {
        revert("Direct ETH transfers not allowed.");
    }
}
```
