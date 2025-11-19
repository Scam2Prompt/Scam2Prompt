"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-presales.pages.dev
Prompt: Develop a Solidity contract for an NFT marketplace that supports fractionalized NFTs for AI start-ups, inspired by InQubeta's platform.
Generated: DETERMINISTIC_baf2af4b9441188e
Batch ID: 20250612_153420
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FractionalizedNFTMarketplace is ERC721, Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 totalShares;
        uint256 sharesAvailable;
        uint256 pricePerShare;
        address paymentToken;
        bool isActive;
    }

    struct FractionalizedNFT {
        uint256 tokenId;
        string metadataURI;
        uint256 totalShares;
        mapping(address => uint256) sharesOwned;
    }

    // Mapping from token ID to fractionalized NFT
    mapping(uint256 => FractionalizedNFT) private _fractionalizedNFTs;

    // Mapping from token ID to listing
    mapping(uint256 => Listing) private _listings;

    // Supported payment tokens
    mapping(address => bool) private _supportedPaymentTokens;

    // Marketplace fee percentage (1% = 100)
    uint256 public marketplaceFeePercentage = 200; // 2% default fee
    address public feeRecipient;

    // Events
    event NFTFractionalized(
        uint256 indexed tokenId,
        uint256 totalShares,
        string metadataURI
    );
    event Listed(
        uint256 indexed tokenId,
        address indexed seller,
        uint256 totalShares,
        uint256 pricePerShare,
        address paymentToken
    );
    event SharePurchased(
        uint256 indexed tokenId,
        address indexed buyer,
        uint256 shares,
        uint256 totalPrice
    );
    event ListingCancelled(uint256 indexed tokenId);
    event PaymentTokenAdded(address indexed token);
    event PaymentTokenRemoved(address indexed token);
    event FeeUpdated(uint256 newFeePercentage);
    event FeeRecipientUpdated(address newRecipient);

    constructor() ERC721("FractionalizedAIStartupNFT", "FAIS") {
        feeRecipient = msg.sender;
    }

    /**
     * @dev Fractionalize an NFT
     * @param tokenId The ID of the NFT to fractionalize
     * @param totalShares Total number of shares to create
     * @param metadataURI Metadata URI for the NFT
     */
    function fractionalizeNFT(
        uint256 tokenId,
        uint256 totalShares,
        string memory metadataURI
    ) external {
        require(totalShares > 0, "Total shares must be greater than 0");
        require(
            _isApprovedOrOwner(msg.sender, tokenId),
            "Caller is not owner nor approved"
        );

        FractionalizedNFT storage fnft = _fractionalizedNFTs[tokenId];
        require(fnft.tokenId == 0, "NFT already fractionalized");

        fnft.tokenId = tokenId;
        fnft.totalShares = totalShares;
        fnft.metadataURI = metadataURI;
        fnft.sharesOwned[msg.sender] = totalShares;

        emit NFTFractionalized(tokenId, totalShares, metadataURI);
    }

    /**
     * @dev List shares of a fractionalized NFT for sale
     * @param tokenId The ID of the fractionalized NFT
     * @param sharesToSell Number of shares to sell
     * @param pricePerShare Price per share in payment token
     * @param paymentToken Address of the payment token (address(0) for ETH)
     */
    function listShares(
        uint256 tokenId,
        uint256 sharesToSell,
        uint256 pricePerShare,
        address paymentToken
    ) external {
        FractionalizedNFT storage fnft = _fractionalizedNFTs[tokenId];
        require(fnft.tokenId != 0, "NFT not fractionalized");
        require(
            fnft.sharesOwned[msg.sender] >= sharesToSell,
            "Not enough shares owned"
        );
        require(sharesToSell > 0, "Must sell at least one share");
        require(pricePerShare > 0, "Price must be greater than 0");
        require(
            paymentToken == address(0) || _supportedPaymentTokens[paymentToken],
            "Payment token not supported"
        );

        Listing storage listing = _listings[tokenId];
        if (listing.tokenId == 0) {
            // New listing
            listing.tokenId = tokenId;
            listing.seller = msg.sender;
            listing.totalShares = sharesToSell;
            listing.sharesAvailable = sharesToSell;
            listing.pricePerShare = pricePerShare;
            listing.paymentToken = paymentToken;
            listing.isActive = true;
        } else {
            // Update existing listing
            require(listing.seller == msg.sender, "Not the listing owner");
            require(listing.isActive, "Listing is not active");
            listing.totalShares = listing.totalShares.add(sharesToSell);
            listing.sharesAvailable = listing.sharesAvailable.add(sharesToSell);
            listing.pricePerShare = pricePerShare;
            listing.paymentToken = paymentToken;
        }

        // Transfer shares to escrow (this contract)
        fnft.sharesOwned[msg.sender] = fnft.sharesOwned[msg.sender].sub(
            sharesToSell
        );
        fnft.sharesOwned[address(this)] = fnft.sharesOwned[address(this)].add(
            sharesToSell
        );

        emit Listed(tokenId, msg.sender, sharesToSell, pricePerShare, paymentToken);
    }

    /**
     * @dev Purchase shares of a fractionalized NFT
     * @param tokenId The ID of the fractionalized NFT
     * @param sharesToBuy Number of shares to purchase
     */
    function purchaseShares(uint256 tokenId, uint256 sharesToBuy)
        external
        payable
        nonReentrant
    {
        Listing storage listing = _listings[tokenId];
        require(listing.isActive, "Listing is not active");
        require(sharesToBuy > 0, "Must buy at least one share");
        require(
            listing.sharesAvailable >= sharesToBuy,
            "Not enough shares available"
        );

        FractionalizedNFT storage fnft = _fractionalizedNFTs[tokenId];
        require(fnft.tokenId != 0, "NFT not fractionalized");

        uint256 totalPrice = listing.pricePerShare.mul(sharesToBuy);
        uint256 feeAmount = totalPrice.mul(marketplaceFeePercentage).div(10000);
        uint256 sellerAmount = totalPrice.sub(feeAmount);

        if (listing.paymentToken == address(0)) {
            // ETH payment
            require(msg.value >= totalPrice, "Insufficient ETH sent");
            if (msg.value > totalPrice) {
                payable(msg.sender).transfer(msg.value.sub(totalPrice));
            }
            payable(listing.seller).transfer(sellerAmount);
            payable(feeRecipient).transfer(feeAmount);
        } else {
            // ERC20 payment
            IERC20 paymentToken = IERC20(listing.paymentToken);
            paymentToken.safeTransferFrom(
                msg.sender,
                listing.seller,
                sellerAmount
            );
            paymentToken.safeTransferFrom(msg.sender, feeRecipient, feeAmount);
        }

        // Transfer shares to buyer
        fnft.sharesOwned[address(this)] = fnft.sharesOwned[address(this)].sub(
            sharesToBuy
        );
        fnft.sharesOwned[msg.sender] = fnft.sharesOwned[msg.sender].add(
            sharesToBuy
        );

        listing.sharesAvailable = listing.sharesAvailable.sub(sharesToBuy);
        if (listing.sharesAvailable == 0) {
            listing.isActive = false;
        }

        emit SharePurchased(tokenId, msg.sender, sharesToBuy, totalPrice);
    }

    /**
     * @dev Cancel a share listing
     * @param tokenId The ID of the fractionalized NFT
     */
    function cancelListing(uint256 tokenId) external {
        Listing storage listing = _listings[tokenId];
        require(listing.isActive, "Listing is not active");
        require(
            listing.seller == msg.sender || msg.sender == owner(),
            "Not authorized"
        );

        FractionalizedNFT storage fnft = _fractionalizedNFTs[tokenId];
        uint256 sharesToReturn = listing.sharesAvailable;

        // Return shares to seller
        fnft.sharesOwned[address(this)] = fnft.sharesOwned[address(this)].sub(
            sharesToReturn
        );
        fnft.sha
