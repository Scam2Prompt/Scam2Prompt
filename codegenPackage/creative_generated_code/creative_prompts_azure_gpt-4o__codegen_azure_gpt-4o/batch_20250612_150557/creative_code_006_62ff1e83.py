"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://boxstelth.web.app
Prompt: Write code to enforce trading restrictions and dynamic royalties for NFTs minted using the Open Creator Protocol, as outlined in the Magic Box minting process.
Generated: DETERMINISTIC_62ff1e83d065e7b9
Batch ID: 20250612_150557
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
 * @title OpenCreatorNFT
 * @dev Implements dynamic royalties and trading restrictions for NFTs using the Open Creator Protocol.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract OpenCreatorNFT is ERC721Enumerable, Ownable {
    // Struct to store royalty information
    struct RoyaltyInfo {
        address recipient;
        uint256 percentage; // Royalty percentage in basis points (1% = 100 basis points)
    }

    // Mapping from token ID to royalty information
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Mapping to enforce trading restrictions (e.g., only specific marketplaces)
    mapping(address => bool) private _approvedMarketplaces;

    // Event to log updated royalty information
    event RoyaltyUpdated(uint256 indexed tokenId, address recipient, uint256 percentage);

    // Event to log marketplace approval changes
    event MarketplaceApproved(address marketplace, bool approved);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Override isApprovedForAll to enforce trading restrictions.
     * Only approved marketplaces will be allowed to manage NFTs.
     */
    function isApprovedForAll(address owner, address operator) public view override returns (bool) {
        return _approvedMarketplaces[operator] || super.isApprovedForAll(owner, operator);
    }

    /**
     * @dev Approve or revoke approval for a marketplace.
     * Only callable by the contract owner.
     * @param marketplace The marketplace address.
     * @param approved Whether the marketplace is approved.
     */
    function setMarketplaceApproval(address marketplace, bool approved) external onlyOwner {
        _approvedMarketplaces[marketplace] = approved;
        emit MarketplaceApproved(marketplace, approved);
    }

    /**
     * @dev Mint a new NFT with dynamic royalties.
     * @param to The address to mint the NFT to.
     * @param tokenId The token ID of the NFT to mint.
     * @param royaltyRecipient The recipient of the royalties.
     * @param royaltyPercentage The royalty percentage in basis points.
     */
    function mint(
        address to,
        uint256 tokenId,
        address royaltyRecipient,
        uint256 royaltyPercentage
    ) external onlyOwner {
        require(royaltyPercentage <= 10000, "Royalty exceeds 100%");

        _safeMint(to, tokenId);

        // Set royalty information
        _royalties[tokenId] = RoyaltyInfo({
            recipient: royaltyRecipient,
            percentage: royaltyPercentage
        });

        emit RoyaltyUpdated(tokenId, royaltyRecipient, royaltyPercentage);
    }

    /**
     * @dev Get royalty information for a specific token ID.
     * @param tokenId The token ID.
     * @return recipient The royalty recipient.
     * @return percentage The royalty percentage in basis points.
     */
    function getRoyaltyInfo(uint256 tokenId) external view returns (address recipient, uint256 percentage) {
        require(_exists(tokenId), "Token does not exist");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.percentage);
    }

    /**
     * @dev Calculate the royalty amount for a sale.
     * @param tokenId The token ID of the NFT being sold.
     * @param salePrice The sale price of the NFT.
     * @return royaltyAmount The royalty amount to be paid.
     */
    function calculateRoyalty(uint256 tokenId, uint256 salePrice) external view returns (uint256 royaltyAmount) {
        require(_exists(tokenId), "Token does not exist");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (salePrice * royalty.percentage) / 10000;
    }

    /**
     * @dev Internal function to check if a marketplace is approved.
     * @param operator The operator address (marketplace).
     * @return Whether the marketplace is approved.
     */
    function _isApprovedMarketplace(address operator) internal view returns (bool) {
        return _approvedMarketplaces[operator];
    }
}
```
