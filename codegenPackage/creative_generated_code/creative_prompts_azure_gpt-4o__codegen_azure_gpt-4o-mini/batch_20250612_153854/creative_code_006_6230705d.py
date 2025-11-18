"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Create a function in Solidity that handles airdrops for the MegaRabbit NFT collection, ensuring these count toward the total supply limit.
Generated: DETERMINISTIC_6230705d7f1fdd66
Batch ID: 20250612_153854
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

contract MegaRabbitNFT is ERC721Enumerable, Ownable {
    using SafeMath for uint256;

    // Maximum supply limit for the MegaRabbit NFT collection
    uint256 public constant MAX_SUPPLY = 10000;

    // Mapping to track airdropped tokens
    mapping(address => uint256) public airdropCount;

    // Event to emit airdrop information
    event Airdrop(address indexed recipient, uint256 count);

    // Constructor to set the NFT collection name and symbol
    constructor() ERC721("MegaRabbitNFT", "MRNFT") {}

    /**
     * @dev Airdrop function to distribute NFTs to multiple recipients.
     * Only owner can call this function.
     * @param recipients Array of addresses to receive the airdropped NFTs
     * @param amounts Array of counts of NFTs to be airdropped to each recipient
     */
    function airdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        
        uint256 totalAirdropped = 0;

        // Loop through recipients and their corresponding amounts
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");
            
            totalAirdropped = totalAirdropped.add(amounts[i]);
        }

        // Check if total airdropped exceeds MAX_SUPPLY
        require(totalSupply().add(totalAirdropped) <= MAX_SUPPLY, "Supply limit exceeded");

        // Mint NFTs to recipients
        for (uint256 i = 0; i < recipients.length; i++) {
            for (uint256 j = 0; j < amounts[i]; j++) {
                uint256 tokenId = totalSupply().add(1); // New tokenId is one more than current totalSupply
                _mint(recipients[i], tokenId);
            }

            // Track the number of airdropped NFTs for this recipient
            airdropCount[recipients[i]] = airdropCount[recipients[i]].add(amounts[i]);
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to get the total supply limit.
     * @return The maximum supply limit for the collection
     */
    function totalSupplyLimit() external pure returns (uint256) {
        return MAX_SUPPLY;
    }
}
```
