"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pre-mpeppe-live.pages.dev
Prompt: Write a smart contract in Solidity to mint Player Card NFTs inspired by soccer legends and Pepe artwork, ensuring the supply is limited to 420 NFTs.
Generated: DETERMINISTIC_06722e626152873a
Batch ID: 20250612_152714
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

// Importing OpenZeppelin's ERC721, Ownable and SafeMath libraries
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// PlayerCardNFT contract
contract PlayerCardNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 420;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new NFT is minted
    event PlayerCardMinted(address indexed to, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Mint new NFT
    function mintPlayerCard() external {
        // Check if the maximum supply has been reached
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        // Increment token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new NFT and assign it to the caller
        _mint(msg.sender, tokenId);

        // Emit event for the minting action
        emit PlayerCardMinted(msg.sender, tokenId);
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Update the base URI (only owner can call this)
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    // Function to withdraw contract's Ether balance (only owner can call this)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
