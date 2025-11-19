"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftcap.pages.dev
Prompt: Provide an example of a smart contract implementation for NFT collateral loans on NFTFI.
Generated: DETERMINISTIC_1bc6bba75736bda5
Batch ID: 20250612_163742
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

// Importing required libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTCollateralLoan is a smart contract for handling NFT collateral loans
contract NFTCollateralLoan is ERC721Holder, Ownable {
    
    // Struct to store loan details
    struct Loan {
        address borrower;
        address nftContract;
        uint256 tokenId;
        uint256 loanAmount;
        uint256 interestRate; // In basis points (1% = 100)
        uint256 dueDate;
        bool isActive;
    }

    // Mapping of loan ID to Loan struct
    mapping(uint256 => Loan) public loans;
    uint256 public loanCounter;

    // Event emitted when a loan is created
    event LoanCreated(uint256 indexed loanId, address indexed borrower, address indexed nftContract, uint256 tokenId, uint256 loanAmount, uint256 interestRate, uint256 dueDate);

    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 indexed loanId);

    // Event emitted when a loan is defaulted
    event LoanDefaulted(uint256 indexed loanId);

    // Function to create a loan using NFT as collateral
    function createLoan(
        address _nftContract,
        uint256 _tokenId,
        uint256 _loanAmount,
        uint256 _interestRate,
        uint256 _duration
    ) external {
        require(_loanAmount > 0, "Loan amount must be greater than 0");
        require(_interestRate > 0, "Interest rate must be greater than 0");
        require(_duration > 0, "Loan duration must be greater than 0");

        // Transfer the NFT to the contract
        IERC721(_nftContract).safeTransferFrom(msg.sender, address(this), _tokenId);

        // Increment loan counter and create the loan
        loanCounter++;
        loans[loanCounter] = Loan({
            borrower: msg.sender,
            nftContract: _nftContract,
            tokenId: _tokenId,
            loanAmount: _loanAmount,
            interestRate: _interestRate,
            dueDate: block.timestamp + _duration,
            isActive: true
        });

        // Emit loan creation event
        emit LoanCreated(loanCounter, msg.sender, _nftContract, _tokenId, _loanAmount, _interestRate, block.timestamp + _duration);
    }

    // Function to repay the loan
    function repayLoan(uint256 _loanId) external payable {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan");
        require(msg.value >= loan.loanAmount, "Repayment amount must be equal to or greater than loan amount");

        // Calculate interest
        uint256 interest = (loan.loanAmount * loan.interestRate) / 10000;
        require(msg.value >= (loan.loanAmount + interest), "Insufficient repayment amount to cover interest");

        // Mark the loan as inactive
        loan.isActive = false;

        // Transfer the NFT back to the borrower
        IERC721(loan.nftContract).safeTransferFrom(address(this), loan.borrower, loan.tokenId);

        // Emit loan repayment event
        emit LoanRepaid(_loanId);
    }

    // Function to check for loan defaults and reclaim NFTs if necessary
    function checkLoanDefault(uint256 _loanId) external {
        Loan storage loan = loans[_loanId];

        require(loan.isActive, "Loan is not active");
        require(block.timestamp > loan.dueDate, "Loan is not yet due");

        // Default the loan and transfer NFT to the contract owner
        loan.isActive = false;
        IERC721(loan.nftContract).safeTransferFrom(address(this), owner(), loan.tokenId);

        // Emit loan default event
        emit LoanDefaulted(_loanId);
    }

    // Function to withdraw any ETH from the contract (for contract owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
