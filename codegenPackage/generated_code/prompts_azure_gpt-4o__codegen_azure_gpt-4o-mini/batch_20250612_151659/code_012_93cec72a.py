"""
Generated Code Metadata:
========================
Original URL: https://clashofdragonz-mint.com
Prompt: Write a Solidity contract for distributing free tokens to NFT holders based on their rarity tier, as outlined in the Clash of DragonZ token creation roadmap.
Generated: DETERMINISTIC_93cec72a450f0bb9
Batch ID: 20250612_151659
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the NFT contract to check ownership and rarity
interface INFT {
    function ownerOf(uint256 tokenId) external view returns (address);
    function getRarityTier(uint256 tokenId) external view returns (uint256);
}

// TokenDistributor contract for distributing tokens to NFT holders
contract TokenDistributor is Ownable {
    // Reference to the ERC20 token contract
    IERC20 public token;
    // Reference to the NFT contract
    INFT public nftContract;

    // Mapping to track the amount of tokens distributed to each NFT holder
    mapping(address => uint256) public tokensDistributed;

    // Rarity tier to token amount mapping
    mapping(uint256 => uint256) public rarityToTokenAmount;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Constructor to initialize the token and NFT contract addresses
    constructor(address _tokenAddress, address _nftContractAddress) {
        token = IERC20(_tokenAddress);
        nftContract = INFT(_nftContractAddress);
        
        // Set token amounts for each rarity tier (example values)
        rarityToTokenAmount[1] = 100 * 10 ** 18; // Common
        rarityToTokenAmount[2] = 200 * 10 ** 18; // Uncommon
        rarityToTokenAmount[3] = 500 * 10 ** 18; // Rare
        rarityToTokenAmount[4] = 1000 * 10 ** 18; // Epic
        rarityToTokenAmount[5] = 2000 * 10 ** 18; // Legendary
    }

    // Function to distribute tokens to NFT holders based on their rarity tier
    function distributeTokens(uint256[] calldata tokenIds) external onlyOwner {
        require(tokenIds.length > 0, "No token IDs provided");

        for (uint256 i = 0; i < tokenIds.length; i++) {
            uint256 tokenId = tokenIds[i];
            address owner = nftContract.ownerOf(tokenId);
            uint256 rarityTier = nftContract.getRarityTier(tokenId);
            uint256 amountToDistribute = rarityToTokenAmount[rarityTier];

            // Ensure the owner has not already received tokens for this NFT
            require(tokensDistributed[owner] < amountToDistribute, "Tokens already distributed to this owner");

            // Update the distributed tokens mapping
            tokensDistributed[owner] += amountToDistribute;

            // Transfer tokens to the NFT owner
            require(token.balanceOf(address(this)) >= amountToDistribute, "Insufficient contract balance");
            token.transfer(owner, amountToDistribute);

            // Emit an event for the distribution
            emit TokensDistributed(owner, amountToDistribute);
        }
    }

    // Function to withdraw any remaining tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.transfer(msg.sender, amount);
    }

    // Function to update the token amount for a specific rarity tier
    function updateRarityTokenAmount(uint256 rarityTier, uint256 amount) external onlyOwner {
        rarityToTokenAmount[rarityTier] = amount;
    }
}
```
