"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panelresolver-dapp.pages.dev
Prompt: Provide an example of how to create and manage NFTs, ensuring smooth functionality in the NFT marketplace, as described on the Resolver DAPP platform.
Generated: DETERMINISTIC_50a1c9764b358b83
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for creating and managing NFTs in an NFT marketplace on a platform similar to Resolver DAPP. The code uses Solidity, which is typically used for developing Ethereum smart contracts. The contract includes minting, transferring, and listing NFTs for sale with proper error handling.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFTMarketplace
 * @dev A smart contract for creating, managing, and trading NFTs in a marketplace.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTMarketplace is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIds;

    // Structure to hold NFT sale details
    struct NFTSale {
        uint256 price;
        address seller;
        bool isListed;
    }

    // Mapping token ID to NFTSale details
    mapping(uint256 => NFTSale) private _nftSales;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 tokenId, address owner);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 tokenId, uint256 price, address seller);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 tokenId, uint256 price, address buyer);

    /**
     * @dev Constructor that initializes the NFT contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT and assign it to the caller.
     * @param tokenURI Metadata URI for the NFT.
     */
    function mintNFT(string memory tokenURI) external {
        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        // Mint the NFT to the caller
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        emit NFTMinted(newTokenId, msg.sender);
    }

    /**
     * @dev List an NFT for sale on the marketplace.
     * @param tokenId ID of the NFT to list for sale.
     * @param price Sale price of the NFT in wei.
     */
    function listNFT(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "NFTMarketplace: Caller is not the owner");
        require(price > 0, "NFTMarketplace: Price must be greater than zero");

        _nftSales[tokenId] = NFTSale(price, msg.sender, true);

        emit NFTListed(tokenId, price, msg.sender);
    }

    /**
     * @dev Buy a listed NFT from the marketplace.
     * @param tokenId ID of the NFT to purchase.
     */
    function buyNFT(uint256 tokenId) external payable {
        NFTSale memory sale = _nftSales[tokenId];

        require(sale.isListed, "NFTMarketplace: NFT is not listed for sale");
        require(msg.value == sale.price, "NFTMarketplace: Incorrect price");

        // Transfer the payment to the seller
        payable(sale.seller).transfer(msg.value);

        // Transfer the NFT to the buyer
        _transfer(sale.seller, msg.sender, tokenId);

        // Remove the NFT from the sale listings
        delete _nftSales[tokenId];

        emit NFTSold(tokenId, sale.price, msg.sender);
    }

    /**
     * @dev Fetch sale details of an NFT.
     * @param tokenId ID of the NFT.
     * @return price Price of the NFT.
     * @return seller Seller of the NFT.
     * @return isListed Whether the NFT is listed for sale.
     */
    function getNFTSaleDetails(uint256 tokenId)
        external
        view
        returns (uint256 price, address seller, bool isListed)
    {
        NFTSale memory sale = _nftSales[tokenId];
        return (sale.price, sale.seller, sale.isListed);
    }

    /**
     * @dev Override function to include token URI management.
     * @param tokenId ID of the NFT.
     * @return URI Metadata URI of the NFT.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "NFTMarketplace: URI query for nonexistent token");
        return super.tokenURI(tokenId);
    }
}
```

This code uses OpenZeppelin libraries for ERC721 functionality and access control (`Ownable`). Make sure to install OpenZeppelin when deploying the contract.
