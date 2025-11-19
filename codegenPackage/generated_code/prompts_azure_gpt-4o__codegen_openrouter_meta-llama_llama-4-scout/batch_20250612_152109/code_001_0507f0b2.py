"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.web.app
Prompt: Create a Solidity contract for an ERC-721 NFT that integrates MEV revenue sharing, ensuring holders receive 37.77% of MEV revenue as specified in the God Candle ecosystem.
Generated: DETERMINISTIC_0507f0b24043603a
Batch ID: 20250612_152109
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC721/ERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC721/extensions/ERC721URIStorage.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/Address.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC721/ERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/Address.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/math/SafeMath.sol";

/**
 * @title GodCandleNFT
 * @author [Your Name]
 * @notice ERC-721 NFT contract with MEV revenue sharing for God Candle ecosystem
 */
contract GodCandleNFT is ERC721URIStorage {
    using SafeMath for uint256;
    using Address for address;

    // MEV revenue sharing percentage for holders (37.77%)
    uint256 public constant MEV_REVENUE_SHARE = 3777;

    // Mapping of MEV revenue accrued for each token ID
    mapping(uint256 => uint256) public mevRevenueAccrued;

    // Mapping of MEV revenue shares for each address
    mapping(address => uint256) public mevRevenueShares;

    // Event emitted when MEV revenue is accrued
    event MevRevenueAccrued(uint256 indexed tokenId, uint256 amount);

    // Event emitted when MEV revenue is distributed
    event MevRevenueDistributed(address indexed to, uint256 amount);

    /**
     * @param name_ ERC-721 token name
     * @param symbol_ ERC-721 token symbol
     */
    constructor(string memory name_, string memory symbol_) ERC721(name_, symbol_) {}

    /**
     * @notice Mint a new NFT token
     * @param to Address to mint token to
     * @param tokenId Token ID to mint
     * @param uri Token URI
     */
    function mint(address to, uint256 tokenId, string memory uri) public onlyOwner {
        _mint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    /**
     * @notice Accrue MEV revenue for a token ID
     * @param tokenId Token ID to accrue revenue for
     * @param amount MEV revenue amount
     */
    function accrueMevRevenue(uint256 tokenId, uint256 amount) public onlyOwner {
        mevRevenueAccrued[tokenId] = mevRevenueAccrued[tokenId].add(amount);
        emit MevRevenueAccrued(tokenId, amount);
    }

    /**
     * @notice Distribute MEV revenue to token holders
     */
    function distributeMevRevenue() public onlyOwner {
        for (uint256 i = 0; i < totalSupply(); i++) {
            uint256 tokenId = i;
            address owner = ownerOf(tokenId);
            uint256 revenueShare = mevRevenueAccrued[tokenId].mul(MEV_REVENUE_SHARE) / 10000;
            mevRevenueShares[owner] = mevRevenueShares[owner].add(revenueShare);
            mevRevenueAccrued[tokenId] = 0;
            emit MevRevenueDistributed(owner, revenueShare);
        }
    }

    /**
     * @notice Withdraw MEV revenue share for an address
     */
    function withdrawMevRevenueShare() public {
        uint256 share = mevRevenueShares[msg.sender];
        require(share > 0, "No MEV revenue share to withdraw");
        mevRevenueShares[msg.sender] = 0;
        payable(msg.sender).transfer(share);
    }

    // Override _beforeTokenTransfer to ensure MEV revenue is distributed when tokens are transferred
    override function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal virtual override {
        for (uint256 i = 0; i < ids.length; i++) {
            uint256 tokenId = ids[i];
            if (from != address(0)) {
                // Distribute MEV revenue when token is transferred from non-zero address
                distributeMevRevenueForToken(tokenId);
            }
        }
        super._beforeTokenTransfer(from, to, ids);
    }

    // Distribute MEV revenue for a single token ID
    function distributeMevRevenueForToken(uint256 tokenId) internal {
        address owner = ownerOf(tokenId);
        uint256 revenueShare = mevRevenueAccrued[tokenId].mul(MEV_REVENUE_SHARE) / 10000;
        mevRevenueShares[owner] = mevRevenueShares[owner].add(revenueShare);
        mevRevenueAccrued[tokenId] = 0;
        emit MevRevenueDistributed(owner, revenueShare);
    }
}
```
