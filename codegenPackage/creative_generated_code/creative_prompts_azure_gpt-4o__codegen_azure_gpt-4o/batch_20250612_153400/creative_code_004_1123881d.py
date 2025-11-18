"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-poodlinu.pages.dev
Prompt: Develop a smart contract for the Poodl Inu staking mechanism that locks tokens and calculates rewards based on the staking percentage (59%) and the annual return rate.
Generated: DETERMINISTIC_1123881d910c8626
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a well-documented and production-ready smart contract for an ERC-20 staking mechanism. The contract is written in Solidity.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PoodlInuStaking
 * @dev Smart contract for staking Poodl Inu tokens with annual rewards.
 */
contract PoodlInuStaking {
    // ERC-20 token interface
    IERC20 public immutable poodlToken;

    // Staking percentage (59%)
    uint256 public constant STAKING_PERCENTAGE = 59;

    // Annual return rate (e.g., 10% = 1000 basis points)
    uint256 public constant ANNUAL_RETURN_RATE_BP = 1000;

    // Time constants
    uint256 private constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Data structure to track stakes
    struct Stake {
        uint256 amount;
        uint256 startTimestamp;
        bool active;
    }

    // Mapping user address to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event RewardsWithdrawn(address indexed user, uint256 reward);
    event TokensUnstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the PoodlInu token address.
     * @param tokenAddress Address of the ERC-20 token used for staking.
     */
    constructor(address tokenAddress) {
        require(tokenAddress != address(0), "Invalid token address");
        poodlToken = IERC20(tokenAddress);
    }

    /**
     * @dev Stake Poodl Inu tokens.
     * @param amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(
            poodlToken.balanceOf(msg.sender) >= amount,
            "Insufficient token balance"
        );

        // Transfer tokens to the staking contract
        require(
            poodlToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Calculate the staking amount based on the staking percentage
        uint256 stakingAmount = (amount * STAKING_PERCENTAGE) / 100;

        // Update stake information
        stakes[msg.sender] = Stake({
            amount: stakingAmount,
            startTimestamp: block.timestamp,
            active: true
        });

        emit TokensStaked(msg.sender, stakingAmount);
    }

    /**
     * @dev Calculate rewards for the user based on staking amount and time elapsed.
     * @param user Address of the user.
     * @return reward Reward amount in tokens.
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        Stake memory stakeInfo = stakes[user];
        require(stakeInfo.active, "No active stake found");

        // Calculate time elapsed since staking
        uint256 timeElapsed = block.timestamp - stakeInfo.startTimestamp;

        // Calculate reward using annual return rate and time elapsed
        reward =
            (stakeInfo.amount * ANNUAL_RETURN_RATE_BP * timeElapsed) /
            (SECONDS_IN_YEAR * 10000);
    }

    /**
     * @dev Withdraw staking rewards.
     */
    function withdrawRewards() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.active, "No active stake found");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Ensure there is a reward to withdraw
        require(reward > 0, "No rewards available");

        // Transfer the reward to the user
        require(
            poodlToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        // Reset start timestamp for staking
        stakeInfo.startTimestamp = block.timestamp;

        emit RewardsWithdrawn(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens and withdraw them.
     */
    function unstakeTokens() external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.active, "No active stake found");

        // Calculate the staking amount to return
        uint256 stakingAmount = stakeInfo.amount;

        // Reset stake information
        stakeInfo.amount = 0;
        stakeInfo.startTimestamp = 0;
        stakeInfo.active = false;

        // Transfer tokens back to the user
        require(
            poodlToken.transfer(msg.sender, stakingAmount),
            "Unstaking transfer failed"
        );

        emit TokensUnstaked(msg.sender, stakingAmount);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Contract does not accept ETH");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Contract does not accept ETH");
    }
}

// Minimal ERC-20 interface for token interactions
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
