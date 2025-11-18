"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlootbot.pages.dev
Prompt: Generate a Solidity smart contract that implements the burning mechanism for $LOOT tokens, ensuring that users receive $xLOOT NFTs (ERC-721) based on the burn amount and bonus tiers described on the LootBot dashboard.
Generated: DETERMINISTIC_6c8776a428d16784
Batch ID: 20250612_153648
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

// Importing OpenZeppelin libraries for ERC-20 and ERC-721 standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LootBurnerNFT is ERC721Enumerable, Ownable {
    // $LOOT token contract
    IERC20 public lootToken;

    // Token ID counter for $xLOOT NFTs
    uint256 private tokenIdCounter;

    // Event emitted after successful burn
    event LootBurned(address indexed burner, uint256 amountBurned, uint256 tokenId);

    // Bonus tiers
    struct BonusTier {
        uint256 minAmount; // Minimum amount of $LOOT required to unlock this tier
        uint256 bonusMultiplier; // Multiplier for the NFT based on the tier
    }

    BonusTier[] public bonusTiers;

    // Mapping to store metadata for minted NFTs (optional: if additional data is needed for NFTs)
    mapping(uint256 => uint256) public nftMetadata;

    // Constructor to initialize the contract
    constructor(address _lootTokenAddress) ERC721("xLOOT NFT", "xLOOT") {
        require(_lootTokenAddress != address(0), "Invalid $LOOT token address");
        lootToken = IERC20(_lootTokenAddress);
    }

    /**
     * @dev Function to set bonus tiers. Callable only by the owner.
     * @param _tiers Array of bonus tier structures.
     */
    function setBonusTiers(BonusTier[] memory _tiers) external onlyOwner {
        delete bonusTiers; // Clear existing tiers
        for (uint256 i = 0; i < _tiers.length; i++) {
            bonusTiers.push(_tiers[i]);
        }
    }

    /**
     * @dev Function to burn $LOOT tokens and receive an $xLOOT NFT.
     * @param burnAmount Amount of $LOOT tokens to burn.
     */
    function burnLoot(uint256 burnAmount) external {
        require(burnAmount > 0, "Burn amount must be greater than zero");

        // Transfer $LOOT tokens from the sender to this contract
        bool success = lootToken.transferFrom(msg.sender, address(this), burnAmount);
        require(success, "Token transfer failed");

        // Calculate bonus multiplier based on the burn amount and tier
        uint256 bonusMultiplier = getBonusMultiplier(burnAmount);

        // Mint the NFT to the sender
        uint256 newTokenId = tokenIdCounter++;
        _mint(msg.sender, newTokenId);

        // Store metadata (optional)
        nftMetadata[newTokenId] = bonusMultiplier;

        // Emit event
        emit LootBurned(msg.sender, burnAmount, newTokenId);
    }

    /**
     * @dev Internal function to determine the bonus multiplier based on burn amount.
     * @param burnAmount Amount of $LOOT tokens burned.
     * @return Bonus multiplier for the NFT.
     */
    function getBonusMultiplier(uint256 burnAmount) internal view returns (uint256) {
        uint256 multiplier = 1; // Default multiplier
        for (uint256 i = 0; i < bonusTiers.length; i++) {
            if (burnAmount >= bonusTiers[i].minAmount) {
                multiplier = bonusTiers[i].bonusMultiplier;
            }
        }
        return multiplier;
    }

    /**
     * @dev Function to withdraw $LOOT tokens from the contract. Callable only by the owner.
     * @param to Address to send the tokens to.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        bool success = lootToken.transfer(to, amount);
        require(success, "Token transfer failed");
    }
}
```
