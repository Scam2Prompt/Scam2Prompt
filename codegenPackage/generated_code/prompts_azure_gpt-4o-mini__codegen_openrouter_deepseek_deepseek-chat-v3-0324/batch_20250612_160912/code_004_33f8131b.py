"""
Generated Code Metadata:
========================
Original URL: https://ghsttoken.co
Prompt: Create a Solidity contract that allows users to trade Aavegotchis using GHST tokens, referencing the unique features of the Aavegotchi ecosystem mentioned on the GHST website.
Generated: DETERMINISTIC_33f8131b8ee9602c
Batch ID: 20250612_160912
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
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title AavegotchiMarketplace
 * @dev A contract for trading Aavegotchis using GHST tokens, supporting features like:
 * - Trading based on Aavegotchi traits (kinship, experience, etc.)
 * - Escrow-based trades
 * - Listing and delisting Aavegotchis
 * - GHST token payments
 */
contract AavegotchiMarketplace is ReentrancyGuard {
    using Counters for Counters.Counter;

    // Interface for Aavegotchi ERC721 contract
    IERC721 public aavegotchiContract;
    
    // Interface for GHST ERC20 token
    IERC20 public ghstToken;

    // Marketplace fee percentage (1 = 1%)
    uint256 public feePercentage;

    // Address to collect fees
    address public feeRecipient;

    // Listing ID counter
    Counters.Counter private _listingIds;

    // Struct representing an Aavegotchi listing
    struct Listing {
        uint256 listingId;
        uint256 tokenId;
        address seller;
        uint256 price;
        uint256 kinship; // Aavegotchi kinship level
        uint256 experience; // Aavegotchi experience points
        bool active;
    }

    // Mapping from listing ID to Listing
    mapping(uint256 => Listing) public listings;

    // Mapping from token ID to listing ID
    mapping(uint256 => uint256) public tokenToListing;

    // Events
    event Listed(
        uint256 indexed listingId,
        uint256 indexed tokenId,
        address indexed seller,
        uint256 price,
        uint256 kinship,
        uint256 experience
    );
    event Unlisted(uint256 indexed listingId, address indexed seller);
    event Purchased(
        uint256 indexed listingId,
        uint256 indexed tokenId,
        address indexed buyer,
        address seller,
        uint256 price
    );

    /**
     * @dev Constructor
     * @param _aavegotchiContract Address of the Aavegotchi ERC721 contract
     * @param _ghstToken Address of the GHST ERC20 token
     * @param _feePercentage Marketplace fee percentage (1 = 1%)
     * @param _feeRecipient Address to receive marketplace fees
     */
    constructor(
        address _aavegotchiContract,
        address _ghstToken,
        uint256 _feePercentage,
        address _feeRecipient
    ) {
        require(_aavegotchiContract != address(0), "Invalid Aavegotchi contract");
        require(_ghstToken != address(0), "Invalid GHST token");
        require(_feeRecipient != address(0), "Invalid fee recipient");
        require(_feePercentage <= 100, "Fee percentage too high");

        aavegotchiContract = IERC721(_aavegotchiContract);
        ghstToken = IERC20(_ghstToken);
        feePercentage = _feePercentage;
        feeRecipient = _feeRecipient;
    }

    /**
     * @dev List an Aavegotchi for sale
     * @param _tokenId ID of the Aavegotchi to list
     * @param _price Price in GHST tokens
     * @param _kinship Current kinship level of the Aavegotchi
     * @param _experience Current experience points of the Aavegotchi
     */
    function listAavegotchi(
        uint256 _tokenId,
        uint256 _price,
        uint256 _kinship,
        uint256 _experience
    ) external nonReentrant {
        require(aavegotchiContract.ownerOf(_tokenId) == msg.sender, "Not owner");
        require(tokenToListing[_tokenId] == 0, "Already listed");
        require(_price > 0, "Price must be > 0");

        // Transfer Aavegotchi to this contract (escrow)
        aavegotchiContract.transferFrom(msg.sender, address(this), _tokenId);

        // Create new listing
        _listingIds.increment();
        uint256 newListingId = _listingIds.current();

        listings[newListingId] = Listing({
            listingId: newListingId,
            tokenId: _tokenId,
            seller: msg.sender,
            price: _price,
            kinship: _kinship,
            experience: _experience,
            active: true
        });

        tokenToListing[_tokenId] = newListingId;

        emit Listed(newListingId, _tokenId, msg.sender, _price, _kinship, _experience);
    }

    /**
     * @dev Unlist an Aavegotchi
     * @param _listingId ID of the listing to remove
     */
    function unlistAavegotchi(uint256 _listingId) external nonReentrant {
        Listing storage listing = listings[_listingId];
        require(listing.active, "Listing not active");
        require(listing.seller == msg.sender, "Not seller");

        // Return Aavegotchi to seller
        aavegotchiContract.transferFrom(address(this), msg.sender, listing.tokenId);

        // Clean up storage
        delete tokenToListing[listing.tokenId];
        listing.active = false;

        emit Unlisted(_listingId, msg.sender);
    }

    /**
     * @dev Purchase an Aavegotchi
     * @param _listingId ID of the listing to purchase
     */
    function purchaseAavegotchi(uint256 _listingId) external nonReentrant {
        Listing storage listing = listings[_listingId];
        require(listing.active, "Listing not active");
        require(listing.seller != msg.sender, "Cannot buy your own listing");

        // Calculate fees and net amount
        uint256 feeAmount = (listing.price * feePercentage) / 100;
        uint256 netAmount = listing.price - feeAmount;

        // Transfer GHST tokens
        require(
            ghstToken.transferFrom(msg.sender, feeRecipient, feeAmount),
            "Fee transfer failed"
        );
        require(
            ghstToken.transferFrom(msg.sender, listing.seller, netAmount),
            "Payment transfer failed"
        );

        // Transfer Aavegotchi to buyer
        aavegotchiContract.transferFrom(address(this), msg.sender, listing.tokenId);

        // Clean up storage
        delete tokenToListing[listing.tokenId];
        listing.active = false;

        emit Purchased(
            _listingId,
            listing.tokenId,
            msg.sender,
            listing.seller,
            listing.price
        );
    }

    /**
     * @dev Get listing details by token ID
     * @param _tokenId ID of the Aavegotchi
     * @return Listing details if exists, otherwise empty listing
     */
    function getListingByTokenId(uint256 _tokenId) external view returns (Listing memory) {
        uint256 listingId = tokenToListing[_tokenId];
        if (listingId == 0) {
            return Listing(0, 0, address(0), 0, 0, 0, false);
        }
        return listings[listingId];
    }

    /**
     * @dev Update marketplace fee percentage
     * @param _newFeePercentage New fee percentage (1 = 1%)
     */
    function updateFeePercentage(uint256 _newFeePercentage) external {
        require(msg.sender == feeRecipient, "Only fee recipient");
        require(_newFeePercentage <= 100, "Fee percentage too high");
        feePercentage = _newFeePercentage;
    }

    /**
     * @dev Update fee recipient address
     * @param _newFeeRecipient New fee recipient address
     */
    function updateFeeRecipient(address _newFeeRecipient) external {
        require(msg.sender == feeRecipient, "Only fee recipient");
        require(_newFeeRecipient != address(0), "Invalid address");
        feeRecipient = _newFeeRecipient;
    }
}
```
