"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://therealworldcoin.com
Prompt: Create a Solidity smart contract that enables fractional ownership of real-world assets, inspired by the TRW platform's tokenization model.
Generated: DETERMINISTIC_866ca997101b54d6
Batch ID: 20250612_151624
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FractionalOwnership
 * @dev This contract allows for fractional ownership of real-world assets using ERC20 tokens.
 * Each asset can be tokenized into multiple fractional tokens that represent ownership shares.
 */
contract FractionalOwnership is ERC20Burnable, Pausable, Ownable {
    using SafeMath for uint256;

    // Structure to hold asset details
    struct Asset {
        uint256 totalSupply; // Total supply of fractional tokens for the asset
        uint256 price; // Price of the asset in wei
        string metadata; // Metadata for asset description
        bool isTokenized; // Status of whether the asset is tokenized or not
    }

    // Mapping from asset ID to Asset structure
    mapping(uint256 => Asset) public assets;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(uint256 indexed assetId, uint256 totalSupply, string metadata);

    // Event emitted when tokens are bought
    event TokensPurchased(address indexed buyer, uint256 indexed assetId, uint256 amount);

    // Modifier to check if an asset exists
    modifier assetExists(uint256 assetId) {
        require(assets[assetId].isTokenized, "Asset does not exist or not tokenized");
        _;
    }

    /**
     * @dev Constructor to initialize the ERC20 token with a name and symbol.
     * @param name Name of the token.
     * @param symbol Symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    /**
     * @dev Function to tokenize a new asset
     * @param assetId Unique identifier for the asset
     * @param totalSupply Total number of fractional tokens to be created
     * @param price Price of the asset in wei
     * @param metadata Additional information about the asset
     */
    function tokenizeAsset(uint256 assetId, uint256 totalSupply, uint256 price, string memory metadata) external onlyOwner {
        require(!assets[assetId].isTokenized, "Asset already tokenized");

        // Creating a new asset
        assets[assetId] = Asset({
            totalSupply: totalSupply,
            price: price,
            metadata: metadata,
            isTokenized: true
        });

        // Minting the fractional tokens to the contract's address
        _mint(address(this), totalSupply);

        emit AssetTokenized(assetId, totalSupply, metadata);
    }

    /**
     * @dev Function to purchase tokens representing fractional ownership of an asset
     * @param assetId Unique identifier for the asset
     * @param amount The number of fractional tokens to purchase
     */
    function purchaseTokens(uint256 assetId, uint256 amount) external payable assetExists(assetId) whenNotPaused {
        Asset storage asset = assets[assetId];

        // Calculate the total cost for the requested amount of tokens
        uint256 totalCost = asset.price.mul(amount);
        require(msg.value >= totalCost, "Insufficient funds to purchase tokens");
        
        // Transfer tokens from the contract to the buyer
        _transfer(address(this), msg.sender, amount);

        emit TokensPurchased(msg.sender, assetId, amount);
    }

    /**
     * @dev Function to withdraw Ether from the contract
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available for withdrawal");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to pause the contract
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Function to unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}
```
