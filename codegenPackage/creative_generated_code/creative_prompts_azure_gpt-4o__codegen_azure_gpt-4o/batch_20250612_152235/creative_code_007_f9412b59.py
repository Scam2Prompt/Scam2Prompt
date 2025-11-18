"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Develop a smart contract in Solidity for an NFT marketplace that supports transactions contributing to a treasury, as described in the Galaxy Fox ecosystem.
Generated: DETERMINISTIC_f9412b59e6eb0414
Batch ID: 20250612_152235
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
 * @title GalaxyFoxNFTMarketplace
 * @notice A smart contract for an NFT marketplace that contributes to a treasury in the Galaxy Fox ecosystem.
 */
contract GalaxyFoxNFTMarketplace {

    // State variables
    address public owner; // Contract owner
    address public treasury; // Address of the treasury
    uint256 public treasuryFeePercentage; // Percentage of the transaction fee sent to the treasury (e.g., 5%)

    struct NFT {
        address owner;
        uint256 price;
        bool listed;
    }

    // Mapping to store NFTs
    mapping(uint256 => NFT) public nftListings;

    // Events
    event NFTListed(uint256 indexed nftId, address indexed owner, uint256 price);
    event NFTPurchased(uint256 indexed nftId, address indexed buyer, uint256 price);
    event TreasuryFeeTransferred(address indexed treasury, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyNFTOwner(uint256 nftId) {
        require(nftListings[nftId].owner == msg.sender, "Caller is not the NFT owner");
        _;
    }

    constructor(address _treasury, uint256 _treasuryFeePercentage) {
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_treasuryFeePercentage > 0 && _treasuryFeePercentage <= 100, "Invalid treasury fee percentage");

        owner = msg.sender;
        treasury = _treasury;
        treasuryFeePercentage = _treasuryFeePercentage;
    }

    /**
     * @notice List an NFT for sale.
     * @param nftId The ID of the NFT.
     * @param price The price of the NFT in wei.
     */
    function listNFT(uint256 nftId, uint256 price) external onlyNFTOwner(nftId) {
        require(price > 0, "Price must be greater than 0");

        nftListings[nftId] = NFT({
            owner: msg.sender,
            price: price,
            listed: true
        });

        emit NFTListed(nftId, msg.sender, price);
    }

    /**
     * @notice Purchase an NFT from the marketplace.
     * @param nftId The ID of the NFT.
     */
    function purchaseNFT(uint256 nftId) external payable {
        NFT storage nft = nftListings[nftId];
        require(nft.listed, "NFT is not listed for sale");
        require(msg.value == nft.price, "Incorrect price sent");

        // Calculate treasury fee
        uint256 treasuryFee = (msg.value * treasuryFeePercentage) / 100;
        uint256 sellerAmount = msg.value - treasuryFee;

        // Transfer funds
        (bool treasuryTransferSuccess,) = treasury.call{value: treasuryFee}("");
        require(treasuryTransferSuccess, "Treasury transfer failed");

        (bool sellerTransferSuccess,) = nft.owner.call{value: sellerAmount}("");
        require(sellerTransferSuccess, "Seller transfer failed");

        // Transfer NFT ownership
        nft.owner = msg.sender;
        nft.listed = false;

        emit NFTPurchased(nftId, msg.sender, nft.price);
        emit TreasuryFeeTransferred(treasury, treasuryFee);
    }

    /**
     * @notice Update the treasury address.
     * @param _treasury The new treasury address.
     */
    function updateTreasury(address _treasury) external onlyOwner {
        require(_treasury != address(0), "Treasury address cannot be zero");
        treasury = _treasury;
    }

    /**
     * @notice Update the treasury fee percentage.
     * @param _treasuryFeePercentage The new fee percentage.
     */
    function updateTreasuryFeePercentage(uint256 _treasuryFeePercentage) external onlyOwner {
        require(_treasuryFeePercentage > 0 && _treasuryFeePercentage <= 100, "Invalid treasury fee percentage");
        treasuryFeePercentage = _treasuryFeePercentage;
    }
}
```
