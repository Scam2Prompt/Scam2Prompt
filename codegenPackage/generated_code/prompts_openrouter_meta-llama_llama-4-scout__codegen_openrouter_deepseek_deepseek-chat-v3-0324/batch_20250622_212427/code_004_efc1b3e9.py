"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Develop a simple smart contract in Solidity that utilizes QiDao's collateralized stablecoin MAI for lending.
Generated: DETERMINISTIC_efc1b3e9985c61e2
Batch ID: 20250622_212427
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

interface IMAI is IERC20 {
    function borrow(uint256 borrowAmount, uint256 collateralAmount) external;
    function repay(uint256 repayAmount) external;
    function getDebt(address user) external view returns (uint256);
}

contract MAILender is Ownable, ReentrancyGuard {
    IMAI public maiToken;
    IERC20 public collateralToken;
    
    mapping(address => uint256) public collateralDeposited;
    mapping(address => uint256) public borrowedAmount;
    
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    
    constructor(address _maiToken, address _collateralToken) {
        require(_maiToken != address(0), "Invalid MAI token address");
        require(_collateralToken != address(0), "Invalid collateral token address");
        
        maiToken = IMAI(_maiToken);
        collateralToken = IERC20(_collateralToken);
    }
    
    function depositCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        collateralToken.transferFrom(msg.sender, address(this), amount);
        collateralDeposited[msg.sender] += amount;
        
        emit Deposited(msg.sender, amount);
    }
    
    function borrowMAI(uint256 borrowAmount, uint256 collateralAmount) external nonReentrant {
        require(borrowAmount > 0, "Borrow amount must be greater than 0");
        require(collateralAmount > 0, "Collateral amount must be greater than 0");
        require(
            collateralDeposited[msg.sender] >= collateralAmount,
            "Insufficient collateral deposited"
        );
        
        maiToken.borrow(borrowAmount, collateralAmount);
        borrowedAmount[msg.sender] += borrowAmount;
        
        emit Borrowed(msg.sender, borrowAmount);
    }
    
    function repayMAI(uint256 repayAmount) external nonReentrant {
        require(repayAmount > 0, "Repay amount must be greater than 0");
        require(
            borrowedAmount[msg.sender] >= repayAmount,
            "Repay amount exceeds borrowed amount"
        );
        
        maiToken.transferFrom(msg.sender, address(this), repayAmount);
        maiToken.repay(repayAmount);
        borrowedAmount[msg.sender] -= repayAmount;
        
        emit Repaid(msg.sender, repayAmount);
    }
    
    function withdrawCollateral(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(
            collateralDeposited[msg.sender] >= amount,
            "Insufficient collateral deposited"
        );
        require(
            maiToken.getDebt(address(this)) == 0,
            "Cannot withdraw while debt exists"
        );
        
        collateralDeposited[msg.sender] -= amount;
        collateralToken.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }
    
    function setMAIToken(address _maiToken) external onlyOwner {
        require(_maiToken != address(0), "Invalid MAI token address");
        maiToken = IMAI(_maiToken);
    }
    
    function setCollateralToken(address _collateralToken) external onlyOwner {
        require(_collateralToken != address(0), "Invalid collateral token address");
        collateralToken = IERC20(_collateralToken);
    }
}
```
