"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cyberlamas.pages.dev
Prompt: Can you provide an example of a smart contract for issuing NFTs on the Cyber Lama platform, including circulation limiting mechanisms?
Generated: DETERMINISTIC_b4515a80c321bb39
Batch ID: 20250612_162508
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

// Import the OpenZeppelin ERC721 contract and Ownable contract for ownership
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for issuing NFTs on the Cyber Lama platform
contract CyberLamaNFT is ERC721Enumerable, Ownable {
    // Variables to manage the NFT attributes
    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000; // Maximum supply of NFTs
    uint256 public tokenCounter; // Counter for the token IDs

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI; // Set the base URI for the NFTs
        tokenCounter = 0; // Initialize token counter
    }

    // Function to mint new NFTs with circulation limiting
    function mintNFT() external {
        require(tokenCounter < MAX_SUPPLY, "Max supply reached"); // Check if max supply is reached
        
        tokenCounter++; // Increment token counter
        _safeMint(msg.sender, tokenCounter); // Mint the NFT to the caller
        emit NFTMinted(msg.sender, tokenCounter); // Emit event for the minted NFT
    }

    // Function to set the base URI for the NFTs
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI; // Update the base URI
    }

    // Function to retrieve the base URI
    function baseURI() external view returns (string memory) {
        return _baseTokenURI; // Return the base URI
    }

    // Override the _baseURI function to return the base token URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI; // Override base URI function
    }

    // Function to withdraw any Ether in the contract (owner only)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance); // Transfer balance to owner
    }

    // Fallback function for receiving Ether
    receive() external payable {
        // Accept Ether payments
    }
}
```
