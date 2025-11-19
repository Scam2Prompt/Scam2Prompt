"""
Generated Code Metadata:
========================
Original URL: https://cyberlamas.pages.dev
Prompt: Generate a smart contract code for issuing and trading NFTs on a blockchain platform, as mentioned in Phase 2 of Cyber Lama AI's roadmap.
Generated: DETERMINISTIC_58e4996bb57cb9b2
Batch ID: 20250622_211009
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

/**
 * @title CyberLamaNFT
 * @dev A smart contract for issuing and trading NFTs on the Ethereum blockchain.
 * Implements ERC721 standard for NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CyberLamaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to store token prices for trading
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is purchased
    event NFTPurchased(address indexed buyer, uint256 indexed tokenId, uint256 price);

    /**
     * @dev Constructor to initialize the NFT contract with a name and symbol.
     */
    constructor() ERC721("CyberLamaNFT", "CLNFT") {}

    /**
     * @dev Mint a new NFT to the specified address.
     * @param to Address to receive the minted NFT.
     */
    function mintNFT(address to) external onlyOwner {
        // Increment the token ID counter
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Mint the NFT
        _safeMint(to, tokenId);

        // Emit the minting event
        emit NFTMinted(to, tokenId);
    }

    /**
     * @dev List an NFT for sale by setting its price.
     * @param tokenId ID of the NFT to list for sale.
     * @param price Sale price of the NFT in wei.
     */
    function listNFTForSale(uint256 tokenId, uint256 price) external {
        // Ensure the caller is the owner of the NFT
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Ensure the price is greater than zero
        require(price > 0, "Price must be greater than zero");

        // Set the price for the NFT
        _tokenPrices[tokenId] = price;

        // Emit the listing event
        emit NFTListed(tokenId, price);
    }

    /**
     * @dev Purchase an NFT listed for sale.
     * @param tokenId ID of the NFT to purchase.
     */
    function purchaseNFT(uint256 tokenId) external payable {
        // Ensure the NFT is listed for sale
        uint256 price = _tokenPrices[tokenId];
        require(price > 0, "NFT is not listed for sale");

        // Ensure the buyer has sent enough Ether
        require(msg.value >= price, "Insufficient payment");

        // Get the owner of the NFT
        address seller = ownerOf(tokenId);

        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);

        // Transfer the payment to the seller
        payable(seller).transfer(price);

        // Clear the price for the NFT
        _tokenPrices[tokenId] = 0;

        // Emit the purchase event
        emit NFTPurchased(msg.sender, tokenId, price);
    }

    /**
     * @dev Get the price of an NFT listed for sale.
     * @param tokenId ID of the NFT.
     * @return Price of the NFT in wei.
     */
    function getNFTPrice(uint256 tokenId) external view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    /**
     * @dev Override the _beforeTokenTransfer hook to ensure proper functionality.
     * @param from Address transferring the NFT.
     * @param to Address receiving the NFT.
     * @param tokenId ID of the NFT being transferred.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);

        // If the NFT is being transferred, clear its price
        if (from != address(0) && to != address(0)) {
            _tokenPrices[tokenId] = 0;
        }
    }
}
```
