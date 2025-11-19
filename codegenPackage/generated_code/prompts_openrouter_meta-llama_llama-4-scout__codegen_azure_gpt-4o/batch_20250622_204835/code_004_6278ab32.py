"""
Generated Code Metadata:
========================
Original URL: https://defiland-website.pages.dev
Prompt: "Design a simple smart contract for a gamified DeFi lending platform inspired by DeFi Land's model."
Generated: DETERMINISTIC_6278ab32a1bf5882
Batch ID: 20250622_204835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title GamifiedDeFiLending
 * @dev A simple smart contract for a gamified DeFi lending platform.
 * Users can deposit funds, earn interest, and unlock rewards based on their activity.
 */
contract GamifiedDeFiLending {
    // Struct to store user data
    struct User {
        uint256 depositedAmount;
        uint256 rewardPoints;
        uint256 lastDepositTime;
    }

    // Mapping to store user data
    mapping(address => User) public users;

    // Interest rate (e.g., 5% annual interest rate)
    uint256 public constant INTEREST_RATE = 5;

    // Reward multiplier for gamification
    uint256 public constant REWARD_MULTIPLIER = 10;

    // Minimum deposit amount
    uint256 public constant MIN_DEPOSIT = 0.01 ether;

    // Owner of the contract
    address public owner;

    // Event declarations
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 rewardPoints);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows users to deposit funds into the platform.
     * Updates their deposited amount, reward points, and last deposit time.
     */
    function deposit() external payable {
        require(msg.value >= MIN_DEPOSIT, "Deposit amount is too low");

        User storage user = users[msg.sender];

        // Calculate interest for previous deposits
        if (user.depositedAmount > 0) {
            uint256 interest = calculateInterest(user.depositedAmount, user.lastDepositTime);
            user.depositedAmount += interest;
        }

        // Update user data
        user.depositedAmount += msg.value;
        user.rewardPoints += msg.value * REWARD_MULTIPLIER;
        user.lastDepositTime = block.timestamp;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their deposited funds along with earned interest.
     */
    function withdraw(uint256 amount) external {
        User storage user = users[msg.sender];
        require(user.depositedAmount >= amount, "Insufficient balance");

        // Calculate interest for the current deposit
        uint256 interest = calculateInterest(user.depositedAmount, user.lastDepositTime);
        user.depositedAmount += interest;

        // Deduct the withdrawal amount
        user.depositedAmount -= amount;

        // Reset last deposit time
        user.lastDepositTime = block.timestamp;

        // Transfer the funds to the user
        payable(msg.sender).transfer(amount);

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their reward points.
     * Reward points are reset after claiming.
     */
    function claimRewards() external {
        User storage user = users[msg.sender];
        require(user.rewardPoints > 0, "No reward points to claim");

        uint256 rewardPoints = user.rewardPoints;
        user.rewardPoints = 0;

        emit RewardClaimed(msg.sender, rewardPoints);
    }

    /**
     * @dev Calculates the interest earned based on the deposited amount and time elapsed.
     * @param amount The deposited amount.
     * @param lastDepositTime The timestamp of the last deposit.
     * @return The calculated interest.
     */
    function calculateInterest(uint256 amount, uint256 lastDepositTime) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastDepositTime;
        uint256 annualInterest = (amount * INTEREST_RATE) / 100;
        return (annualInterest * timeElapsed) / 365 days;
    }

    /**
     * @dev Allows the owner to withdraw contract funds (e.g., for platform maintenance).
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {
        deposit();
    }
}
```
