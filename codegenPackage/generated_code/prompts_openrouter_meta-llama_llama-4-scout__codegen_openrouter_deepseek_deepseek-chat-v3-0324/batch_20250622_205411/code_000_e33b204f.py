"""
Generated Code Metadata:
========================
Original URL: https://de-fi.webflow.io
Prompt: "Generate a basic smart contract for a De-Fi lending platform using Solidity."
Generated: DETERMINISTIC_e33b204f9a388973
Batch ID: 20250622_205411
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFiLendingPlatform
 * @dev A simple decentralized lending platform allowing users to deposit and borrow ERC20 tokens
 */
contract DeFiLendingPlatform is ReentrancyGuard {
    using SafeMath for uint256;

    // Token details
    IERC20 public token;
    
    // Interest rate (in basis points, e.g., 100 = 1%)
    uint256 public interestRate;
    
    // Platform owner
    address public owner;
    
    // Mapping of lenders to their deposited amounts
    mapping(address => uint256) public deposits;
    
    // Mapping of borrowers to their borrowed amounts
    mapping(address => uint256) public borrows;
    
    // Total deposited amount
    uint256 public totalDeposited;
    
    // Total borrowed amount
    uint256 public totalBorrowed;
    
    // Events
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor initializes the lending platform
     * @param _token Address of the ERC20 token to be used
     * @param _interestRate Annual interest rate in basis points (100 = 1%)
     */
    constructor(IERC20 _token, uint256 _interestRate) {
        require(address(_token) != address(0), "Invalid token address");
        require(_interestRate > 0, "Interest rate must be positive");
        
        token = _token;
        interestRate = _interestRate;
        owner = msg.sender;
    }
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Deposit tokens to the lending platform
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");
        
        deposits[msg.sender] = deposits[msg.sender].add(amount);
        totalDeposited = totalDeposited.add(amount);
        
        emit Deposited(msg.sender, amount);
    }
    
    /**
     * @dev Borrow tokens from the lending platform
     * @param amount Amount of tokens to borrow
     */
    function borrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= availableLiquidity(), "Insufficient liquidity");
        
        borrows[msg.sender] = borrows[msg.sender].add(amount);
        totalBorrowed = totalBorrowed.add(amount);
        
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit Borrowed(msg.sender, amount);
    }
    
    /**
     * @dev Repay borrowed tokens plus interest
     * @param amount Amount of tokens to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(borrows[msg.sender] > 0, "No borrow to repay");
        
        uint256 interest = calculateInterest(msg.sender);
        uint256 totalRepayment = amount.add(interest);
        
        bool success = token.transferFrom(msg.sender, address(this), totalRepayment);
        require(success, "Token transfer failed");
        
        borrows[msg.sender] = borrows[msg.sender].sub(amount);
        totalBorrowed = totalBorrowed.sub(amount);
        
        emit Repaid(msg.sender, totalRepayment);
    }
    
    /**
     * @dev Withdraw deposited tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(deposits[msg.sender] >= amount, "Insufficient deposit balance");
        
        deposits[msg.sender] = deposits[msg.sender].sub(amount);
        totalDeposited = totalDeposited.sub(amount);
        
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }
    
    /**
     * @dev Calculate interest for a borrower
     * @param borrower Address of the borrower
     * @return Interest amount in tokens
     */
    function calculateInterest(address borrower) public view returns (uint256) {
        uint256 borrowedAmount = borrows[borrower];
        return borrowedAmount.mul(interestRate).div(10000);
    }
    
    /**
     * @dev Get available liquidity in the platform
     * @return Available tokens for borrowing
     */
    function availableLiquidity() public view returns (uint256) {
        return totalDeposited.sub(totalBorrowed);
    }
    
    /**
     * @dev Update interest rate (owner only)
     * @param newRate New interest rate in basis points
     */
    function updateInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be positive");
        interestRate = newRate;
    }
    
    /**
     * @dev Withdraw platform fees (owner only)
     * @param amount Amount of tokens to withdraw
     */
    function withdrawFees(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= token.balanceOf(address(this)).sub(totalDeposited), "Insufficient fee balance");
        
        bool success = token.transfer(owner, amount);
        require(success, "Token transfer failed");
    }
}
```
