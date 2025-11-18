"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ie.pages.dev
Prompt: Develop a smart contract in Solidity for staking $WAI tokens that mimics the high APY rewards described on the WienerAI website. Include functions for staking, withdrawing, and calculating rewards.
Generated: DETERMINISTIC_7d2c0ae4a7d104e8
Batch ID: 20250612_152235
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
 * @dev A smart contract for staking $WAI tokens and earning rewards.
 * High APY rewards mechanism inspired by the WienerAI website.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Token being staked
    IERC20 public waiToken;

    // Annual Percentage Yield (APY) for rewards (e.g., 20% = 2000 basis points)
    uint256 public constant APY_BASIS_POINTS = 2000;

    // Basis points denominator for APY calculations
    uint256 private constant BASIS_POINTS_DIVISOR = 10000;

    // Time periods
    uint256 private constant SECONDS_IN_A_YEAR = 365 days;

    // Struct for staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking began
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsPaid(address indexed user, uint256 rewards);

    /**
     * @dev Constructor initializes the contract with the token to be staked.
     * @param _waiToken Address of the $WAI token contract.
     */
    constructor(IERC20 _waiToken) {
        waiToken = _waiToken;
    }

    /**
     * @dev Stake $WAI tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the sender to the contract
        bool success = waiToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Calculate rewards for any previous stake
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            uint256 pendingRewards = calculateRewards(msg.sender);
            emit RewardsPaid(msg.sender, pendingRewards);
        }

        // Update user's stake
        userStake.amount += amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens and receive any earned rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Transfer staked tokens and rewards to the user
        uint256 totalAmount = userStake.amount + rewards;
        bool success = waiToken.transfer(msg.sender, totalAmount);
        require(success, "Token transfer failed");

        // Reset user's stake
        delete stakes[msg.sender];

        emit Withdrawn(msg.sender, userStake.amount);
        emit RewardsPaid(msg.sender, rewards);
    }

    /**
     * @dev Calculate the rewards earned by the user.
     * @param user Address of the user to calculate rewards for.
     * @return The amount of rewards earned.
     */
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate duration the tokens have been staked
        uint256 stakingDuration = block.timestamp - userStake.startTime;

        // Calculate rewards based on APY
        uint256 rewards = (userStake.amount * APY_BASIS_POINTS * stakingDuration) /
            (SECONDS_IN_A_YEAR * BASIS_POINTS_DIVISOR);

        return rewards;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Cannot send ETH to this contract");
    }
}
```
