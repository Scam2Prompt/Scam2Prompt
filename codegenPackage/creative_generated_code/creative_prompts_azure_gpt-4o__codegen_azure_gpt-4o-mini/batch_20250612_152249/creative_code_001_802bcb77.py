"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotclaim.pages.dev
Prompt: Generate code to burn $LOOT tokens and receive $xLOOT NFTs using the ERC-721 standard. Include functionality to calculate bonuses based on the amount of $LOOT burnt.
Generated: DETERMINISTIC_802bcb77e4304847
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LootBurner
 * @dev A contract to burn $LOOT tokens and mint corresponding $xLOOT NFTs.
 */
contract LootBurner is ERC721, Ownable {
    IERC20 public lootToken; // Reference to the $LOOT token contract
    uint256 public totalBurned; // Total amount of $LOOT burned
    uint256 public nextTokenId; // Token ID for the next NFT to be minted
    uint256 public bonusRate; // Bonus rate for $xLOOT NFTs based on $LOOT burned

    // Mapping from token ID to amount of $LOOT that was burnt for that NFT
    mapping(uint256 => uint256) public lootBurnedForToken;

    // Event emitted when a new $xLOOT NFT is minted
    event LootBurnedAndNFTMinted(address indexed user, uint256 indexed tokenId, uint256 lootAmount);

    /**
     * @dev Constructor that sets the $LOOT token address and the bonus rate.
     * @param _lootToken The address of the $LOOT token contract.
     * @param _bonusRate The rate at which bonuses are calculated.
     */
    constructor(IERC20 _lootToken, uint256 _bonusRate) ERC721("xLOOT", "xLOOT") {
        lootToken = _lootToken;
        bonusRate = _bonusRate; // E.g., 1000 = 10%
    }

    /**
     * @dev Burns a specified amount of $LOOT tokens and mints a new $xLOOT NFT.
     * @param amount The amount of $LOOT tokens to burn.
     */
    function burnLootAndMintNFT(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lootToken.balanceOf(msg.sender) >= amount, "Insufficient $LOOT balance");

        // Burn the specified amount of $LOOT tokens
        require(lootToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        totalBurned += amount;

        // Mint a new NFT
        uint256 tokenId = nextTokenId;
        _mint(msg.sender, tokenId);
        lootBurnedForToken[tokenId] = amount;
        nextTokenId++;

        emit LootBurnedAndNFTMinted(msg.sender, tokenId, amount);
    }

    /**
     * @dev Calculate the bonus based on the amount of $LOOT burned for a specific NFT.
     * @param tokenId The ID of the $xLOOT NFT.
     * @return The bonus amount calculated for the given tokenId.
     */
    function calculateBonus(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        uint256 lootAmount = lootBurnedForToken[tokenId];
        return (lootAmount * bonusRate) / 10000; // Example for bonus calculation
    }

    /**
     * @dev Allows the owner to withdraw the $LOOT tokens held by the contract.
     */
    function withdrawLoot() external onlyOwner {
        uint256 balance = lootToken.balanceOf(address(this));
        require(balance > 0, "No $LOOT to withdraw");
        require(lootToken.transfer(msg.sender, balance), "Transfer failed");
    }
}
```
