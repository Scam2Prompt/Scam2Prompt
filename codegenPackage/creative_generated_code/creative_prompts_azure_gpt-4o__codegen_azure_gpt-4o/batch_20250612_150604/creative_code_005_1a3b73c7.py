"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Generate a smart contract for a token adoption system where users can adopt digital assets (e.g., penguins) that provide rewards like discounts and event access, all paid in the token.
Generated: DETERMINISTIC_1a3b73c7f29f8c3b
Batch ID: 20250612_150604
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
 * @title TokenAdoption
 * @dev A smart contract for adopting digital assets that provide rewards.
 * Users can adopt assets like penguins using the native ERC20 token.
 * Adopted assets offer features such as discounts and event access.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenAdoption is Ownable {
    // The ERC20 token used for payments
    IERC20 public paymentToken;

    // Struct to represent an adoptable asset
    struct Asset {
        string name;          // Name of the asset (e.g., penguin)
        uint256 price;        // Price in paymentToken to adopt
        bool isAvailable;     // Adoption availability status
    }

    // Mapping to store assets and adoption status
    mapping(uint256 => Asset) public assets;         // Asset ID => Asset details
    mapping(uint256 => address) public adopters;     // Asset ID => Adopter address
    uint256 public totalAssets;                      // Total number of assets

    // Events
    event AssetAdded(uint256 assetId, string name, uint256 price);
    event AssetAdopted(uint256 assetId, address adopter);
    event AssetReleased(uint256 assetId, address adopter);

    /**
     * @dev Constructor initializes the contract with the payment token address.
     * @param _paymentToken Address of the ERC20 token used for payments.
     */
    constructor(IERC20 _paymentToken) {
        require(address(_paymentToken) != address(0), "Invalid token address");
        paymentToken = _paymentToken;
    }

    // ------------------------- Owner Functions -------------------------

    /**
     * @dev Adds a new adoptable asset.
     * @param name Name of the asset (e.g., penguin).
     * @param price Price in tokens required to adopt the asset.
     */
    function addAsset(string memory name, uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");

        assets[totalAssets] = Asset({
            name: name,
            price: price,
            isAvailable: true
        });

        emit AssetAdded(totalAssets, name, price);
        totalAssets++;
    }

    /**
     * @dev Updates the price of an existing asset.
     * @param assetId ID of the asset to update.
     * @param newPrice New price in tokens.
     */
    function updateAssetPrice(uint256 assetId, uint256 newPrice) external onlyOwner {
        require(assetId < totalAssets, "Invalid asset ID");
        require(newPrice > 0, "Price must be greater than zero");

        assets[assetId].price = newPrice;
    }

    /**
     * @dev Toggles the availability status of an asset.
     * @param assetId ID of the asset to update.
     * @param isAvailable New availability status.
     */
    function toggleAssetAvailability(uint256 assetId, bool isAvailable) external onlyOwner {
        require(assetId < totalAssets, "Invalid asset ID");

        assets[assetId].isAvailable = isAvailable;
    }

    // ------------------------- User Functions -------------------------

    /**
     * @dev Adopts an asset by paying the required token price.
     * @param assetId ID of the asset to adopt.
     */
    function adoptAsset(uint256 assetId) external {
        require(assetId < totalAssets, "Invalid asset ID");
        require(assets[assetId].isAvailable, "Asset not available");
        require(adopters[assetId] == address(0), "Asset already adopted");

        Asset memory asset = assets[assetId];

        // Transfer the token payment from the adopter to the contract
        bool success = paymentToken.transferFrom(msg.sender, address(this), asset.price);
        require(success, "Token transfer failed");

        // Record the adoption
        adopters[assetId] = msg.sender;

        emit AssetAdopted(assetId, msg.sender);
    }

    /**
     * @dev Releases an adopted asset by the adopter.
     * @param assetId ID of the asset to release.
     */
    function releaseAsset(uint256 assetId) external {
        require(assetId < totalAssets, "Invalid asset ID");
        require(adopters[assetId] == msg.sender, "Not the adopter of this asset");

        // Clear adoption record
        adopters[assetId] = address(0);

        emit AssetReleased(assetId, msg.sender);
    }

    // ------------------------- Utility Functions -------------------------

    /**
     * @dev Withdraws tokens from the contract to the owner's address.
     * Can be used to collect adoption fees.
     */
    function withdrawTokens() external onlyOwner {
        uint256 contractBalance = paymentToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        bool success = paymentToken.transfer(owner(), contractBalance);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Returns the details of an asset.
     * @param assetId ID of the asset to query.
     */
    function getAssetDetails(uint256 assetId) external view returns (string memory name, uint256 price, bool isAvailable, address adopter) {
        require(assetId < totalAssets, "Invalid asset ID");

        Asset memory asset = assets[assetId];
        return (asset.name, asset.price, asset.isAvailable, adopters[assetId]);
    }
}
```
