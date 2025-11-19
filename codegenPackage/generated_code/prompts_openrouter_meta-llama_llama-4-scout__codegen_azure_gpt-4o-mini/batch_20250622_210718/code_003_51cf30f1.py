"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnfts.com
Prompt: Design a smart contract for a free minting event of NFTs, similar to the one offered by Cornucopias, using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_51cf30f1154924f9
Batch ID: 20250622_210718
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for a free minting event of NFTs
contract FreeMintNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if an address has already minted
    mapping(address => bool) private _hasMinted;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("FreeMintNFT", "FMNFT") {}

    // Function to mint a new NFT
    function mint() external {
        // Check if the caller has already minted an NFT
        require(!_hasMinted[msg.sender], "You have already minted an NFT.");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the caller
        _mint(msg.sender, tokenId);

        // Mark the caller as having minted
        _hasMinted[msg.sender] = true;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to check if an address has minted an NFT
    function hasMinted(address account) external view returns (bool) {
        return _hasMinted[account];
    }

    // Function to withdraw any Ether sent to the contract (if applicable)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("This contract does not accept Ether.");
    }
}
```
