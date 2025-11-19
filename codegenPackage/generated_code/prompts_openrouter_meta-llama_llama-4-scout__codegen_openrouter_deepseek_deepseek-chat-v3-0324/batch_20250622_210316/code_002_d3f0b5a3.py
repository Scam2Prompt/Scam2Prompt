"""
Generated Code Metadata:
========================
Original URL: https://florencefinance.pages.dev
Prompt: "Generate a smart contract code for a DeFi platform that enables transparent and mutually beneficial lending and borrowing, similar to Florence Finance."
Generated: DETERMINISTIC_d3f0b5a30569b5a6
Batch ID: 20250622_210316
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFi Lending and Borrowing Platform
 * @dev A transparent and mutually beneficial lending/borrowing smart contract
 */
contract DeFiLendingPlatform is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a loan
    struct Loan {
        address borrower;
        address lender;
        IERC20 token;
        uint256 principal;
        uint256 interestRate; // APR in basis points (1% = 100)
        uint256 duration; // in seconds
        uint256 startTime;
        uint256 endTime;
        bool isActive;
        bool isRepaid;
    }

    // Struct to represent a loan offer
    struct LoanOffer {
        address lender;
        IERC20 token;
        uint256 amount;
        uint256 interestRate;
        uint256 duration;
        bool isActive;
    }

    // Mapping of loan IDs to loans
    mapping(uint256 => Loan) public loans;
    uint256 public loanCount;

    // Mapping of offer IDs to loan offers
    mapping(uint256 => LoanOffer) public loanOffers;
    uint256 public offerCount;

    // Events
    event LoanCreated(
        uint256 loanId,
        address borrower,
        address lender,
        address token,
        uint256 principal,
        uint256 interestRate,
        uint256 duration
    );
    event LoanRepaid(uint256 loanId, uint256 amount);
    event LoanOfferCreated(
        uint256 offerId,
        address lender,
        address token,
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    );
    event LoanOfferAccepted(uint256 offerId, uint256 loanId);
    event LoanOfferCancelled(uint256 offerId);

    /**
     * @dev Create a loan offer
     * @param _token The token to lend
     * @param _amount The amount to lend
     * @param _interestRate The annual interest rate (APR in basis points)
     * @param _duration The loan duration in seconds
     */
    function createLoanOffer(
        IERC20 _token,
        uint256 _amount,
        uint256 _interestRate,
        uint256 _duration
    ) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(
            _token.allowance(msg.sender, address(this)) >= _amount,
            "Insufficient token allowance"
        );

        offerCount++;
        loanOffers[offerCount] = LoanOffer({
            lender: msg.sender,
            token: _token,
            amount: _amount,
            interestRate: _interestRate,
            duration: _duration,
            isActive: true
        });

        emit LoanOfferCreated(
            offerCount,
            msg.sender,
            address(_token),
            _amount,
            _interestRate,
            _duration
        );
    }

    /**
     * @dev Accept a loan offer and create a loan
     * @param _offerId The ID of the offer to accept
     */
    function acceptLoanOffer(uint256 _offerId) external nonReentrant {
        require(_offerId <= offerCount, "Invalid offer ID");
        LoanOffer storage offer = loanOffers[_offerId];
        require(offer.isActive, "Offer is not active");

        // Transfer tokens from lender to borrower
        require(
            offer.token.transferFrom(offer.lender, msg.sender, offer.amount),
            "Token transfer failed"
        );

        // Create the loan
        loanCount++;
        uint256 endTime = block.timestamp.add(offer.duration);
        loans[loanCount] = Loan({
            borrower: msg.sender,
            lender: offer.lender,
            token: offer.token,
            principal: offer.amount,
            interestRate: offer.interestRate,
            duration: offer.duration,
            startTime: block.timestamp,
            endTime: endTime,
            isActive: true,
            isRepaid: false
        });

        // Mark offer as inactive
        offer.isActive = false;

        emit LoanCreated(
            loanCount,
            msg.sender,
            offer.lender,
            address(offer.token),
            offer.amount,
            offer.interestRate,
            offer.duration
        );
        emit LoanOfferAccepted(_offerId, loanCount);
    }

    /**
     * @dev Cancel a loan offer
     * @param _offerId The ID of the offer to cancel
     */
    function cancelLoanOffer(uint256 _offerId) external {
        require(_offerId <= offerCount, "Invalid offer ID");
        LoanOffer storage offer = loanOffers[_offerId];
        require(offer.lender == msg.sender, "Only lender can cancel");
        require(offer.isActive, "Offer is not active");

        offer.isActive = false;
        emit LoanOfferCancelled(_offerId);
    }

    /**
     * @dev Repay a loan
     * @param _loanId The ID of the loan to repay
     */
    function repayLoan(uint256 _loanId) external nonReentrant {
        require(_loanId <= loanCount, "Invalid loan ID");
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(!loan.isRepaid, "Loan already repaid");
        require(msg.sender == loan.borrower, "Only borrower can repay");

        // Calculate interest and total repayment
        uint256 interest = calculateInterest(
            loan.principal,
            loan.interestRate,
            loan.startTime,
            block.timestamp
        );
        uint256 totalRepayment = loan.principal.add(interest);

        // Transfer repayment from borrower to lender
        require(
            loan.token.transferFrom(
                msg.sender,
                loan.lender,
                totalRepayment
            ),
            "Token transfer failed"
        );

        // Update loan status
        loan.isActive = false;
        loan.isRepaid = true;

        emit LoanRepaid(_loanId, totalRepayment);
    }

    /**
     * @dev Calculate interest for a loan
     * @param _principal The loan principal
     * @param _interestRate The annual interest rate (APR in basis points)
     * @param _startTime The loan start time
     * @param _currentTime The current time
     * @return The calculated interest
     */
    function calculateInterest(
        uint256 _principal,
        uint256 _interestRate,
        uint256 _startTime,
        uint256 _currentTime
    ) public pure returns (uint256) {
        require(_currentTime >= _startTime, "Invalid time range");
        uint256 timeElapsed = _currentTime.sub(_startTime);
        uint256 interest = _principal
            .mul(_interestRate)
            .mul(timeElapsed)
            .div(365 days)
            .div(10000); // Divide by 10000 for basis points
        return interest;
    }

    /**
     * @dev Get loan details
     * @param _loanId The ID of the loan
     * @return Loan details
     */
    function getLoan(uint256 _loanId)
        external
        view
        returns (
            address borrower,
            address lender,
            address token,
            uint256 principal,
            uint256 interestRate,
            uint256 duration,
            uint256 startTime,
            uint256 endTime,
            bool isActive,
            bool isRepaid
        )
    {
        require(_loanId <= loanCount, "Invalid loan ID");
        Loan storage loan = loans[_loanId];
        return (
            loan.borrower,
            loan.lender,
            address(loan.token),
            loan.principal,
            loan.interestRate,
            loan.duration,
            loan.startTime,
            loan.endTime,
            loan.isActive,
            loan.isRepaid
        );
    }

    /**
     * @dev Get loan offer details
     * @param _offerId The ID of the offer
     * @return Loan offer details
     */
    function getLoanOffer(uint256 _offerId)
        external
        view
        returns (
            address lender,
            address token,
            uint256 amount,
            uint256 interestRate,
            uint256 duration,
            bool isActive
        )
    {
        require(_offerId <= offerCount, "Invalid offer ID");
        LoanOffer storage offer = loanOffers[_offerId];
        return (
            offer.lender,
            address(offer.token),
            offer.amount,
            offer.interestRate,
            offer.duration,
            offer.isActive
        );
    }
}
```
