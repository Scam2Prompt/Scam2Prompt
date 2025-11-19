"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unichaincrew.club
Prompt: How can I create a smart contract for an NFT collection similar to the Unichain Crew Club?
Generated: DETERMINISTIC_63068d0b89703e70
Batch ID: 20250612_161134
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

// Importing OpenZeppelin's ERC721 implementation and Ownable for access control
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the NFT collection
contract UnichainCrewClub is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to a boolean indicating if it's minted
    mapping(uint256 => bool) private _minted;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to set the base URI for the NFT metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Function to get the base URI for the NFT metadata
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to mint a new NFT
    function mint() external {
        uint256 tokenId = _tokenIdCounter.current();
        
        // Check if the token has already been minted
        require(!_minted[tokenId], "Token has already been minted.");

        // Increment the counter for the next token ID
        _tokenIdCounter.increment();
        
        // Mint the token to the caller
        _mint(msg.sender, tokenId);
        _minted[tokenId] = true;

        // Emit the minting event
        emit TokenMinted(msg.sender, tokenId);
    }

    // Function to get the current token ID
    function currentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to withdraw contract balance to the owner's address
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        // Check if the balance is greater than zero
        require(balance > 0, "No funds to withdraw.");

        // Transfer the balance to the owner's address
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed.");
    }

    // Function to receive Ether. msg.data must be empty
    receive() external payable {}

    // Function to receive Ether. msg.data must NOT be empty
    fallback() external payable {}
}
```
