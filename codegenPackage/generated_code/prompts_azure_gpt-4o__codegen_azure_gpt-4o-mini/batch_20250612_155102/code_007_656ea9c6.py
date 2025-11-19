"""
Generated Code Metadata:
========================
Original URL: https://abstractdog.testnet.nfts2.me
Prompt: Write a smart contract for minting abstract art-inspired dog meme NFTs on the Abstract Testnet, compatible with NFTs2Me.com.
Generated: DETERMINISTIC_656ea9c671dd39c6
Batch ID: 20250612_155102
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

// Importing the ERC721 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// AbstractArtDogMemeNFT contract inherits from ERC721Enumerable and Ownable
contract AbstractArtDogMemeNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to a boolean indicating if it's minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(uint256 tokenId) external onlyOwner {
        require(!_mintedTokens[tokenId], "Token ID already minted");
        
        // Mint the NFT to the caller's address
        _mint(msg.sender, tokenId);
        _mintedTokens[tokenId] = true;

        // Emit the Minted event
        emit Minted(msg.sender, tokenId);
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to check if a token ID has been minted
    function isMinted(uint256 tokenId) external view returns (bool) {
        return _mintedTokens[tokenId];
    }
}
```
