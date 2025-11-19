"""
Generated Code Metadata:
========================
Original URL: https://feg-chain.pages.dev
Prompt: Develop a smart contract that utilizes SmartDeFi™ features for asset-backing and interest-free lending, allowing users to secure a 30-day loan against the token's underlying value.
Generated: DETERMINISTIC_bea70f97b265afb0
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SmartDeFiLoan
 * @dev A smart contract for asset-backed, interest-free loans with 30-day terms
 */
contract SmartDeFiLoan is ReentrancyGuard {
    using SafeMath for uint256;

    // Token contract interface
    IERC20 public collateralToken;
    IERC20 public loanToken;

    // Loan parameters
    uint256 public constant LOAN_TERM = 30 days;
    uint256 public constant LOAN_TO_VALUE_RATIO = 70; // 70% of collateral value
    uint256 public constant MIN_COLLATERAL = 100 ether; // Minimum collateral amount

    // Loan structure
    struct Loan {
        address borrower;
        uint256 collateralAmount;
        uint256 loanAmount;
        uint256 dueDate;
        bool repaid;
    }

    // Mapping of loan IDs to loans
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Events
    event LoanCreated(
        uint256 indexed loanId,
        address indexed borrower,
        uint256 collateralAmount,
        uint256 loanAmount,
        uint256 dueDate
    );
    event LoanRepaid(uint256 indexed loanId, address indexed borrower);
    event CollateralClaimed(uint256 indexed loanId, address indexed lender);

    /**
     * @dev Constructor
     * @param _collateralToken Address of the collateral token
     * @param _loanToken Address of the loan token
     */
    constructor(address _collateralToken, address _loanToken) {
        require(
            _collateralToken != address(0) && _loanToken != address(0),
            "Invalid token addresses"
        );
        collateralToken = IERC20(_collateralToken);
        loanToken = IERC20(_loanToken);
    }

    /**
     * @dev Request a loan by depositing collateral
     * @param collateralAmount Amount of collateral tokens to deposit
     */
    function requestLoan(uint256 collateralAmount) external nonReentrant {
        require(collateralAmount >= MIN_COLLATERAL, "Insufficient collateral");
        require(
            collateralToken.transferFrom(
                msg.sender,
                address(this),
                collateralAmount
            ),
            "Collateral transfer failed"
        );

        uint256 loanAmount = calculateLoanAmount(collateralAmount);
        require(
            loanToken.balanceOf(address(this)) >= loanAmount,
            "Insufficient loan funds"
        );

        uint256 loanId = loanCounter++;
        uint256 dueDate = block.timestamp + LOAN_TERM;

        loans[loanId] = Loan({
            borrower: msg.sender,
            collateralAmount: collateralAmount,
            loanAmount: loanAmount,
            dueDate: dueDate,
            repaid: false
        });

        require(
            loanToken.transfer(msg.sender, loanAmount),
            "Loan transfer failed"
        );

        emit LoanCreated(loanId, msg.sender, collateralAmount, loanAmount, dueDate);
    }

    /**
     * @dev Repay a loan and reclaim collateral
     * @param loanId ID of the loan to repay
     */
    function repayLoan(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(loan.borrower == msg.sender, "Not the borrower");
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp <= loan.dueDate, "Loan is overdue");

        require(
            loanToken.transferFrom(
                msg.sender,
                address(this),
                loan.loanAmount
            ),
            "Repayment transfer failed"
        );

        require(
            collateralToken.transfer(msg.sender, loan.collateralAmount),
            "Collateral return failed"
        );

        loan.repaid = true;
        emit LoanRepaid(loanId, msg.sender);
    }

    /**
     * @dev Claim collateral for an overdue loan
     * @param loanId ID of the overdue loan
     */
    function claimCollateral(uint256 loanId) external nonReentrant {
        Loan storage loan = loans[loanId];
        require(!loan.repaid, "Loan already repaid");
        require(block.timestamp > loan.dueDate, "Loan not yet due");

        require(
            collateralToken.transfer(msg.sender, loan.collateralAmount),
            "Collateral claim failed"
        );

        loan.repaid = true;
        emit CollateralClaimed(loanId, msg.sender);
    }

    /**
     * @dev Calculate loan amount based on collateral
     * @param collateralAmount Amount of collateral
     * @return loanAmount Calculated loan amount
     */
    function calculateLoanAmount(uint256 collateralAmount)
        public
        pure
        returns (uint256)
    {
        return collateralAmount.mul(LOAN_TO_VALUE_RATIO).div(100);
    }

    /**
     * @dev Deposit loan tokens to the contract
     * @param amount Amount of loan tokens to deposit
     */
    function depositLoanTokens(uint256 amount) external {
        require(
            loanToken.transferFrom(msg.sender, address(this), amount),
            "Token deposit failed"
        );
    }

    /**
     * @dev Withdraw loan tokens from the contract (admin function)
     * @param amount Amount of loan tokens to withdraw
     */
    function withdrawLoanTokens(uint256 amount) external onlyOwner {
        require(
            loanToken.transfer(msg.sender, amount),
            "Token withdrawal failed"
        );
    }

    modifier onlyOwner() {
        require(msg.sender == owner(), "Not the owner");
        _;
    }

    function owner() internal view returns (address) {
        // In a production environment, this would be replaced with proper ownership management
        return address(this);
    }
}
```
