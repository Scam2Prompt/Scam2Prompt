"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Write a tutorial for integrating ERC-20 compliant tenderized tokens into a DeFi lending protocol, allowing users to leverage their staked assets.
Generated: DETERMINISTIC_81ab68781f6eff0f
Batch ID: 20250612_145913
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface ITenderizedToken {
    function underlying() external view returns (address);
    function deposit(uint256 amount) external;
    function withdraw(uint256 shares) external;
    function balanceOf(address account) external view returns (uint256);
}

contract DeFiLendingProtocol is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    struct Loan {
        address borrower;
        address collateralToken;
        uint256 collateralAmount;
        uint256 borrowedAmount;
        uint256 interestRate;
        uint256 startTime;
        uint256 dueTime;
        bool isActive;
    }

    mapping(address => uint256) public collateralFactors;
    mapping(address => uint256) public interestRates;
    mapping(address => bool) public supportedTokens;
    mapping(address => Loan[]) public userLoans;
    mapping(address => mapping(address => uint256)) public userCollateral;

    event TokenSupported(address indexed token, uint256 collateralFactor, uint256 interestRate);
    event LoanCreated(address indexed borrower, uint256 loanId, uint256 amount);
    event LoanRepaid(address indexed borrower, uint256 loanId);
    event LoanLiquidated(address indexed borrower, uint256 loanId);

    constructor() {}

    /**
     * @dev Add a supported token with collateral factor and interest rate
     * @param token Address of the ERC20 token
     * @param collateralFactor Collateral factor (e.g., 7500 for 75%)
     * @param interestRate Annual interest rate (e.g., 500 for 5%)
     */
    function supportToken(address token, uint256 collateralFactor, uint256 interestRate) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(collateralFactor > 0 && collateralFactor <= 10000, "Invalid collateral factor");
        
        supportedTokens[token] = true;
        collateralFactors[token] = collateralFactor;
        interestRates[token] = interestRate;
        
        emit TokenSupported(token, collateralFactor, interestRate);
    }

    /**
     * @dev Deposit tenderized tokens as collateral
     * @param tenderizedToken Address of the tenderized token contract
     * @param amount Amount of tenderized tokens to deposit
     */
    function depositCollateral(address tenderizedToken, uint256 amount) external nonReentrant {
        require(supportedTokens[tenderizedToken], "Token not supported");
        
        ITenderizedToken token = ITenderizedToken(tenderizedToken);
        address underlyingToken = token.underlying();
        
        IERC20(tenderizedToken).safeTransferFrom(msg.sender, address(this), amount);
        userCollateral[msg.sender][tenderizedToken] += amount;
    }

    /**
     * @dev Withdraw collateral from the protocol
     * @param tenderizedToken Address of the tenderized token contract
     * @param amount Amount of tenderized tokens to withdraw
     */
    function withdrawCollateral(address tenderizedToken, uint256 amount) external nonReentrant {
        require(userCollateral[msg.sender][tenderizedToken] >= amount, "Insufficient collateral");
        
        // Check if withdrawal would make existing loans undercollateralized
        uint256 totalBorrowed = 0;
        for (uint256 i = 0; i < userLoans[msg.sender].length; i++) {
            if (userLoans[msg.sender][i].isActive) {
                totalBorrowed += userLoans[msg.sender][i].borrowedAmount;
            }
        }
        
        uint256 newCollateralValue = calculateCollateralValue(msg.sender) - 
            (amount * collateralFactors[tenderizedToken] / 10000);
        
        require(newCollateralValue >= totalBorrowed, "Withdrawal would make loans undercollateralized");
        
        userCollateral[msg.sender][tenderizedToken] -= amount;
        IERC20(tenderizedToken).safeTransfer(msg.sender, amount);
    }

    /**
     * @dev Borrow against deposited collateral
     * @param token Address of the token to borrow
     * @param amount Amount to borrow
     */
    function borrow(address token, uint256 amount) external nonReentrant {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 collateralValue = calculateCollateralValue(msg.sender);
        uint256 maxBorrow = collateralValue * collateralFactors[token] / 10000;
        
        require(amount <= maxBorrow, "Insufficient collateral");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient protocol liquidity");
        
        // Create new loan
        Loan memory newLoan = Loan({
            borrower: msg.sender,
            collateralToken: token,
            collateralAmount: amount,
            borrowedAmount: amount,
            interestRate: interestRates[token],
            startTime: block.timestamp,
            dueTime: block.timestamp + 30 days, // 30-day loan term
            isActive: true
        });
        
        userLoans[msg.sender].push(newLoan);
        IERC20(token).safeTransfer(msg.sender, amount);
        
        emit LoanCreated(msg.sender, userLoans[msg.sender].length - 1, amount);
    }

    /**
     * @dev Repay a loan
     * @param loanId ID of the loan to repay
     */
    function repay(uint256 loanId) external nonReentrant {
        require(loanId < userLoans[msg.sender].length, "Invalid loan ID");
        Loan storage loan = userLoans[msg.sender][loanId];
        require(loan.isActive, "Loan is not active");
        
        uint256 interest = calculateInterest(loan.borrowedAmount, loan.interestRate, loan.startTime);
        uint256 totalRepayment = loan.borrowedAmount + interest;
        
        IERC20(loan.collateralToken).safeTransferFrom(msg.sender, address(this), totalRepayment);
        loan.isActive = false;
        
        emit LoanRepaid(msg.sender, loanId);
    }

    /**
     * @dev Liquidate an undercollateralized loan
     * @param borrower Address of the borrower
     * @param loanId ID of the loan to liquidate
     */
    function liquidate(address borrower, uint256 loanId) external nonReentrant {
        require(loanId < userLoans[borrower].length, "Invalid loan ID");
        Loan storage loan = userLoans[borrower][loanId];
        require(loan.isActive, "Loan is not active");
        
        uint256 collateralValue = calculateCollateralValue(borrower);
        require(collateralValue < loan.borrowedAmount, "Loan is not undercollateralized");
        
        // Transfer collateral to liquidator
        userCollateral[borrower][loan.collateralToken] -= loan.collateralAmount;
        IERC20(loan.collateralToken).safeTransfer(msg.sender, loan.collateralAmount);
        
        loan.isActive = false;
        emit LoanLiquidated(borrower, loanId);
    }

    /**
     * @dev Calculate the total collateral value for a user
     * @param user Address of the user
     * @return Total collateral value
     */
    function calculateCollateralValue(address user) public view returns (uint256) {
        uint256 totalValue = 0;
        
        // Iterate through all supported tokens to calculate collateral value
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            address token = supportedTokens[i];
            if (userCollateral[user][token] > 0) {
                totalValue += userCollateral[user][token] * collateralFactors[token] / 10000;
            }
        }
        
        return totalValue;
    }

    /**
     * @dev Calculate interest for a loan
     * @param principal Loan principal amount
     * @param rate Annual interest rate
     * @param startTime Loan start time
     * @return Interest amount
     */
    function calculateInterest(uint256 principal, uint256 rate, uint256 startTime) public view returns (uint256) {
        uint256 duration = block.timestamp - startTime;
        return principal * rate * duration / (365 days * 10000);
    }

    /**
     * @dev Emergency withdraw protocol funds (owner only)
     * @param token Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
