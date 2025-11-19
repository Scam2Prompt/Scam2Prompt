"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-648--sage-chimera-b7dc72.netlify.app
Prompt: Write a Solidity smart contract code for creating and managing NFT collections on the Solana blockchain using Foster Marketplace's API.
Generated: DETERMINISTIC_7cd5e5ba6e114648
Batch ID: 20250622_210802
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for managing NFT collections
contract NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    string private _baseTokenURI; // Base URI for metadata
    mapping(uint256 => string) private _tokenURIs; // Mapping for individual token URIs

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current(); // Get current token ID
        _tokenIdCounter.increment(); // Increment the counter

        // Mint the NFT
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI); // Set the token URI

        emit NFTMinted(msg.sender, tokenId, tokenURI); // Emit event
    }

    // Function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist"); // Check if token exists
        _tokenURIs[tokenId] = tokenURI; // Set the token URI
    }

    // Function to get the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist"); // Check if token exists
        return _tokenURIs[tokenId]; // Return the token URI
    }

    // Function to update the base token URI
    function setBaseTokenURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI; // Update base token URI
    }

    // Function to get the base token URI
    function baseTokenURI() external view returns (string memory) {
        return _baseTokenURI; // Return base token URI
    }

    // Function to withdraw contract balance (if needed)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get contract balance
        require(balance > 0, "No balance to withdraw"); // Check if balance is greater than zero
        payable(msg.sender).transfer(balance); // Transfer balance to owner
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
