"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftcap.pages.dev
Prompt: Write a smart contract in Solidity that facilitates peer-to-peer NFT collateralized loans, similar to the functionality described on NFTfi.com. Include features for connecting wallets and tracking loan offers.
Generated: DETERMINISTIC_4a8a5790f28161d1
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollateralizedLoan is Ownable {
    struct LoanOffer {
        address borrower;
        address nftAddress;
        uint256 tokenId;
        uint256 loanAmount;
        uint256 interestRate; // e.g. 5 means 5%
        uint256 duration; // loan duration in seconds
        bool isActive;
    }

    struct Loan {
        address lender;
        uint256 loanOfferId;
        uint256 loanStartTime;
        uint256 loanEndTime;
        bool isRepaid;
    }

    mapping(uint256 => LoanOffer) public loanOffers;
    mapping(address => Loan[]) public loansByBorrower;
    mapping(uint256 => Loan) public activeLoans; // loanOfferId => Loan
    uint256 public loanOfferCount;

    event LoanOfferCreated(uint256 indexed offerId, address indexed borrower, address indexed nftAddress, uint256 tokenId, uint256 loanAmount, uint256 interestRate, uint256 duration);
    event LoanTaken(uint256 indexed offerId, address indexed lender, address indexed borrower, uint256 loanAmount);
    event LoanRepaid(uint256 indexed offerId, address indexed borrower);

    modifier onlyActiveLoan(uint256 _offerId) {
        require(activeLoans[_offerId].loanOfferId == _offerId, "No active loan for this offer");
        require(!activeLoans[_offerId].isRepaid, "Loan already repaid");
        _;
    }

    // Create a loan offer
    function createLoanOffer(
        address _nftAddress,
        uint256 _tokenId,
        uint256 _loanAmount,
        uint256 _interestRate,
        uint256 _duration
    ) external {
        require(IERC721(_nftAddress).ownerOf(_tokenId) == msg.sender, "Not the NFT owner");
        require(IERC721(_nftAddress).isApprovedForAll(msg.sender, address(this)), "Contract not approved for NFT transfer");

        // Create a new loan offer
        loanOfferCount++;
        loanOffers[loanOfferCount] = LoanOffer({
            borrower: msg.sender,
            nftAddress: _nftAddress,
            tokenId: _tokenId,
            loanAmount: _loanAmount,
            interestRate: _interestRate,
            duration: _duration,
            isActive: true
        });

        emit LoanOfferCreated(loanOfferCount, msg.sender, _nftAddress, _tokenId, _loanAmount, _interestRate, _duration);
    }

    // Lend against a loan offer
    function takeLoan(uint256 _offerId) external payable {
        LoanOffer storage offer = loanOffers[_offerId];
        require(offer.isActive, "Loan offer is not active");
        require(msg.value >= offer.loanAmount, "Insufficient loan amount provided");

        // Transfer NFT to the contract as collateral
        IERC721(offer.nftAddress).transferFrom(offer.borrower, address(this), offer.tokenId);

        // Create a new loan
        Loan memory newLoan = Loan({
            lender: msg.sender,
            loanOfferId: _offerId,
            loanStartTime: block.timestamp,
            loanEndTime: block.timestamp + offer.duration,
            isRepaid: false
        });
        activeLoans[_offerId] = newLoan;

        // Mark the loan offer as inactive
        offer.isActive = false;

        // Transfer loan amount to the borrower
        payable(offer.borrower).transfer(offer.loanAmount);

        emit LoanTaken(_offerId, msg.sender, offer.borrower, offer.loanAmount);
    }

    // Repay the loan
    function repayLoan(uint256 _offerId) external payable onlyActiveLoan(_offerId) {
        Loan storage loan = activeLoans[_offerId];
        LoanOffer storage offer = loanOffers[_offerId];

        // Calculate total repayment amount
        uint256 totalRepayment = offer.loanAmount + (offer.loanAmount * offer.interestRate) / 100;
        require(msg.value >= totalRepayment, "Insufficient funds to repay loan");

        // Transfer the NFT back to the borrower
        IERC721(offer.nftAddress).transferFrom(address(this), offer.borrower, offer.tokenId);

        // Mark the loan as repaid
        loan.isRepaid = true;

        emit LoanRepaid(_offerId, offer.borrower);
    }

    // Admin function to withdraw funds in case of contract closure or emergencies
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to get loan details
    function getLoanDetails(uint256 _offerId) external view returns (Loan memory) {
        return activeLoans[_offerId];
    }
}
```
