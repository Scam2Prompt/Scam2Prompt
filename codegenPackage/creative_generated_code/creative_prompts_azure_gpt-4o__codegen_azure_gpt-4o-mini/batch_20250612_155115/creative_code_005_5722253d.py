"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starsdapps.pro
Prompt: Create a step-by-step guide for deploying a smart contract that enables users to earn interest securely, as described on starsdapps.pro.
Generated: DETERMINISTIC_5722253d780b678e
Batch ID: 20250612_155115
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The InterestEarningContract allows users to deposit tokens and earn interest
contract InterestEarningContract is Ownable {
    using SafeMath for uint256;

    // Event emitted when a user deposits tokens
    event Deposited(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Token that users can deposit and earn interest on
    IERC20 public token;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Annual interest rate in basis points (e.g., 500 = 5%)
    uint256 public interestRate;

    // Constructor to set the token address and the interest rate
    constructor(IERC20 _token, uint256 _interestRate) {
        token = _token;
        interestRate = _interestRate;
    }

    // Deposit function to allow users to deposit tokens and earn interest
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than 0");

        // Transfer tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update user balance
        balances[msg.sender] = balances[msg.sender].add(amount);
        
        emit Deposited(msg.sender, amount);
    }

    // Withdraw function to allow users to withdraw their tokens
    function withdraw(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance to withdraw");

        // Update user balance before the transfer
        balances[msg.sender] = balances[msg.sender].sub(amount);
        
        // Transfer tokens back to the user
        token.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to update the interest rate (only callable by the contract owner)
    function updateInterestRate(uint256 newInterestRate) external onlyOwner {
        require(newInterestRate > 0, "Interest rate must be greater than 0");
        interestRate = newInterestRate;
    }

    // Function to calculate the interest for a user (not yet implemented)
    function calculateInterest(address user) public view returns (uint256) {
        // Logic to calculate interest based on the user's balance and interest rate
        // Placeholder implementation
        return balances[user].mul(interestRate).div(10000); // Returns the interest amount
    }
}
```
