"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Create a Solidity smart contract that allows users to mint NFTs from the MegaRabbit collection, ensuring it adheres to the specified limits per wallet.
Generated: DETERMINISTIC_206581bd643aec1c
Batch ID: 20250612_162811
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

// Import ERC721 and Ownable contracts from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MegaRabbitNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Token ID counter
    Counters.Counter private _tokenIds;

    // Maximum NFTs allowed per wallet
    uint256 public constant MAX_PER_WALLET = 5;

    // Mapping to track minted tokens per wallet
    mapping(address => uint256) private _mintedPerWallet;

    // Base URI for metadata
    string private _baseTokenURI;

    // Constructor to initialize the contract
    constructor(string memory baseURI) ERC721("MegaRabbitNFT", "MRNFT") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @param numberOfTokens Number of NFTs to mint.
     */
    function mint(uint256 numberOfTokens) external {
        // Ensure requested mint amount is positive
        require(numberOfTokens > 0, "Must mint at least one NFT");

        // Check wallet mint limit
        require(
            _mintedPerWallet[msg.sender] + numberOfTokens <= MAX_PER_WALLET,
            "Minting exceeds wallet limit"
        );

        // Mint specified number of NFTs
        for (uint256 i = 0; i < numberOfTokens; i++) {
            _tokenIds.increment();
            uint256 newTokenId = _tokenIds.current();

            // Mint the token
            _safeMint(msg.sender, newTokenId);
        }

        // Update wallet's minted count
        _mintedPerWallet[msg.sender] += numberOfTokens;
    }

    /**
     * @dev Function to check how many NFTs a wallet has minted.
     * @param wallet Address of the wallet to check.
     * @return Number of NFTs minted by the wallet.
     */
    function mintedCount(address wallet) external view returns (uint256) {
        return _mintedPerWallet[wallet];
    }

    /**
     * @dev Override baseURI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Function to update the base URI for metadata.
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }
}
```
