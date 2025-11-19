"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Generate a smart contract in Solidity for minting NFTs in a Web 3.0 environment, specifically for a collection like "Cats World" with unique ownership features.
Generated: DETERMINISTIC_27d324f033d12356
Batch ID: 20250612_164152
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

// Import OpenZeppelin's ERC721 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for minting NFTs in "Cats World"
contract CatsWorld is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variable to keep track of token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the token's metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event CatMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor - sets the name and symbol of the NFT collection
    constructor() ERC721("Cats World", "CATS") {}

    // Function to mint a new cat NFT
    // @param _tokenURI: The URI pointing to the NFT's metadata
    function mintCat(string memory _tokenURI) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        
        // Mint the NFT to the caller's address
        _mint(msg.sender, tokenId);
        
        // Set the token URI for the newly minted NFT
        _setTokenURI(tokenId, _tokenURI);
        
        // Emit the CatMinted event
        emit CatMinted(msg.sender, tokenId, _tokenURI);
        
        // Increment the counter for the next token ID
        _tokenIdCounter.increment();
    }

    // Function to set the token URI (internal)
    // @param tokenId: The ID of the token
    // @param tokenURI: The URI pointing to the token's metadata
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Override the base URI function
    // @param tokenId: The ID of the token
    // @return string: The token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }
}
```
