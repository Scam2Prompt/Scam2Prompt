"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doglibretoken.web.app
Prompt: Design a simple NFT minting function for DogLibre's gamified NFTs, ensuring it aligns with their multichain strategy across Ethereum and Polygon.
Generated: DETERMINISTIC_a4212b09a32b21ef
Batch ID: 20250612_164035
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

// Import OpenZeppelin contracts for ERC721 and Ownable functionality
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Polygon bridge if needed
interface IPolygonBridge {
    function deposit(address _token, address _to, uint256 _value) external;
}

// DogLibreNFT contract for minting NFTs on Ethereum and Polygon
contract DogLibreNFT is ERC721Enumerable, Ownable {
    // Counter for tracking the number of minted NFTs
    uint256 private _tokenIdCounter;

    // Base URI for metadata of NFTs
    string private _baseTokenURI;

    // Mapping to track if a token has been minted
    mapping(uint256 => bool) private _mintedTokens;

    // Event emitted when an NFT is minted
    event Minted(address indexed owner, uint256 tokenId);

    // Constructor to initialize the NFT with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
    }

    // Function to mint a new NFT
    function mintNFT() external onlyOwner {
        uint256 tokenId = _tokenIdCounter;
        
        // Ensure the token has not already been minted
        require(!_mintedTokens[tokenId], "Token already minted");

        // Mint the NFT
        _mint(msg.sender, tokenId);
        
        // Mark the token as minted
        _mintedTokens[tokenId] = true;

        // Increment the token ID counter
        _tokenIdCounter++;

        // Emit the minted event
        emit Minted(msg.sender, tokenId);
    }

    // Function to set the base URI for token metadata
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Override the baseURI function for metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to withdraw Ether (if needed) from the contract
    function withdraw() external onlyOwner {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Transfer failed.");
    }
}
```
