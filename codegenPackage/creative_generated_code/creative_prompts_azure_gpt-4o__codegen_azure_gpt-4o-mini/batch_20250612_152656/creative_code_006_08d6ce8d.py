"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghozali-49z.pages.dev
Prompt: Create a smart contract template for minting NFTs linked to "Ghozali 404" memecoin on the Base blockchain.
Generated: DETERMINISTIC_08d6ce8ddefc16c5
Batch ID: 20250612_152656
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Ghozali404NFT is a smart contract for minting NFTs linked to the Ghozali 404 memecoin
contract Ghozali404NFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    string private _baseTokenURI; // Base URI for the token metadata
    mapping(uint256 => address) private _tokenOwners; // Mapping from token ID to owner address

    // Events
    event Minted(address indexed owner, uint256 indexed tokenId);

    // Constructor initializes the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mint() external {
        // Increment token ID counter and get new token ID
        uint256 tokenId = _tokenIdCounter.current();
        
        // Mint the NFT to the sender
        _mint(msg.sender, tokenId);
        
        // Store the token owner
        _tokenOwners[tokenId] = msg.sender;

        // Emit the Minted event
        emit Minted(msg.sender, tokenId);
        
        // Increment the token ID counter for the next mint
        _tokenIdCounter.increment();
    }

    // Function to get the base URI for the token metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to get the owner of a specific token ID (publicly accessible)
    function ownerOf(uint256 tokenId) public view override returns (address) {
        address owner = _tokenOwners[tokenId];
        require(owner != address(0), "Token does not exist");
        return owner;
    }

    // Function to update the base URI (only owner can update)
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to withdraw any Ether from the contract (only owner can withdraw)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Please use the withdraw function.");
    }
}
```
