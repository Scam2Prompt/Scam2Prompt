"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Create a smart contract in Solidity to manage NFT sales on the Artyfact marketplace, ensuring 50% of profits are allocated to the prize pool for monthly leaderboard rewards.
Generated: DETERMINISTIC_a07a415b8a80ddb7
Batch ID: 20250612_152441
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

/// @title Artyfact NFT Marketplace
/// @notice This contract manages NFT sales and allocates 50% of profits to a prize pool for monthly leaderboard rewards.
contract ArtyfactMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Struct to represent an NFT
    struct NFT {
        uint256 id;
        string uri;
        address creator;
        uint256 price;
        bool isForSale;
    }

    // State variables
    Counters.Counter private _nftIdCounter; // Counter for NFT IDs
    mapping(uint256 => NFT) public nfts; // Mapping from NFT ID to NFT details
    uint256 public prizePool; // Total amount in the prize pool
    uint256 public totalSales; // Total sales amount for profit calculation

    // Events
    event NFTCreated(uint256 indexed id, string uri, address indexed creator, uint256 price);
    event NFTSold(uint256 indexed id, address indexed buyer, uint256 price);
    event PrizePoolUpdated(uint256 newPrizePool);

    /// @dev Constructor to initialize the contract with a name and symbol
    constructor() ERC721("ArtyfactNFT", "ARTY") {}

    /// @notice Create a new NFT
    /// @param _uri The URI of the NFT metadata
    /// @param _price The sale price of the NFT
    function createNFT(string memory _uri, uint256 _price) external onlyOwner {
        require(_price > 0, "Price must be greater than zero");

        _nftIdCounter.increment();
        uint256 newNftId = _nftIdCounter.current();

        nfts[newNftId] = NFT({
            id: newNftId,
            uri: _uri,
            creator: msg.sender,
            price: _price,
            isForSale: true
        });

        emit NFTCreated(newNftId, _uri, msg.sender, _price);
    }

    /// @notice Buy an NFT
    /// @param _nftId The ID of the NFT to buy
    function buyNFT(uint256 _nftId) external payable {
        NFT storage nft = nfts[_nftId];
        require(nft.isForSale, "NFT is not for sale");
        require(msg.value >= nft.price, "Insufficient funds sent");

        // Calculate profit and update prize pool
        uint256 profit = msg.value;
        uint256 prizeContribution = profit / 2; // 50% to prize pool
        prizePool += prizeContribution;
        totalSales += profit;

        // Transfer the NFT to the buyer
        _safeMint(msg.sender, nft.id);
        nft.isForSale = false;

        // Transfer funds to the creator
        payable(nft.creator).transfer(profit - prizeContribution);

        emit NFTSold(_nftId, msg.sender, nft.price);
        emit PrizePoolUpdated(prizePool);
    }

    /// @notice Withdraw funds from the prize pool (only owner)
    /// @param _amount The amount to withdraw
    function withdrawFromPrizePool(uint256 _amount) external onlyOwner {
        require(_amount <= prizePool, "Insufficient prize pool balance");
        prizePool -= _amount;
        payable(msg.sender).transfer(_amount);
    }

    /// @notice Get the details of an NFT
    /// @param _nftId The ID of the NFT
    /// @return The NFT details
    function getNFTDetails(uint256 _nftId) external view returns (NFT memory) {
        return nfts[_nftId];
    }

    /// @notice Get the current prize pool balance
    /// @return The current prize pool balance
    function getPrizePool() external view returns (uint256) {
        return prizePool;
    }
}
```
