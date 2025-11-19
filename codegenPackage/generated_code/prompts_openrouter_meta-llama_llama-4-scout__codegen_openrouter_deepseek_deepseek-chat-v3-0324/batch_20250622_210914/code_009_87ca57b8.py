"""
Generated Code Metadata:
========================
Original URL: https://oeth-v-0-0.pages.dev
Prompt: Outline a decentralized application (dApp) concept that leverages OUSD for stablecoin lending or borrowing, including how the dApp would interact with OUSD's smart contracts.
Generated: DETERMINISTIC_87ca57b8991926a3
Batch ID: 20250622_210914
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
import "@openzeppelin/contracts/access/Ownable.sol";

interface IOUSD {
    function rebaseOptIn() external;
    function rebaseOptOut() external;
    function mint(address _account, uint256 _amount) external;
    function burn(address _account, uint256 _amount) external;
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract OUSDLendingPlatform is ReentrancyGuard, Ownable {
    IERC20 public ousd;
    uint256 public interestRate; // in basis points (1% = 100)
    uint256 public totalLiquidity;
    uint256 public totalBorrowed;
    
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 startTime;
        uint256 interest;
        bool active;
    }
    
    mapping(address => uint256) public lenderBalances;
    mapping(address => Loan) public loans;
    
    event Deposited(address indexed lender, uint256 amount);
    event Withdrawn(address indexed lender, uint256 amount);
    event Borrowed(address indexed borrower, uint256 amount);
    event Repaid(address indexed borrower, uint256 amount, uint256 interest);
    
    constructor(address _ousdAddress, uint256 _interestRate) {
        ousd = IERC20(_ousdAddress);
        interestRate = _interestRate;
        
        // Opt into rebasing by default
        IOUSD(_ousdAddress).rebaseOptIn();
    }
    
    function deposit(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        bool success = ousd.transferFrom(msg.sender, address(this), _amount);
        require(success, "Transfer failed");
        
        lenderBalances[msg.sender] += _amount;
        totalLiquidity += _amount;
        
        emit Deposited(msg.sender, _amount);
    }
    
    function withdraw(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(lenderBalances[msg.sender] >= _amount, "Insufficient balance");
        require(totalLiquidity >= _amount, "Insufficient platform liquidity");
        
        lenderBalances[msg.sender] -= _amount;
        totalLiquidity -= _amount;
        
        bool success = ousd.transfer(msg.sender, _amount);
        require(success, "Transfer failed");
        
        emit Withdrawn(msg.sender, _amount);
    }
    
    function borrow(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(totalLiquidity >= _amount, "Insufficient platform liquidity");
        require(loans[msg.sender].active == false, "Active loan exists");
        
        totalLiquidity -= _amount;
        totalBorrowed += _amount;
        
        loans[msg.sender] = Loan({
            borrower: msg.sender,
            amount: _amount,
            startTime: block.timestamp,
            interest: calculateInterest(_amount),
            active: true
        });
        
        bool success = ousd.transfer(msg.sender, _amount);
        require(success, "Transfer failed");
        
        emit Borrowed(msg.sender, _amount);
    }
    
    function repay() external nonReentrant {
        Loan storage loan = loans[msg.sender];
        require(loan.active, "No active loan");
        
        uint256 totalAmount = loan.amount + loan.interest;
        
        bool success = ousd.transferFrom(msg.sender, address(this), totalAmount);
        require(success, "Transfer failed");
        
        totalLiquidity += totalAmount;
        totalBorrowed -= loan.amount;
        
        emit Repaid(msg.sender, loan.amount, loan.interest);
        
        delete loans[msg.sender];
    }
    
    function calculateInterest(uint256 _amount) public view returns (uint256) {
        return (_amount * interestRate) / 10000; // Convert basis points to percentage
    }
    
    function setInterestRate(uint256 _newRate) external onlyOwner {
        require(_newRate <= 1000, "Rate too high"); // Max 10%
        interestRate = _newRate;
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = ousd.balanceOf(address(this));
        ousd.transfer(owner(), balance);
        totalLiquidity = 0;
    }
}
```
