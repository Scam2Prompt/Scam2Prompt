"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub.web.app
Prompt: "Write a Solidity function to handle NFT minting and trading on the Bitcoin blockchain, similar to the features described for the 10k Ordinals NFT Club on Bitcoin Dogs."
Generated: DETERMINISTIC_a59a5f7938d5eb89
Batch ID: 20250622_210216
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

// Importing necessary libraries
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// NFTMintingAndTrading contract inherits from ERC721 and Ownable
contract NFTMintingAndTrading is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to owner address
    mapping(uint256 => address) private _tokenOwners;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Event emitted when an NFT is traded
    event NFTTraded(address indexed from, address indexed to, uint256 indexed tokenId);

    // Constructor to initialize the ERC721 token with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to trade an NFT
    function tradeNFT(address to, uint256 tokenId) external {
        // Ensure the sender is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        // Ensure the recipient address is valid
        require(to != address(0), "Invalid recipient address");

        // Transfer the NFT
        _transfer(msg.sender, to, tokenId);
        emit NFTTraded(msg.sender, to, tokenId);
    }

    // Function to get the total supply of minted NFTs
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to get the owner of a specific token
    function getOwnerOfToken(uint256 tokenId) external view returns (address) {
        return ownerOf(tokenId);
    }
}
```
