"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotclaim.pages.dev
Prompt: Write a smart contract in Solidity that automates the burning of $LOOT tokens and issuance of $xLOOT NFTs with bonus calculations based on thresholds (e.g., 15K, 75K, 150K $LOOT).
Generated: DETERMINISTIC_0e04221201c12f68
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the LOOT Token
contract LootToken is IERC20 {
    // ... IERC20 implementation ...
}

// Contract for the xLOOT NFTs
contract XLootNFT is ERC721, Ownable {
    uint256 public nextTokenId;

    constructor() ERC721("xLOOT", "xLOOT") {}

    function mint(address to) external onlyOwner returns (uint256) {
        uint256 tokenId = nextTokenId;
        nextTokenId++;
        _mint(to, tokenId);
        return tokenId;
    }
}

// Main contract for burning LOOT and minting xLOOT NFTs
contract LootBurnAndMint is Ownable {
    IERC20 public lootToken;          // Reference to the LOOT token
    XLootNFT public xLootNFT;        // Reference to the xLOOT NFT contract

    mapping(address => uint256) public userLootBurned; // Track how much LOOT each user has burned

    // Bonus thresholds
    uint256[] public bonusThresholds = [15000 * 10**18, 75000 * 10**18, 150000 * 10**18];
    uint256[] public bonusAmounts = [1, 5, 10]; // Corresponding xLOOT NFTs for each threshold

    event LootBurned(address indexed user, uint256 amount, uint256 tokenId);

    constructor(address _lootToken, address _xLootNFT) {
        lootToken = IERC20(_lootToken);
        xLootNFT = XLootNFT(_xLootNFT);
    }

    // Function to burn LOOT tokens and mint xLOOT NFTs
    function burnLootAndMint(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lootToken.balanceOf(msg.sender) >= amount, "Insufficient LOOT balance");

        // Transfer LOOT from user to this contract (burning)
        lootToken.transferFrom(msg.sender, address(0), amount);
        userLootBurned[msg.sender] += amount;

        // Calculate the number of NFTs to mint based on burned amount
        uint256 tokenIdToMint = calculateBonus(msg.sender);
        emit LootBurned(msg.sender, amount, tokenIdToMint);
    }

    // Function to calculate bonus xLOOT NFTs based on burned amount
    function calculateBonus(address user) internal view returns (uint256) {
        uint256 totalBurned = userLootBurned[user];
        uint256 nftCount = 0;

        // Check thresholds and calculate NFTs to mint
        for (uint256 i = 0; i < bonusThresholds.length; i++) {
            if (totalBurned >= bonusThresholds[i]) {
                nftCount += bonusAmounts[i];
            }
        }

        // Mint the corresponding xLOOT NFTs for the user
        for (uint256 i = 0; i < nftCount; i++) {
            xLootNFT.mint(user);
        }

        return nftCount;
    }

    // Function to set new thresholds and bonus amounts (only owner can call)
    function setBonusThresholds(uint256[] calldata thresholds, uint256[] calldata amounts) external onlyOwner {
        require(thresholds.length == amounts.length, "Arrays must be the same length");
        bonusThresholds = thresholds;
        bonusAmounts = amounts;
    }

    // Function to withdraw any accidentally sent ERC20 tokens
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
