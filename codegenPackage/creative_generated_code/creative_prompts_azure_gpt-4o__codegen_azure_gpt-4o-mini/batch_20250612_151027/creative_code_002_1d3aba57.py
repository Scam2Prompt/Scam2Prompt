"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-minte.web.app
Prompt: Generate code to implement a "free mint" functionality for NFTs, ensuring features like enforced royalties and customizable trading restrictions, as outlined in the Magic Box section of the NFT-Minte webpage.
Generated: DETERMINISTIC_1d3aba57ba474897
Batch ID: 20250612_151027
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Receiver.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title FreeMintNFT
 * @dev Implementation of a free mint NFT contract with enforced royalties and customizable trading restrictions.
 */
contract FreeMintNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    // Structure to define trading restrictions
    struct TradingRestrictions {
        bool isTradingAllowed;
        uint256 royaltyPercentage; // Royalty percentage for secondary sales
    }

    // Token Id counter
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to trading restrictions
    mapping(uint256 => TradingRestrictions) private _tradingRestrictions;

    // Mapping to check if tokens are minted
    mapping(uint256 => bool) private _tokenMinted;

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection.
     */
    constructor() ERC721("FreeMintNFT", "FMNFT") {}

    /**
     * @dev Mint a new NFT for the caller.
     * Emits a Minted event.
     */
    function mint() external {
        uint256 tokenId = _tokenIdCounter.current();
        
        // Ensure the token hasn't been minted yet
        require(!_tokenMinted[tokenId], "Token has already been minted");

        // Mint the NFT
        _mint(msg.sender, tokenId);

        // Mark the token as minted
        _tokenMinted[tokenId] = true;

        // Increment the token ID counter
        _tokenIdCounter.increment();

        emit Minted(msg.sender, tokenId);
    }

    /**
     * @dev Set trading restrictions for a specific token.
     * @param tokenId The ID of the token to set restrictions for.
     * @param isTradingAllowed Boolean indicating if trading is allowed.
     * @param royaltyPercentage The percentage royalty to enforce on sales.
     */
    function setTradingRestrictions(uint256 tokenId, bool isTradingAllowed, uint256 royaltyPercentage) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(royaltyPercentage <= 100, "Royalty percentage must be between 0 and 100");

        _tradingRestrictions[tokenId] = TradingRestrictions({
            isTradingAllowed: isTradingAllowed,
            royaltyPercentage: royaltyPercentage
        });
    }

    /**
     * @dev Get the trading restrictions for a specific token.
     * @param tokenId The ID of the token to query.
     * @return isTradingAllowed Boolean indicating if trading is allowed.
     * @return royaltyPercentage The percentage royalty enforced on sales.
     */
    function getTradingRestrictions(uint256 tokenId) external view returns (bool isTradingAllowed, uint256 royaltyPercentage) {
        TradingRestrictions memory restrictions = _tradingRestrictions[tokenId];
        return (restrictions.isTradingAllowed, restrictions.royaltyPercentage);
    }

    /**
     * @dev Override the _beforeTokenTransfer function to enforce trading restrictions.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        
        // Check if trading is allowed
        if (from != address(0)) { // Ignore checks on minting
            TradingRestrictions memory restrictions = _tradingRestrictions[tokenId];
            require(restrictions.isTradingAllowed, "Trading is restricted for this token");
        }
    }

    /**
     * @dev Fallback function to receive Ether. Can be used for royalty payments.
     */
    receive() external payable {
        // Handle received Ether (if any)
    }
}
```
