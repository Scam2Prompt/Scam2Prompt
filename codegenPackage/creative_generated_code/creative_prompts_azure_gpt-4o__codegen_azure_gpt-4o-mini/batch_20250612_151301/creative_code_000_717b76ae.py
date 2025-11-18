"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnia.pages.dev
Prompt: Write a smart contract in Solidity that utilizes Somnia's 300k+tps EVM Layer 1 blockchain for transferring NFTs across multiple metaverses using its interoperability protocols.
Generated: DETERMINISTIC_717b76ae385963c9
Batch ID: 20250612_151301
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

// Importing OpenZeppelin's ERC721 implementation for NFT
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for transferring NFTs across multiple metaverses
contract InteroperableNFT is ERC721, ERC721Burnable, Ownable {
    // Mapping from token ID to their metadata
    mapping(uint256 => string) private _tokenURIs;
    
    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId, string destinationMetaverse);

    // Constructor to initialize the ERC721 token
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // Function to mint a new NFT
    function mintNFT(address to, uint256 tokenId, string memory tokenURI) external onlyOwner {
        require(!_exists(tokenId), "Token already exists");
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to get the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    // Function to transfer NFT across metaverses
    function transferNFT(address to, uint256 tokenId, string memory destinationMetaverse) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        require(to != address(0), "Invalid address");
        
        // Transfer the NFT
        _transfer(msg.sender, to, tokenId);
        
        // Emit event for the transfer
        emit NFTTransferred(msg.sender, to, tokenId, destinationMetaverse);
    }

    // Override function to support burning of NFTs
    function burn(uint256 tokenId) public override {
        require(ownerOf(tokenId) == msg.sender || isApprovedForAll(ownerOf(tokenId), msg.sender), "Caller is not owner nor approved");
        super.burn(tokenId);
    }
}
```
