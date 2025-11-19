"""
Generated Code Metadata:
========================
Original URL: https://jwzt-verification.pages.dev
Prompt: Write a Solidity contract to mint equity-based NFTs for AI start-ups, ensuring fractionalization of the NFTs for budget-friendly investments.
Generated: DETERMINISTIC_5b60a92c659a7b2f
Batch ID: 20250612_145837
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title FractionalNFT
 * @dev A contract for minting equity-based NFTs for AI start-ups with fractionalization capabilities.
 */
contract FractionalNFT is ERC721Enumerable, ERC721Burnable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the total supply of fractions
    mapping(uint256 => uint256) public totalFractions;

    // Mapping from token ID to the owner of each fraction
    mapping(uint256 => mapping(address => uint256)) public fractionsOwned;

    // Event emitted when fractions are minted
    event FractionsMinted(uint256 indexed tokenId, address indexed owner, uint256 amount);

    // Event emitted when fractions are transferred
    event FractionTransferred(uint256 indexed tokenId, address indexed from, address indexed to, uint256 amount);

    // Constructor to initialize the NFT contract
    constructor() ERC721("EquityNFT", "EQUITY") {}

    /**
     * @dev Mint a new NFT with a specified number of fractions.
     * @param recipient The address that will receive the NFT.
     * @param fractionCount The number of fractions to mint for the NFT.
     */
    function mintNFT(address recipient, uint256 fractionCount) external onlyOwner {
        require(fractionCount > 0, "Fraction count must be greater than zero");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _mint(recipient, tokenId);
        totalFractions[tokenId] = fractionCount;
        fractionsOwned[tokenId][recipient] = fractionCount;

        emit FractionsMinted(tokenId, recipient, fractionCount);
    }

    /**
     * @dev Transfer fractions of an NFT from one address to another.
     * @param tokenId The ID of the NFT.
     * @param to The address to transfer fractions to.
     * @param amount The number of fractions to transfer.
     */
    function transferFraction(uint256 tokenId, address to, uint256 amount) external {
        require(_exists(tokenId), "NFT does not exist");
        require(fractionsOwned[tokenId][msg.sender] >= amount, "Insufficient fractions");

        fractionsOwned[tokenId][msg.sender] -= amount;
        fractionsOwned[tokenId][to] += amount;

        emit FractionTransferred(tokenId, msg.sender, to, amount);
    }

    /**
     * @dev Get the number of fractions owned by an address for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @param owner The address to query.
     * @return The number of fractions owned.
     */
    function getFractionBalance(uint256 tokenId, address owner) external view returns (uint256) {
        return fractionsOwned[tokenId][owner];
    }

    /**
     * @dev Get the total number of fractions for a specific NFT.
     * @param tokenId The ID of the NFT.
     * @return The total number of fractions.
     */
    function getTotalFractions(uint256 tokenId) external view returns (uint256) {
        return totalFractions[tokenId];
    }
}
```
