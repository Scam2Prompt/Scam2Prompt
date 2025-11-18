"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-reward.web.app
Prompt: Create a Solidity implementation for a staking contract that supports multiple meme coins, including Dogecoin, Shiba Inu, and Floki Inu, as described in the MemeVault protocol.
Generated: DETERMINISTIC_0ab8cc4fd54725d6
Batch ID: 20250612_154133
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

// Interface for ERC20-compliant tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract MemeVault {
    // Struct to keep track of user stakes
    struct Stake {
        uint256 amount;       // Amount staked
        uint256 timestamp;    // Timestamp of when the stake was made
    }

    // Supported meme coins for staking
    IERC20 public dogecoin;
    IERC20 public shibaInu;
    IERC20 public flokiInu;

    // Mapping: user -> token -> stake details
    mapping(address => mapping(IERC20 => Stake)) public stakes;

    // Staking duration for reward calculation
    uint256 public constant MIN_STAKE_DURATION = 1 days;

    // Reward rate per second (e.g., 0.0001 tokens rewarded per second)
    uint256 public constant REWARD_RATE = 1e14;

    // Modifier to check valid token
    modifier validToken(IERC20 token) {
        require(
            token == dogecoin || token == shibaInu || token == flokiInu,
            "Unsupported token."
        );
        _;
    }

    // Events
    event Staked(address indexed user, IERC20 indexed token, uint256 amount);
    event Unstaked(address indexed user, IERC20 indexed token, uint256 amount, uint256 reward);

    constructor(
        address _dogecoin,
        address _shibaInu,
        address _flokiInu
    ) {
        dogecoin = IERC20(_dogecoin);
        shibaInu = IERC20(_shibaInu);
        flokiInu = IERC20(_flokiInu);
    }

    /**
     * @dev Allows users to stake supported meme coins in the vault.
     * @param token The token user wants to stake.
     * @param amount The amount of tokens to stake.
     */
    function stake(IERC20 token, uint256 amount) external validToken(token) {
        require(amount > 0, "Stake amount must be greater than zero.");

        // Transfer tokens from user to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed.");

        // Update or initialize the user's stake
        Stake storage userStake = stakes[msg.sender][token];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, token, amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     * @param token The token user wants to unstake.
     */
    function unstake(IERC20 token) external validToken(token) {
        Stake storage userStake = stakes[msg.sender][token];
        uint256 stakedAmount = userStake.amount;

        require(stakedAmount > 0, "No tokens staked.");

        // Calculate rewards based on staking duration
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = 0;

        if (stakingDuration >= MIN_STAKE_DURATION) {
            reward = stakingDuration * REWARD_RATE;
        }

        // Reset user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked tokens back to the user
        require(token.transfer(msg.sender, stakedAmount), "Token transfer failed.");

        // Transfer reward tokens (if applicable)
        if (reward > 0) {
            require(token.transfer(msg.sender, reward), "Reward transfer failed.");
        }

        emit Unstaked(msg.sender, token, stakedAmount, reward);
    }

    /**
     * @dev Allows users to check their current stake.
     * @param token The token to check stake for.
     * @return The amount of tokens staked and the timestamp of the stake.
     */
    function getStake(IERC20 token) external view validToken(token) returns (uint256, uint256) {
        Stake storage userStake = stakes[msg.sender][token];
        return (userStake.amount, userStake.timestamp);
    }
}
```
