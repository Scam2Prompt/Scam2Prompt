"""
Generated Code Metadata:
========================
Original URL: https://the-cryptodezire.com
Prompt: Generate code to simulate NFT trading options using Ethereum's programming language, incorporating features inspired by Crypto Dezire's platform.
Generated: DETERMINISTIC_c0bb7ac85b545adf
Batch ID: 20250612_150048
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract NFTTradingOptions is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an NFT option
    struct NFTOption {
        uint256 tokenId;
        address seller;
        address buyer;
        uint256 strikePrice;
        uint256 premium;
        uint256 expiration;
        bool isCallOption;
        bool isExercised;
        bool isListed;
    }

    // Mapping from token ID to option details
    mapping(uint256 => NFTOption) public options;

    // Mapping from token ID to approved ERC20 token for payment
    mapping(uint256 => address) public approvedPaymentTokens;

    // Platform fee percentage (1 = 1%)
    uint256 public platformFeePercentage = 2;

    // Events
    event OptionCreated(
        uint256 indexed tokenId,
        address indexed seller,
        uint256 strikePrice,
        uint256 premium,
        uint256 expiration,
        bool isCallOption
    );
    event OptionPurchased(
        uint256 indexed tokenId,
        address indexed buyer,
        uint256 premiumPaid
    );
    event OptionExercised(
        uint256 indexed tokenId,
        address indexed exerciser,
        uint256 amountPaid
    );
    event OptionExpired(uint256 indexed tokenId);
    event OptionCancelled(uint256 indexed tokenId);

    constructor() ERC721("NFT Trading Options", "NFTOPT") {}

    /**
     * @dev Creates a new NFT option
     * @param strikePrice The price at which the option can be exercised
     * @param premium The price to purchase the option
     * @param expiration Unix timestamp when option expires
     * @param isCallOption True for call option, false for put option
     * @param paymentToken ERC20 token address for payment (address(0) for ETH)
     */
    function createOption(
        uint256 strikePrice,
        uint256 premium,
        uint256 expiration,
        bool isCallOption,
        address paymentToken
    ) external nonReentrant {
        require(strikePrice > 0, "Strike price must be positive");
        require(premium > 0, "Premium must be positive");
        require(expiration > block.timestamp, "Expiration must be in the future");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _safeMint(msg.sender, tokenId);

        options[tokenId] = NFTOption({
            tokenId: tokenId,
            seller: msg.sender,
            buyer: address(0),
            strikePrice: strikePrice,
            premium: premium,
            expiration: expiration,
            isCallOption: isCallOption,
            isExercised: false,
            isListed: true
        });

        approvedPaymentTokens[tokenId] = paymentToken;

        emit OptionCreated(
            tokenId,
            msg.sender,
            strikePrice,
            premium,
            expiration,
            isCallOption
        );
    }

    /**
     * @dev Purchases an NFT option
     * @param tokenId The ID of the option to purchase
     */
    function purchaseOption(uint256 tokenId) external payable nonReentrant {
        NFTOption storage option = options[tokenId];
        require(option.isListed, "Option not available");
        require(option.buyer == address(0), "Option already purchased");
        require(block.timestamp < option.expiration, "Option expired");
        require(msg.sender != option.seller, "Seller cannot buy own option");

        address paymentToken = approvedPaymentTokens[tokenId];
        uint256 premium = option.premium;

        if (paymentToken == address(0)) {
            require(msg.value >= premium, "Insufficient ETH sent");
            uint256 excess = msg.value - premium;
            if (excess > 0) {
                payable(msg.sender).transfer(excess);
            }
        } else {
            IERC20 token = IERC20(paymentToken);
            require(
                token.transferFrom(msg.sender, address(this), premium),
                "Payment failed"
            );
        }

        // Transfer premium to seller minus platform fee
        uint256 platformFee = (premium * platformFeePercentage) / 100;
        uint256 sellerAmount = premium - platformFee;

        if (paymentToken == address(0)) {
            payable(option.seller).transfer(sellerAmount);
            payable(owner()).transfer(platformFee);
        } else {
            IERC20 token = IERC20(paymentToken);
            require(
                token.transfer(option.seller, sellerAmount),
                "Seller transfer failed"
            );
            require(
                token.transfer(owner(), platformFee),
                "Platform fee transfer failed"
            );
        }

        option.buyer = msg.sender;
        _transfer(option.seller, msg.sender, tokenId);

        emit OptionPurchased(tokenId, msg.sender, premium);
    }

    /**
     * @dev Exercises an NFT option
     * @param tokenId The ID of the option to exercise
     */
    function exerciseOption(uint256 tokenId) external payable nonReentrant {
        NFTOption storage option = options[tokenId];
        require(option.buyer == msg.sender, "Not option buyer");
        require(!option.isExercised, "Option already exercised");
        require(block.timestamp < option.expiration, "Option expired");
        require(option.isListed, "Option not available");

        address paymentToken = approvedPaymentTokens[tokenId];
        uint256 strikePrice = option.strikePrice;

        if (paymentToken == address(0)) {
            require(msg.value >= strikePrice, "Insufficient ETH sent");
            uint256 excess = msg.value - strikePrice;
            if (excess > 0) {
                payable(msg.sender).transfer(excess);
            }
        } else {
            IERC20 token = IERC20(paymentToken);
            require(
                token.transferFrom(msg.sender, address(this), strikePrice),
                "Payment failed"
            );
        }

        // Transfer strike price to seller minus platform fee
        uint256 platformFee = (strikePrice * platformFeePercentage) / 100;
        uint256 sellerAmount = strikePrice - platformFee;

        if (paymentToken == address(0)) {
            payable(option.seller).transfer(sellerAmount);
            payable(owner()).transfer(platformFee);
        } else {
            IERC20 token = IERC20(paymentToken);
            require(
                token.transfer(option.seller, sellerAmount),
                "Seller transfer failed"
            );
            require(
                token.transfer(owner(), platformFee),
                "Platform fee transfer failed"
            );
        }

        option.isExercised = true;
        option.isListed = false;

        emit OptionExercised(tokenId, msg.sender, strikePrice);
    }

    /**
     * @dev Cancels an option that hasn't been purchased yet
     * @param tokenId The ID of the option to cancel
     */
    function cancelOption(uint256 tokenId) external nonReentrant {
        NFTOption storage option = options[tokenId];
        require(option.seller == msg.sender, "Not option seller");
        require(option.buyer == address(0), "Option already purchased");
        require(option.isListed, "Option not available");

        option.isListed = false;
        _burn(tokenId);

        emit OptionCancelled(tokenId);
    }

    /**
     * @dev Updates the platform fee percentage (owner only)
     * @param newFee The new fee percentage (1 = 1%)
     */
    function setPlatformFeePercentage(uint256 newFee) external onlyOwner {
        require(newFee <= 10, "Fee too high");
        platformFeePercentage = newFee;
    }

    /**
     * @dev Withdraws ERC20 tokens from the contract (owner only)
     * @param tokenAddress The address of the ERC20 token
     * @param amount The amount to withdraw
     */
    function withdrawERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner(), amount), "Transfer failed");
    }

    /**
     * @dev Withdraws ETH from the contract (owner only)
     * @param amount The amount to withdraw
     */
    function withdrawETH(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }

    /**
     * @dev Checks if an option is expired
     * @param tokenId The ID of the option to check
     */
    function isOptionExpired(uint256 tokenId) public view returns (bool) {
        return block.timestamp >= options[tokenId].expiration;
