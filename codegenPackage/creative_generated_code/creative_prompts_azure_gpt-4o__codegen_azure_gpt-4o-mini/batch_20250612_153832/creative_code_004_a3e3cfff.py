"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-morpho.github.io
Prompt: Write a smart contract in Solidity that matches borrowers with available liquidity pools and calculates competitive interest rates dynamically, as described in Morpho's borrowing process.
Generated: DETERMINISTIC_a3e3cfff3c9f86ee
Batch ID: 20250612_153832
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for liquidity pool
interface ILiquidityPool {
    function getAvailableLiquidity() external view returns (uint256);
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Smart contract for managing borrowing and liquidity
contract BorrowingPlatform is Ownable {
    // Struct to hold borrower information
    struct Borrower {
        address borrowerAddress;
        uint256 amountBorrowed;
        uint256 interestRate;
        uint256 borrowTime;
    }

    // State variables
    mapping(address => Borrower) public borrowers;
    ILiquidityPool public liquidityPool;
    uint256 public constant MAX_INTEREST_RATE = 200; // Max interest rate in basis points (2%)
    uint256 public constant MIN_INTEREST_RATE = 50; // Min interest rate in basis points (0.5%)

    // Event to emit when a borrow is made
    event Borrow(address indexed borrower, uint256 amount, uint256 interestRate);

    // Constructor to set the liquidity pool address
    constructor(address _liquidityPool) {
        liquidityPool = ILiquidityPool(_liquidityPool);
    }

    // Function to calculate competitive interest rates based on liquidity
    function calculateInterestRate(uint256 amount) internal view returns (uint256) {
        uint256 availableLiquidity = liquidityPool.getAvailableLiquidity();
        
        // Simple rate calculation based on available liquidity
        if (availableLiquidity < amount) {
            return MAX_INTEREST_RATE; // High rate if not enough liquidity
        } else {
            return MIN_INTEREST_RATE + ((availableLiquidity - amount) * (MAX_INTEREST_RATE - MIN_INTEREST_RATE) / availableLiquidity);
        }
    }

    // Function for borrowers to request a loan
    function borrow(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(borrowers[msg.sender].amountBorrowed == 0, "Outstanding loan exists");

        uint256 interestRate = calculateInterestRate(amount);

        // Update borrower details
        borrowers[msg.sender] = Borrower({
            borrowerAddress: msg.sender,
            amountBorrowed: amount,
            interestRate: interestRate,
            borrowTime: block.timestamp
        });

        // Transfer funds to borrower (assuming pool has sufficient balance)
        liquidityPool.withdraw(amount);
        
        // Emit borrow event
        emit Borrow(msg.sender, amount, interestRate);
    }

    // Function for the owner to deposit liquidity into the pool
    function depositToPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer funds from owner to liquidity pool
        IERC20 token = IERC20(address(liquidityPool));
        require(token.transferFrom(msg.sender, address(liquidityPool), amount), "Transfer failed");

        // Deposit into the liquidity pool
        liquidityPool.deposit(amount);
    }

    // Function to check the outstanding loan details
    function getLoanDetails() external view returns (Borrower memory) {
        return borrowers[msg.sender];
    }

    // Function for the borrower to repay the loan (not detailed here)
    // Implement repayment logic as needed

    // Function to withdraw liquidity from the pool by the owner (not detailed here)
    // Implement withdrawal logic as needed
}
```
