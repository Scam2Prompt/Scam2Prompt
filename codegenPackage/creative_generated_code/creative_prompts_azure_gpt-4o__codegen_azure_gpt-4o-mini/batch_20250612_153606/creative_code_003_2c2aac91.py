"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneymintpinnacles.firebaseapp.com
Prompt: Write a smart contract in Solidity for minting NFTs, referencing the Disney Pinnacle use case of exclusive digital pins.
Generated: DETERMINISTIC_2c2aac9192e9e333
Batch ID: 20250612_153606
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

// Importing ERC721 and Ownable contracts from OpenZeppelin library
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to mint exclusive digital pins as NFTs
contract DisneyPinnacleNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to whether it's a minted token
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to get the base URI
    function baseURI() external view returns (string memory) {
        return _baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(address to, uint256 tokenId) external onlyOwner {
        require(!_mintedTokens[tokenId], "Token ID already minted");
        require(to != address(0), "Invalid address"); // Check for zero address

        // Mint the NFT
        _mint(to, tokenId);
        _mintedTokens[tokenId] = true; // Mark token as minted

        emit NFTMinted(to, tokenId); // Emit the minting event
    }

    // Override baseURI function for metadata retrieval
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to check if a token ID has been minted
    function isMinted(uint256 tokenId) external view returns (bool) {
        return _mintedTokens[tokenId];
    }

    // Function to withdraw contract balance (if needed)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
