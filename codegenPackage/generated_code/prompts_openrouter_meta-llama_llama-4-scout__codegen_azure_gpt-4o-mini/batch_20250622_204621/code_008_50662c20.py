"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-ie.web.app
Prompt: "Propose a new feature for Kangamoon's Play-to-Earn game that integrates NFT rewards, including how it could be implemented using their existing smart contract and tokenomics."
Generated: DETERMINISTIC_50662c20f36d65a9
Batch ID: 20250622_204621
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the existing Kangamoon token contract
interface IKangamoonToken {
    function mint(address to, uint256 amount) external;
}

// NFT contract for rewards in the Play-to-Earn game
contract KangamoonNFTRewards is ERC721, Ownable {
    // Mapping from token ID to the player's address
    mapping(uint256 => address) private _owners;

    // Counter for the next token ID
    uint256 private _nextTokenId;

    // Reference to the existing Kangamoon token contract
    IKangamoonToken public kangamoonToken;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed player, uint256 tokenId);

    // Constructor to initialize the NFT contract and the token contract reference
    constructor(address tokenAddress) ERC721("KangamoonRewardNFT", "KRNFT") {
        kangamoonToken = IKangamoonToken(tokenAddress);
    }

    // Function to mint a new NFT as a reward
    function mintRewardNFT(address player) external onlyOwner {
        require(player != address(0), "Invalid address");

        // Mint the NFT
        uint256 tokenId = _nextTokenId++;
        _mint(player, tokenId);
        _owners[tokenId] = player;

        // Emit the NFT minted event
        emit NFTMinted(player, tokenId);
    }

    // Function to reward players with Kangamoon tokens when they earn an NFT
    function rewardPlayerWithTokens(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        // Mint the specified amount of Kangamoon tokens to the player
        kangamoonToken.mint(player, amount);
    }

    // Function to get the owner of a specific NFT
    function ownerOfNFT(uint256 tokenId) external view returns (address) {
        return _owners[tokenId];
    }

    // Function to get the next token ID (for testing purposes)
    function getNextTokenId() external view returns (uint256) {
        return _nextTokenId;
    }
}
```
