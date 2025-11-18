"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Generate a Solidity contract for a decentralized marketplace where users can trade tokenized assets, as described in Ethereum.org's NFT use cases.
Generated: DETERMINISTIC_431891bd4637341d
Batch ID: 20250612_151948
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

// Import OpenZeppelin contracts for secure and efficient implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title Decentralized Marketplace for Tokenized Assets
/// @dev This contract implements a basic marketplace for trading NFT assets.
contract Marketplace is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent an asset
    struct Asset {
        uint256 id;
        string name;
        uint256 price;
        address owner;
        bool isListed;
    }

    // Mapping from asset ID to Asset details
    mapping(uint256 => Asset) public assets;
    // Counter for asset IDs
    Counters.Counter private _assetIdCounter;

    // Event emitted when an asset is listed for sale
    event AssetListed(uint256 indexed assetId, uint256 price);
    // Event emitted when an asset is sold
    event AssetSold(uint256 indexed assetId, address buyer);

    /// @dev Initializes the contract with a name and symbol for the NFTs
    constructor() ERC721("TokenizedAsset", "TKA") {}

    /// @dev Lists an asset for sale on the marketplace
    /// @param name The name of the asset
    /// @param price The price in wei for which the asset is listed
    function listAsset(string memory name, uint256 price) public onlyOwner {
        require(price > 0, "Price must be greater than zero");

        // Increment the asset ID counter and create a new asset
        _assetIdCounter.increment();
        uint256 assetId = _assetIdCounter.current();
        assets[assetId] = Asset(assetId, name, price, msg.sender, true);

        // Mint the NFT for the asset
        _mint(msg.sender, assetId);

        emit AssetListed(assetId, price);
    }

    /// @dev Buys an asset from the marketplace
    /// @param assetId The ID of the asset to buy
    function buyAsset(uint256 assetId) public payable {
        Asset storage asset = assets[assetId];
        
        // Check if the asset is listed for sale and verify the price
        require(asset.isListed, "Asset not listed for sale");
        require(msg.value >= asset.price, "Insufficient funds sent");

        // Transfer ownership of the asset
        asset.owner = msg.sender;
        asset.isListed = false;

        // Transfer funds to the previous owner
        payable(owner()).transfer(asset.price);

        emit AssetSold(assetId, msg.sender);
    }

    /// @dev Allows the owner to withdraw any funds in the contract
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
