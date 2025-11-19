"""
Generated Code Metadata:
========================
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Generate a Solidity contract for a decentralized marketplace where users can trade tokenized assets, as described in Ethereum.org's NFT use cases.
Generated: DETERMINISTIC_431891bd4637341d
Batch ID: 20250612_151948
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title Decentralized Marketplace for Tokenized Assets
// @notice This contract allows users to mint, buy, and sell tokenized assets (NFTs).
contract Marketplace is ERC721, ERC721URIStorage, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to represent an asset listing
    struct Asset {
        address owner;
        uint256 price;
        bool isListed;
    }

    // Mapping from token ID to asset details
    mapping(uint256 => Asset) private _assets;

    // Event emitted when an asset is listed for sale
    event AssetListed(uint256 indexed tokenId, uint256 price);

    // Event emitted when an asset is sold
    event AssetSold(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to initialize the ERC721 token
    constructor() ERC721("TokenizedAsset", "TKA") {}

    // @notice Mint a new token and list it for sale
    // @param tokenURI The metadata URI for the token
    // @param price The sale price of the token
    function mintAndList(string memory tokenURI, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        _assets[tokenId] = Asset({
            owner: msg.sender,
            price: price,
            isListed: true
        });

        _tokenIdCounter.increment();
        emit AssetListed(tokenId, price);
    }

    // @notice Buy a listed asset
    // @param tokenId The ID of the token to buy
    function buyAsset(uint256 tokenId) external payable {
        Asset storage asset = _assets[tokenId];

        require(asset.isListed, "Asset is not listed for sale");
        require(msg.value >= asset.price, "Insufficient funds sent");

        // Transfer ownership of the asset
        _transfer(asset.owner, msg.sender, tokenId);
        asset.owner = msg.sender;
        asset.isListed = false;

        // Transfer funds to the previous owner
        payable(asset.owner).transfer(asset.price);

        emit AssetSold(tokenId, msg.sender, asset.price);
    }

    // @notice List an existing asset for sale
    // @param tokenId The ID of the token to list
    // @param price The sale price of the token
    function listAsset(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this asset");
        require(price > 0, "Price must be greater than zero");

        _assets[tokenId] = Asset({
            owner: msg.sender,
            price: price,
            isListed: true
        });

        emit AssetListed(tokenId, price);
    }

    // @notice Unlist an asset from sale
    // @param tokenId The ID of the token to unlist
    function unlistAsset(uint256 tokenId) external {
        Asset storage asset = _assets[tokenId];

        require(asset.owner == msg.sender, "You do not own this asset");
        require(asset.isListed, "Asset is not listed");

        asset.isListed = false;
    }

    // @notice Get asset details by token ID
    // @param tokenId The ID of the token
    // @return owner The owner of the asset
    // @return price The price of the asset
    // @return isListed Whether the asset is listed for sale
    function getAssetDetails(uint256 tokenId) external view returns (address owner, uint256 price, bool isListed) {
        Asset storage asset = _assets[tokenId];
        return (asset.owner, asset.price, asset.isListed);
    }
}
```
