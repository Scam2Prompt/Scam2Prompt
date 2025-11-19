"""
Generated Code Metadata:
========================
Original URL: https://zksync-nft.vercel.app
Prompt: Generate a simple smart contract using ZKSync and Internet Friends Creator for NFT minting.
Generated: DETERMINISTIC_4d683e0acd5a75f3
Batch ID: 20250622_205054
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

// Importing the ERC721 interface for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Simple NFT contract for minting Internet Friends
contract InternetFriendsNFT is ERC721, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping from token ID to token URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("InternetFriends", "IFNFT") {
        _tokenIdCounter = 1; // Start token IDs from 1
    }

    // Function to mint a new NFT
    // @param to The address that will own the minted NFT
    // @param tokenURI The metadata URI for the NFT
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Invalid address: cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Invalid token URI: cannot be empty");

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter;
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId, tokenURI);

        // Increment the token ID counter for the next mint
        _tokenIdCounter++;
    }

    // Internal function to set the token URI
    // @param tokenId The ID of the token
    // @param tokenURI The metadata URI for the token
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI
    // @param tokenId The ID of the token
    // @return The metadata URI of the token
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }
}
```
