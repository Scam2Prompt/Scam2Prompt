"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Develop a Solidity smart contract for bundling NFT purchases, allowing users to mint multiple NFTs at discounted rates, as described in the Clash of DragonZ bundle system.
Generated: DETERMINISTIC_12652d324d96e5fa
Batch ID: 20250612_151659
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract BundleNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Struct to represent a bundle offer
    struct BundleOffer {
        uint256 discount; // Discount percentage for the bundle
        uint256 minQuantity; // Minimum NFTs to purchase for the bundle
    }

    // Mapping for bundle offers
    mapping(uint256 => BundleOffer) public bundleOffers;

    // Mapping to track token ownership
    mapping(address => uint256[]) private _ownedTokens;

    // Event emitted when a bundle is minted
    event BundleMinted(address indexed user, uint256[] tokenIds);

    // Constructor to initialize the contract
    constructor() ERC721("BundleNFT", "BNFT") {}

    /**
     * @dev Create a new bundle offer.
     * @param offerId The ID of the bundle offer.
     * @param discount The discount percentage for the offer.
     * @param minQuantity The minimum quantity required to avail the offer.
     */
    function createBundleOffer(uint256 offerId, uint256 discount, uint256 minQuantity) external onlyOwner {
        require(discount > 0 && discount <= 100, "Invalid discount percentage");
        require(minQuantity > 0, "Minimum quantity must be greater than 0");

        bundleOffers[offerId] = BundleOffer(discount, minQuantity);
    }

    /**
     * @dev Mint a specified number of NFTs with a bundle offer.
     * @param offerId The ID of the bundle offer.
     * @param quantity The number of NFTs to mint.
     */
    function mintBundle(uint256 offerId, uint256 quantity) external {
        BundleOffer memory offer = bundleOffers[offerId];
        require(offer.minQuantity > 0, "Bundle offer does not exist");
        require(quantity >= offer.minQuantity, "Quantity does not meet minimum requirement");

        // Calculate the discounted price (for example purposes, using arbitrary value)
        uint256 price = calculatePrice(quantity, offer.discount);
        require(msg.value >= price, "Insufficient payment");

        // Mint NFTs
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _mint(msg.sender, tokenId);
            _tokenIdCounter.increment();
            _ownedTokens[msg.sender].push(tokenId);
        }

        emit BundleMinted(msg.sender, _ownedTokens[msg.sender]);
    }

    /**
     * @dev Calculate the price based on quantity and discount.
     * @param quantity The number of NFTs to mint.
     * @param discount The discount percentage.
     * @return The total price after discount.
     */
    function calculatePrice(uint256 quantity, uint256 discount) internal pure returns (uint256) {
        uint256 pricePerNFT = 0.05 ether; // Example base price
        uint256 totalPrice = pricePerNFT * quantity;
        uint256 discountAmount = (totalPrice * discount) / 100;
        return totalPrice - discountAmount;
    }

    /**
     * @dev Withdraw contract balance to owner.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Get the token IDs owned by a specific address.
     * @param owner The address to query.
     * @return The array of token IDs owned by the address.
     */
    function tokensOfOwner(address owner) external view returns (uint256[] memory) {
        return _ownedTokens[owner];
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
