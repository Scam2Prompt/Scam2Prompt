"""
Generated Code Metadata:
========================
Original URL: https://pancakeswap.vn
Prompt: Write a smart contract in Solidity for a lending and borrowing system, inspired by the EasyCake DeFi platform's functionality.
Generated: DETERMINISTIC_01c4a6791e0dc77a
Batch ID: 20250612_145730
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

contract EasyLend is ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract
    IERC20 public token;

    // Interest rate (1 = 0.01%)
    uint256 public interestRate;

    // Platform fee (1 = 0.01%)
    uint256 public platformFee;

    // Platform fee collector
    address public feeCollector;

    // Loan struct
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 collateral;
        uint256 startTime;
        uint256 duration;
        bool repaid;
    }

    // Mapping of loan IDs to loans
    mapping(uint256 => Loan) public loans;

    // Loan counter
    uint256 public loanCounter;

    // Collateral ratio (1 = 0.01%)
    uint256 public collateralRatio;

    // Events
    event LoanCreated(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 amount,
        uint256 collateral,
        uint256 duration
    );
    event LoanRepaid(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 amount,
        uint256 interest
    );
    event LoanLiquidated(
        uint256 indexed loanId,
        address indexed liquidator,
        uint256 collateralSeized
    );
    event ParametersUpdated(
        uint256 interestRate,
        uint256 platformFee,
        uint256 collateralRatio
    );

    constructor(
        address _token,
        address _feeCollector,
        uint256 _interestRate,
        uint256 _platformFee,
        uint256 _collateralRatio
    ) {
        require(_token != address(0), "Invalid token address");
        require(_feeCollector != address(0), "Invalid fee collector address");
        require(_interestRate > 0, "Interest rate must be positive");
        require(_platformFee >= 0, "Platform fee cannot be negative");
        require(_collateralRatio > 0, "Collateral ratio must be positive");

        token = IERC20(_token);
        feeCollector = _feeCollector;
        interestRate = _interestRate;
        platformFee = _platformFee;
        collateralRatio = _collateralRatio;
    }

    /**
     * @dev Create a new loan
     * @param amount Amount to borrow
     * @param collateral Amount of collateral
     * @param duration Loan duration in seconds
     */
    function borrow(
        uint256 amount,
        uint256 collateral,
        uint256 duration
    ) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(duration > 0, "Duration must be positive");
        require(
            collateral >= amount.mul(collateralRatio).div(10000),
            "Insufficient collateral"
        );

        // Transfer collateral from borrower to contract
        require(
            token.transferFrom(msg.sender, address(this), collateral),
            "Collateral transfer failed"
        );

        // Create new loan
        uint256 loanId = loanCounter++;
        loans[loanId] = Loan({
            borrower: msg.sender,
            amount: amount,
            collateral: collateral,
            startTime: block.timestamp,
            duration: duration,
            repaid: false
        });

        // Transfer borrowed amount to borrower
        require(
            token.transfer(msg.sender, amount),
            "Loan transfer failed"
        );

        emit LoanCreated(loanId, msg.sender, amount, collateral, duration);
    }

    /**
     * @dev Repay a loan
     * @param loanId ID of the loan to repay
     */
    function repay(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(loan.borrower == msg.sender, "Not the borrower");
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp <= loan.startTime + loan.duration, "Loan expired");

        uint256 interest = calculateInterest(loan.amount, loan.startTime);
        uint256 totalRepayment = loan.amount.add(interest);
        uint256 fee = totalRepayment.mul(platformFee).div(10000);
        uint256 repaymentAfterFee = totalRepayment.sub(fee);

        // Transfer repayment + interest from borrower
        require(
            token.transferFrom(msg.sender, address(this), totalRepayment),
            "Repayment transfer failed"
        );

        // Transfer fee to fee collector
        if (fee > 0) {
            require(
                token.transfer(feeCollector, fee),
                "Fee transfer failed"
            );
        }

        // Return collateral to borrower
        require(
            token.transfer(loan.borrower, loan.collateral),
            "Collateral return failed"
        );

        loan.repaid = true;

        emit LoanRepaid(loanId, msg.sender, loan.amount, interest);
    }

    /**
     * @dev Liquidate an expired loan
     * @param loanId ID of the loan to liquidate
     */
    function liquidate(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp > loan.startTime + loan.duration, "Loan not expired");

        // Transfer collateral to liquidator
        require(
            token.transfer(msg.sender, loan.collateral),
            "Collateral transfer failed"
        );

        loan.repaid = true;

        emit LoanLiquidated(loanId, msg.sender, loan.collateral);
    }

    /**
     * @dev Calculate interest for a loan
     * @param amount Loan amount
     * @param startTime Loan start time
     * @return interest Calculated interest
     */
    function calculateInterest(uint256 amount, uint256 startTime) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp.sub(startTime);
        return amount.mul(interestRate).mul(timeElapsed).div(365 days).div(10000);
    }

    /**
     * @dev Update contract parameters (only owner)
     * @param _interestRate New interest rate
     * @param _platformFee New platform fee
     * @param _collateralRatio New collateral ratio
     */
    function updateParameters(
        uint256 _interestRate,
        uint256 _platformFee,
        uint256 _collateralRatio
    ) external {
        require(msg.sender == feeCollector, "Only fee collector can update");
        require(_interestRate > 0, "Interest rate must be positive");
        require(_platformFee >= 0, "Platform fee cannot be negative");
        require(_collateralRatio > 0, "Collateral ratio must be positive");

        interestRate = _interestRate;
        platformFee = _platformFee;
        collateralRatio = _collateralRatio;

        emit ParametersUpdated(_interestRate, _platformFee, _collateralRatio);
    }

    /**
     * @dev Change fee collector address (only owner)
     * @param _feeCollector New fee collector address
     */
    function changeFeeCollector(address _feeCollector) external {
        require(msg.sender == feeCollector, "Only fee collector can change");
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }
}
```
