"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babysamocoin-nft.web.app
Prompt: How can I implement a minting function for the Baby SAMO Coin NFT using the $BABY Tokenomics?
Generated: DETERMINISTIC_1ce8defdbadd0edb
Batch ID: 20250612_161617
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

// Importing OpenZeppelin Contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// BabySAMO NFT Contract
contract BabySAMO is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter; // Counter for token IDs
    uint256 public maxSupply;                 // Maximum supply of NFTs
    uint256 public mintPrice;                 // Price to mint an NFT
    string private baseTokenURI;              // Base URI for metadata

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    // Constructor to initialize the contract
    constructor(string memory name, string memory symbol, uint256 _maxSupply, uint256 _mintPrice, string memory _baseTokenURI) 
        ERC721(name, symbol) 
    {
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        baseTokenURI = _baseTokenURI;
    }

    // Minting function for NFTs
    function mint() external payable {
        // Check if minting is still allowed
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        // Check if the correct payment is sent
        require(msg.value >= mintPrice, "Insufficient funds sent");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(msg.sender, tokenId);

        // Emit the Minted event
        emit Minted(msg.sender, tokenId);
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    // Function to withdraw funds from the contract (only owner)
    function withdraw() external onlyOwner {
        // Transfer the contract balance to the owner
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        // Use call to prevent reentrancy issues
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to accept direct Ether transfers
    receive() external payable {}
}
```
