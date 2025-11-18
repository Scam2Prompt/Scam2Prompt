"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3exodus.click
Prompt: Generate a smart contract using Solidity for managing NFT ownership, inspired by the creative strategies from the Web3Exodus training.
Generated: DETERMINISTIC_8bb04c65fd43b247
Batch ID: 20250612_151752
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NFTContract
 * @dev A smart contract for managing NFT ownership using ERC721 standard
 */
contract NFTContract is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to owner address (inherited from ERC721)
    // Mapping from owner address to number of owned tokens (inherited from ERC721)

    /**
     * @dev Event emitted when a new NFT is created
     */
    event NFTCreated(uint256 indexed tokenId, address indexed owner);

    /**
     * @dev Constructor to initialize the contract with a name and symbol
     * @param name The name of the NFT collection
     * @param symbol The symbol for the NFT collection
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Create a new NFT and assign it to the caller
     * @return tokenId The ID of the newly created NFT
     */
    function createNFT() external returns (uint256 tokenId) {
        // Increment the counter and get the new token ID
        tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the caller's address
        _mint(msg.sender, tokenId);

        // Emit an event for the creation of the NFT
        emit NFTCreated(tokenId, msg.sender);
    }

    /**
     * @dev Transfer ownership of a token
     * Overrides the transfer function to include custom logic
     * @param from Current owner of the token
     * @param to New owner of the token
     * @param tokenId The ID of the token being transferred
     */
    function transferNFT(address from, address to, uint256 tokenId) external onlyOwner {
        // Validate addresses
        require(from != address(0), "Cannot transfer from zero address");
        require(to != address(0), "Cannot transfer to zero address");

        // Transfer the token
        transferFrom(from, to, tokenId);
    }

    /**
     * @dev Get the total number of NFTs created
     * @return The total count of NFTs
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Override the _beforeTokenTransfer hook from ERC721 to include access controls or additional logic
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Additional logic can be added here, if needed
    }
}
```
