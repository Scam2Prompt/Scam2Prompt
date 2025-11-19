"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fineturtie.events
Prompt: What are the best practices for setting up a minting process for NFTs with different pricing tiers, similar to those outlined on the FineTurtle Mint page?
Generated: DETERMINISTIC_eb353a273c6f1a48
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready implementation of an NFT minting process with pricing tiers in Solidity, following best practices:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/*
 * @title NFT Minting Contract with Pricing Tiers
 * @dev This contract allows minting NFTs at different price tiers for public sales.
 *      It includes proper error handling, access control, and follows best practices.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TieredNFTMinting is ERC721Enumerable, Ownable {
    // Variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum number of NFTs
    uint256 public totalMinted;                // Tracks the total number of minted NFTs

    // Pricing tiers
    mapping(uint256 => uint256) public tierPrices; // Price per token tier
    mapping(uint256 => uint256) public tierLimits; // Limit of tokens per tier

    // Events
    event Minted(address indexed minter, uint256 tokenId, uint256 tier, uint256 price);

    // Constructor
    constructor() ERC721("FineTurtleNFT", "FTNFT") {
        // Initialize tiers
        tierPrices[1] = 0.05 ether; // Tier 1 price
        tierPrices[2] = 0.1 ether;  // Tier 2 price
        tierPrices[3] = 0.2 ether;  // Tier 3 price

        tierLimits[1] = 4000;       // Tier 1 max supply
        tierLimits[2] = 3000;       // Tier 2 max supply
        tierLimits[3] = 3000;       // Tier 3 max supply
    }

    // Mint function
    function mint(uint256 tier) external payable {
        require(tierPrices[tier] > 0, "Invalid tier"); // Check tier validity
        require(tierLimits[tier] > 0, "Tier exhausted"); // Check tier availability
        require(totalMinted < MAX_SUPPLY, "Max supply reached"); // Check total supply limit
        require(msg.value == tierPrices[tier], "Incorrect payment amount"); // Check payment

        // Mint token logic
        uint256 tokenId = totalMinted + 1;
        totalMinted++;
        tierLimits[tier]--;

        _safeMint(msg.sender, tokenId);

        // Emit event
        emit Minted(msg.sender, tokenId, tier, tierPrices[tier]);
    }

    // Owner functionalities
    function setTierPrice(uint256 tier, uint256 price) external onlyOwner {
        tierPrices[tier] = price;
    }

    function setTierLimit(uint256 tier, uint256 limit) external onlyOwner {
        tierLimits[tier] = limit;
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    // Fallback function
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```

### Notes:
- Uses OpenZeppelin's libraries for security and standard functionality.
- Implements tier-specific pricing and limits.
- Proper error handling for tier validity, payment amount, and supply limits.
- Owner can update pricing and limits or withdraw funds securely.
- Events for minting provide transparency and traceability.
