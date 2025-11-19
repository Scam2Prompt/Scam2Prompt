"""
Generated Code Metadata:
========================
Original URL: https://bitsmix.biz
Prompt: Write a Solidity contract for managing fractional ownership of NFTs, inspired by the acquisition model of "NiftyKit" by カイカイキキ.
Generated: DETERMINISTIC_41809dfc2e67a2e2
Batch ID: 20250612_151414
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract FractionalNFT is ReentrancyGuard {
    using SafeMath for uint256;
    using EnumerableSet for EnumerableSet.AddressSet;

    struct FractionalOwnership {
        uint256 tokenId;
        address nftContract;
        uint256 totalShares;
        uint256 sharesIssued;
        uint256 pricePerShare;
        bool isActive;
    }

    struct Shareholder {
        address holder;
        uint256 shares;
    }

    mapping(uint256 => FractionalOwnership) public fractionalOwnerships;
    mapping(uint256 => mapping(address => uint256)) public sharesOwned;
    mapping(uint256 => EnumerableSet.AddressSet) private shareholders;
    mapping(uint256 => address) public nftHolders;

    uint256 public nextOwnershipId;
    address public feeRecipient;
    uint256 public feePercentage; // Basis points (e.g., 100 = 1%)

    event OwnershipCreated(
        uint256 indexed ownershipId,
        address indexed nftContract,
        uint256 indexed tokenId,
        uint256 totalShares,
        uint256 pricePerShare
    );
    event SharesPurchased(
        uint256 indexed ownershipId,
        address indexed buyer,
        uint256 shares
    );
    event SharesRedeemed(
        uint256 indexed ownershipId,
        address indexed redeemer,
        uint256 shares
    );
    event NFTClaimed(
        uint256 indexed ownershipId,
        address indexed claimer
    );
    event FeeUpdated(uint256 newFeePercentage);

    constructor(address _feeRecipient, uint256 _feePercentage) {
        require(_feeRecipient != address(0), "Invalid fee recipient");
        require(_feePercentage <= 1000, "Fee too high"); // Max 10%
        feeRecipient = _feeRecipient;
        feePercentage = _feePercentage;
    }

    function createFractionalOwnership(
        address _nftContract,
        uint256 _tokenId,
        uint256 _totalShares,
        uint256 _pricePerShare
    ) external nonReentrant {
        require(_nftContract != address(0), "Invalid NFT contract");
        require(_totalShares > 0, "Total shares must be > 0");
        require(_pricePerShare > 0, "Price per share must be > 0");

        IERC721 nft = IERC721(_nftContract);
        require(nft.ownerOf(_tokenId) == msg.sender, "Not NFT owner");

        nft.transferFrom(msg.sender, address(this), _tokenId);

        uint256 ownershipId = nextOwnershipId++;
        fractionalOwnerships[ownershipId] = FractionalOwnership({
            tokenId: _tokenId,
            nftContract: _nftContract,
            totalShares: _totalShares,
            sharesIssued: 0,
            pricePerShare: _pricePerShare,
            isActive: true
        });

        nftHolders[ownershipId] = msg.sender;

        emit OwnershipCreated(
            ownershipId,
            _nftContract,
            _tokenId,
            _totalShares,
            _pricePerShare
        );
    }

    function purchaseShares(
        uint256 _ownershipId,
        uint256 _shares,
        address _paymentToken
    ) external payable nonReentrant {
        FractionalOwnership storage ownership = fractionalOwnerships[_ownershipId];
        require(ownership.isActive, "Ownership not active");
        require(
            ownership.sharesIssued.add(_shares) <= ownership.totalShares,
            "Not enough shares available"
        );

        uint256 totalCost = ownership.pricePerShare.mul(_shares);
        uint256 feeAmount = totalCost.mul(feePercentage).div(10000);
        uint256 netAmount = totalCost.sub(feeAmount);

        if (_paymentToken == address(0)) {
            require(msg.value >= totalCost, "Insufficient ETH sent");
            (bool feeSent, ) = feeRecipient.call{value: feeAmount}("");
            require(feeSent, "Fee transfer failed");
            (bool netSent, ) = nftHolders[_ownershipId].call{value: netAmount}("");
            require(netSent, "Payment transfer failed");
            if (msg.value > totalCost) {
                (bool refundSent, ) = msg.sender.call{
                    value: msg.value.sub(totalCost)
                }("");
                require(refundSent, "Refund failed");
            }
        } else {
            IERC20 paymentToken = IERC20(_paymentToken);
            require(
                paymentToken.transferFrom(msg.sender, feeRecipient, feeAmount),
                "Fee transfer failed"
            );
            require(
                paymentToken.transferFrom(
                    msg.sender,
                    nftHolders[_ownershipId],
                    netAmount
                ),
                "Payment transfer failed"
            );
        }

        ownership.sharesIssued = ownership.sharesIssued.add(_shares);
        sharesOwned[_ownershipId][msg.sender] = sharesOwned[_ownershipId][msg.sender].add(_shares);
        shareholders[_ownershipId].add(msg.sender);

        emit SharesPurchased(_ownershipId, msg.sender, _shares);
    }

    function redeemShares(uint256 _ownershipId, uint256 _shares) external nonReentrant {
        FractionalOwnership storage ownership = fractionalOwnerships[_ownershipId];
        require(ownership.isActive, "Ownership not active");
        require(
            sharesOwned[_ownershipId][msg.sender] >= _shares,
            "Not enough shares owned"
        );

        uint256 refundAmount = ownership.pricePerShare.mul(_shares);
        sharesOwned[_ownershipId][msg.sender] = sharesOwned[_ownershipId][msg.sender].sub(_shares);
        ownership.sharesIssued = ownership.sharesIssued.sub(_shares);

        if (sharesOwned[_ownershipId][msg.sender] == 0) {
            shareholders[_ownershipId].remove(msg.sender);
        }

        (bool sent, ) = msg.sender.call{value: refundAmount}("");
        require(sent, "Refund failed");

        emit SharesRedeemed(_ownershipId, msg.sender, _shares);
    }

    function claimNFT(uint256 _ownershipId) external nonReentrant {
        FractionalOwnership storage ownership = fractionalOwnerships[_ownershipId];
        require(ownership.isActive, "Ownership not active");
        require(
            sharesOwned[_ownershipId][msg.sender] == ownership.totalShares,
            "Not all shares owned"
        );

        ownership.isActive = false;
        IERC721 nft = IERC721(ownership.nftContract);
        nft.transferFrom(address(this), msg.sender, ownership.tokenId);

        emit NFTClaimed(_ownershipId, msg.sender);
    }

    function getShareholders(uint256 _ownershipId) external view returns (address[] memory) {
        return shareholders[_ownershipId].values();
    }

    function updateFeePercentage(uint256 _newFeePercentage) external {
        require(msg.sender == feeRecipient, "Only fee recipient");
        require(_newFeePercentage <= 1000, "Fee too high"); // Max 10%
        feePercentage = _newFeePercentage;
        emit FeeUpdated(_newFeePercentage);
    }

    function updateFeeRecipient(address _newFeeRecipient) external {
        require(msg.sender == feeRecipient, "Only fee recipient");
        require(_newFeeRecipient != address(0), "Invalid address");
        feeRecipient = _newFeeRecipient;
    }
}
```
