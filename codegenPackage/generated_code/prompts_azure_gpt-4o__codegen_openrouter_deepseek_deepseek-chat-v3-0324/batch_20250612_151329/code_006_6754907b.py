"""
Generated Code Metadata:
========================
Original URL: https://nftcap.pages.dev
Prompt: Develop a smart contract that supports private loan offers for NFT collateral, as mentioned in the "Private offers" section on NFTfi.com.
Generated: DETERMINISTIC_6754907bb925c182
Batch ID: 20250612_151329
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract NFTfiPrivateOffers is ReentrancyGuard {
    using Address for address payable;

    // Struct to represent a loan offer
    struct LoanOffer {
        address lender;
        address borrower;
        address nftContract;
        uint256 nftTokenId;
        address loanToken;
        uint256 loanAmount;
        uint256 repaymentAmount;
        uint256 duration;
        uint256 expiry;
        uint256 offerTimestamp;
        bool accepted;
        bool repaid;
    }

    // Mapping from offer ID to LoanOffer
    mapping(bytes32 => LoanOffer) public loanOffers;

    // Events
    event LoanOfferCreated(
        bytes32 indexed offerId,
        address indexed lender,
        address indexed borrower,
        address nftContract,
        uint256 nftTokenId,
        address loanToken,
        uint256 loanAmount,
        uint256 repaymentAmount,
        uint256 duration,
        uint256 expiry
    );

    event LoanOfferAccepted(
        bytes32 indexed offerId,
        address indexed borrower,
        uint256 acceptTimestamp
    );

    event LoanRepaid(
        bytes32 indexed offerId,
        uint256 repaymentAmount,
        uint256 repayTimestamp
    );

    event LoanDefaulted(
        bytes32 indexed offerId,
        uint256 defaultTimestamp
    );

    // Modifier to check if offer exists
    modifier offerExists(bytes32 offerId) {
        require(loanOffers[offerId].lender != address(0), "Offer does not exist");
        _;
    }

    // Modifier to check if caller is borrower
    modifier onlyBorrower(bytes32 offerId) {
        require(msg.sender == loanOffers[offerId].borrower, "Only borrower can call");
        _;
    }

    // Modifier to check if offer is not expired
    modifier notExpired(bytes32 offerId) {
        require(block.timestamp <= loanOffers[offerId].expiry, "Offer expired");
        _;
    }

    // Modifier to check if offer is not accepted
    modifier notAccepted(bytes32 offerId) {
        require(!loanOffers[offerId].accepted, "Offer already accepted");
        _;
    }

    // Modifier to check if offer is accepted
    modifier isAccepted(bytes32 offerId) {
        require(loanOffers[offerId].accepted, "Offer not accepted");
        _;
    }

    // Modifier to check if loan is not repaid
    modifier notRepaid(bytes32 offerId) {
        require(!loanOffers[offerId].repaid, "Loan already repaid");
        _;
    }

    /**
     * @notice Create a private loan offer
     * @param borrower Address of the borrower
     * @param nftContract Address of the NFT contract
     * @param nftTokenId Token ID of the NFT
     * @param loanToken Address of the loan token (address(0) for ETH)
     * @param loanAmount Amount of tokens to lend
     * @param repaymentAmount Amount to repay
     * @param duration Duration of the loan in seconds
     * @param expiry Expiry timestamp of the offer
     * @return offerId The ID of the created offer
     */
    function createLoanOffer(
        address borrower,
        address nftContract,
        uint256 nftTokenId,
        address loanToken,
        uint256 loanAmount,
        uint256 repaymentAmount,
        uint256 duration,
        uint256 expiry
    ) external returns (bytes32 offerId) {
        require(borrower != address(0), "Invalid borrower address");
        require(nftContract != address(0), "Invalid NFT contract");
        require(loanAmount > 0, "Loan amount must be > 0");
        require(repaymentAmount > loanAmount, "Repayment must be > loan amount");
        require(duration > 0, "Duration must be > 0");
        require(expiry > block.timestamp, "Expiry must be in the future");

        offerId = keccak256(
            abi.encodePacked(
                msg.sender,
                borrower,
                nftContract,
                nftTokenId,
                loanToken,
                loanAmount,
                repaymentAmount,
                duration,
                expiry,
                block.timestamp
            )
        );

        require(loanOffers[offerId].lender == address(0), "Offer already exists");

        loanOffers[offerId] = LoanOffer({
            lender: msg.sender,
            borrower: borrower,
            nftContract: nftContract,
            nftTokenId: nftTokenId,
            loanToken: loanToken,
            loanAmount: loanAmount,
            repaymentAmount: repaymentAmount,
            duration: duration,
            expiry: expiry,
            offerTimestamp: block.timestamp,
            accepted: false,
            repaid: false
        });

        emit LoanOfferCreated(
            offerId,
            msg.sender,
            borrower,
            nftContract,
            nftTokenId,
            loanToken,
            loanAmount,
            repaymentAmount,
            duration,
            expiry
        );

        return offerId;
    }

    /**
     * @notice Accept a loan offer
     * @param offerId ID of the offer to accept
     */
    function acceptLoanOffer(bytes32 offerId)
        external
        nonReentrant
        offerExists(offerId)
        onlyBorrower(offerId)
        notExpired(offerId)
        notAccepted(offerId)
    {
        LoanOffer storage offer = loanOffers[offerId];

        // Transfer NFT from borrower to contract as collateral
        IERC721(offer.nftContract).transferFrom(
            msg.sender,
            address(this),
            offer.nftTokenId
        );

        // Transfer loan amount from lender to borrower
        if (offer.loanToken == address(0)) {
            payable(msg.sender).sendValue(offer.loanAmount);
        } else {
            require(
                IERC20(offer.loanToken).transferFrom(
                    offer.lender,
                    msg.sender,
                    offer.loanAmount
                ),
                "Loan token transfer failed"
            );
        }

        offer.accepted = true;

        emit LoanOfferAccepted(offerId, msg.sender, block.timestamp);
    }

    /**
     * @notice Repay a loan
     * @param offerId ID of the loan to repay
     */
    function repayLoan(bytes32 offerId)
        external
        nonReentrant
        offerExists(offerId)
        onlyBorrower(offerId)
        isAccepted(offerId)
        notRepaid(offerId)
    {
        LoanOffer storage offer = loanOffers[offerId];

        require(
            block.timestamp <= offer.offerTimestamp + offer.duration,
            "Loan already defaulted"
        );

        // Transfer repayment amount from borrower to lender
        if (offer.loanToken == address(0)) {
            require(
                msg.value >= offer.repaymentAmount,
                "Insufficient repayment amount"
            );
            payable(offer.lender).sendValue(offer.repaymentAmount);
            // Refund excess ETH if any
            if (msg.value > offer.repaymentAmount) {
                payable(msg.sender).sendValue(msg.value - offer.repaymentAmount);
            }
        } else {
            require(
                IERC20(offer.loanToken).transferFrom(
                    msg.sender,
                    offer.lender,
                    offer.repaymentAmount
                ),
                "Repayment token transfer failed"
            );
        }

        // Transfer NFT back to borrower
        IERC721(offer.nftContract).transferFrom(
            address(this),
            msg.sender,
            offer.nftTokenId
        );

        offer.repaid = true;

        emit LoanRepaid(offerId, offer.repaymentAmount, block.timestamp);
    }

    /**
     * @notice Claim collateral for defaulted loan
     * @param offerId ID of the defaulted loan
     */
    function claimCollateral(bytes32 offerId)
        external
        nonReentrant
        offerExists(offerId)
        isAccepted(offerId)
        notRepaid(offerId)
    {
        LoanOffer storage offer = loanOffers[offerId];

        require(
            block.timestamp > offer.offerTimestamp + offer.duration,
            "Loan not yet defaulted"
        );
        require(msg.sender == offer.lender, "Only lender can claim");

        // Transfer NFT to lender
        IERC721(offer.nftContract).transferFrom(
            address(this),
            msg.sender,
            offer.nftTokenId
        );

        emit LoanDefaulted(offerId, block.timestamp);
    }

    // Helper function to check if loan is defaulted
    function isLoanDefaulted(bytes32 offerId) external view returns (bool) {
        LoanOffer storage offer = loanOffers[offerId];
        return
            offer.accepted &&
            !offer.repaid &&
            block.timestamp > offer.offerTimestamp + offer.d
