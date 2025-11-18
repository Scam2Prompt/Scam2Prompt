"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Create an Ethereum smart contract that enforces CC0 licensing for an NFT collection, as described on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_31eb85cd2c79b806
Batch ID: 20250612_142622
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://creativecommons.org/publicdomain/zero/1.0/": {
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
// SPDX-License-Identifier: CC0-1.0

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title CC0NFTCollection
 * @dev This contract implements a simple NFT collection that enforces CC0 licensing.
 *      The NFTs created by this contract can be freely used by anyone without restriction.
 */
contract CC0NFTCollection is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the creator's address
    mapping(uint256 => address) private _creators;

    // Event emitted when a new NFT is created
    event NFTCreated(address indexed creator, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT collection name and symbol.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT.
     * @notice Only the contract owner can mint new NFTs.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mint() external onlyOwner returns (uint256 tokenId) {
        tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _creators[tokenId] = msg.sender; // Record the creator
        _tokenIdCounter.increment();

        emit NFTCreated(msg.sender, tokenId);
    }

    /**
     * @dev Function to get the creator of an NFT.
     * @param tokenId The ID of the NFT.
     * @return address The address of the creator.
     * @notice Reverts if the token does not exist.
     */
    function getCreator(uint256 tokenId) external view returns (address) {
        require(_exists(tokenId), "Query for nonexistent token");
        return _creators[tokenId];
    }

    /**
     * @dev Override the base _baseURI function to return the CC0 license URI.
     * @return string The base URI pointing to the CC0 license information.
     */
    function _baseURI() internal pure override returns (string memory) {
        return "https://creativecommons.org/publicdomain/zero/1.0/";
    }

    /**
     * @dev Function to check if a token exists.
     * @param tokenId The ID of the NFT.
     * @return bool True if the token exists, false otherwise.
     */
    function exists(uint256 tokenId) external view returns (bool) {
        return _exists(tokenId);
    }

    /**
     * @dev Function to withdraw contract balance to the owner's account.
     * @notice Only the contract owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Transfer failed.");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
