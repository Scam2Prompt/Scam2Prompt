"""
Generated Code Metadata:
========================
Original URL: https://boxstelth.web.app
Prompt: Write code to enforce trading restrictions and dynamic royalties for NFTs minted using the Open Creator Protocol, as outlined in the Magic Box minting process.
Generated: DETERMINISTIC_62ff1e83d065e7b9
Batch ID: 20250612_150557
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/interfaces/IERC2981.sol";

contract OpenCreatorProtocolNFT is ERC721, IERC2981, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct RoyaltyInfo {
        address recipient;
        uint24 basisPoints;
    }

    struct TradingRestriction {
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    mapping(uint256 => RoyaltyInfo) private _tokenRoyalties;
    mapping(uint256 => TradingRestriction) private _tokenTradingRestrictions;
    mapping(address => bool) private _approvedMarketplaces;

    event RoyaltyUpdated(uint256 tokenId, address recipient, uint256 basisPoints);
    event TradingRestrictionUpdated(uint256 tokenId, uint256 startTime, uint256 endTime, bool isActive);
    event MarketplaceApprovalUpdated(address marketplace, bool isApproved);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    function safeMint(
        address to,
        string memory tokenURI,
        address royaltyRecipient,
        uint24 royaltyBasisPoints,
        uint256 tradingStartTime,
        uint256 tradingEndTime
    ) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);
        
        _setTokenRoyalty(tokenId, royaltyRecipient, royaltyBasisPoints);
        _setTradingRestriction(tokenId, tradingStartTime, tradingEndTime, true);
    }

    function _setTokenRoyalty(
        uint256 tokenId,
        address recipient,
        uint24 basisPoints
    ) internal {
        require(basisPoints <= 10000, "Royalty exceeds 100%");
        _tokenRoyalties[tokenId] = RoyaltyInfo(recipient, basisPoints);
        emit RoyaltyUpdated(tokenId, recipient, basisPoints);
    }

    function updateTokenRoyalty(
        uint256 tokenId,
        address recipient,
        uint24 basisPoints
    ) external onlyOwner {
        require(_exists(tokenId), "Nonexistent token");
        _setTokenRoyalty(tokenId, recipient, basisPoints);
    }

    function _setTradingRestriction(
        uint256 tokenId,
        uint256 startTime,
        uint256 endTime,
        bool isActive
    ) internal {
        require(startTime < endTime, "Invalid time range");
        _tokenTradingRestrictions[tokenId] = TradingRestriction(startTime, endTime, isActive);
        emit TradingRestrictionUpdated(tokenId, startTime, endTime, isActive);
    }

    function updateTradingRestriction(
        uint256 tokenId,
        uint256 startTime,
        uint256 endTime,
        bool isActive
    ) external onlyOwner {
        require(_exists(tokenId), "Nonexistent token");
        _setTradingRestriction(tokenId, startTime, endTime, isActive);
    }

    function approveMarketplace(address marketplace, bool isApproved) external onlyOwner {
        _approvedMarketplaces[marketplace] = isApproved;
        emit MarketplaceApprovalUpdated(marketplace, isApproved);
    }

    function isMarketplaceApproved(address marketplace) public view returns (bool) {
        return _approvedMarketplaces[marketplace];
    }

    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        override
        returns (address receiver, uint256 royaltyAmount)
    {
        require(_exists(tokenId), "Nonexistent token");
        RoyaltyInfo memory royalty = _tokenRoyalties[tokenId];
        royaltyAmount = (salePrice * royalty.basisPoints) / 10000;
        return (royalty.recipient, royaltyAmount);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0) && to != address(0)) { // Skip for minting and burning
            TradingRestriction memory restriction = _tokenTradingRestrictions[tokenId];
            if (restriction.isActive) {
                require(
                    block.timestamp >= restriction.startTime && block.timestamp <= restriction.endTime,
                    "Token trading is restricted at this time"
                );
            }
        }
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, IERC165)
        returns (bool)
    {
        return
            interfaceId == type(IERC2981).interfaceId ||
            super.supportsInterface(interfaceId);
    }
}
```
