"""
Generated Code Metadata:
========================
Original URL: https://topgtest.vercel.app
Prompt: Outline a smart contract in Solidity for managing the distribution of 50 ETH NFTs in a fair manner.
Generated: DETERMINISTIC_fa2b0e603910e874
Batch ID: 20250612_161224
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title FairNFTDistribution
 * @dev A smart contract for managing the distribution of 50 ETH NFTs in a fair manner.
 */
contract FairNFTDistribution is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking the number of NFTs minted
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_NFTS = 50;

    // Mapping to track if an address has already claimed an NFT
    mapping(address => bool) public hasClaimed;

    // Event emitted when an NFT is successfully claimed
    event NFTClaimed(address indexed claimant, uint256 tokenId);

    /**
     * @dev Constructor to initialize the contract with a name and symbol for the NFT.
     */
    constructor() ERC721("FairNFT", "FNFT") {}

    /**
     * @dev Function to claim an NFT. Can only be called if the maximum supply has not been reached.
     * Requires that the caller has not already claimed an NFT.
     */
    function claimNFT() external {
        require(_tokenIdCounter.current() < MAX_NFTS, "All NFTs have been claimed");
        require(!hasClaimed[msg.sender], "You have already claimed an NFT");

        // Increment the token ID counter and mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        hasClaimed[msg.sender] = true;

        _mint(msg.sender, tokenId);
        emit NFTClaimed(msg.sender, tokenId);
    }

    /**
     * @dev Function to withdraw any ETH from the contract. Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Function to receive ETH. This allows the contract to accept ETH.
     */
    receive() external payable {}

    /**
     * @dev Function to get the current number of NFTs minted.
     * @return The current count of minted NFTs.
     */
    function currentSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
