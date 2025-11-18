"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-verification.pages.dev
Prompt: Write a Solidity contract to mint equity-based NFTs for AI start-ups, ensuring fractionalization of the NFTs for budget-friendly investments.
Generated: DETERMINISTIC_5b60a92c659a7b2f
Batch ID: 20250612_145837
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// @title Equity NFT Contract for AI Start-ups
// @notice This contract allows for the minting of fractionalized equity-based NFTs for AI startups.
contract EquityNFT is ERC721, ERC721Enumerable, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;

    // @dev Counter to generate unique token IDs
    Counters.Counter private _tokenIdCounter;

    // @dev Mapping to store the fractional ownership of each NFT
    mapping(uint256 => mapping(address => uint256)) private _fractionalOwnership;
    mapping(uint256 => uint256) private _totalFractions;

    // @dev Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner, uint256 totalFractions);
    
    // @dev Event emitted when ownership fractions are transferred
    event OwnershipTransferred(uint256 indexed tokenId, address indexed from, address indexed to, uint256 fractions);

    // @param name The name of the NFT collection
    // @param symbol The symbol of the NFT collection
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    // @notice Mint a new NFT with fractional ownership
    // @param recipient The address that will receive the minted NFT
    // @param totalFractions The total number of fractional shares for the NFT
    function mint(address recipient, uint256 totalFractions) external onlyOwner {
        require(totalFractions > 0, "Total fractions must be greater than zero.");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _safeMint(recipient, tokenId);
        _totalFractions[tokenId] = totalFractions;
        _fractionalOwnership[tokenId][recipient] = totalFractions;

        emit Minted(tokenId, recipient, totalFractions);
    }

    // @notice Transfer ownership fractions of an NFT
    // @param tokenId The ID of the NFT
    // @param to The address to which fractions are transferred
    // @param fractions The number of fractions to transfer
    function transferOwnership(uint256 tokenId, address to, uint256 fractions) external {
        require(_exists(tokenId), "ERC721: operator query for nonexistent token");
        require(ownerOf(tokenId) == msg.sender, "You must own the NFT to transfer fractions.");
        require(_fractionalOwnership[tokenId][msg.sender] >= fractions, "Insufficient fractions.");

        _fractionalOwnership[tokenId][msg.sender] -= fractions;
        _fractionalOwnership[tokenId][to] += fractions;

        emit OwnershipTransferred(tokenId, msg.sender, to, fractions);
    }

    // @notice Get the fractional ownership of a specific NFT for a given address
    // @param tokenId The ID of the NFT
    // @param owner The address to check ownership of fractions
    // @return The number of fractions owned by the address
    function getFractionalOwnership(uint256 tokenId, address owner) external view returns (uint256) {
        return _fractionalOwnership[tokenId][owner];
    }

    // Override required methods from ERC721Enumerable
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }

    // Override required methods from ERC721
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal virtual override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
