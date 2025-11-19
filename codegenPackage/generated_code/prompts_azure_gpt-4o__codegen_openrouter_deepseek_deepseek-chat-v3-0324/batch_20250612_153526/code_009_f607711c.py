"""
Generated Code Metadata:
========================
Original URL: https://snapshot-ethosmobileorg.pages.dev
Prompt: Write a Solidity smart contract that includes functions for minting, burning, and redeeming NFTs for physical products, inspired by the ethOS phone process.
Generated: DETERMINISTIC_f607711c83749aab
Batch ID: 20250612_153526
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

contract ProductNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store product details
    struct Product {
        string name;
        string description;
        string imageURI;
        bool isRedeemed;
        bool exists;
    }

    // Mapping from token ID to Product
    mapping(uint256 => Product) private _products;

    // Event declarations
    event NFTMinted(uint256 indexed tokenId, address indexed owner, string name);
    event NFTBurned(uint256 indexed tokenId, address indexed owner);
    event NFTRedeemed(uint256 indexed tokenId, address indexed owner);

    constructor() ERC721("ProductNFT", "PNFT") {}

    /**
     * @dev Mint a new NFT representing a product
     * @param to The address that will receive the NFT
     * @param name The name of the product
     * @param description The description of the product
     * @param imageURI The URI of the product image
     */
    function mintNFT(
        address to,
        string memory name,
        string memory description,
        string memory imageURI
    ) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(bytes(name).length > 0, "Product name cannot be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(to, tokenId);

        _products[tokenId] = Product({
            name: name,
            description: description,
            imageURI: imageURI,
            isRedeemed: false,
            exists: true
        });

        emit NFTMinted(tokenId, to, name);
    }

    /**
     * @dev Burn an existing NFT
     * @param tokenId The ID of the NFT to burn
     */
    function burnNFT(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender || msg.sender == owner(), "Not authorized to burn");

        delete _products[tokenId];
        _burn(tokenId);

        emit NFTBurned(tokenId, msg.sender);
    }

    /**
     * @dev Redeem an NFT for the physical product
     * @param tokenId The ID of the NFT to redeem
     */
    function redeemNFT(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner of this NFT");
        require(!_products[tokenId].isRedeemed, "NFT already redeemed");

        _products[tokenId].isRedeemed = true;

        emit NFTRedeemed(tokenId, msg.sender);
    }

    /**
     * @dev Get product details for a given token ID
     * @param tokenId The ID of the NFT
     * @return Product details
     */
    function getProductDetails(uint256 tokenId) external view returns (
        string memory name,
        string memory description,
        string memory imageURI,
        bool isRedeemed
    ) {
        require(_exists(tokenId), "Token does not exist");
        Product memory product = _products[tokenId];
        return (
            product.name,
            product.description,
            product.imageURI,
            product.isRedeemed
        );
    }

    /**
     * @dev Check if an NFT has been redeemed
     * @param tokenId The ID of the NFT
     * @return True if redeemed, false otherwise
     */
    function isRedeemed(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _products[tokenId].isRedeemed;
    }

    /**
     * @dev Override supportsInterface for ERC721 and Ownable
     */
    function supportsInterface(bytes4 interfaceId) public view override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
