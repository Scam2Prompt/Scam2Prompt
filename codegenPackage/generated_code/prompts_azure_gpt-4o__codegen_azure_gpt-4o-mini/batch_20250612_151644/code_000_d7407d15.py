"""
Generated Code Metadata:
========================
Original URL: https://zerobeings.app
Prompt: Write a smart contract in Solidity that mimics the functionality of the "Zero Beings" verified contract, ensuring compatibility with OpenSea.
Generated: DETERMINISTIC_d7407d153a605cb4
Batch ID: 20250612_151644
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

// Importing OpenZeppelin's ERC721 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for the Zero Beings NFT collection
contract ZeroBeings is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to a boolean indicating if it's a special being
    mapping(uint256 => bool) private _isSpecialBeing;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 indexed tokenId, bool isSpecial);

    // Constructor to initialize the contract with a name and symbol
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new token
    function mint(bool isSpecial) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _isSpecialBeing[tokenId] = isSpecial;
        _tokenIdCounter.increment();

        emit TokenMinted(msg.sender, tokenId, isSpecial);
    }

    // Function to get the base URI for token metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to check if a token is a special being
    function isSpecialBeing(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _isSpecialBeing[tokenId];
    }

    // Function to set a new base URI (only owner)
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
