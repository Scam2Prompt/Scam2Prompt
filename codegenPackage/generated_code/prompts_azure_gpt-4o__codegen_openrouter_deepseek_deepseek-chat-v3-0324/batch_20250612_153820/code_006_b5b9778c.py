"""
Generated Code Metadata:
========================
Original URL: https://web-ethena.com
Prompt: Provide code examples for setting up permissionless access to financial tools in a blockchain application, inspired by Ethena Fi's intermediary-free approach.
Generated: DETERMINISTIC_b5b9778c18808c8c
Batch ID: 20250612_153820
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PermissionlessYieldVault
 * @dev A contract that allows permissionless deposits and withdrawals
 * with yield generation capabilities
 */
contract PermissionlessYieldVault is ReentrancyGuard, Ownable {
    IERC20 public immutable token;
    uint256 public totalDeposits;
    uint256 public yieldRate; // Annual yield rate in basis points (100 = 1%)
    
    mapping(address => uint256) public userDeposits;
    
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event YieldRateUpdated(uint256 newRate);
    
    /**
     * @dev Initializes the contract with the token address
     * @param _token Address of the ERC20 token to be used
     * @param _initialYieldRate Initial annual yield rate in basis points
     */
    constructor(address _token, uint256 _initialYieldRate) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        yieldRate = _initialYieldRate;
    }
    
    /**
     * @dev Permissionless deposit function
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        bool success = token.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");
        
        userDeposits[msg.sender] += amount;
        totalDeposits += amount;
        
        emit Deposited(msg.sender, amount);
    }
    
    /**
     * @dev Permissionless withdrawal function
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userDeposits[msg.sender] >= amount, "Insufficient balance");
        
        uint256 yield = calculateYield(msg.sender);
        userDeposits[msg.sender] -= amount;
        totalDeposits -= amount;
        
        bool success = token.transfer(msg.sender, amount + yield);
        require(success, "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }
    
    /**
     * @dev Calculates yield for a user based on their deposit duration
     * @param user Address of the user
     * @return yieldAmount Calculated yield amount
     */
    function calculateYield(address user) public view returns (uint256 yieldAmount) {
        // Simplified yield calculation - in production you'd use time-based calculation
        uint256 depositAmount = userDeposits[user];
        yieldAmount = (depositAmount * yieldRate) / 10000; // Basis points conversion
        return yieldAmount;
    }
    
    /**
     * @dev Updates the yield rate (owner only)
     * @param newRate New annual yield rate in basis points
     */
    function updateYieldRate(uint256 newRate) external onlyOwner {
        require(newRate <= 5000, "Yield rate too high"); // Max 50% APY
        yieldRate = newRate;
        emit YieldRateUpdated(newRate);
    }
}

/**
 * @title PermissionlessSwap
 * @dev A simple permissionless token swap contract
 */
contract PermissionlessSwap {
    IERC20 public immutable tokenA;
    IERC20 public immutable tokenB;
    uint256 public exchangeRate; // Amount of tokenB per tokenA (scaled by 1e18)
    
    event Swapped(address indexed user, uint256 amountA, uint256 amountB);
    
    constructor(address _tokenA, address _tokenB, uint256 _exchangeRate) {
        require(_tokenA != address(0) && _tokenB != address(0), "Invalid token address");
        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        exchangeRate = _exchangeRate;
    }
    
    /**
     * @dev Permissionless token swap function
     * @param amountA Amount of tokenA to swap
     */
    function swapAForB(uint256 amountA) external {
        require(amountA > 0, "Amount must be greater than 0");
        
        uint256 amountB = (amountA * exchangeRate) / 1e18;
        require(tokenB.balanceOf(address(this)) >= amountB, "Insufficient liquidity");
        
        bool successA = tokenA.transferFrom(msg.sender, address(this), amountA);
        bool successB = tokenB.transfer(msg.sender, amountB);
        
        require(successA && successB, "Transfer failed");
        
        emit Swapped(msg.sender, amountA, amountB);
    }
    
    /**
     * @dev Updates the exchange rate (permissionless governance could be added)
     * @param newRate New exchange rate (tokenB per tokenA, scaled by 1e18)
     */
    function updateExchangeRate(uint256 newRate) external {
        exchangeRate = newRate;
    }
}

/**
 * @title PermissionlessLending
 * @dev A simple permissionless lending protocol
 */
contract PermissionlessLending is ReentrancyGuard {
    IERC20 public immutable token;
    uint256 public totalLent;
    uint256 public interestRate; // Annual interest rate in basis points
    
    mapping(address => uint256) public loans;
    mapping(address => uint256) public lastActionBlock;
    
    event Lent(address indexed borrower, uint256 amount);
    event Repaid(address indexed borrower, uint256 amount);
    
    constructor(address _token, uint256 _interestRate) {
        token = IERC20(_token);
        interestRate = _interestRate;
    }
    
    /**
     * @dev Permissionless loan function
     * @param amount Amount to borrow
     */
    function borrow(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient liquidity");
        
        loans[msg.sender] += amount;
        totalLent += amount;
        lastActionBlock[msg.sender] = block.number;
        
        bool success = token.transfer(msg.sender, amount);
        require(success, "Transfer failed");
        
        emit Lent(msg.sender, amount);
    }
    
    /**
     * @dev Permissionless repayment function
     * @param amount Amount to repay
     */
    function repay(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(loans[msg.sender] > 0, "No active loan");
        
        uint256 interest = calculateInterest(msg.sender);
        uint256 totalRepayment = amount + interest;
        
        loans[msg.sender] -= amount;
        totalLent -= amount;
        
        bool success = token.transferFrom(msg.sender, address(this), totalRepayment);
        require(success, "Transfer failed");
        
        emit Repaid(msg.sender, amount);
    }
    
    /**
     * @dev Calculates interest for a loan
     * @param borrower Address of the borrower
     * @return interest Calculated interest amount
     */
    function calculateInterest(address borrower) public view returns (uint256 interest) {
        uint256 blocksElapsed = block.number - lastActionBlock[borrower];
        // Simplified interest calculation - in production you'd use time-based calculation
        interest = (loans[borrower] * interestRate * blocksElapsed) / (10000 * 2102400); // ~2102400 blocks per year
        return interest;
    }
}
```
