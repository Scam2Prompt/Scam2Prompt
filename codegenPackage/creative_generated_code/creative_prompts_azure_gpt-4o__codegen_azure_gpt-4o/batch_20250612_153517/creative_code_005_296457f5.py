"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehe-com.pages.dev
Prompt: Write a script in Solidity to implement a fee-sharing mechanism where 0.05% of each trade is distributed to staked $HEHE token holders.
Generated: DETERMINISTIC_296457f592968c0a
Batch ID: 20250612_153517
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
 * @title FeeSharingMechanism
 * @dev Contract to distribute a fee (0.05% of each trade) to staked $HEHE token holders.
 */
contract FeeSharingMechanism {
    // Address of the $HEHE token contract
    IERC20 public HEHE;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Mapping to store staked amounts by user addresses
    mapping(address => uint256) public stakes;

    // Mapping to track rewards owed to stakers
    mapping(address => uint256) public rewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to ensure a user has staked tokens
    modifier hasStake() {
        require(stakes[msg.sender] > 0, "No staked tokens for user");
        _;
    }

    constructor(address _HEHE) {
        HEHE = IERC20(_HEHE);
    }

    /**
     * @dev Function to stake $HEHE tokens in the contract.
     * @param amount Amount of tokens to be staked.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(HEHE.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update the user's stake and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $HEHE tokens.
     * @param amount Amount of tokens to be unstaked.
     */
    function unstake(uint256 amount) external hasStake {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked tokens");

        // Update the user's stake and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the user
        require(HEHE.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to distribute trade fees as rewards to staked token holders.
     * @param tradeAmount Amount involved in the trade.
     */
    function distributeFee(uint256 tradeAmount) external {
        require(totalStaked > 0, "No tokens staked in the contract");

        // Calculate the fee to be distributed (0.05% of trade amount)
        uint256 fee = (tradeAmount * 5) / 10000;

        // Iterate through all stakers and distribute the fee proportionally
        for (uint256 i = 0; i < totalStakersCount(); i++) {
            address staker = stakerList[i];
            uint256 stakerShare = (stakes[staker] * fee) / totalStaked;
            rewards[staker] += stakerShare;
        }
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external hasStake {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset user's reward balance
rewrrexxz
