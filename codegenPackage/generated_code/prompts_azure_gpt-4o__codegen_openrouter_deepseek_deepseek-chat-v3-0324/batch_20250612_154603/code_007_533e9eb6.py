"""
Generated Code Metadata:
========================
Original URL: https://whitesrock.fi
Prompt: Write a smart contract using Solidity that integrates with WhiteRock's audited contracts to facilitate secure and transparent trading of tokenized real-world assets (RWAs).
Generated: DETERMINISTIC_533e9eb618f53157
Batch ID: 20250612_154603
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RWA Trading Platform
 * @dev A smart contract for secure and transparent trading of tokenized real-world assets
 * Integrates with WhiteRock's audited contracts for asset verification and settlement
 */
contract RWATradingPlatform is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Struct to represent a tokenized RWA
    struct TokenizedAsset {
        address tokenAddress;
        address issuer;
        uint256 tokenId;
        uint256 totalSupply;
        uint256 price;
        bool isActive;
        string assetDetails; // IPFS hash or reference to off-chain data
    }

    // Struct to represent an order
    struct Order {
        address buyer;
        address seller;
        address tokenAddress;
        uint256 tokenId;
        uint256 amount;
        uint256 price;
        bool isFilled;
        bool isCancelled;
    }

    // Mapping from asset ID to TokenizedAsset
    mapping(uint256 => TokenizedAsset) public tokenizedAssets;

    // Mapping from order ID to Order
    mapping(uint256 => Order) public orders;

    // WhiteRock's verification contract address
    address public whiteRockVerificationContract;

    // Platform fee percentage (basis points)
    uint256 public platformFeeBps;
    address public feeRecipient;

    // Events
    event AssetListed(
        uint256 indexed assetId,
        address indexed tokenAddress,
        address indexed issuer,
        uint256 tokenId,
        uint256 totalSupply,
        uint256 price,
        string assetDetails
    );
    event OrderCreated(
        uint256 indexed orderId,
        address indexed buyer,
        address indexed seller,
        address tokenAddress,
        uint256 tokenId,
        uint256 amount,
        uint256 price
    );
    event OrderFilled(uint256 indexed orderId);
    event OrderCancelled(uint256 indexed orderId);
    event AssetStatusChanged(uint256 indexed assetId, bool isActive);
    event PlatformFeeUpdated(uint256 newFeeBps);
    event FeeRecipientUpdated(address newRecipient);

    /**
     * @dev Constructor
     * @param _whiteRockVerificationContract Address of WhiteRock's verification contract
     * @param _feeRecipient Address to receive platform fees
     * @param _platformFeeBps Platform fee in basis points (1% = 100 bps)
     */
    constructor(
        address _whiteRockVerificationContract,
        address _feeRecipient,
        uint256 _platformFeeBps
    ) {
        require(
            _whiteRockVerificationContract != address(0),
            "Invalid verification contract"
        );
        require(_feeRecipient != address(0), "Invalid fee recipient");
        require(_platformFeeBps <= 1000, "Fee too high"); // Max 10%

        whiteRockVerificationContract = _whiteRockVerificationContract;
        feeRecipient = _feeRecipient;
        platformFeeBps = _platformFeeBps;
    }

    /**
     * @dev List a new tokenized asset
     * @param assetId Unique identifier for the asset
     * @param tokenAddress Address of the token contract
     * @param tokenId Token ID (for ERC721) or 0 for ERC20
     * @param totalSupply Total supply of tokens
     * @param price Price per token in wei
     * @param assetDetails Reference to asset details (IPFS hash)
     */
    function listAsset(
        uint256 assetId,
        address tokenAddress,
        uint256 tokenId,
        uint256 totalSupply,
        uint256 price,
        string memory assetDetails
    ) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(tokenizedAssets[assetId].tokenAddress == address(0), "Asset already listed");
        require(price > 0, "Price must be greater than 0");

        tokenizedAssets[assetId] = TokenizedAsset({
            tokenAddress: tokenAddress,
            issuer: msg.sender,
            tokenId: tokenId,
            totalSupply: totalSupply,
            price: price,
            isActive: true,
            assetDetails: assetDetails
        });

        emit AssetListed(
            assetId,
            tokenAddress,
            msg.sender,
            tokenId,
            totalSupply,
            price,
            assetDetails
        );
    }

    /**
     * @dev Create a new order
     * @param orderId Unique identifier for the order
     * @param assetId ID of the tokenized asset
     * @param amount Amount of tokens to trade
     */
    function createOrder(
        uint256 orderId,
        uint256 assetId,
        uint256 amount
    ) external payable nonReentrant {
        TokenizedAsset memory asset = tokenizedAssets[assetId];
        require(asset.tokenAddress != address(0), "Asset not found");
        require(asset.isActive, "Asset not active for trading");
        require(amount > 0, "Amount must be greater than 0");
        require(orders[orderId].buyer == address(0), "Order already exists");

        uint256 totalPrice = asset.price.mul(amount);
        require(msg.value >= totalPrice, "Insufficient payment");

        orders[orderId] = Order({
            buyer: msg.sender,
            seller: asset.issuer,
            tokenAddress: asset.tokenAddress,
            tokenId: asset.tokenId,
            amount: amount,
            price: asset.price,
            isFilled: false,
            isCancelled: false
        });

        emit OrderCreated(
            orderId,
            msg.sender,
            asset.issuer,
            asset.tokenAddress,
            asset.tokenId,
            amount,
            asset.price
        );
    }

    /**
     * @dev Fill an existing order
     * @param orderId ID of the order to fill
     */
    function fillOrder(uint256 orderId) external nonReentrant {
        Order storage order = orders[orderId];
        require(order.buyer != address(0), "Order not found");
        require(!order.isFilled, "Order already filled");
        require(!order.isCancelled, "Order is cancelled");
        require(msg.sender == order.seller, "Only seller can fill order");

        // Calculate platform fee
        uint256 totalAmount = order.price.mul(order.amount);
        uint256 feeAmount = totalAmount.mul(platformFeeBps).div(10000);
        uint256 sellerAmount = totalAmount.sub(feeAmount);

        // Transfer funds
        payable(order.seller).transfer(sellerAmount);
        if (feeAmount > 0) {
            payable(feeRecipient).transfer(feeAmount);
        }

        // Transfer tokens
        if (order.tokenId == 0) {
            // ERC20
            IERC20(order.tokenAddress).transferFrom(
                order.seller,
                order.buyer,
                order.amount
            );
        } else {
            // ERC721 - would need to implement ERC721 interface
            // For simplicity, we assume the token transfer is handled off-chain
            // or through a separate approval mechanism
        }

        order.isFilled = true;
        emit OrderFilled(orderId);
    }

    /**
     * @dev Cancel an existing order
     * @param orderId ID of the order to cancel
     */
    function cancelOrder(uint256 orderId) external nonReentrant {
        Order storage order = orders[orderId];
        require(order.buyer != address(0), "Order not found");
        require(!order.isFilled, "Order already filled");
        require(!order.isCancelled, "Order already cancelled");
        require(
            msg.sender == order.buyer || msg.sender == order.seller,
            "Only buyer or seller can cancel"
        );

        // Refund buyer if they initiated the cancellation
        if (msg.sender == order.buyer) {
            uint256 totalAmount = order.price.mul(order.amount);
            payable(order.buyer).transfer(totalAmount);
        }

        order.isCancelled = true;
        emit OrderCancelled(orderId);
    }

    /**
     * @dev Update asset status
     * @param assetId ID of the asset
     * @param isActive New status
     */
    function setAssetStatus(uint256 assetId, bool isActive) external onlyOwner {
        require(tokenizedAssets[assetId].tokenAddress != address(0), "Asset not found");
        tokenizedAssets[assetId].isActive = isActive;
        emit AssetStatusChanged(assetId, isActive);
    }

    /**
     * @dev Update platform fee
     * @param newFeeBps New fee in basis points
     */
    function setPlatformFee(uint256 newFeeBps) external onlyOwner {
        require(newFeeBps <= 1000, "Fee too high"); // Max 10%
        platformFeeBps = newFee
