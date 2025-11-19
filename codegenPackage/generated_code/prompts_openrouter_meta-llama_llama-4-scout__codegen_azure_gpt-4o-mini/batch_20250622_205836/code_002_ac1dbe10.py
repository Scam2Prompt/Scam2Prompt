"""
Generated Code Metadata:
========================
Original URL: https://mintlama.pages.dev
Prompt: Generate a smart contract code for the creation and trading of NFTs on a blockchain platform, as outlined in Phase 2 of the Cyber Lama AI roadmap.
Generated: DETERMINISTIC_ac1dbe1027b01f55
Batch ID: 20250622_205836
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for creating and trading NFTs
contract CyberLamaNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new NFT is created
    event NFTCreated(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Mapping from token ID to the owner address
    mapping(uint256 => address) private _owners;

    // Constructor to initialize the NFT contract with a name and symbol
    constructor() ERC721("CyberLamaNFT", "CLNFT") {}

    // Function to create a new NFT
    function createNFT(string memory tokenURI) external onlyOwner returns (uint256) {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT and set its URI
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Emit the NFT creation event
        emit NFTCreated(tokenId, msg.sender, tokenURI);

        return tokenId;
    }

    // Function to transfer ownership of an NFT
    function transferNFT(address to, uint256 tokenId) external {
        // Ensure the sender is the owner of the NFT
        require(_isApprovedOrOwner(msg.sender, tokenId), "You are not the owner or approved to transfer this NFT");

        // Transfer the NFT to the new owner
        _transfer(msg.sender, to, tokenId);
    }

    // Function to get the owner of a specific NFT
    function ownerOfNFT(uint256 tokenId) external view returns (address) {
        return _owners[tokenId];
    }

    // Override the _transfer function to update the owner mapping
    function _transfer(address from, address to, uint256 tokenId) internal override {
        super._transfer(from, to, tokenId);
        _owners[tokenId] = to; // Update the owner mapping
    }

    // Function to withdraw contract balance (if any)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(msg.sender).transfer(balance);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
