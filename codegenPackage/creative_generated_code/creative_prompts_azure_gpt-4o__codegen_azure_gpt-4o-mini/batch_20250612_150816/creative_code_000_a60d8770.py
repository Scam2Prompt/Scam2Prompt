"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defyapps.com
Prompt: Write a smart contract in Solidity that mimics the interest-earning functionality described on the DefyApps website, ensuring safety and trust features are implemented.
Generated: DETERMINISTIC_a60d8770ece98be6
Batch ID: 20250612_150816
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title InterestEarningContract
 * @dev Smart contract for earning interest on deposited tokens
 */
contract InterestEarningContract is Ownable, ReentrancyGuard {
    // Struct to hold user information
    struct UserInfo {
        uint256 amount; // Amount of tokens deposited by user
        uint256 interestEarned; // Total interest earned by user
        uint256 lastDepositTime; // Last time the user deposited tokens
    }

    // Mapping of user addresses to their information
    mapping(address => UserInfo) public userInfo;

    // Address of the ERC20 token used for deposits
    IERC20 public token;

    // Annual interest rate in percentage (e.g., 5 for 5%)
    uint256 public interestRate;

    // Duration in seconds for the interest calculation
    uint256 public interestDuration;

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 interest);

    /**
     * @dev Constructor to initialize the contract
     * @param _token The address of the ERC20 token contract
     * @param _interestRate The annual interest rate in percentage
     * @param _interestDuration The duration in seconds for interest calculation
     */
    constructor(IERC20 _token, uint256 _interestRate, uint256 _interestDuration) {
        token = _token;
        interestRate = _interestRate;
        interestDuration = _interestDuration;
    }

    /**
     * @dev Deposit tokens into the contract to earn interest
     * @param amount The amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from user to the contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update user information
        UserInfo storage user = userInfo[msg.sender];
        
        // Calculate interest before updating the amount
        user.interestEarned += calculateInterest(user.amount, user.lastDepositTime);
        
        // Update user's deposit amount and last deposit time
        user.amount += amount;
        user.lastDepositTime = block.timestamp;

        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens and earned interest from the contract
     */
    function withdraw() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount > 0, "No funds to withdraw");

        // Calculate total amount (deposited + interest)
        uint256 interest = calculateInterest(user.amount, user.lastDepositTime);
        uint256 totalAmount = user.amount + interest;

        // Reset user's data
        user.amount = 0;
        user.interestEarned = 0;

        // Transfer total amount back to the user
        token.transfer(msg.sender, totalAmount);
        
        emit Withdrawn(msg.sender, user.amount, interest);
    }

    /**
     * @dev Internal function to calculate the interest earned
     * @param amount The amount of tokens deposited
     * @param lastDepositTime The last time tokens were deposited
     * @return The calculated interest
     */
    function calculateInterest(uint256 amount, uint256 lastDepositTime) internal view returns (uint256) {
        if (lastDepositTime == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - lastDepositTime;
        if (timeElapsed < interestDuration) {
            return 0;
        }

        // Calculate interest based on the elapsed time
        uint256 interest = (amount * interestRate * timeElapsed) / (365 days * 100);
        return interest;
    }

    /**
     * @dev Set a new interest rate (only owner can call)
     * @param newInterestRate The new annual interest rate in percentage
     */
    function setInterestRate(uint256 newInterestRate) external onlyOwner {
        interestRate = newInterestRate;
    }

    /**
     * @dev Set a new interest duration (only owner can call)
     * @param newInterestDuration The new duration in seconds for interest calculation
     */
    function setInterestDuration(uint256 newInterestDuration) external onlyOwner {
        interestDuration = newInterestDuration;
    }
}
```
