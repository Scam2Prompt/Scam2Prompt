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

// Interface for interacting with ERC721 tokens (NFTs).
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Struct representing a loan bundle.
struct LoanBundle {
    address borrower;
    uint256 loanAmount;
    uint256 interestRate; // Interest rate in basis points (1% = 100 basis points)
    uint256 duration; // Loan duration in seconds
    uint256[] nftTokenIds; // List of NFT token IDs used as collateral
    address nftContract; // Address of the NFT contract
    bool isActive; // True if the loan is active
}

contract MultiNFTCollaterizedLoan {
    // Mapping loan ID to LoanBundle details
    mapping(uint256 => LoanBundle) public loanBundles;

    // Counter for generating unique loan IDs
    uint256 private loanIdCounter;

    // Event emitted when a loan bundle is created
    event LoanBundleCreated(
        uint256 loanId,
        address borrower,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration,
        address nftContract,
        uint256[] nftTokenIds
    );

    // Event emitted when a loan is repaid
    event LoanRepaid(uint256 loanId);

    // Function to create a loan bundle with NFTs as collateral
    function createLoanBundle(
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration,
        address nftContract,
        uint256[] calldata nftTokenIds
    ) external returns (uint256) {
        require(nftTokenIds.length > 0, "At least one NFT must be provided as collateral");
        require(loanAmount > 0, "Loan amount must be greater than 0");
        require(duration > 0, "Loan duration must be greater than 0");

        // Verify ownership and transfer NFTs to the contract
        for (uint256 i = 0; i < nftTokenIds.length; i++) {
            require(IERC721(nftContract).ownerOf(nftTokenIds[i]) == msg.sender, "Caller does not own the NFT");
            IERC721(nftContract).transferFrom(msg.sender, address(this), nftTokenIds[i]);
        }

        // Increment loan ID counter
        loanIdCounter++;

        // Create and store the loan bundle
        loanBundles[loanIdCounter] = LoanBundle({
            borrower: msg.sender,
            loanAmount: loanAmount,
            interestRate: interestRate,
            duration: duration,
            nftTokenIds: nftTokenIds,
            nftContract: nftContract,
            isActive: true
        });

        // Emit LoanBundleCreated event
        emit LoanBundleCreated(
            loanIdCounter,
            msg.sender,
            loanAmount,
            interestRate,
            duration,
            nftContract,
            nftTokenIds
        );

        return loanIdCounter;
    }

    // Function to repay the loan and retrieve the NFTs
    function repayLoan(uint256 loanId) external payable {
        LoanBundle storage loan = loanBundles[loanId];
        require(loan.isActive, "Loan is not active");
        require(msg.sender == loan.borrower, "Only the borrower can repay the loan");
        require(msg.value >= loan.loanAmount, "Insufficient repayment amount");

        // Mark the loan as inactive
        loan.isActive = false;

        // Transfer NFTs back to the borrower
        for (uint256 i = 0; i < loan.nftTokenIds.length; i++) {
            IERC721(loan.nftContract).transferFrom(address(this), loan.borrower, loan.nftTokenIds[i]);
        }

        // Emit LoanRepaid event
        emit LoanRepaid(loanId);
    }

    // Fallback function to prevent accidental ETH transfers
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
