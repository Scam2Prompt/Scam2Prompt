"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgtest.vercel.app
Prompt: Outline a smart contract in Solidity for managing the distribution of 50 ETH NFTs in a fair manner.
Generated: DETERMINISTIC_fa2b0e603910e874
Batch ID: 20250612_161224
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
 * @title FairNFTDistribution
 * @dev A smart contract for managing the distribution of 50 ETH NFTs.
 */
contract FairNFTDistribution is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Total supply of NFTs
    uint256 public constant MAX_SUPPLY = 50;

    // Mapping to track if an address has already claimed an NFT
    mapping(address => bool) public hasClaimed;

    // Event to emit when an NFT is claimed
    event NFTClaimed(address indexed claimant, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the NFT contract.
     */
    constructor() ERC721("FairNFT", "FNFT") {}

    /**
     * @dev Function to claim an NFT. Can only be called if there are NFTs available.
     */
    function claimNFT() external {
        // Check if the maximum supply of NFTs has been reached
        require(_tokenIdCounter.current() < MAX_SUPPLY, "All NFTs have been claimed.");

        // Check if the caller has already claimed an NFT
        require(!hasClaimed[msg.sender], "You have already claimed an NFT.");

        // Mark the caller as having claimed an NFT
        hasClaimed[msg.sender] = true;

        // Increment the token ID counter and mint the new NFT
        uint256 newTokenId = _tokenIdCounter.current();
        _mint(msg.sender, newTokenId);

        // Emit an event for the claimed NFT
        emit NFTClaimed(msg.sender, newTokenId);

        // Increment the counter for the next token ID
        _tokenIdCounter.increment();
    }

    /**
     * @dev Function to withdraw any ETH sent to the contract.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw.");

        // Transfer the balance to the owner
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Transfer failed.");
    }

    /**
     * @dev Function to receive ETH. This can be used to fund the contract.
     */
    receive() external payable {}
}
```
