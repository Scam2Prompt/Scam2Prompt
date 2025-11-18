"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Write a smart contract in Solidity for minting NFTs similar to the "Cats World" collection, ensuring features like tier-based pricing and free initial mints are included.
Generated: DETERMINISTIC_d10ac8b32eea1090
Batch ID: 20250612_150040
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
import "@openzeppelin/contracts/utils/Strings.sol";

contract CatsWorldNFT is ERC721Enumerable, Ownable {
    using Strings for uint256;

    // Base URI for metadata
    string private _baseTokenURI;

    // Pricing tiers: tokenCount => price
    mapping(uint256 => uint256) public tierPricing;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Free mint count
    uint256 public constant FREE_MINT_LIMIT = 100;

    // Minted token count
    uint256 public freeMintedCount = 0;

    // Events
    event NFTMinted(address indexed minter, uint256 indexed tokenId);

    constructor(string memory baseURI) ERC721("Cats World", "CATS") {
        _baseTokenURI = baseURI;

        // Initialize tier-based pricing (example: first 1000 = 0.05 ETH, etc.)
        tierPricing[1000] = 0.05 ether;
        tierPricing[5000] = 0.08 ether;
        tierPricing[MAX_SUPPLY] = 0.1 ether;
    }

    /**
     * @dev Function to mint NFTs.
     * @param quantity Number of NFTs to mint.
     */
    function mint(uint256 quantity) external payable {
        require(totalSupply() + quantity <= MAX_SUPPLY, "Minting would exceed max supply");
        require(quantity > 0, "Quantity must be greater than zero");

        uint256 totalCost = 0;

        for (uint256 i = 1; i <= quantity; i++) {
            // Check if free mints are still available
            if (freeMintedCount < FREE_MINT_LIMIT) {
                freeMintedCount++;
            } else {
                // Determine tier-based pricing
                totalCost += _getMintPrice(totalSupply() + i);
            }
        }

        // Verify payment
        require(msg.value >= totalCost, "Insufficient ETH for minting");

        // Mint tokens
        for (uint256 i = 0; i < quantity; i++) {
            uint256 newTokenId = totalSupply() + 1;
            _safeMint(msg.sender, newTokenId);
            emit NFTMinted(msg.sender, newTokenId);
        }

        // Refund excess payment
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Internal function to get mint price based on tiers.
     * @param tokenId Token ID being minted.
     * @return Price for the given token ID.
     */
    function _getMintPrice(uint256 tokenId) internal view returns (uint256) {
        if (tokenId <= 1000) {
            return tierPricing[1000];
        } else if (tokenId <= 5000) {
            return tierPricing[5000];
        } else {
            return tierPricing[MAX_SUPPLY];
        }
    }

    /**
     * @dev Function to set base URI.
     * @param baseURI New base URI for the tokens.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override base URI function.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "Contract balance is zero");

        payable(owner()).transfer(balance);
    }
}
```
