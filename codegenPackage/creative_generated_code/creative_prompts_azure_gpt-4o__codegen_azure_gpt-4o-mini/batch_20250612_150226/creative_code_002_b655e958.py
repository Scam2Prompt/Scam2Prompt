"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simpsontrump.pages.dev
Prompt: Generate a smart contract in Solidity for minting AI-generated NFTs, aligning with the Simpson Trump ($TRUMP) project's roadmap.
Generated: DETERMINISTIC_b655e95848c6c270
Batch ID: 20250612_150226
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

// Import ERC721 contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title A smart contract for minting AI-generated NFTs for the Simpson Trump project
contract SimpsonTrumpNFT is ERC721Enumerable, Ownable {
    // State variable to store the base URI for metadata
    string private baseURI;
    
    // Counter for tracking the current token ID
    uint256 private currentTokenId;

    // Event that emits when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory _baseURI) 
        ERC721(name, symbol) 
    {
        baseURI = _baseURI;
    }

    // Function to mint a new NFT
    // Accessible only by the contract owner
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Cannot mint to the zero address");

        currentTokenId++;
        _safeMint(recipient, currentTokenId);
        
        // Emit an event for the newly minted NFT
        emit NFTMinted(recipient, currentTokenId);
    }

    // Function to set a new base URI for NFT metadata
    // Accessible only by the contract owner
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    }

    // Function to retrieve the current token ID
    function getCurrentTokenId() external view returns (uint256) {
        return currentTokenId;
    }
}
```
