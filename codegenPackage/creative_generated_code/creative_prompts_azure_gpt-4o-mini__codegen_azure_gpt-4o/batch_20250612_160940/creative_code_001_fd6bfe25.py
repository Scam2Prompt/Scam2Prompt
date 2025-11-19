"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintlama.pages.dev
Prompt: Write a smart contract for issuing and trading NFTs on the Cyber Lama platform, considering the project's unique NFT creation process.
Generated: DETERMINISTIC_fd6bfe25d31ac22c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an implementation of a smart contract using Solidity (the programming language for Ethereum smart contracts) for issuing and trading NFTs on the Cyber Lama platform:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation and other required utilities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/// @title CyberLamaNFT
/// @dev Smart contract for creating and trading NFTs on the Cyber Lama platform
contract CyberLamaNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIds;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed creator, uint256 indexed tokenId);

    // Event emitted when an NFT is sold
    event NFTSold(address indexed seller, address indexed buyer, uint256 indexed tokenId, uint256 price);

    // Struct to store sale details
    struct Sale {
        address seller;
        uint256 price;
        bool isAvailable;
    }

    // Mapping from token ID to sale details
    mapping(uint256 => Sale) public tokenSales;

    /// @dev Constructor to initialize the contract
    /// @param name The name of the NFT collection
    /// @param symbol The symbol of the NFT collection
    /// @param baseTokenURI The base URI for metadata
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /// @dev Function to set the base URI for metadata
    /// @param baseTokenURI The new base URI
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /// @dev Internal function to get the base URI
    /// @return The base URI string
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /// @dev Function to mint a new NFT
    /// @return tokenId The ID of the newly minted NFT
    function mintNFT() external returns (uint256 tokenId) {
        _tokenIds.increment();
        tokenId = _tokenIds.current();

        // Mint the NFT to the sender
        _mint(msg.sender, tokenId);

        // Emit minting event
        emit NFTMinted(msg.sender, tokenId);
    }

    /// @dev Function to list an NFT for sale
    /// @param tokenId The ID of the NFT to list
    /// @param price The sale price of the NFT in wei
    function listNFTForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(price > 0, "Price must be greater than zero");

        tokenSales[tokenId] = Sale({
            seller: msg.sender,
            price: price,
            isAvailable: true
        });
    }

    /// @dev Function to buy an NFT listed for sale
    /// @param tokenId The ID of the NFT to buy
    function buyNFT(uint256 tokenId) external payable {
        Sale memory sale = tokenSales[tokenId];
        require(sale.isAvailable, "This NFT is not for sale");
        require(msg.value >= sale.price, "Insufficient funds to purchase this NFT");

        address seller = sale.seller;

        // Transfer funds to the seller
        payable(seller).transfer(sale.price);

        // Transfer the NFT to the buyer
        _transfer(seller, msg.sender, tokenId);

        // Mark NFT as no longer for sale
        tokenSales[tokenId].isAvailable = false;

        // Emit sale event
        emit NFTSold(seller, msg.sender, tokenId, sale.price);
    }

    /// @dev Function to cancel an NFT listing
    /// @param tokenId The ID of the NFT to cancel
    function cancelNFTListing(uint256 tokenId) external {
        Sale memory sale = tokenSales[tokenId];
        require(sale.seller == msg.sender, "You are not the seller of this NFT");
        require(sale.isAvailable, "This NFT is not currently listed for sale");

        // Mark NFT as no longer for sale
        tokenSales[tokenId].isAvailable = false;
    }
}
```

### Notes:
- This contract is built on the OpenZeppelin library for the ERC721 standard.
- Proper error handling ensures invalid operations (e.g., unauthorized actions, insufficient funds, invalid token IDs) are prevented.
- Events are used for transparency, enabling off-chain tracking of minting and sale activities.
- The contract owner has the ability to set the base URI for metadata.
