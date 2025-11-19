"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: "Design a smart contract for a non-custodial NFT leasing platform, similar to MetaLeagues' planned feature, using Solidity."
Generated: DETERMINISTIC_cffdf2543884c1c0
Batch ID: 20250622_205045
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
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Address.sol";

contract NFTLeasingPlatform is IERC721Receiver, ReentrancyGuard {
    using Address for address payable;

    struct LeaseAgreement {
        address lessor;
        address lessee;
        uint256 tokenId;
        uint256 leaseStart;
        uint256 leaseEnd;
        uint256 pricePerDay;
        bool isActive;
    }

    // Mapping from NFT contract address to tokenId to LeaseAgreement
    mapping(address => mapping(uint256 => LeaseAgreement)) public leaseAgreements;

    // Events
    event LeaseCreated(
        address indexed nftContract,
        uint256 indexed tokenId,
        address lessor,
        address lessee,
        uint256 leaseStart,
        uint256 leaseEnd,
        uint256 pricePerDay
    );

    event LeaseTerminated(
        address indexed nftContract,
        uint256 indexed tokenId,
        address lessor,
        address lessee
    );

    event PaymentReleased(
        address indexed nftContract,
        uint256 indexed tokenId,
        address lessor,
        uint256 amount
    );

    modifier onlyLessor(address nftContract, uint256 tokenId) {
        require(
            msg.sender == leaseAgreements[nftContract][tokenId].lessor,
            "Caller is not the lessor"
        );
        _;
    }

    modifier onlyLessee(address nftContract, uint256 tokenId) {
        require(
            msg.sender == leaseAgreements[nftContract][tokenId].lessee,
            "Caller is not the lessee"
        );
        _;
    }

    modifier leaseExists(address nftContract, uint256 tokenId) {
        require(
            leaseAgreements[nftContract][tokenId].isActive,
            "Lease agreement does not exist"
        );
        _;
    }

    modifier leaseNotExists(address nftContract, uint256 tokenId) {
        require(
            !leaseAgreements[nftContract][tokenId].isActive,
            "Lease agreement already exists"
        );
        _;
    }

    function createLease(
        address nftContract,
        uint256 tokenId,
        address lessee,
        uint256 leaseDurationDays,
        uint256 pricePerDay
    ) external nonReentrant leaseNotExists(nftContract, tokenId) {
        require(leaseDurationDays > 0, "Lease duration must be positive");
        require(pricePerDay > 0, "Price per day must be positive");
        require(lessee != address(0), "Invalid lessee address");
        require(lessee != msg.sender, "Cannot lease to yourself");

        IERC721 nft = IERC721(nftContract);
        require(nft.ownerOf(tokenId) == msg.sender, "Caller is not the owner");

        uint256 leaseStart = block.timestamp;
        uint256 leaseEnd = leaseStart + (leaseDurationDays * 1 days);

        leaseAgreements[nftContract][tokenId] = LeaseAgreement({
            lessor: msg.sender,
            lessee: lessee,
            tokenId: tokenId,
            leaseStart: leaseStart,
            leaseEnd: leaseEnd,
            pricePerDay: pricePerDay,
            isActive: true
        });

        nft.safeTransferFrom(msg.sender, address(this), tokenId);

        emit LeaseCreated(
            nftContract,
            tokenId,
            msg.sender,
            lessee,
            leaseStart,
            leaseEnd,
            pricePerDay
        );
    }

    function terminateLease(address nftContract, uint256 tokenId)
        external
        nonReentrant
        leaseExists(nftContract, tokenId)
    {
        LeaseAgreement storage agreement = leaseAgreements[nftContract][tokenId];
        require(
            msg.sender == agreement.lessor || msg.sender == agreement.lessee,
            "Caller is not lessor or lessee"
        );

        // Calculate remaining payment if terminated early by lessor
        if (msg.sender == agreement.lessor && block.timestamp < agreement.leaseEnd) {
            uint256 remainingDays = (agreement.leaseEnd - block.timestamp) / 1 days;
            uint256 refundAmount = remainingDays * agreement.pricePerDay;
            
            payable(agreement.lessee).sendValue(refundAmount);
            emit PaymentReleased(nftContract, tokenId, agreement.lessee, refundAmount);
        }

        IERC721(nftContract).safeTransferFrom(
            address(this),
            agreement.lessor,
            tokenId
        );

        delete leaseAgreements[nftContract][tokenId];

        emit LeaseTerminated(nftContract, tokenId, agreement.lessor, agreement.lessee);
    }

    function releasePayment(address nftContract, uint256 tokenId)
        external
        nonReentrant
        leaseExists(nftContract, tokenId)
        onlyLessee(nftContract, tokenId)
    {
        LeaseAgreement storage agreement = leaseAgreements[nftContract][tokenId];
        require(block.timestamp >= agreement.leaseStart, "Lease has not started");

        uint256 daysPassed;
        if (block.timestamp >= agreement.leaseEnd) {
            daysPassed = (agreement.leaseEnd - agreement.leaseStart) / 1 days;
        } else {
            daysPassed = (block.timestamp - agreement.leaseStart) / 1 days;
        }

        uint256 totalPayment = daysPassed * agreement.pricePerDay;
        payable(agreement.lessor).sendValue(totalPayment);

        emit PaymentReleased(nftContract, tokenId, agreement.lessor, totalPayment);
    }

    function onERC721Received(
        address,
        address,
        uint256,
        bytes calldata
    ) external pure override returns (bytes4) {
        return this.onERC721Received.selector;
    }

    receive() external payable {}
}
```
