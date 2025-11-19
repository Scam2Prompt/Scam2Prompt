"""
Generated Code Metadata:
========================
Original URL: https://symbioticfinance.xyz
Prompt: "Design a smart contract function to automate the creation and management of asset-backed loans on Symbiotic Finance, considering factors like loan duration and interest rates."
Generated: DETERMINISTIC_6dfa66e7c8535748
Batch ID: 20250622_210840
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

contract AssetBackedLoans is ReentrancyGuard {
    using SafeMath for uint256;

    // Loan structure
    struct Loan {
        address borrower;
        address lender;
        address collateralToken;
        uint256 collateralAmount;
        address loanToken;
        uint256 loanAmount;
        uint256 interestRate; // APR in basis points (1% = 100)
        uint256 duration; // in seconds
        uint256 startTime;
        bool isActive;
        bool isLiquidated;
    }

    // Mapping of loan IDs to loans
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Events
    event LoanCreated(
        uint256 loanId,
        address indexed borrower,
        address indexed lender,
        address collateralToken,
        uint256 collateralAmount,
        address loanToken,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration
    );
    event LoanRepaid(uint256 loanId, uint256 amountRepaid);
    event LoanLiquidated(uint256 loanId, address liquidator);

    // Constants
    uint256 public constant MIN_LOAN_DURATION = 1 days;
    uint256 public constant MAX_LOAN_DURATION = 365 days;
    uint256 public constant MIN_INTEREST_RATE = 100; // 1% APR
    uint256 public constant MAX_INTEREST_RATE = 5000; // 50% APR

    /**
     * @notice Creates a new asset-backed loan
     * @param _collateralToken Address of the collateral token
     * @param _collateralAmount Amount of collateral
     * @param _loanToken Address of the loan token
     * @param _loanAmount Amount to borrow
     * @param _interestRate APR in basis points (1% = 100)
     * @param _duration Loan duration in seconds
     */
    function createLoan(
        address _collateralToken,
        uint256 _collateralAmount,
        address _loanToken,
        uint256 _loanAmount,
        uint256 _interestRate,
        uint256 _duration
    ) external nonReentrant {
        require(_collateralAmount > 0, "Collateral amount must be positive");
        require(_loanAmount > 0, "Loan amount must be positive");
        require(_duration >= MIN_LOAN_DURATION && _duration <= MAX_LOAN_DURATION, "Invalid loan duration");
        require(_interestRate >= MIN_INTEREST_RATE && _interestRate <= MAX_INTEREST_RATE, "Invalid interest rate");

        // Transfer collateral from borrower to contract
        IERC20 collateral = IERC20(_collateralToken);
        require(collateral.transferFrom(msg.sender, address(this), _collateralAmount), "Collateral transfer failed");

        // Create new loan
        uint256 loanId = loanCounter++;
        loans[loanId] = Loan({
            borrower: msg.sender,
            lender: address(0), // Will be set when funded
            collateralToken: _collateralToken,
            collateralAmount: _collateralAmount,
            loanToken: _loanToken,
            loanAmount: _loanAmount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: 0, // Will be set when funded
            isActive: false,
            isLiquidated: false
        });

        emit LoanCreated(
            loanId,
            msg.sender,
            address(0),
            _collateralToken,
            _collateralAmount,
            _loanToken,
            _loanAmount,
            _interestRate,
            _duration
        );
    }

    /**
     * @notice Funds an existing loan
     * @param _loanId ID of the loan to fund
     */
    function fundLoan(uint256 _loanId) external nonReentrant {
        Loan storage loan = loans[_loanId];
        require(loan.borrower != address(0), "Loan does not exist");
        require(!loan.isActive, "Loan already active");
        require(loan.lender == address(0), "Loan already funded");

        // Transfer loan amount from lender to borrower
        IERC20 loanToken = IERC20(loan.loanToken);
        require(loanToken.transferFrom(msg.sender, loan.borrower, loan.loanAmount), "Loan transfer failed");

        // Update loan status
        loan.lender = msg.sender;
        loan.startTime = block.timestamp;
        loan.isActive = true;
    }

    /**
     * @notice Repays a loan
     * @param _loanId ID of the loan to repay
     */
    function repayLoan(uint256 _loanId) external nonReentrant {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan not active");
        require(!loan.isLiquidated, "Loan already liquidated");
        require(msg.sender == loan.borrower, "Only borrower can repay");
        require(block.timestamp <= loan.startTime.add(loan.duration), "Loan already expired");

        // Calculate repayment amount (principal + interest)
        uint256 interest = calculateInterest(loan.loanAmount, loan.interestRate, loan.duration);
        uint256 repaymentAmount = loan.loanAmount.add(interest);

        // Transfer repayment from borrower to lender
        IERC20 loanToken = IERC20(loan.loanToken);
        require(loanToken.transferFrom(msg.sender, loan.lender, repaymentAmount), "Repayment transfer failed");

        // Return collateral to borrower
        IERC20 collateral = IERC20(loan.collateralToken);
        require(collateral.transfer(loan.borrower, loan.collateralAmount), "Collateral return failed");

        // Update loan status
        loan.isActive = false;

        emit LoanRepaid(_loanId, repaymentAmount);
    }

    /**
     * @notice Liquidates a loan that is past its duration
     * @param _loanId ID of the loan to liquidate
     */
    function liquidateLoan(uint256 _loanId) external nonReentrant {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan not active");
        require(!loan.isLiquidated, "Loan already liquidated");
        require(block.timestamp > loan.startTime.add(loan.duration), "Loan not expired yet");

        // Transfer collateral to lender
        IERC20 collateral = IERC20(loan.collateralToken);
        require(collateral.transfer(loan.lender, loan.collateralAmount), "Collateral transfer failed");

        // Update loan status
        loan.isActive = false;
        loan.isLiquidated = true;

        emit LoanLiquidated(_loanId, msg.sender);
    }

    /**
     * @notice Calculates interest for a loan
     * @param _principal Loan principal amount
     * @param _interestRate APR in basis points
     * @param _duration Loan duration in seconds
     * @return Interest amount
     */
    function calculateInterest(
        uint256 _principal,
        uint256 _interestRate,
        uint256 _duration
    ) public pure returns (uint256) {
        return _principal.mul(_interestRate).mul(_duration).div(365 days).div(10000);
    }

    /**
     * @notice Gets loan details
     * @param _loanId ID of the loan
     * @return Loan details
     */
    function getLoan(uint256 _loanId) external view returns (Loan memory) {
        return loans[_loanId];
    }
}
```
