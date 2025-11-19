"""
Generated Code Metadata:
========================
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Generate a smart contract in Solidity for minting NFTs in a Web 3.0 environment, specifically for a collection like "Cats World" with unique ownership features.
Generated: DETERMINISTIC_27d324f033d12356
Batch ID: 20250612_164152
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

// Importing the OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the "Cats World" NFT collection
contract CatsWorld is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to unique attributes (if needed)
    mapping(uint256 => string) private _catAttributes;

    // Event emitted when a new cat is minted
    event CatMinted(address indexed owner, uint256 indexed tokenId, string attributes);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new cat NFT
    function mintCat(string memory attributes) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _catAttributes[tokenId] = attributes; // Store unique attributes
        _tokenIdCounter.increment();

        emit CatMinted(msg.sender, tokenId, attributes);
    }

    // Function to get the attributes of a specific cat
    function getCatAttributes(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Cat does not exist");
        return _catAttributes[tokenId];
    }

    // Override required by Solidity for ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Override to return the base URI for metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to set a new base URI (only owner)
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to withdraw contract balance (if needed)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
