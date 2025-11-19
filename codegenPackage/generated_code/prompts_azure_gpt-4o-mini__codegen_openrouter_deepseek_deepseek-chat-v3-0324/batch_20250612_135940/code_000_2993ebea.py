"""
Generated Code Metadata:
========================
Original URL: https://defiethereum.com
Prompt: Write a smart contract in Solidity for a decentralized lending platform on Ethereum.
Generated: DETERMINISTIC_2993ebeae66cd860
Batch ID: 20250612_135940
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

contract DecentralizedLendingPlatform is ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a loan
    struct Loan {
        address borrower;
        address lender;
        address tokenAddress;
        uint256 principal;
        uint256 interestRate; // Annual percentage rate (APR)
        uint256 duration; // In seconds
        uint256 startTime;
        bool isActive;
        bool isRepaid;
    }

    // Mapping from loan ID to Loan
    mapping(uint256 => Loan) public loans;

    // Mapping from token address to whether it's supported
    mapping(address => bool) public supportedTokens;

    // Loan counter
    uint256 public loanCounter;

    // Events
    event LoanCreated(
        uint256 loanId,
        address indexed borrower,
        address indexed lender,
        address tokenAddress,
        uint256 principal,
        uint256 interestRate,
        uint256 duration
    );
    event LoanFunded(uint256 loanId, address indexed lender);
    event LoanRepaid(uint256 loanId, uint256 amount);
    event LoanLiquidated(uint256 loanId);

    // Modifier to check if loan exists
    modifier loanExists(uint256 loanId) {
        require(loans[loanId].borrower != address(0), "Loan does not exist");
        _;
    }

    // Modifier to check if loan is active
    modifier loanActive(uint256 loanId) {
        require(loans[loanId].isActive, "Loan is not active");
        _;
    }

    // Modifier to check if token is supported
    modifier tokenSupported(address tokenAddress) {
        require(supportedTokens[tokenAddress], "Token not supported");
        _;
    }

    // Constructor to initialize supported tokens
    constructor(address[] memory _supportedTokens) {
        for (uint256 i = 0; i < _supportedTokens.length; i++) {
            supportedTokens[_supportedTokens[i]] = true;
        }
    }

    // Function to create a loan request
    function createLoan(
        address tokenAddress,
        uint256 principal,
        uint256 interestRate,
        uint256 duration
    ) external tokenSupported(tokenAddress) {
        require(principal > 0, "Principal must be greater than 0");
        require(interestRate > 0, "Interest rate must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        uint256 loanId = loanCounter++;
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

        emit LoanCreated(
            loanId,
            msg.sender,
            address(0),
            tokenAddress,
            principal,
            interestRate,
            duration
        );
    }

    // Function to fund a loan
    function fundLoan(uint256 loanId) external nonReentrant loanExists(loanId) {
        Loan storage loan = loans[loanId];
        require(!loan.isActive, "Loan is already active");
        require(loan.lender == address(0), "Loan already has a lender");
        require(msg.sender != loan.borrower, "Borrower cannot fund their own loan");

        IERC20 token = IERC20(loan.tokenAddress);
        uint256 amount = loan.principal;

        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        loan.lender = msg.sender;
        loan.isActive = true;
        loan.startTime = block.timestamp;

        emit LoanFunded(loanId, msg.sender);
    }

    // Function to repay a loan
    function repayLoan(uint256 loanId) external nonReentrant loanExists(loanId) loanActive(loanId) {
        Loan storage loan = loans[loanId];
        require(msg.sender == loan.borrower, "Only borrower can repay");
        require(!loan.isRepaid, "Loan already repaid");

        IERC20 token = IERC20(loan.tokenAddress);
        uint256 interest = calculateInterest(loanId);
        uint256 totalAmount = loan.principal.add(interest);

        require(
            token.transferFrom(msg.sender, address(this), totalAmount),
            "Token transfer failed"
        );

        // Transfer principal back to lender and interest to lender
        require(
            token.transfer(loan.lender, loan.principal.add(interest)),
            "Token transfer to lender failed"
        );

        loan.isActive = false;
        loan.isRepaid = true;

        emit LoanRepaid(loanId, totalAmount);
    }

    // Function to liquidate a loan if not repaid in time
    function liquidateLoan(uint256 loanId) external nonReentrant loanExists(loanId) loanActive(loanId) {
        Loan storage loan = loans[loanId];
        require(block.timestamp > loan.startTime.add(loan.duration), "Loan is not overdue");

        IERC20 token = IERC20(loan.tokenAddress);
        uint256 interest = calculateInterest(loanId);
        uint256 totalAmount = loan.principal.add(interest);

        // Transfer collateral to lender
        require(
            token.transfer(loan.lender, totalAmount),
            "Token transfer to lender failed"
        );

        loan.isActive = false;

        emit LoanLiquidated(loanId);
    }

    // Function to calculate interest for a loan
    function calculateInterest(uint256 loanId) public view loanExists(loanId) returns (uint256) {
        Loan storage loan = loans[loanId];
        if (!loan.isActive || loan.startTime == 0) return 0;

        uint256 timeElapsed = block.timestamp.sub(loan.startTime);
        uint256 interest = loan.principal
            .mul(loan.interestRate)
            .mul(timeElapsed)
            .div(365 days)
            .div(100);

        return interest;
    }

    // Function to add supported token (onlyOwner should be added in production)
    function addSupportedToken(address tokenAddress) external {
        supportedTokens[tokenAddress] = true;
    }

    // Function to remove supported token (onlyOwner should be added in production)
    function removeSupportedToken(address tokenAddress) external {
        supportedTokens[tokenAddress] = false;
    }
}
```
