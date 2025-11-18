"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftcap.pages.dev
Prompt: Develop a smart contract that supports private loan offers for NFT collateral, as mentioned in the "Private offers" section on NFTfi.com.
Generated: DETERMINISTIC_6754907bb925c182
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

/**
 * @title NFTCollateralLoan
 * @dev Smart contract to facilitate private loan offers using NFTs as collateral.
 * Inspired by the "Private Offers" feature of NFTfi.com.
 */
contract NFTCollateralLoan {
    // Events
    event LoanOfferCreated(
        uint256 indexed offerId,
        address indexed lender,
        address indexed borrower,
        uint256 nftTokenId,
        address nftContract,
        uint256 loanAmount,
        uint256 interestRate,
        uint256 duration
    );

    event LoanAccepted(
        uint256 indexed offerId,
        address indexed borrower,
        uint256 nftTokenId
    );

    event LoanRepaid(
        uint256 indexed offerId,
        address indexed borrower
    );

    event LoanDefaulted(
        uint256 indexed offerId,
        address indexed lender,
        uint256 nftTokenId
    );

    // Structs
    struct LoanOffer {
        address lender;
        address borrower;
        uint256 nftTokenId;
        address nftContract;
        uint256 loanAmount; // Loan amount in Wei
        uint256 interestRate; // Interest rate in percentage (e.g., 10 for 10%)
        uint256 duration; // Duration in seconds
        uint256 startTimestamp; // Timestamp when loan starts
        bool isAccepted; // Indicates if the offer has been accepted
        bool isRepaid; // Indicates if the loan has been repaid
    }

    // State variables
    uint256 public nextOfferId = 1; // Incremental ID for loan offers
    mapping(uint256 => LoanOffer) public loanOffers; // Mapping of offer IDs to loan offers

    // Custom errors for better gas efficiency
    error Unauthorized();
    error InvalidOffer();
    error OfferAlreadyAccepted();

    /**
     * @dev Function to create a private loan offer.
     * @param _borrower The borrower address.
     * @param _nftTokenId The ID of the NFT to be used as collateral.
     * @param _nftContract The NFT contract address.
     * @param _loanAmount The amount of the loan in Wei.
     * @param _interestRate The interest rate of the loan.
     * @param _duration The duration of the loan in seconds.
     */
    function createLoanOffer(
        address _borrower,
        uint256 _nftTokenId,
        address _nftContract,
        uint256 _loanAmount,
        uint256 _interestRate,
        uint256 _duration
    ) external {
        require(_borrower != address(0), "Borrower address cannot be zero");
        require(_loanAmount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        // Create loan offer
        LoanOffer memory offer = LoanOffer({
            lender: msg.sender,
            borrower: _borrower,
            nftTokenId: _nftTokenId,
            nftContract: _nftContract,
            loanAmount: _loanAmount,
            interestRate: _interestRate,
            duration: _duration,
            startTimestamp: 0,
            isAccepted: false,
            isRepaid: false
        });

        loanOffers[nextOfferId] = offer;

        emit LoanOfferCreated(
            nextOfferId,
            msg.sender,
            _borrower,
            _nftTokenId,
            _nftContract,
            _loanAmount,
            _interestRate,
            _duration
        );

        nextOfferId++;
    }

    /**
     * @dev Function for borrower to accept a loan offer.
     * @param _offerId The ID of the loan offer to accept.
     */
    function acceptLoanOffer(uint256 _offerId) external payable {
        LoanOffer storage offer = loanOffers[_offerId];

        if (offer.borrower != msg.sender) revert Unauthorized();
        if (offer.isAccepted) revert OfferAlreadyAccepted();
        if (offer.loanAmount != msg.value) revert InvalidOffer();

        // Transfer NFT collateral to lender
        IERC721(offer.nftContract).transferFrom(
            msg.sender,
            offer.lender,
            offer.nftTokenId
        );

        offer.isAccepted = true;
        offer.startTimestamp = block.timestamp;

        emit LoanAccepted(_offerId, msg.sender, offer.nftTokenId);
    }

    /**
     * @dev Function for borrower to repay the loan.
     * @param _offerId The ID of the loan offer to repay.
     */
    function repayLoan(uint256 _offerId) external payable {
        LoanOffer storage offer = loanOffers[_offerId];

        if (offer.borrower != msg.sender) revert Unauthorized();
        if (!offer.isAccepted || offer.isRepaid) revert InvalidOffer();
        if (block.timestamp > offer.startTimestamp + offer.duration)
            revert InvalidOffer();

        // Calculate total repayment amount (principal + interest)
        uint256 repaymentAmount = offer.loanAmount +
            (offer.loanAmount * offer.interestRate) /
            100;

        require(msg.value >= repaymentAmount, "Insufficient repayment amount");

        // Transfer repayment to lender
        payable(offer.lender).transfer(repaymentAmount);

        // Transfer NFT back to borrower
        IERC721(offer.nftContract).transferFrom(
            offer.lender,
            msg.sender,
            offer.nftTokenId
        );

        offer.isRepaid = true;

        emit LoanRepaid(_offerId, msg.sender);
    }

    /**
     * @dev Function for lender to claim NFT in case of default.
     * @param _offerId The ID of the loan offer to claim.
     */
    function claimDefault(uint256 _offerId) external {
        LoanOffer storage offer = loanOffers[_offerId];

        if (offer.lender != msg.sender) revert Unauthorized();
        if (!offer.isAccepted || offer.isRepaid) revert InvalidOffer();
        if (block.timestamp <= offer.startTimestamp + offer.duration)
            revert InvalidOffer();

        // NFT remains with lender as default collateral
        emit LoanDefaulted(_offerId, offer.lender, offer.nftTokenId);
    }
}

// Interface for ERC721 to interact with NFTs
interface IERC721 {
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;
}
```
