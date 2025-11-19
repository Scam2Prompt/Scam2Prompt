"""
Generated Code Metadata:
========================
Original URL: https://1-dv2.pages.dev
Prompt: Generate code to deploy a TIP-4 NFT collection on the Venom mainnet with at least 30 distinctive items, ensuring compatibility with Oasis.Gallery for trading.
Generated: DETERMINISTIC_cf134c558ae1a1fb
Batch ID: 20250612_153224
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// TIP-4 NFT contract for deploying a collection on the Venom mainnet
contract TIP4NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to token metadata
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) external onlyOwner {
        require(_tokenIdCounter.current() < 30, "Maximum supply reached");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT
        _mint(msg.sender, tokenId);
        
        // Set the token URI
        _setTokenURI(tokenId, tokenURI);

        // Emit the TokenMinted event
        emit TokenMinted(tokenId, msg.sender, tokenURI);
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Override the base URI function
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to retrieve the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    // Function to update the base URI (only owner)
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to withdraw contract balance (if needed)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
