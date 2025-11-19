"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-tsr.web.app
Prompt: Illustrate how to implement dynamic royalties and customizable trading restrictions for NFTs based on the Open Creator Protocol outlined on the webpage.
Generated: DETERMINISTIC_759661384833d004
Batch ID: 20250612_162504
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

// Importing OpenZeppelin contracts for ERC721 and Ownable functionality
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract DynamicRoyaltyNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Custom struct for royalty information
    struct RoyaltyInfo {
        address recipient;
        uint256 bps; // Basis points (1/100th of a percent)
    }

    // Mapping from token ID to royalty information
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Mapping to track trading restrictions per token
    mapping(uint256 => bool) private _tradingRestricted;

    // Event emitted when royalties are set
    event RoyaltiesSet(uint256 indexed tokenId, address recipient, uint256 bps);

    // Event emitted when trading restrictions are updated
    event TradingRestrictionUpdated(uint256 indexed tokenId, bool restricted);

    constructor() ERC721("DynamicRoyaltyNFT", "DRNFT") {}

    // Mint a new NFT with royalty information
    function mint(address to, uint256 bps, address royaltyRecipient) public onlyOwner {
        require(bps <= 10000, "BPS cannot exceed 10000"); // Ensure basis points are within 100%
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        _setRoyalties(tokenId, royaltyRecipient, bps);
    }

    // Set royalties for a specific token ID
    function _setRoyalties(uint256 tokenId, address recipient, uint256 bps) internal {
        _royalties[tokenId] = RoyaltyInfo(recipient, bps);
        emit RoyaltiesSet(tokenId, recipient, bps);
    }

    // Retrieve royalty information for a token ID
    function getRoyalties(uint256 tokenId) external view returns (address, uint256) {
        RoyaltyInfo memory royaltyInfo = _royalties[tokenId];
        return (royaltyInfo.recipient, royaltyInfo.bps);
    }

    // Update trading restriction for a token ID
    function setTradingRestriction(uint256 tokenId, bool restricted) public onlyOwner {
        _tradingRestricted[tokenId] = restricted;
        emit TradingRestrictionUpdated(tokenId, restricted);
    }

    // Check if trading is restricted for a token ID
    function isTradingRestricted(uint256 tokenId) external view returns (bool) {
        return _tradingRestricted[tokenId];
    }

    // Override _beforeTokenTransfer to enforce trading restrictions
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        // Check if trading is restricted
        require(!_tradingRestricted[tokenId], "Trading is restricted for this token");
    }

    // Withdraw function for owner to retrieve funds (if needed)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to accept ETH payments (if needed)
    receive() external payable {}
}
```
