"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftcap.pages.dev
Prompt: Write a Solidity function for bundling multiple NFTs as collateral for a single loan, inspired by the "Get a loan on multiple NFTs" feature on NFTfi.com.
Generated: DETERMINISTIC_7cdf43d0bd34faa4
Batch ID: 20250612_151329
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

// Import interface for ERC721 standard
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";

// Define a contract for handling loans against multiple NFTs
contract MultiNFTLoan {
    // Structure to hold loan details
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 dueDate;
        bool isActive;
    }

    // Mapping from NFT contract address and token ID to loan details
    mapping(address => mapping(uint256 => Loan)) public loans;

    // Event emitted when a loan is created
    event LoanCreated(address indexed borrower, address indexed nftContract, uint256 indexed tokenId, uint256 amount, uint256 dueDate);

    // Function to bundle multiple NFTs as collateral for a loan
    function createLoan(address[] memory nftContracts, uint256[] memory tokenIds, uint256 loanAmount, uint256 loanDuration) public {
        require(nftContracts.length == tokenIds.length, "Mismatched input lengths");
        require(loanAmount > 0, "Loan amount must be greater than 0");
        require(loanDuration > 0, "Loan duration must be greater than 0");

        // Ensure the borrower owns all NFTs
        for (uint256 i = 0; i < nftContracts.length; i++) {
            IERC721 nftContract = IERC721(nftContracts[i]);
            require(nftContract.ownerOf(tokenIds[i]) == msg.sender, "You must own the NFT");
            
            // Transfer the NFT to the contract to secure it as collateral
            nftContract.transferFrom(msg.sender, address(this), tokenIds[i]);
        }

        // Calculate due date based on loan duration
        uint256 dueDate = block.timestamp + loanDuration;

        // Create the loan entry for the first NFT (as an example, could modify for multiple loans)
        loans[nftContracts[0]][tokenIds[0]] = Loan(msg.sender, loanAmount, dueDate, true);

        // Emit loan creation event
        emit LoanCreated(msg.sender, nftContracts[0], tokenIds[0], loanAmount, dueDate);
    }

    // Function to repay the loan
    function repayLoan(address nftContract, uint256 tokenId) public payable {
        Loan storage loan = loans[nftContract][tokenId];
        
        // Check if the loan is active
        require(loan.isActive, "No active loan for this NFT");
        require(msg.value >= loan.amount, "Insufficient repayment amount");

        // Ensure loan is not overdue
        require(block.timestamp <= loan.dueDate, "Loan is overdue");

        // Transfer funds to the contract owner (lender)
        payable(address(this)).transfer(msg.value);

        // Mark loan as repaid and return NFT to borrower
        loan.isActive = false;
        IERC721(nftContract).transferFrom(address(this), loan.borrower, tokenId);
    }

    // Function to allow the owner to withdraw funds (for simplicity)
    function withdraw(address payable to, uint256 amount) public {
        require(amount > 0, "Withdrawal amount must be greater than 0");
        require(address(this).balance >= amount, "Insufficient contract balance");
        to.transfer(amount);
    }
}
```
