"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venom-dh8.pages.dev
Prompt: Generate code to implement a VEP-1155 tokenized asset project on the Venom blockchain, including functionality for trading on Oasis.Gallery.
Generated: DETERMINISTIC_594eb926e8db2de5
Batch ID: 20250612_153401
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
 * @title VEP-1155 Tokenized Asset Contract for Venom Blockchain
 * @dev Implements VEP-1155 standard with trading functionality on Oasis.Gallery.
 */
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract TokenizedAsset is ERC1155, Ownable, Pausable {
    // Mapping to store asset metadata URLs
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when an asset is listed for sale
    event AssetListed(uint256 indexed tokenId, address indexed seller, uint256 price);

    // Event emitted when an asset is purchased
    event AssetPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Struct to store asset sale data
    struct AssetSale {
        address seller;
        uint256 price;
    }

    // Mapping to store assets listed for sale
    mapping(uint256 => AssetSale) public assetsForSale;

    constructor(string memory baseURI) ERC1155(baseURI) {}

    /**
     * @dev Creates a new tokenized asset.
     * @param tokenId Unique ID of the asset.
     * @param amount Amount of tokens to mint.
     * @param metadataURI URI pointing to the asset metadata.
     */
    function createAsset(
        uint256 tokenId,
        uint256 amount,
        string memory metadataURI
    ) external onlyOwner {
        _mint(msg.sender, tokenId, amount, "");
        _tokenURIs[tokenId] = metadataURI;
    }

    /**
     * @dev Sets the URI for a specific token.
     * @param tokenId Unique ID of the asset.
     * @param metadataURI URI pointing to the asset metadata.
     */
    function setTokenURI(uint256 tokenId, string memory metadataURI) external onlyOwner {
        _tokenURIs[tokenId] = metadataURI;
    }

    /**
     * @dev Overrides the URI function from ERC1155 to fetch token-specific URIs.
     * @param tokenId Unique ID of the asset.
     */
    function uri(uint256 tokenId) public view override returns (string memory) {
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Allows an owner of the asset to list it for sale.
     * @param tokenId Unique ID of the asset.
     * @param price Sale price in Wei.
     */
    function listAssetForSale(uint256 tokenId, uint256 price) external whenNotPaused {
        require(balanceOf(msg.sender, tokenId) > 0, "You don't own this asset");
        require(price > 0, "Price must be greater than zero");

        assetsForSale[tokenId] = AssetSale(msg.sender, price);
        emit AssetListed(tokenId, msg.sender, price);
    }

    /**
     * @dev Allows a buyer to purchase an asset listed for sale.
     * @param tokenId Unique ID of the asset.
     */
    function purchaseAsset(uint256 tokenId) external payable whenNotPaused {
        AssetSale memory sale = assetsForSale[tokenId];
        require(sale.price > 0, "Asset not listed for sale");
        require(msg.value == sale.price, "Incorrect payment amount");

        // Transfer payment to seller
        payable(sale.seller).transfer(msg.value);

        // Transfer asset to buyer
        safeTransferFrom(sale.seller, msg.sender, tokenId, 1, "");

        // Clear asset from sale listings
        delete assetsForSale[tokenId];

        emit AssetPurchased(tokenId, msg.sender, sale.price);
    }

    /**
     * @dev Pauses trading and asset listing.
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses trading and asset listing.
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}
```
