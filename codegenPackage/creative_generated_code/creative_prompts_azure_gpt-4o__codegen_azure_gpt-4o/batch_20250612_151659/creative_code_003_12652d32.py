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

/**
 * @title NFTBundleMint
 * @dev Smart contract for bundling and minting NFTs at discounted rates.
 */
contract NFTBundleMint {
    // Event emitted when a bundle is purchased
    event BundlePurchased(address indexed buyer, uint256 bundleId, uint256 amountPaid);

    // Address of the NFT contract
    address public nftContract;

    // Owner of the contract
    address public owner;

    // Struct to define a bundle
    struct Bundle {
        uint256 price; // Discounted price for the bundle
        uint256 quantity; // Number of NFTs in the bundle
    }

    // Mapping to store bundle details (bundleId => Bundle)
    mapping(uint256 => Bundle) public bundles;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the NFT contract address and initialize the owner.
     * @param _nftContract Address of the NFT contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
        owner = msg.sender;
    }

    /**
     * @dev Function to add or update a bundle.
     * @param bundleId Unique identifier for the bundle.
     * @param price Discounted price for the bundle.
     * @param quantity Number of NFTs in the bundle.
     */
    function setBundle(uint256 bundleId, uint256 price, uint256 quantity) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        require(quantity > 0, "Quantity must be greater than zero");

        bundles[bundleId] = Bundle(price, quantity);
    }

    /**
     * @dev Function to purchase a bundle and mint the NFTs.
     * @param bundleId The ID of the bundle to purchase.
     */
    function purchaseBundle(uint256 bundleId) external payable {
        Bundle memory bundle = bundles[bundleId];

        // Validate the bundle and payment
        require(bundle.quantity > 0, "Bundle does not exist");
        require(msg.value == bundle.price, "Incorrect payment amount");

        // Mint NFTs for the buyer
        for (uint256 i = 0; i < bundle.quantity; i++) {
            (bool success, ) = nftContract.call(
                abi.encodeWithSignature("mint(address)", msg.sender)
            );
            require(success, "NFT minting failed");
        }

        emit BundlePurchased(msg.sender, bundleId, msg.value);
    }

    /**
     * @dev Function to withdraw contract balance (only owner).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
