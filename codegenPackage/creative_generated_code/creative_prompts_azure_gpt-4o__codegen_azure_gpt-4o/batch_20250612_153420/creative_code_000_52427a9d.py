"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-verse.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that distributes rewards based on a 0.05% fee from each trade within the HEHE ecosystem.
Generated: DETERMINISTIC_52427a9da49fe60d
Batch ID: 20250612_153420
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
 * @title HEHE Token Staking Contract
 * @dev This smart contract allows users to stake HEHE tokens and receive rewards.
 * Rewards are distributed based on a 0.05% fee collected from each trade within the HEHE ecosystem.
 */
contract HEHEStaking {
    // Address of the HEHE token
    IERC20 public immutable HEHEToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Total rewards collected from trade fees
    uint256 public totalRewards;

    // Reward pool for distribution
    uint256 public rewardPool;

    // Mapping of each staker's information
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 rewardAmount);
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    constructor(address _HEHEToken) {
        require(_HEHEToken != address(0), "Invalid token address");
        HEHEToken = IERC20(_HEHEToken);
    }

    /**
     * @dev Stake HEHE tokens into the contract.
     * @param _amount Amount of HEHE tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer HEHE tokens from the user's wallet to the contract
        require(
            HEHEToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking balances
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked HEHE tokens from the contract.
     * @param _amount Amount of HEHE tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );
        require(_amount > 0, "Amount must be greater than zero");

        // Update staking balances
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer HEHE tokens back to the user's wallet
        require(
            HEHEToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Deposit trade fee rewards into the contract.
     * @param _rewardAmount Amount of HEHE tokens to deposit as rewards.
     */
    function depositRewards(uint256 _rewardAmount) external {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        // Transfer HEHE tokens from the depositor's wallet to the contract
        require(
            HEHEToken.transferFrom(msg.sender, address(this), _rewardAmount),
            "Token transfer failed"
        );

        // Update reward pool
        rewardPool += _rewardAmount;
        totalRewards += _rewardAmount;

        emit RewardsDistributed(_rewardAmount);
    }

    /**
     * @dev Distribute rewards based on staked balances.
     * Rewards are distributed proportionally to the amount staked.
     */
    function distributeRewards() external {
        require(rewardPool > 0, "No rewards available for distribution");
        require(totalStaked > 0, "No tokens staked");

        for (address staker in stakedBalances) {
            uint256 stakedAmount = stakedBalances[staker];
            uint percentage
