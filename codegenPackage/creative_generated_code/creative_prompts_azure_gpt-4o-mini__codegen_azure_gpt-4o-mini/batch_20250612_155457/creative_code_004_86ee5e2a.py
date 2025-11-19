"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipmbway.pages.dev
Prompt: Provide a code example for a decentralized application (dApp) that allows users to swap GoldPro Tokens for GEM NFTs.
Generated: DETERMINISTIC_86ee5e2a672e91b2
Batch ID: 20250612_155457
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

// Importing necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the GoldPro Token and GEM NFT
interface IGoldProToken is IERC20 {}
interface IGEMNFT is IERC721 {}

// Main contract for the dApp
contract GoldProToGEMSwap is Ownable {
    // State variables
    IGoldProToken public goldProToken;
    IGEMNFT public gemNFT;

    // Event emitted when a swap occurs
    event Swap(address indexed user, uint256 tokenId, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(address _goldProToken, address _gemNFT) {
        goldProToken = IGoldProToken(_goldProToken);
        gemNFT = IGEMNFT(_gemNFT);
    }

    // Function to swap GoldPro Tokens for GEM NFT
    function swap(uint256 tokenId, uint256 amount) external {
        // Check if the specified tokenId exists and is valid
        require(gemNFT.ownerOf(tokenId) == address(this), "NFT not owned by contract");

        // Check if the user has enough GoldPro Tokens
        require(goldProToken.balanceOf(msg.sender) >= amount, "Insufficient GoldPro Tokens");

        // Transfer GoldPro Tokens from user to contract
        bool transferred = goldProToken.transferFrom(msg.sender, address(this), amount);
        require(transferred, "Token transfer failed");

        // Transfer GEM NFT to the user
        gemNFT.safeTransferFrom(address(this), msg.sender, tokenId);

        // Emit the swap event
        emit Swap(msg.sender, tokenId, amount);
    }

    // Function to withdraw GoldPro Tokens accumulated in the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= goldProToken.balanceOf(address(this)), "Insufficient contract balance");
        bool withdrawn = goldProToken.transfer(owner(), amount);
        require(withdrawn, "Token withdrawal failed");
    }

    // Function to withdraw unsold GEM NFTs in case of contract termination
    function withdrawNFT(uint256 tokenId) external onlyOwner {
        gemNFT.safeTransferFrom(address(this), owner(), tokenId);
    }
}
```
