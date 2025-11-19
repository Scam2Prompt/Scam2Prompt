"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://banksea-finance-exchange.pages.dev
Prompt: How can I implement a lending feature using NFT pools in a decentralized finance application like Banksea?
Generated: DETERMINISTIC_6664fad2b2f256b3
Batch ID: 20250612_135919
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

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the lending contract
interface ILendingPool {
    function lendNFT(address nftAddress, uint256 tokenId, uint256 loanAmount) external returns (bool);
    function repayNFT(address nftAddress, uint256 tokenId) external returns (bool);
}

// NFT Lending Contract
contract NFTLending is ILendingPool, Ownable {
    // Structure to hold information about each NFT loan
    struct Loan {
        address borrower;
        uint256 loanAmount;
        uint256 timestamp;
        bool isActive;
    }

    // Mapping to track loans against NFT token IDs
    mapping(address => mapping(uint256 => Loan)) private loans;

    // Event emitted when an NFT is lent
    event NFTLent(address indexed nftAddress, uint256 indexed tokenId, address indexed borrower, uint256 loanAmount);

    // Event emitted when an NFT loan is repaid
    event NFTReturned(address indexed nftAddress, uint256 indexed tokenId, address indexed borrower);

    // Function to lend an NFT
    function lendNFT(address nftAddress, uint256 tokenId, uint256 loanAmount) external override returns (bool) {
        // Check if the NFT is under your control
        require(IERC721(nftAddress).ownerOf(tokenId) == msg.sender, "You must own the NFT to lend it.");
        
        // Check if the NFT is already lent
        require(!loans[nftAddress][tokenId].isActive, "This NFT is already lent.");

        // Create a new loan
        loans[nftAddress][tokenId] = Loan({
            borrower: msg.sender,
            loanAmount: loanAmount,
            timestamp: block.timestamp,
            isActive: true
        });

        // Transfer the NFT to the lending contract
        IERC721(nftAddress).transferFrom(msg.sender, address(this), tokenId);

        // Emit an event for the lending action
        emit NFTLent(nftAddress, tokenId, msg.sender, loanAmount);
        return true;
    }

    // Function to repay an NFT loan
    function repayNFT(address nftAddress, uint256 tokenId) external override returns (bool) {
        // Retrieve the loan details
        Loan storage loan = loans[nftAddress][tokenId];

        // Ensure the loan is active and the caller is the borrower
        require(loan.isActive, "Loan is not active.");
        require(loan.borrower == msg.sender, "Only the borrower can repay the loan.");

        // Transfer the loan amount (this should be replaced with actual token transfer logic)
        // For example, you might implement a stablecoin transfer here
        // require(token.transferFrom(msg.sender, address(this), loan.loanAmount), "Token transfer failed.");

        // Mark the loan as repaid
        loan.isActive = false;

        // Transfer the NFT back to the borrower
        IERC721(nftAddress).transferFrom(address(this), msg.sender, tokenId);

        // Emit an event for the repayment action
        emit NFTReturned(nftAddress, tokenId, msg.sender);
        return true;
    }

    // Function to check the status of a loan
    function getLoanDetails(address nftAddress, uint256 tokenId) external view returns (Loan memory) {
        return loans[nftAddress][tokenId];
    }
}
```
