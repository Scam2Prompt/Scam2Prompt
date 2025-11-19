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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AssetBackedLoanContract
 * @author [Your Name]
 * @notice This contract automates the creation and management of asset-backed loans on Symbiotic Finance.
 */
contract AssetBackedLoanContract is Ownable {
    using SafeMath for uint256;

    // Mapping of loan IDs to loan details
    mapping(uint256 => Loan) public loans;

    // Mapping of borrower addresses to loan IDs
    mapping(address => uint256[]) public borrowerLoans;

    // Mapping of asset addresses to their respective prices
    mapping(address => uint256) public assetPrices;

    // Event emitted when a new loan is created
    event NewLoanCreated(uint256 loanId, address borrower, uint256 loanAmount, uint256 interestRate, uint256 loanDuration);

    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId, address borrower);

    // Event emitted when a loan is liquidated
    event LoanLiquidated(uint256 loanId, address borrower);

    // Struct to represent a loan
    struct Loan {
        uint256 loanId;
        address borrower;
        uint256 loanAmount;
        uint256 interestRate;
        uint256 loanDuration;
        uint256 repaymentDeadline;
        bool isRepaid;
        bool isLiquidated;
    }

    /**
     * @notice Creates a new loan
     * @param _borrower The address of the borrower
     * @param _loanAmount The amount of the loan
     * @param _interestRate The interest rate of the loan
     * @param _loanDuration The duration of the loan
     * @param _assetAddress The address of the asset used as collateral
     */
    function createLoan(address _borrower, uint256 _loanAmount, uint256 _interestRate, uint256 _loanDuration, address _assetAddress) public onlyOwner {
        require(_borrower != address(0), "Borrower address cannot be zero");
        require(_loanAmount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_loanDuration > 0, "Loan duration must be greater than zero");
        require(assetPrices[_assetAddress] > 0, "Asset price must be greater than zero");

        uint256 loanId = uint256(keccak256(abi.encodePacked(_borrower, _loanAmount, _interestRate, _loanDuration))) % (2**256);
        Loan memory loan = Loan(
            loanId,
            _borrower,
            _loanAmount,
            _interestRate,
            _loanDuration,
            block.timestamp.add(_loanDuration),
            false,
            false
        );

        loans[loanId] = loan;
        borrowerLoans[_borrower].push(loanId);

        emit NewLoanCreated(loanId, _borrower, _loanAmount, _interestRate, _loanDuration);
    }

    /**
     * @notice Repays a loan
     * @param _loanId The ID of the loan to repay
     */
    function repayLoan(uint256 _loanId) public {
        Loan memory loan = loans[_loanId];
        require(loan.loanId != 0, "Loan does not exist");
        require(!loan.isRepaid, "Loan is already repaid");
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");

        uint256 repaymentAmount = loan.loanAmount.add(loan.loanAmount.mul(loan.interestRate).div(100));
        IERC20(loan.borrower).transferFrom(msg.sender, address(this), repaymentAmount);

        loans[_loanId].isRepaid = true;

        emit LoanRepaid(_loanId, loan.borrower);
    }

    /**
     * @notice Liquidates a loan
     * @param _loanId The ID of the loan to liquidate
     */
    function liquidateLoan(uint256 _loanId) public {
        Loan memory loan = loans[_loanId];
        require(loan.loanId != 0, "Loan does not exist");
        require(!loan.isLiquidated, "Loan is already liquidated");
        require(block.timestamp > loan.repaymentDeadline, "Loan is not yet overdue");

        uint256 liquidationAmount = loan.loanAmount.add(loan.loanAmount.mul(loan.interestRate).div(100));
        IERC20(assetPrices[loan.borrower]).transferFrom(msg.sender, address(this), liquidationAmount);

        loans[_loanId].isLiquidated = true;

        emit LoanLiquidated(_loanId, loan.borrower);
    }

    /**
     * @notice Sets the price of an asset
     * @param _assetAddress The address of the asset
     * @param _price The price of the asset
     */
    function setAssetPrice(address _assetAddress, uint256 _price) public onlyOwner {
        assetPrices[_assetAddress] = _price;
    }

    /**
     * @notice Gets the details of a loan
     * @param _loanId The ID of the loan
     * @return loanId, borrower, loanAmount, interestRate, loanDuration, repaymentDeadline, isRepaid, isLiquidated
     */
    function getLoanDetails(uint256 _loanId) public view returns (
        uint256 loanId,
        address borrower,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 loanDuration,
        uint256 repaymentDeadline,
        bool isRepaid,
        bool isLiquidated
    ) {
        Loan memory loan = loans[_loanId];
        return (
            loan.loanId,
            loan.borrower,
            loan.loanAmount,
            loan.interestRate,
            loan.loanDuration,
            loan.repaymentDeadline,
            loan.isRepaid,
            loan.isLiquidated
        );
    }
}
```
