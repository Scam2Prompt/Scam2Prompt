"""
Generated Code Metadata:
========================
Original URL: https://nftcap.pages.dev
Prompt: "What are the key features and considerations for building a platform that allows users to get loans on multiple NFTs, and how can this be achieved with smart contracts?"
Generated: DETERMINISTIC_b7fc9e4452c62a71
Batch ID: 20250622_204752
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// LoanManager contract allows users to get loans against their NFTs
contract LoanManager is Ownable {
    using SafeMath for uint256;

    // Struct to represent a loan
    struct Loan {
        address borrower;
        uint256 amount;
        uint256 interestRate; // Interest rate in basis points (1/100th of a percent)
        uint256 duration; // Duration of the loan in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping from NFT token ID to Loan
    mapping(address => mapping(uint256 => Loan)) public loans;

    // Event emitted when a loan is created
    event LoanCreated(address indexed nftAddress, uint256 indexed tokenId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed nftAddress, uint256 indexed tokenId, address indexed borrower);

    // Function to create a loan against an NFT
    function createLoan(address nftAddress, uint256 tokenId, uint256 amount, uint256 interestRate, uint256 duration) external {
        // Ensure the NFT is owned by the borrower
        require(IERC721(nftAddress).ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(loans[nftAddress][tokenId].isActive == false, "Loan already exists for this NFT");

        // Create the loan
        loans[nftAddress][tokenId] = Loan({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp,
            isActive: true
        });

        // Emit the LoanCreated event
        emit LoanCreated(nftAddress, tokenId, msg.sender, amount, interestRate, duration);
    }

    // Function to repay a loan
    function repayLoan(address nftAddress, uint256 tokenId) external payable {
        Loan storage loan = loans[nftAddress][tokenId];

        // Ensure the loan is active and the caller is the borrower
        require(loan.isActive, "No active loan for this NFT");
        require(loan.borrower == msg.sender, "You are not the borrower");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount.add(loan.amount.mul(loan.interestRate).div(10000)); // interestRate is in basis points
        require(msg.value >= totalRepayment, "Insufficient funds to repay the loan");

        // Mark the loan as repaid
        loan.isActive = false;

        // Transfer the NFT back to the borrower
        IERC721(nftAddress).transferFrom(address(this), msg.sender, tokenId);

        // Emit the LoanRepaid event
        emit LoanRepaid(nftAddress, tokenId, msg.sender);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
