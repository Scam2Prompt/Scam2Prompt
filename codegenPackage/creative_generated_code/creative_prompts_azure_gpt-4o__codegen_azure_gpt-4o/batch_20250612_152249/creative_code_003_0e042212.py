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

/**
 * @title LOOTBurnerNFTIssuer
 * @dev Smart contract to automate the burning of $LOOT tokens and issuance of $xLOOT NFTs.
 * Bonus NFT attributes are calculated based on predefined thresholds: 15K, 75K, 150K $LOOT.
 */

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function burn(uint256 amount) external;
}

interface IERC721 {
    function mint(address to, string memory uri) external;
}

contract LootBurnerNFTIssuer {
    IERC20 public lootToken;            // ERC20 $LOOT token contract
    IERC721 public xLootNFT;           // ERC721 $xLOOT NFT contract
    address public owner;              // Contract owner
    
    // Define the thresholds for bonus calculations
    uint256 public constant BONUS_THRESHOLD_1 = 15000;    // 15K $LOOT
    uint256 public constant BONUS_THRESHOLD_2 = 75000;    // 75K $LOOT
    uint256 public constant BONUS_THRESHOLD_3 = 150000;   // 150K $LOOT
    
    // Events
    event LootBurned(address indexed user, uint256 lootAmount);
    event NFTIssued(address indexed user, string nftUri);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the ERC20 and ERC721 contract addresses and the owner.
     * @param _lootToken Address of the $LOOT token contract.
     * @param _xLootNFT Address of the $xLOOT NFT contract.
     */
    constructor(address _lootToken, address _xLootNFT) {
        lootToken = IERC20(_lootToken);
        xLootNFT = IERC721(_xLootNFT);
        owner = msg.sender;
    }

    /**
     * @dev Function to burn $LOOT tokens and issue $xLOOT NFT.
     * @param lootAmount Amount of $LOOT tokens to burn.
     */
    function burnLootAndIssueNFT(uint256 lootAmount) external {
        require(lootAmount > 0, "Loot amount must be greater than zero");
        require(lootToken.balanceOf(msg.sender) >= lootAmount, "Insufficient LOOT balance");
        
        // Transfer $LOOT tokens from the user to this contract
        bool transferSuccess = lootToken.transferFrom(msg.sender, address(this), lootAmount);
        require(transferSuccess, "Failed to transfer LOOT tokens");

        // Burn the transferred LOOT tokens
        lootToken.burn(lootAmount);
        emit LootBurned(msg.sender, lootAmount);

        // Calculate bonus and determine NFT URI based on thresholds
        string memory nftUri = calculateNFTUri(lootAmount);

        // Mint the $xLOOT NFT to the user
        xLootNFT.mint(msg.sender, nftUri);
        emit NFTIssued(msg.sender, nftUri);
    }

    /**
     * @dev Internal function to calculate NFT URI based on burn thresholds.
     * @param lootAmount Amount of $LOOT tokens burned.
     * @return nftUri URI of the issued NFT.
     */
    function calculateNFTUri(uint256 lootAmount) internal pure returns (string memory) {
        if (lootAmount >= BONUS_THRESHOLD_3) {
            return "ipfs://bonus_tier_3";
        } else if (lootAmount >= BONUS_THRESHOLD_2) {
            return "ipfs://bonus_tier_2";
        } else if (lootAmount >= BONUS_THRESHOLD_1) {
            return "ipfs://bonus_tier_1";
        } else {
            return "ipfs://standard_tier";
        }
    }

    /**
     * @dev Function to update ERC20 and ERC721 contract addresses (only owner).
     * @param _lootToken Address of the new $LOOT token contract.
     * @param _xLootNFT Address of the new $xLOOT NFT contract.
     */
    function updateContracts(address _lootToken, address _xLootNFT) external onlyOwner {
        lootToken = IERC20(_lootToken);
        xLootNFT = IERC721(_xLootNFT);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }
}
```
