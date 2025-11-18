"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimanyinu.pages.dev
Prompt: Write a Solidity contract to mint soulbound receipt tokens for locked $AI tokens, ensuring compliance with the Diamond Hands app specifications.
Generated: DETERMINISTIC_f0b8e6f32a15faae
Batch ID: 20250612_152710
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

// Import OpenZeppelin's ERC721 contract
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// SoulboundReceiptToken contract that manages minting of soulbound tokens
contract SoulboundReceiptToken is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from user address to their locked $AI tokens
    mapping(address => uint256) public lockedAITokens;

    // Event emitted when a token is minted
    event TokenMinted(address indexed user, uint256 tokenId, uint256 lockedAmount);

    // Constructor to set the name and symbol of the token
    constructor() ERC721("SoulboundReceiptToken", "SRT") {}

    // Function to lock $AI tokens (dummy function for the example)
    // Only the owner can lock tokens
    function lockAITokens(address user, uint256 amount) external onlyOwner {
        // Simulate locking of tokens (this should interact with actual $AI token contract)
        lockedAITokens[user] += amount;
    }

    // Function to mint a soulbound token
    function mint() external {
        require(lockedAITokens[msg.sender] > 0, "No locked $AI tokens found");

        // Increment token ID and assign to user
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the token and assign it to the user
        _mint(msg.sender, tokenId);

        // Emit event for the minting
        emit TokenMinted(msg.sender, tokenId, lockedAITokens[msg.sender]);
    }

    // Function to retrieve the total locked $AI tokens for a user
    function getLockedAITokens(address user) external view returns (uint256) {
        return lockedAITokens[user];
    }

    // Function to withdraw locked $AI tokens (for simplicity)
    // Only the owner can withdraw tokens
    function withdrawAITokens(address user, uint256 amount) external onlyOwner {
        require(lockedAITokens[user] >= amount, "Insufficient locked tokens");
        lockedAITokens[user] -= amount;

        // Logic to transfer the tokens back to user (dummy)
        // This should interact with actual $AI token contract
    }
}
```
