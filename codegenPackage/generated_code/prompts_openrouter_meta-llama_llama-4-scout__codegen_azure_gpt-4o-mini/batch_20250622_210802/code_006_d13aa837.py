"""
Generated Code Metadata:
========================
Original URL: https://receive-eesee.pages.dev
Prompt: "Write a Solidity smart contract for creating and managing NFTs on the eesee platform, including functions for minting, transferring, and burning NFTs."
Generated: DETERMINISTIC_d13aa837d0cb1665
Batch ID: 20250622_210802
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

// Importing the ERC721 interface and the Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for managing NFTs on the eesee platform
contract EeseeNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the owner address
    mapping(uint256 => address) private _tokenOwners;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Event emitted when an NFT is burned
    event NFTBurned(uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("EeseeNFT", "EES") {}

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();
        
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to transfer an NFT from one address to another
    function transferNFT(address to, uint256 tokenId) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(to != address(0), "Invalid address");

        _transfer(msg.sender, to, tokenId);
    }

    // Function to burn an NFT
    function burnNFT(uint256 tokenId) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        _burn(tokenId);
        emit NFTBurned(tokenId);
    }

    // Function to check if a token exists
    function _exists(uint256 tokenId) internal view override returns (bool) {
        return super._exists(tokenId);
    }
}
```
