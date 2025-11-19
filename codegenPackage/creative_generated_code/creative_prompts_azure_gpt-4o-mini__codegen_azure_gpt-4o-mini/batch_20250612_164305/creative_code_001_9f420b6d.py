"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write a smart contract that allows for permissionless borrowing and lending of crypto assets in a Silo, ensuring shared liquidity.
Generated: DETERMINISTIC_9f420b6d4f3d5bd1
Batch ID: 20250612_164305
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Silo Lending and Borrowing Smart Contract
 * @dev This contract allows users to deposit assets into a shared liquidity pool,
 *      enabling permissionless borrowing and lending of ERC20 tokens.
 */
contract Silo is Ownable {
    // Struct to hold user's balance and borrow details
    struct User {
        uint256 depositedAmount;  // Total amount deposited by the user
        uint256 borrowedAmount;    // Total amount borrowed by the user
        uint256 collateralAmount;  // Amount of collateral deposited
    }

    // Mapping to keep track of users' deposits and borrowings
    mapping(address => User) public users;

    // Event declarations for deposit, withdrawal, borrow, and repay actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    // Variables to manage the ERC20 token and interest rate
    IERC20 public stablecoin;
    uint256 public interestRate; // Interest rate expressed in basis points (1/100th of a percent)

    // Constructor to initialize the contract with the ERC20 token address and interest rate
    constructor(IERC20 _stablecoin, uint256 _interestRate) {
        require(address(_stablecoin) != address(0), "Invalid token address");
        require(_interestRate > 0, "Interest rate must be greater than 0");

        stablecoin = _stablecoin;
        interestRate = _interestRate;
    }

    // Function to deposit tokens into the Silo
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than 0");
        
        // Transfer tokens from user to this contract
        stablecoin.transferFrom(msg.sender, address(this), amount);
        
        // Update user's deposit information
        users[msg.sender].depositedAmount += amount;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw tokens from the Silo
    function withdraw(uint256 amount) external {
        User storage user = users[msg.sender];
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(user.depositedAmount >= amount, "Insufficient balance to withdraw");

        // Update user's deposit information before transferring tokens
        user.depositedAmount -= amount;

        // Transfer tokens back to the user
        stablecoin.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to borrow tokens from the Silo
    function borrow(uint256 amount) external {
        User storage user = users[msg.sender];
        require(amount > 0, "Borrow amount must be greater than 0");
        require(user.depositedAmount > 0, "No collateral deposited");

        // Update borrow amount and transfer tokens to user
        user.borrowedAmount += amount;
        stablecoin.transfer(msg.sender, amount);

        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed tokens
    function repay(uint256 amount) external {
        User storage user = users[msg.sender];
        require(amount > 0, "Repay amount must be greater than 0");
        require(user.borrowedAmount >= amount, "Repay amount exceeds borrowed amount");

        // Update user's borrow amount before transferring tokens
        user.borrowedAmount -= amount;

        // Transfer tokens from user to this contract
        stablecoin.transferFrom(msg.sender, address(this), amount);

        emit Repaid(msg.sender, amount);
    }

    // Function to get user details
    function getUserInfo(address userAddress) external view returns (uint256 deposited, uint256 borrowed) {
        User storage user = users[userAddress];
        return (user.depositedAmount, user.borrowedAmount);
    }
}
```
