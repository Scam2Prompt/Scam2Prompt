"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asterdx.com
Prompt: Write a Solidity smart contract to integrate staking functionality for assets like CAKE and BTC, inspired by Aster's staking model.
Generated: DETERMINISTIC_2b119da10ed616f4
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title StakingContract
 * @dev Allows users to stake CAKE and BTC tokens, earn rewards, and withdraw their stake.
 * Inspired by Aster's staking model.
 */
contract StakingContract {
    // Struct to represent stakes
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when the stake started
    }

    // Token types supported for staking
    enum TokenType {
        CAKE,
        BTC
    }

    // Events
    event Staked(address indexed user, TokenType tokenType, uint256 amount);
    event Withdrawn(address indexed user, TokenType tokenType, uint256 amount);
    event RewardsClaimed(address indexed user, TokenType tokenType, uint256 reward);

    // State variables
    mapping(address => mapping(TokenType => Stake)) public stakes; // User stakes
    mapping(TokenType => uint256) public rewardRates; // Reward rates for each token type (per second)
    mapping(TokenType => address) public tokenAddresses; // Addresses of the CAKE and BTC tokens
    address public owner; // Contract owner

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Modifier to ensure staking amount is valid
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _cakeToken, address _btcToken, uint256 _cakeRewardRate, uint256 _btcRewardRate) {
        owner = msg.sender;
        tokenAddresses[TokenType.CAKE] = _cakeToken;
        tokenAddresses[TokenType.BTC] = _btcToken;
        rewardRates[TokenType.CAKE] = _cakeRewardRate;
        rewardRates[TokenType.BTC] = _btcRewardRate;
    }

    /**
     * @dev Stakes specified amount of tokens.
     * @param tokenType Token type to stake (CAKE or BTC).
     * @param amount Amount of tokens to stake.
     */
    function stake(TokenType tokenType, uint256 amount) external validAmount(amount) {
        // Transfer tokens from user to contract
        require(
            IERC20(tokenAddresses[tokenType]).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update stake record
        Stake storage userStake = stakes[msg.sender][tokenType];
        claimRewards(tokenType); // Claim existing rewards before updating the stake
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, tokenType, amount);
    }

    /**
     * @dev Withdraws staked tokens and claims outstanding rewards.
     * @param tokenType Token type to withdraw (CAKE or BTC).
     */
    function withdraw(TokenType tokenType) external {
        // Fetch user stake
        Stake storage userStake = stakes[msg.sender][tokenType];
        uint256 amount = userStake.amount;
        require(amount > 0, "No tokens to withdraw");

        // Claim rewards before removing stake
        claimRewards(tokenType);

        // Reset stake record
        userStake.amount = 0;
        userStake.startTime = 0;

        // Transfer tokens back to user
        require(
            IERC20(tokenAddresses[tokenType]).transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, tokenType, amount);
    }

    /**
     * @dev Claims outstanding staking rewards.
     * @param tokenType Token type to claim rewards for (CAKE or BTC).
     */
    function claimRewards(TokenType tokenType) public {
        Stake storage userStake = stakes[msg.sender][tokenType];
        uint256 reward = calculateReward(msg.sender, tokenType);
        require(reward > 0, "No rewards to claim");

        // Reset startTime to now to prevent double claiming
        userStake.startTime = block.timestamp;

        // Transfer reward tokens to user
        require(
            IERC20(tokenAddresses[tokenType]).transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, tokenType, reward);
    }

    /**
     * @dev Calculates outstanding rewards for a user.
     * @param user Address of the user.
     * @param tokenType Token type to calculate rewards for (CAKE or BTC).
     * @return reward Outstanding reward amount.
     */
    function calculateReward(address user, TokenType tokenType) public view returns (uint256 reward) {
        Stake storage userStake = stakes[user][tokenType];
        if (userStake.amount == 0) return 0; // No stake, no rewards

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        reward = userStake.amount * rewardRates[tokenType] * stakingDuration;
    }

    /**
     * @dev Updates the reward rate for a token type.
     * @param tokenType Token type to update reward rate for (CAKE or BTC).
     * @param newRewardRate New reward rate (per second).
     */
    function updateRewardRate(TokenType tokenType, uint256 newRewardRate) external onlyOwner {
        rewardRates[tokenType] = newRewardRate;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("ETH not accepted");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
}
```
