"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotclaim.pages.dev
Prompt: Develop a Solidity function that verifies the minimum burn requirement of 15,000 $LOOT tokens before issuing $xLOOT NFTs and calculates bonuses for higher burn amounts.
Generated: DETERMINISTIC_532649b14d83f929
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

// Interface for ERC20 Token
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Interface for the NFT contract
interface IXLootNFT {
    function mintNFT(address recipient, uint256 bonus) external returns (uint256);
}

contract LootBurner {
    // State variables
    IERC20 public lootToken; // The $LOOT token contract
    IXLootNFT public xLootNFT; // The $xLOOT NFT contract

    // Minimum burn requirement
    uint256 public constant MIN_BURN_AMOUNT = 15000 * 10**18; // Adjust for token decimals

    // Event to log successful burns and NFT minting
    event BurnAndMint(address indexed user, uint256 amountBurned, uint256 bonus, uint256 tokenId);

    // Constructor to initialize the contract with token addresses
    constructor(address _lootToken, address _xLootNFT) {
        lootToken = IERC20(_lootToken);
        xLootNFT = IXLootNFT(_xLootNFT);
    }

    /**
     * @dev Burns $LOOT tokens and mints $xLOOT NFT based on the burn amount.
     * @param amount The amount of $LOOT tokens to burn.
     */
    function burnAndMint(uint256 amount) external {
        require(amount >= MIN_BURN_AMOUNT, "Insufficient LOOT burned. Minimum is 15,000 $LOOT.");
        
        // Transfer $LOOT tokens from sender to this contract
        bool transferred = lootToken.transferFrom(msg.sender, address(this), amount);
        require(transferred, "Token transfer failed.");

        // Calculate bonus based on burn amount (example calculation, adjust as needed)
        uint256 bonus = calculateBonus(amount);

        // Mint NFT for the sender
        uint256 tokenId = xLootNFT.mintNFT(msg.sender, bonus);

        // Emit an event for the burn and mint action
        emit BurnAndMint(msg.sender, amount, bonus, tokenId);
    }

    /**
     * @dev Calculates the bonus based on the amount of $LOOT burned.
     * @param amount The amount of $LOOT burned.
     * @return bonus The calculated bonus.
     */
    function calculateBonus(uint256 amount) internal pure returns (uint256) {
        // Example bonus calculation: 1% of the burned amount
        // Adjust logic as per requirements
        return amount / 100; // 1% bonus
    }
}
```
