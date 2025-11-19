"""
Generated Code Metadata:
========================
Original URL: https://elephant-claim.pages.dev
Prompt: How can I implement a smart contract that utilizes the TRUNK token as collateral in a DeFi ecosystem, similar to the Elephant Money protocol?
Generated: DETERMINISTIC_00c4760bd4b49914
Batch ID: 20250612_155122
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

interface ITRUNK {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TRUNKCollateralDeFi is Ownable, ReentrancyGuard {
    ITRUNK public trunkToken;
    uint256 public collateralRatio = 150; // 150% collateralization ratio
    uint256 public interestRate = 10; // 10% annual interest
    uint256 public liquidationPenalty = 5; // 5% liquidation penalty
    
    struct Loan {
        uint256 collateralAmount;
        uint256 borrowedAmount;
        uint256 startTime;
        bool isActive;
    }
    
    mapping(address => Loan) public loans;
    uint256 public totalCollateral;
    uint256 public totalBorrowed;
    
    event LoanCreated(address indexed borrower, uint256 collateralAmount, uint256 borrowedAmount);
    event LoanRepaid(address indexed borrower, uint256 repaidAmount);
    event LoanLiquidated(address indexed borrower, uint256 liquidatedAmount);
    
    constructor(address _trunkTokenAddress) {
        trunkToken = ITRUNK(_trunkTokenAddress);
    }
    
    function depositCollateralAndBorrow(uint256 _collateralAmount, uint256 _borrowAmount) external nonReentrant {
        require(_collateralAmount > 0, "Collateral amount must be greater than 0");
        require(_borrowAmount > 0, "Borrow amount must be greater than 0");
        require(loans[msg.sender].isActive == false, "Active loan already exists");
        
        // Calculate minimum collateral required
        uint256 minCollateral = (_borrowAmount * collateralRatio) / 100;
        require(_collateralAmount >= minCollateral, "Insufficient collateral");
        
        // Transfer TRUNK tokens from user to contract
        require(trunkToken.transferFrom(msg.sender, address(this), _collateralAmount), "TRUNK transfer failed");
        
        // Create loan
        loans[msg.sender] = Loan({
            collateralAmount: _collateralAmount,
            borrowedAmount: _borrowAmount,
            startTime: block.timestamp,
            isActive: true
        });
        
        totalCollateral += _collateralAmount;
        totalBorrowed += _borrowAmount;
        
        // Transfer borrowed tokens to user (assuming native token for simplicity)
        (bool success, ) = msg.sender.call{value: _borrowAmount}("");
        require(success, "Borrow transfer failed");
        
        emit LoanCreated(msg.sender, _collateralAmount, _borrowAmount);
    }
    
    function repayLoan() external payable nonReentrant {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan");
        
        uint256 interest = calculateInterest(loan.borrowedAmount, loan.startTime);
        uint256 totalRepayment = loan.borrowedAmount + interest;
        require(msg.value >= totalRepayment, "Insufficient repayment amount");
        
        // Return excess payment
        if (msg.value > totalRepayment) {
            (bool excessSuccess, ) = msg.sender.call{value: msg.value - totalRepayment}("");
            require(excessSuccess, "Excess transfer failed");
        }
        
        // Return collateral
        require(trunkToken.transfer(msg.sender, loan.collateralAmount), "Collateral return failed");
        
        totalCollateral -= loan.collateralAmount;
        totalBorrowed -= loan.borrowedAmount;
        
        delete loans[msg.sender];
        
        emit LoanRepaid(msg.sender, totalRepayment);
    }
    
    function liquidateLoan(address _borrower) external nonReentrant {
        Loan storage loan = loans[_borrower];
        require(loan.isActive, "No active loan");
        
        uint256 interest = calculateInterest(loan.borrowedAmount, loan.startTime);
        uint256 totalDebt = loan.borrowedAmount + interest;
        
        // Check if collateral value is below required ratio
        uint256 currentCollateralValue = loan.collateralAmount;
        uint256 requiredCollateral = (totalDebt * collateralRatio) / 100;
        
        if (currentCollateralValue < requiredCollateral) {
            // Calculate liquidation amount with penalty
            uint256 liquidationAmount = (loan.collateralAmount * (100 - liquidationPenalty)) / 100;
            
            // Transfer collateral to liquidator
            require(trunkToken.transfer(msg.sender, liquidationAmount), "Liquidation transfer failed");
            
            // Burn the remaining collateral (or send to treasury)
            uint256 remainingCollateral = loan.collateralAmount - liquidationAmount;
            if (remainingCollateral > 0) {
                require(trunkToken.transfer(owner(), remainingCollateral), "Remaining collateral transfer failed");
            }
            
            totalCollateral -= loan.collateralAmount;
            totalBorrowed -= loan.borrowedAmount;
            
            delete loans[_borrower];
            
            emit LoanLiquidated(_borrower, liquidationAmount);
        }
    }
    
    function calculateInterest(uint256 _principal, uint256 _startTime) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - _startTime;
        uint256 interest = (_principal * interestRate * timeElapsed) / (365 days * 100);
        return interest;
    }
    
    function setCollateralRatio(uint256 _newRatio) external onlyOwner {
        require(_newRatio >= 110, "Collateral ratio too low");
        collateralRatio = _newRatio;
    }
    
    function setInterestRate(uint256 _newRate) external onlyOwner {
        require(_newRate <= 50, "Interest rate too high");
        interestRate = _newRate;
    }
    
    function setLiquidationPenalty(uint256 _newPenalty) external onlyOwner {
        require(_newPenalty <= 20, "Liquidation penalty too high");
        liquidationPenalty = _newPenalty;
    }
    
    receive() external payable {}
    
    // Emergency function to recover ERC20 tokens
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
    
    // Emergency function to recover native currency
    function recoverNative(uint256 amount) external onlyOwner {
        (bool success, ) = owner().call{value: amount}("");
        require(success, "Transfer failed");
    }
}
```
