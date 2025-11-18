"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disney-pinnacles.web.app
Prompt: Develop a smart contract that enables users to mint Disney-themed NFTs, referencing the collaboration between Disney and Dapper Labs.
Generated: DETERMINISTIC_1cbe28ea25759293
Batch ID: 20250612_153526
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

// Import OpenZeppelin's ERC721 implementation for NFT standards
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for Disney-themed NFTs
contract DisneyNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for unique token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for the metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override base URI for metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Override required functions from ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) 
        public 
        view 
        override(ERC721, ERC721Enumerable) 
        returns (bool) 
    {
        return super.supportsInterface(interfaceId);
    }

    // Function to get the total supply of NFTs
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to retrieve the token ID of a given index
    function tokenByIndex(uint256 index) public view returns (uint256) {
        return super.tokenByIndex(index);
    }

    // Function to retrieve the token ID owned by an address at a given index
    function tokenOfOwnerByIndex(address owner, uint256 index) 
        public 
        view 
        returns (uint256) 
    {
        return super.tokenOfOwnerByIndex(owner, index);
    }
}
```
