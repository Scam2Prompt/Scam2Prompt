"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate a smart contract for a decentralized betting platform that allows users to stake $BCB tokens and receive rewards in stable coins.
Generated: DETERMINISTIC_b7a11231a0d2b817
Batch ID: 20250612_163616
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
 * @title Decentralized Betting Platform
 * @notice This smart contract allows users to stake $BCB tokens and receive rewards in stable coins.
 * @dev The contract uses ERC20 standards for token transfers and includes basic security measures.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BettingPlatform is Ownable {
    // Struct to represent a user's stake
    struct Stake {
        uint256 amount; // Amount of $BCB tokens staked
        uint256 timestamp; // Time of staking
    }

    // Mapping to track stakes for each user
    mapping(address => Stake) public stakes;

    // Address of the $BCB token contract
    IERC20 public bcbToken;

    // Address of the stable coin contract for rewards
    IERC20 public stableCoin;

    // Reward rate constants (e.g., 0.01 means 1% reward per week)
    uint256 public constant REWARD_RATE = 100; // 100 basis points = 1%
    uint256 public constant REWARD_INTERVAL = 1 weeks;

    /**
     * @dev Event emitted when a user stakes tokens.
     * @param user Address of the user.
     * @param amount Amount of $BCB tokens staked.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Event emitted when a user withdraws their stake and rewards.
     * @param user Address of the user.
     * @param stakeAmount Amount of $BCB tokens withdrawn.
     * @param rewardAmount Amount of stable coin rewards transferred.
     */
    event Withdrawn(address indexed user, uint256 stakeAmount, uint256 rewardAmount);

    /**
     * @dev Constructor to initialize the token contracts.
     * @param _bcbToken Address of the $BCB token contract.
     * @param _stableCoin Address of the stable coin contract.
     */
    constructor(IERC20 _bcbToken, IERC20 _stableCoin) {
        require(address(_bcbToken) != address(0), "Invalid BCB token address");
        require(address(_stableCoin) != address(0), "Invalid stable coin address");

        bcbToken = _bcbToken;
        stableCoin = _stableCoin;
    }

    /**
     * @dev Function to stake $BCB tokens.
     * @param amount Amount of $BCB tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer $BCB tokens from the user to the contract
        bool success = bcbToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked $BCB tokens and claim rewards.
     */
    function withdraw() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");

        // Calculate rewards based on staking duration
        uint256 duration = block.timestamp - userStake.timestamp;
        uint256 rewardPeriods = duration / REWARD_INTERVAL;
        uint256 rewardAmount = (userStake.amount * REWARD_RATE * rewardPeriods) / 10000;

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Transfer staked $BCB tokens back to the user
        bool successBCB = bcbToken.transfer(msg.sender, userStake.amount);
        require(successBCB, "BCB token transfer failed");

        // Transfer stable coin rewards to the user
        bool successReward = stableCoin.transfer(msg.sender, rewardAmount);
        require(successReward, "Reward transfer failed");

        emit Withdrawn(msg.sender, userStake.amount, rewardAmount);
    }

    /**
     * @dev Function to allow the owner to update reward parameters.
     * @param newRewardRate New reward rate in basis points.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        REWARD_RATE = newRewardRate;
    }

    /**
     * @dev Function to allow the owner to recover tokens accidentally sent to the contract.
     * @param token Address of the token to recover.
     * @param amount Amount of tokens to recover.
     */
    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(address(token) != address(0), "Invalid token address");
        require(amount > 0, "Recovery amount must be greater than zero");

        bool success = token.transfer(owner(), amount);
        require(success, "Token recovery failed");
    }
}
```
