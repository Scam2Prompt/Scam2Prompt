"""
Generated Code Metadata:
========================
Original URL: https://sol-boxs.web.app
Prompt: Write code to enforce trading restrictions and royalties on NFTs minted using the Open Creator Protocol, as highlighted in the Magic Box section.
Generated: DETERMINISTIC_340b92b7eb8cfdf7
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
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title OpenCreatorProtocolNFT
 * @dev ERC721 token with trading restrictions and royalties enforcement
 */
contract OpenCreatorProtocolNFT is ERC721, Ownable {
    using Address for address payable;

    struct RoyaltyInfo {
        address recipient;
        uint24 basisPoints;
    }

    // Mapping from token ID to royalty information
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Mapping from token ID to minimum price
    mapping(uint256 => uint256) private _minimumPrices;

    // Protocol fee basis points (e.g. 250 = 2.5%)
    uint24 public protocolFeeBasisPoints;

    // Protocol fee recipient
    address public protocolFeeRecipient;

    // Trading restriction flag
    bool public tradingRestricted;

    event RoyaltySet(uint256 indexed tokenId, address recipient, uint256 basisPoints);
    event MinimumPriceSet(uint256 indexed tokenId, uint256 minimumPrice);
    event ProtocolFeeUpdated(uint24 newFee, address newRecipient);
    event TradingRestrictionUpdated(bool restricted);

    /**
     * @dev Initializes the contract
     * @param name_ Token name
     * @param symbol_ Token symbol
     * @param feeRecipient_ Protocol fee recipient address
     * @param protocolFee_ Protocol fee basis points
     */
    constructor(
        string memory name_,
        string memory symbol_,
        address feeRecipient_,
        uint24 protocolFee_
    ) ERC721(name_, symbol_) {
        require(protocolFee_ <= 10000, "Fee exceeds maximum");
        protocolFeeRecipient = feeRecipient_;
        protocolFeeBasisPoints = protocolFee_;
    }

    /**
     * @dev Mints a new token
     * @param to Address to mint to
     * @param tokenId Token ID to mint
     * @param royaltyRecipient Address to receive royalties
     * @param royaltyBasisPoints Royalty percentage in basis points
     * @param minimumPrice Minimum price for the token
     */
    function mint(
        address to,
        uint256 tokenId,
        address royaltyRecipient,
        uint24 royaltyBasisPoints,
        uint256 minimumPrice
    ) external onlyOwner {
        require(royaltyBasisPoints <= 10000, "Royalty exceeds maximum");
        _safeMint(to, tokenId);
        
        _royalties[tokenId] = RoyaltyInfo(royaltyRecipient, royaltyBasisPoints);
        _minimumPrices[tokenId] = minimumPrice;
        
        emit RoyaltySet(tokenId, royaltyRecipient, royaltyBasisPoints);
        emit MinimumPriceSet(tokenId, minimumPrice);
    }

    /**
     * @dev Updates protocol fee settings
     * @param newFee New protocol fee in basis points
     * @param newRecipient New protocol fee recipient
     */
    function updateProtocolFee(uint24 newFee, address newRecipient) external onlyOwner {
        require(newFee <= 10000, "Fee exceeds maximum");
        protocolFeeBasisPoints = newFee;
        protocolFeeRecipient = newRecipient;
        emit ProtocolFeeUpdated(newFee, newRecipient);
    }

    /**
     * @dev Toggles trading restrictions
     * @param restricted New restriction status
     */
    function setTradingRestriction(bool restricted) external onlyOwner {
        tradingRestricted = restricted;
        emit TradingRestrictionUpdated(restricted);
    }

    /**
     * @dev Returns royalty info for a token
     * @param tokenId Token ID to query
     * @param salePrice Sale price of the token
     * @return receiver Royalty recipient address
     * @return royaltyAmount Royalty amount
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address receiver, uint256 royaltyAmount)
    {
        RoyaltyInfo memory royalty = _royalties[tokenId];
        royaltyAmount = (salePrice * royalty.basisPoints) / 10000;
        return (royalty.recipient, royaltyAmount);
    }

    /**
     * @dev Returns minimum price for a token
     * @param tokenId Token ID to query
     * @return Minimum price
     */
    function getMinimumPrice(uint256 tokenId) external view returns (uint256) {
        return _minimumPrices[tokenId];
    }

    /**
     * @dev Overrides transfer functions to enforce restrictions
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 /* batchSize */
    ) internal virtual override {
        if (from != address(0) && to != address(0) && tradingRestricted) {
            revert("Trading is currently restricted");
        }
    }

    /**
     * @dev Handles royalty payments on transfers
     */
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 tokenId,
        uint256 /* batchSize */
    ) internal virtual override {
        if (from != address(0) && to != address(0)) {
            // In a real implementation, this would integrate with a marketplace
            // to ensure proper royalty payments. This is a placeholder.
        }
    }

    /**
     * @dev Checks if a transfer would violate minimum price requirements
     * @param tokenId Token ID being transferred
     * @param value Value being paid for the transfer
     */
    function _checkMinimumPrice(uint256 tokenId, uint256 value) internal view {
        uint256 minimumPrice = _minimumPrices[tokenId];
        if (value < minimumPrice) {
            revert("Price below minimum required");
        }
    }

    /**
     * @dev EIP-2981 royalty info
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override returns (bool) {
        return
            interfaceId == 0x2a55205a || // ERC165 Interface ID for ERC2981
            super.supportsInterface(interfaceId);
    }
}
```
