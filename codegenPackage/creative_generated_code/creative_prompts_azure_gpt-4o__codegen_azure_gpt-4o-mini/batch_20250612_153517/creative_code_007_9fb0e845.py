"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mong-life-mong.pages.dev
Prompt: Provide code to mint and manage $MONG-related NFTs, considering the 6.9% allocation for MONGS NFTs in its tokenomics.
Generated: DETERMINISTIC_9fb0e8450efb43c2
Batch ID: 20250612_153517
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title MONGNFT
 * @dev A contract to mint and manage $MONG-related NFTs
 */
contract MONGNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Total allocated percentage for MONGS NFTs
    uint256 public constant ALLOCATION_PERCENTAGE = 690; // 6.9% expressed in basis points
    uint256 public constant MAX_SUPPLY = 10000; // Maximum supply of NFTs

    // Mapping to track NFT ownership and allocation
    mapping(address => uint256) public allocation;

    event Minted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Initializes the contract with a name and symbol for the NFTs.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new NFT to the specified address.
     * @param to The address to receive the minted NFT.
     */
    function mint(address to) external onlyOwner {
        require(to != address(0), "Mint to the zero address");
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _mint(to, tokenId);
        emit Minted(to, tokenId);
    }

    /**
     * @dev Returns the base URI for the NFT metadata.
     * @return The base URI as a string.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set a new base URI for the NFT metadata.
     * @param baseTokenURI The new base URI to be set.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Calculate the total allocation for MONGS NFTs.
     * @return The total number of NFTs allocated based on the tokenomics.
     */
    function calculateAllocation() external view returns (uint256) {
        return (totalSupply() * ALLOCATION_PERCENTAGE) / 10000; // Calculate based on current total supply
    }

    /**
     * @dev Withdraw contract balance (if applicable).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
