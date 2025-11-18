"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi7.vip
Prompt: Generate a smart contract in Solidity for a basic DeFi application that interacts with ETH tokens.
Generated: DETERMINISTIC_409b25e3b3a66321
Batch ID: 20250612_154002
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
 * @title BasicDeFiApp
 * @dev A simple DeFi application that allows users to deposit, withdraw, and earn interest on ETH tokens
 */
contract BasicDeFiApp is Ownable, ReentrancyGuard {
    // Mapping to track user deposits
    mapping(address => uint256) private deposits;

    // Annual interest rate in basis points (100 basis points = 1%)
    uint256 public interestRateBasisPoints;

    // Event emitted when a user deposits ETH
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a user withdraws ETH
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the interest rate
    constructor(uint256 _interestRateBasisPoints) {
        require(_interestRateBasisPoints > 0, "Interest rate must be greater than 0");
        interestRateBasisPoints = _interestRateBasisPoints;
    }

    /**
     * @dev Deposit ETH into the DeFi application
     */
    function deposit() external payable nonReentrant {
        require(msg.value > 0, "Must deposit a positive amount");

        // Update the user's deposit amount
        deposits[msg.sender] += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw ETH from the DeFi application
     * @param amount The amount of ETH to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(deposits[msg.sender] >= amount, "Insufficient balance to withdraw");
        
        // Update the user's deposit amount
        deposits[msg.sender] -= amount;

        // Transfer the funds to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Calculate the total deposits for a user including interest
     * @param user The address of the user
     * @return totalAmount The total amount including interest
     */
    function calculateTotalWithInterest(address user) public view returns (uint256 totalAmount) {
        uint256 principal = deposits[user];
        uint256 interest = (principal * interestRateBasisPoints) / 10000;

        totalAmount = principal + interest;
    }

    /**
     * @dev Check the deposit balance of a user
     * @param user The address of the user
     * @return balance The user's deposit balance
     */
    function getDepositBalance(address user) external view returns (uint256 balance) {
        return deposits[user];
    }

    /**
     * @dev Updates the interest rate. Only callable by the owner.
     * @param newInterestRateBasisPoints The new interest rate in basis points
     */
    function updateInterestRate(uint256 newInterestRateBasisPoints) external onlyOwner {
        require(newInterestRateBasisPoints > 0, "Interest rate must be greater than 0");
        interestRateBasisPoints = newInterestRateBasisPoints;
    }

    /**
     * @dev Fallback function to receive ETH
     */
    receive() external payable {
        deposit();
    }
}
```
