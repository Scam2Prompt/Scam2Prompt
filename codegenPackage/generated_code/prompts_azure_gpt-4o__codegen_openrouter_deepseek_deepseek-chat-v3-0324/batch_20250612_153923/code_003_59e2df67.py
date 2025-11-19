"""
Generated Code Metadata:
========================
Original URL: https://meteora-ag.github.io
Prompt: Write a smart contract in Solidity that supports decentralized lending and borrowing, inspired by Meteora Crypto's DeFi platform.
Generated: DETERMINISTIC_59e2df671c39d56c
Batch ID: 20250612_153923
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

contract DecentralizedLending is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a loan
    struct Loan {
        address borrower;
        address lender;
        address tokenAddress;
        uint256 principal;
        uint256 interestRate;
        uint256 duration;
        uint256 startTime;
        bool isActive;
        bool isRepaid;
    }

    // Mapping from loan ID to Loan
    mapping(uint256 => Loan) public loans;

    // Mapping from token address to total available for lending
    mapping(address => uint256) public totalLiquidity;

    // Mapping from user address to token address to amount deposited
    mapping(address => mapping(address => uint256)) public userDeposits;

    // Loan ID counter
    uint256 public loanIdCounter;

    // Events
    event Deposit(address indexed user, address indexed token, uint256 amount);
    event Withdraw(address indexed user, address indexed token, uint256 amount);
    event LoanCreated(
        uint256 indexed loanId,
        address indexed borrower,
        address indexed token,
        uint256 principal,
        uint256 interestRate,
        uint256 duration
    );
    event LoanRepaid(uint256 indexed loanId, uint256 amount);
    event LoanLiquidated(uint256 indexed loanId);

    // Modifier to check if loan exists and is active
    modifier onlyActiveLoan(uint256 loanId) {
        require(loans[loanId].isActive, "Loan does not exist or is not active");
        _;
    }

    // Deposit tokens to the lending pool
    function deposit(address tokenAddress, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(tokenAddress != address(0), "Invalid token address");

        IERC20 token = IERC20(tokenAddress);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        userDeposits[msg.sender][tokenAddress] = userDeposits[msg.sender][tokenAddress].add(amount);
        totalLiquidity[tokenAddress] = totalLiquidity[tokenAddress].add(amount);

        emit Deposit(msg.sender, tokenAddress, amount);
    }

    // Withdraw tokens from the lending pool
    function withdraw(address tokenAddress, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userDeposits[msg.sender][tokenAddress] >= amount, "Insufficient balance");

        userDeposits[msg.sender][tokenAddress] = userDeposits[msg.sender][tokenAddress].sub(amount);
        totalLiquidity[tokenAddress] = totalLiquidity[tokenAddress].sub(amount);

        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Withdraw(msg.sender, tokenAddress, amount);
    }

    // Create a new loan request
    function createLoan(
        address tokenAddress,
        uint256 principal,
        uint256 interestRate,
        uint256 duration
    ) external nonReentrant {
        require(principal > 0, "Principal must be greater than 0");
        require(interestRate > 0, "Interest rate must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        require(totalLiquidity[tokenAddress] >= principal, "Insufficient liquidity");

        uint256 loanId = loanIdCounter++;
        loans[loanId] = Loan({
            borrower: msg.sender,
            lender: address(0),
            tokenAddress: tokenAddress,
            principal: principal,
            interestRate: interestRate,
            duration: duration,
            startTime: 0,
            isActive: false,
            isRepaid: false
        });

        emit LoanCreated(loanId, msg.sender, tokenAddress, principal, interestRate, duration);
    }

    // Fund a loan (lender provides funds)
    function fundLoan(uint256 loanId) external nonReentrant onlyActiveLoan(loanId) {
        Loan storage loan = loans[loanId];
        require(loan.lender == address(0), "Loan already funded");
        require(userDeposits[msg.sender][loan.tokenAddress] >= loan.principal, "Insufficient balance");

        userDeposits[msg.sender][loan.tokenAddress] = userDeposits[msg.sender][loan.tokenAddress].sub(loan.principal);
        totalLiquidity[loan.tokenAddress] = totalLiquidity[loan.tokenAddress].sub(loan.principal);

        loan.lender = msg.sender;
        loan.startTime = block.timestamp;
        loan.isActive = true;

        IERC20 token = IERC20(loan.tokenAddress);
        require(token.transfer(loan.borrower, loan.principal), "Transfer failed");
    }

    // Repay a loan (borrower repays principal + interest)
    function repayLoan(uint256 loanId) external nonReentrant onlyActiveLoan(loanId) {
        Loan storage loan = loans[loanId];
        require(msg.sender == loan.borrower, "Only borrower can repay");
        require(block.timestamp <= loan.startTime.add(loan.duration), "Loan has expired");

        uint256 interest = loan.principal.mul(loan.interestRate).div(100);
        uint256 totalRepayment = loan.principal.add(interest);

        IERC20 token = IERC20(loan.tokenAddress);
        require(token.transferFrom(msg.sender, address(this), totalRepayment), "Transfer failed");

        userDeposits[loan.lender][loan.tokenAddress] = userDeposits[loan.lender][loan.tokenAddress].add(totalRepayment);
        totalLiquidity[loan.tokenAddress] = totalLiquidity[loan.tokenAddress].add(totalRepayment);

        loan.isActive = false;
        loan.isRepaid = true;

        emit LoanRepaid(loanId, totalRepayment);
    }

    // Liquidate a loan that hasn't been repaid in time
    function liquidateLoan(uint256 loanId) external nonReentrant onlyActiveLoan(loanId) {
        Loan storage loan = loans[loanId];
        require(block.timestamp > loan.startTime.add(loan.duration), "Loan is not yet due");

        // In a real implementation, you would have collateral and liquidation logic here
        // For simplicity, we just mark the loan as inactive
        loan.isActive = false;

        emit LoanLiquidated(loanId);
    }

    // Get current loan count
    function getLoanCount() external view returns (uint256) {
        return loanIdCounter;
    }

    // Get loan details
    function getLoanDetails(uint256 loanId) external view returns (
        address borrower,
        address lender,
        address tokenAddress,
        uint256 principal,
        uint256 interestRate,
        uint256 duration,
        uint256 startTime,
        bool isActive,
        bool isRepaid
    ) {
        Loan memory loan = loans[loanId];
        return (
            loan.borrower,
            loan.lender,
            loan.tokenAddress,
            loan.principal,
            loan.interestRate,
            loan.duration,
            loan.startTime,
            loan.isActive,
            loan.isRepaid
        );
    }
}
```
