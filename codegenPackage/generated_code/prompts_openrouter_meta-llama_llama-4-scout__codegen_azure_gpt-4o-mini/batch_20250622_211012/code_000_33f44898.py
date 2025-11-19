"""
Generated Code Metadata:
========================
Original URL: https://dappass.neocities.org
Prompt: Write a smart contract for minting a limited supply of 88 digital assets, where each asset has a price of 0 ETH and can be minted only once per wallet.
Generated: DETERMINISTIC_33f44898c6c4fdd0
Batch ID: 20250622_211012
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";

contract LimitedMintingNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the number of minted tokens
    Counters.Counter private _tokenIdCounter;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 88;

    // Mapping to track if an address has minted an NFT
    mapping(address => bool) public hasMinted;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("LimitedMintingNFT", "LMNFT") {}

    /**
     * @dev Function to mint a new NFT.
     * Can only be called once per wallet.
     */
    function mint() external {
        // Check if the maximum supply has been reached
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        // Check if the caller has already minted an NFT
        require(!hasMinted[msg.sender], "You have already minted an NFT");

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);

        // Update the state
        hasMinted[msg.sender] = true;
        _tokenIdCounter.increment();

        // Emit the minting event
        emit Minted(msg.sender, tokenId);
    }

    /**
     * @dev Function to get the total supply of minted NFTs.
     * @return The total number of minted NFTs.
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
