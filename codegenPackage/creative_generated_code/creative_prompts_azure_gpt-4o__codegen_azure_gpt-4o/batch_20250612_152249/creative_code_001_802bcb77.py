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

// Import ERC721 standard from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function burn(uint256 amount) external;
}

contract xLOOTNFT is ERC721Enumerable, Ownable, ReentrancyGuard {
    // Token counter for NFTs
    uint256 private _tokenCounter;

    // Address of the $LOOT ERC-20 token contract
    IERC20 public lootToken;

    // Event emitted when NFT is minted
    event NFTMinted(address indexed user, uint256 tokenId, uint256 amountBurned, uint256 bonus);

    // Constructor to initialize the NFT contract
    constructor(address _lootTokenAddress) ERC721("xLOOTNFT", "xLOOT") {
        require(_lootTokenAddress != address(0), "Invalid $LOOT token address");
        lootToken = IERC20(_lootTokenAddress);
        _tokenCounter = 0;
    }

    /**
     * @dev Burn $LOOT tokens and mint $xLOOT NFT
     * @param amount Amount of $LOOT tokens to burn
     */
    function burnLootAndMint(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        // Calculate bonus based on the amount burnt
        uint256 bonus = _calculateBonus(amount);

        // Transfer $LOOT tokens to this contract
        bool transferred = lootToken.transferFrom(msg.sender, address(this), amount);
        require(transferred, "Token transfer failed");

        // Burn the $LOOT tokens
        lootToken.burn(amount);

        // Mint xLOOT NFT
        uint256 tokenId = _mintNFT(msg.sender);

        // Emit event for minting
        emit NFTMinted(msg.sender, tokenId, amount, bonus);
    }

    /**
     * @dev Internal function to mint NFT
     * @param recipient Address of the recipient
     * @return tokenId The token ID of the minted NFT
     */
    function _mintNFT(address recipient) internal returns (uint256 tokenId) {
        tokenId = ++_tokenCounter;
        _safeMint(recipient, tokenId);
    }

    /**
     * @dev Calculate bonus based on $LOOT burnt
     * @param amount Amount of $LOOT tokens burnt
     * @return bonus Calculated bonus
     */
    function _calculateBonus(uint256 amount) internal pure returns (uint256 bonus) {
        // Example bonus calculation logic:
        // 1% bonus for every 100 $LOOT burnt
        bonus = (amount / 100) * 1;
    }

    /**
     * @dev Override `supportsInterface` to include ERC721Enumerable
     * @param interfaceId Interface ID to check
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
