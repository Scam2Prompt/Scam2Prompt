"""
Generated Code Metadata:
========================
Original URL: https://ed-boxes.web.app
Prompt: Design a smart contract on the Solana blockchain to manage NFT minting and trading with dynamic royalties, inspired by Magic Eden's Open Creator Protocol.
Generated: DETERMINISTIC_49eaadf86a572fc2
Batch ID: 20250622_211115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DynamicRoyaltyNFT
 * @dev NFT contract with dynamic royalties and trading capabilities
 * Inspired by Magic Eden's Open Creator Protocol
 */
contract DynamicRoyaltyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    struct RoyaltyInfo {
        address recipient;
        uint24 percentage; // Basis points (10000 = 100%)
    }

    // Mapping from token ID to royalty info
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Platform fee recipient and percentage
    address private _platformFeeRecipient;
    uint24 private _platformFeePercentage;

    // Events
    event Minted(address indexed to, uint256 indexed tokenId, RoyaltyInfo royalty);
    event RoyaltyUpdated(uint256 indexed tokenId, RoyaltyInfo royalty);
    event PlatformFeeUpdated(address recipient, uint24 percentage);
    event Traded(
        uint256 indexed tokenId,
        address indexed from,
        address indexed to,
        uint256 price,
        uint256 royaltyAmount,
        uint256 platformFeeAmount
    );

    /**
     * @dev Initializes the contract
     * @param name_ NFT name
     * @param symbol_ NFT symbol
     * @param baseTokenURI_ Base URI for token metadata
     * @param platformFeeRecipient_ Address to receive platform fees
     * @param platformFeePercentage_ Platform fee percentage in basis points
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_,
        address platformFeeRecipient_,
        uint24 platformFeePercentage_
    ) ERC721(name_, symbol_) {
        require(platformFeePercentage_ <= 10000, "Fee cannot exceed 100%");
        _baseTokenURI = baseTokenURI_;
        _platformFeeRecipient = platformFeeRecipient_;
        _platformFeePercentage = platformFeePercentage_;
    }

    /**
     * @dev Mints a new NFT with specified royalty
     * @param to Address to mint the NFT to
     * @param royaltyRecipient Address to receive royalties
     * @param royaltyPercentage Royalty percentage in basis points
     */
    function mint(
        address to,
        address royaltyRecipient,
        uint24 royaltyPercentage
    ) external onlyOwner {
        require(royaltyPercentage <= 10000, "Royalty cannot exceed 100%");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _royalties[tokenId] = RoyaltyInfo(royaltyRecipient, royaltyPercentage);
        _safeMint(to, tokenId);

        emit Minted(to, tokenId, _royalties[tokenId]);
    }

    /**
     * @dev Updates royalty information for a token
     * @param tokenId ID of the token
     * @param royaltyRecipient New royalty recipient
     * @param royaltyPercentage New royalty percentage
     */
    function updateRoyalty(
        uint256 tokenId,
        address royaltyRecipient,
        uint24 royaltyPercentage
    ) external {
        require(_exists(tokenId), "Nonexistent token");
        require(
            _isApprovedOrOwner(_msgSender(), tokenId) || owner() == _msgSender(),
            "Not approved or owner"
        );
        require(royaltyPercentage <= 10000, "Royalty cannot exceed 100%");

        _royalties[tokenId] = RoyaltyInfo(royaltyRecipient, royaltyPercentage);
        emit RoyaltyUpdated(tokenId, _royalties[tokenId]);
    }

    /**
     * @dev Updates platform fee information
     * @param recipient New platform fee recipient
     * @param percentage New platform fee percentage
     */
    function updatePlatformFee(address recipient, uint24 percentage) external onlyOwner {
        require(percentage <= 10000, "Fee cannot exceed 100%");
        _platformFeeRecipient = recipient;
        _platformFeePercentage = percentage;
        emit PlatformFeeUpdated(recipient, percentage);
    }

    /**
     * @dev Executes a trade between two parties
     * @param tokenId ID of the token being traded
     * @param from Seller address
     * @param to Buyer address
     * @param price Sale price in wei
     */
    function trade(
        uint256 tokenId,
        address from,
        address to,
        uint256 price
    ) external payable {
        require(_exists(tokenId), "Nonexistent token");
        require(ownerOf(tokenId) == from, "Seller not owner");
        require(msg.value >= price, "Insufficient payment");

        RoyaltyInfo memory royalty = _royalties[tokenId];
        uint256 royaltyAmount = price.mul(royalty.percentage).div(10000);
        uint256 platformFeeAmount = price.mul(_platformFeePercentage).div(10000);
        uint256 sellerAmount = price.sub(royaltyAmount).sub(platformFeeAmount);

        // Transfer token
        _transfer(from, to, tokenId);

        // Distribute funds
        payable(from).transfer(sellerAmount);
        payable(royalty.recipient).transfer(royaltyAmount);
        payable(_platformFeeRecipient).transfer(platformFeeAmount);

        emit Traded(tokenId, from, to, price, royaltyAmount, platformFeeAmount);
    }

    /**
     * @dev Returns the royalty information for a token
     * @param tokenId ID of the token
     * @return recipient Royalty recipient address
     * @return percentage Royalty percentage in basis points
     */
    function getRoyalty(uint256 tokenId) external view returns (address recipient, uint256 percentage) {
        require(_exists(tokenId), "Nonexistent token");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.percentage);
    }

    /**
     * @dev Returns the platform fee information
     * @return recipient Platform fee recipient address
     * @return percentage Platform fee percentage in basis points
     */
    function getPlatformFee() external view returns (address recipient, uint256 percentage) {
        return (_platformFeeRecipient, _platformFeePercentage);
    }

    /**
     * @dev Base URI for computing tokenURI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Updates base URI for token metadata
     * @param baseTokenURI New base URI
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev See {IERC165-supportsInterface}
     */
    function supportsInterface(bytes4 interfaceId) public view override returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
