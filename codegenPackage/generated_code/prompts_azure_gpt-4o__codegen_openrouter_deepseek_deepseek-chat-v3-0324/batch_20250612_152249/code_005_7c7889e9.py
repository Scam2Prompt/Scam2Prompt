"""
Generated Code Metadata:
========================
Original URL: https://getretik.pages.dev
Prompt: Develop a smart contract for AI-powered P2P lending that evaluates borrowers' profiles and offers lending solutions, as described in Retik Finance's ecosystem.
Generated: DETERMINISTIC_7c7889e981bdebfe
Batch ID: 20250612_152249
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract AIP2PLending is Ownable, ReentrancyGuard {
    // Structs
    struct LoanRequest {
        address borrower;
        uint256 amount;
        uint256 interestRate;
        uint256 duration;
        uint256 riskScore;
        uint256 collateralAmount;
        address collateralToken;
        uint256 requestTime;
        bool isActive;
    }

    struct Loan {
        address lender;
        address borrower;
        uint256 amount;
        uint256 interestRate;
        uint256 startTime;
        uint256 dueTime;
        uint256 collateralAmount;
        address collateralToken;
        bool isRepaid;
        bool isLiquidated;
    }

    // State variables
    IERC20 public lendingToken;
    uint256 public totalLoans;
    uint256 public totalActiveLoans;
    uint256 public protocolFeePercentage; // 100 = 1%
    address public feeCollector;
    address public aiOracle;

    // Mappings
    mapping(uint256 => LoanRequest) public loanRequests;
    mapping(uint256 => Loan) public loans;
    mapping(address => uint256[]) public borrowerLoans;
    mapping(address => uint256[]) public lenderLoans;
    mapping(address => uint256) public creditScores;

    // Events
    event LoanRequestCreated(
        uint256 requestId,
        address borrower,
        uint256 amount,
        uint256 interestRate,
        uint256 duration,
        uint256 riskScore
    );
    event LoanFunded(
        uint256 loanId,
        address lender,
        address borrower,
        uint256 amount,
        uint256 interestRate,
        uint256 dueTime
    );
    event LoanRepaid(uint256 loanId, uint256 amountRepaid);
    event LoanLiquidated(uint256 loanId, uint256 liquidatedAmount);
    event CreditScoreUpdated(address borrower, uint256 newScore);

    // Modifiers
    modifier onlyAIOracle() {
        require(msg.sender == aiOracle, "Caller is not the AI Oracle");
        _;
    }

    constructor(
        address _lendingToken,
        address _feeCollector,
        uint256 _protocolFeePercentage
    ) {
        require(_lendingToken != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        
        lendingToken = IERC20(_lendingToken);
        feeCollector = _feeCollector;
        protocolFeePercentage = _protocolFeePercentage;
    }

    /**
     * @dev Create a new loan request with AI-evaluated parameters
     * @param amount The loan amount
     * @param interestRate The proposed interest rate
     * @param duration The loan duration in seconds
     * @param riskScore The AI-generated risk score (0-100)
     * @param collateralAmount The collateral amount
     * @param collateralToken The collateral token address
     */
    function createLoanRequest(
        uint256 amount,
        uint256 interestRate,
        uint256 duration,
        uint256 riskScore,
        uint256 collateralAmount,
        address collateralToken
    ) external nonReentrant {
        require(amount > 0, "Loan amount must be positive");
        require(interestRate > 0, "Interest rate must be positive");
        require(duration > 0, "Duration must be positive");
        require(riskScore <= 100, "Risk score must be <= 100");
        require(collateralToken != address(0), "Invalid collateral token");

        if (collateralAmount > 0) {
            IERC20 collateral = IERC20(collateralToken);
            require(
                collateral.balanceOf(msg.sender) >= collateralAmount,
                "Insufficient collateral balance"
            );
            require(
                collateral.allowance(msg.sender, address(this)) >= collateralAmount,
                "Insufficient collateral allowance"
            );
        }

        uint256 requestId = totalLoans + 1;
        loanRequests[requestId] = LoanRequest({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            riskScore: riskScore,
            collateralAmount: collateralAmount,
            collateralToken: collateralToken,
            requestTime: block.timestamp,
            isActive: true
        });

        emit LoanRequestCreated(
            requestId,
            msg.sender,
            amount,
            interestRate,
            duration,
            riskScore
        );
    }

    /**
     * @dev Fund an active loan request
     * @param requestId The ID of the loan request to fund
     */
    function fundLoan(uint256 requestId) external nonReentrant {
        LoanRequest storage request = loanRequests[requestId];
        require(request.isActive, "Loan request is not active");
        require(
            lendingToken.balanceOf(msg.sender) >= request.amount,
            "Insufficient balance"
        );
        require(
            lendingToken.allowance(msg.sender, address(this)) >= request.amount,
            "Insufficient allowance"
        );

        // Transfer collateral from borrower to contract
        if (request.collateralAmount > 0) {
            IERC20(request.collateralToken).transferFrom(
                request.borrower,
                address(this),
                request.collateralAmount
            );
        }

        // Transfer loan amount from lender to borrower
        lendingToken.transferFrom(msg.sender, request.borrower, request.amount);

        // Calculate protocol fee
        uint256 protocolFee = (request.amount * protocolFeePercentage) / 10000;
        if (protocolFee > 0) {
            lendingToken.transferFrom(msg.sender, feeCollector, protocolFee);
        }

        // Create loan
        uint256 loanId = totalLoans + 1;
        loans[loanId] = Loan({
            lender: msg.sender,
            borrower: request.borrower,
            amount: request.amount,
            interestRate: request.interestRate,
            startTime: block.timestamp,
            dueTime: block.timestamp + request.duration,
            collateralAmount: request.collateralAmount,
            collateralToken: request.collateralToken,
            isRepaid: false,
            isLiquidated: false
        });

        // Update mappings
        borrowerLoans[request.borrower].push(loanId);
        lenderLoans[msg.sender].push(loanId);
        totalLoans++;
        totalActiveLoans++;

        // Mark request as inactive
        request.isActive = false;

        emit LoanFunded(
            loanId,
            msg.sender,
            request.borrower,
            request.amount,
            request.interestRate,
            block.timestamp + request.duration
        );
    }

    /**
     * @dev Repay a loan
     * @param loanId The ID of the loan to repay
     */
    function repayLoan(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(msg.sender == loan.borrower, "Only borrower can repay");
        require(!loan.isRepaid, "Loan already repaid");
        require(!loan.isLiquidated, "Loan is liquidated");

        uint256 interest = calculateInterest(loan.amount, loan.interestRate, loan.startTime);
        uint256 totalRepayment = loan.amount + interest;

        require(
            lendingToken.balanceOf(msg.sender) >= totalRepayment,
            "Insufficient balance for repayment"
        );
        require(
            lendingToken.allowance(msg.sender, address(this)) >= totalRepayment,
            "Insufficient allowance for repayment"
        );

        // Transfer repayment to lender
        lendingToken.transferFrom(msg.sender, loan.lender, totalRepayment);

        // Return collateral to borrower
        if (loan.collateralAmount > 0) {
            IERC20(loan.collateralToken).transfer(
                msg.sender,
                loan.collateralAmount
            );
        }

        // Update loan status
        loan.isRepaid = true;
        totalActiveLoans--;

        emit LoanRepaid(loanId, totalRepayment);
    }

    /**
     * @dev Liquidate a defaulted loan
     * @param loanId The ID of the loan to liquidate
     */
    function liquidateLoan(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(!loan.isRepaid, "Loan is already repaid");
        require(!loan.isLiquidated, "Loan is already liquidated");
        require(block.timestamp > loan.dueTime, "Loan is not yet due");

        // Transfer collateral to lender
        if (loan.collateralAmount > 0) {
            IERC20(loan.collateralToken).transfer(
                loan.lender,
                loan.collateralAmount
            );
        }

        // Update loan status
        loan.isLiquidated = true;
        totalActiveLoans
