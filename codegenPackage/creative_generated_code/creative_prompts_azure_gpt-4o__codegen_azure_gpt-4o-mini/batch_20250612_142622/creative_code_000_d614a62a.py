"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Write a smart contract in Solidity for minting NFTs with a 10k supply, a maximum of 10 per transaction, and 50 per wallet, similar to the "Fuck OpenSea" collection's minting rules.
Generated: DETERMINISTIC_d614a62a5b1e0f84
Batch ID: 20250612_142622
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/metadata/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NFTCollection is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter;
    uint256 public constant MAX_SUPPLY = 10000; // Maximum NFTs supply
    uint256 public constant MAX_PER_TX = 10; // Maximum mints per transaction
    uint256 public constant MAX_PER_WALLET = 50; // Maximum mints per wallet

    // Mapping to track how many NFTs each address has minted
    mapping(address => uint256) private _mintedCount;

    // Event emitted for minting
    event Minted(address indexed to, uint256 quantity);

    constructor() ERC721("NFTCollection", "NFTC") {}

    /**
     * @dev Mint NFTs to the caller's address.
     * @param quantity The number of NFTs to mint.
     */
    function mint(uint256 quantity) external {
        // Validate quantity
        require(quantity > 0 && quantity <= MAX_PER_TX, "Invalid mint quantity");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(_mintedCount[msg.sender] + quantity <= MAX_PER_WALLET, "Exceeds max per wallet");

        // Update minted count for the wallet
        _mintedCount[msg.sender] += quantity;

        // Mint NFTs
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(msg.sender, tokenId);
            _tokenIdCounter.increment();
        }

        emit Minted(msg.sender, quantity);
    }

    /**
     * @dev Get the number of NFTs minted by a specific address.
     * @param owner The address to check.
     * @return The number of NFTs minted by the address.
     */
    function mintedCount(address owner) external view returns (uint256) {
        return _mintedCount[owner];
    }

    /**
     * @dev Set the maximum supply of NFTs - only callable by the owner.
     * @param newMaxSupply The new maximum supply.
     */
    function setMaxSupply(uint256 newMaxSupply) external onlyOwner {
        require(newMaxSupply >= totalSupply(), "New max supply must be >= current supply");
        MAX_SUPPLY = newMaxSupply; // No direct state variable modification, add this in the constructor
    }

    /**
     * @dev Override the _baseURI function if needed.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.example.com/metadata/"; // Replace with your metadata URI
    }
}
```
