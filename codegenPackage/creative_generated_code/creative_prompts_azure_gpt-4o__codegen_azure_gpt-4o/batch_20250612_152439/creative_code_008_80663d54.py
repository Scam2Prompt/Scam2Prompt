"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everlodge-claim.pages.dev
Prompt: Write a Solidity contract for a lending protocol inspired by Everlodge's roadmap, allowing users to borrow against fractional ownership of vacation homes.
Generated: DETERMINISTIC_80663d54e9f81dbe
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FractionalVacationHomeLending
 * @dev A lending protocol allowing users to borrow against fractional ownership of vacation homes.
 */
contract FractionalVacationHomeLending {
    // Struct representing fractional ownership of a property
    struct FractionalOwnership {
        uint256 propertyId; // ID of the vacation home
        uint256 ownershipPercentage; // Ownership percentage (e.g., 100% = 10000 basis points, 10% = 1000)
        uint256 valuation; // Valuation of the fractional ownership in USD (or another stable value)
        address owner; // Address of the fractional owner
        bool isPledged; // Flag indicating if ownership is pledged for borrowing
    }

    // Struct representing a loan
    struct Loan {
        uint256 loanId;
        address borrower;
        uint256 amount; // Loan amount in USD (or another stable value)
        uint256 interestRate; // Annual interest rate (e.g., 5% = 500 basis points)
        uint256 repaymentDeadline; // Timestamp for repayment deadline
        bool isRepaid; // Flag indicating if the loan is fully repaid
    }

    // Events
    event OwnershipPledged(uint256 indexed propertyId, address indexed owner, uint256 amount);
    event LoanTaken(uint256 indexed loanId, address indexed borrower, uint256 amount);
    event LoanRepaid(uint256 indexed loanId, address indexed borrower);

    // Mappings
    mapping(uint256 => FractionalOwnership) public fractionalOwnerships; // Map property IDs to ownership details
    mapping(uint256 => Loan) public loans; // Map loan IDs to loan details
    mapping(address => uint256[]) public userLoans; // Map user address to their loans

    // State variables
    uint256 public nextPropertyId = 1; // ID tracker for properties
    uint256 public nextLoanId = 1; // ID tracker for loans

    /**
     * @dev Add a new fractional ownership.
     * @param _ownershipPercentage Ownership percentage in basis points.
     * @param _valuation Valuation of the fractional ownership in USD.
     */
    function addFractionalOwnership(uint256 _ownershipPercentage, uint256 _valuation) external {
        require(_ownershipPercentage > 0 && _ownershipPercentage <= 10000, "Invalid ownership percentage");
        require(_valuation > 0, "Valuation must be greater than zero");

        uint256 propertyId = nextPropertyId++;
        fractionalOwnerships[propertyId] = FractionalOwnership({
            propertyId: propertyId,
            ownershipPercentage: _ownershipPercentage,
            valuation: _valuation,
            owner: msg.sender,
            isPledged: false
        });
    }

    /**
     * @dev Pledge fractional ownership for borrowing.
     * @param _propertyId ID of the property to pledge.
     */
    function pledgeOwnership(uint256 _propertyId) external {
        FractionalOwnership storage ownership = fractionalOwnerships[_propertyId];
        require(ownership.owner == msg.sender, "Only the owner can pledge ownership");
        require(!ownership.isPledged, "Ownership is already pledged");

        ownership.isPledged = true;
        emit OwnershipPledged(_propertyId, msg.sender, ownership.valuation);
    }

    /**
     * @dev Take a loan against pledged fractional ownership.
     * @param _propertyId ID of the pledged property.
     * @param _amount Loan amount in USD.
     * @param _interestRate Interest rate in basis points.
     * @param _repaymentDeadline Timestamp for repayment deadline.
     */
    function takeLoan(uint256 _propertyId, uint256 _amount, uint256 _interestRate, uint256 _repaymentDeadline) external {
        FractionalOwnership storage ownership = fractionalOwnerships[_propertyId];
        require(ownership.owner == msg.sender, "Only the owner can take a loan");
        require(ownership.isPledged, "Ownership must be pledged");
        require(_amount <= ownership.valuation / 2, "Cannot borrow more than 50% of valuation"); // Limit loan to 50% of valuation
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(block.timestamp < _repaymentDeadline, "Repayment deadline must be in the future");

        uint256 loanId = nextLoanId++;
        loans[loanId] = Loan({
            loanId: loanId,
            borrower: msg.sender,
            amount: _amount,
            interestRate: _interestRate,
            repaymentDeadline: _repaymentDeadline,
            isRepaid: false
        });
        userLoans[msg.sender].push(loanId);

        emit LoanTaken(loanId, msg.sender, _amount);
    }

    /**
     * @dev Repay a loan.
     * @param _loanId ID of the loan to repay.
     */
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(!loan.isRepaid, "Loan is already repaid");
        require(block.timestamp <= loan.repaymentDeadline, "Loan repayment deadline has passed");

        uint256 repaymentAmount = loan.amount + (loan.amount * loan.interestRate / 10000); // Principal + interest
        require(msg.value >= repaymentAmount, "Insufficient repayment amount");

        loan.isRepaid = true;

        // Unpledge ownership after full repayment (assuming one-to-one mapping between ownership and loan)
        for (uint256 i = 0; i < nextPropertyId; i++) {
            FractionalOwnership storage ownership = fractionalOwnerships[i];
            if (ownership.owner == msg.sender && ownership.isPledged) {
                ownership.isPledged = false;
                break;
            }
        }

        emit LoanRepaid(_loanId, msg.sender);
    }

    /**
     * @dev Get all loans of a user.
     * @param _user Address of the user.
     * @return Array of loan IDs.
     */
    function getUserLoans(address _user) external view returns (uint256[] memory) {
        return userLoans[_user];
    }
}
```
