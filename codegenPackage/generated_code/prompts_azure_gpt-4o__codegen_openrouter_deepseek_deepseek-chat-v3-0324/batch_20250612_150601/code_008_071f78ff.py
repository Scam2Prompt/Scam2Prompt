"""
Generated Code Metadata:
========================
Original URL: https://nft-trades.web.app
Prompt: Create a function to enforce dynamic royalties and trading restrictions for NFTs minted using the Open Creator Protocol, as described in the Magic Box minting process.
Generated: DETERMINISTIC_071f78ffe6178871
Batch ID: 20250612_150601
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract OpenCreatorProtocolNFT is ERC721, Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    struct RoyaltyInfo {
        address recipient;
        uint24 basisPoints;
    }

    struct TradingRestriction {
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    // Token ID to royalty info mapping
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Token ID to trading restriction mapping
    mapping(uint256 => TradingRestriction) private _tradingRestrictions;

    // Addresses with special permissions
    EnumerableSet.AddressSet private _operators;

    // Events
    event RoyaltySet(uint256 indexed tokenId, address recipient, uint24 basisPoints);
    event TradingRestrictionSet(uint256 indexed tokenId, uint256 startTime, uint256 endTime, bool isActive);
    event OperatorAdded(address indexed operator);
    event OperatorRemoved(address indexed operator);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    modifier onlyOperatorOrOwner() {
        require(
            _operators.contains(msg.sender) || msg.sender == owner(),
            "Caller is not operator or owner"
        );
        _;
    }

    /**
     * @dev Mint a new NFT with optional royalty and trading restrictions
     */
    function mint(
        address to,
        uint256 tokenId,
        address royaltyRecipient,
        uint24 royaltyBasisPoints,
        uint256 restrictionStartTime,
        uint256 restrictionEndTime
    ) external onlyOperatorOrOwner {
        _safeMint(to, tokenId);

        if (royaltyRecipient != address(0) && royaltyBasisPoints > 0) {
            _setRoyaltyInfo(tokenId, royaltyRecipient, royaltyBasisPoints);
        }

        if (restrictionEndTime > block.timestamp) {
            _setTradingRestriction(
                tokenId,
                restrictionStartTime,
                restrictionEndTime,
                true
            );
        }
    }

    /**
     * @dev Set royalty information for a specific token
     */
    function setRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint24 basisPoints
    ) external onlyOperatorOrOwner {
        require(_exists(tokenId), "Nonexistent token");
        _setRoyaltyInfo(tokenId, recipient, basisPoints);
    }

    function _setRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint24 basisPoints
    ) private {
        require(basisPoints <= 10000, "Royalty exceeds 100%");
        _royalties[tokenId] = RoyaltyInfo(recipient, basisPoints);
        emit RoyaltySet(tokenId, recipient, basisPoints);
    }

    /**
     * @dev Get royalty information for a specific token
     */
    function getRoyaltyInfo(uint256 tokenId)
        external
        view
        returns (address, uint24)
    {
        require(_exists(tokenId), "Nonexistent token");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.basisPoints);
    }

    /**
     * @dev Set trading restrictions for a specific token
     */
    function setTradingRestriction(
        uint256 tokenId,
        uint256 startTime,
        uint256 endTime,
        bool isActive
    ) external onlyOperatorOrOwner {
        require(_exists(tokenId), "Nonexistent token");
        _setTradingRestriction(tokenId, startTime, endTime, isActive);
    }

    function _setTradingRestriction(
        uint256 tokenId,
        uint256 startTime,
        uint256 endTime,
        bool isActive
    ) private {
        require(endTime > startTime, "Invalid time range");
        _tradingRestrictions[tokenId] = TradingRestriction(
            startTime,
            endTime,
            isActive
        );
        emit TradingRestrictionSet(tokenId, startTime, endTime, isActive);
    }

    /**
     * @dev Get trading restrictions for a specific token
     */
    function getTradingRestriction(uint256 tokenId)
        external
        view
        returns (
            uint256,
            uint256,
            bool
        )
    {
        require(_exists(tokenId), "Nonexistent token");
        TradingRestriction memory restriction = _tradingRestrictions[tokenId];
        return (restriction.startTime, restriction.endTime, restriction.isActive);
    }

    /**
     * @dev Check if trading is restricted for a token
     */
    function isTradingRestricted(uint256 tokenId) public view returns (bool) {
        if (!_exists(tokenId)) return false;
        
        TradingRestriction memory restriction = _tradingRestrictions[tokenId];
        if (!restriction.isActive) return false;

        uint256 currentTime = block.timestamp;
        return (currentTime >= restriction.startTime &&
            currentTime <= restriction.endTime);
    }

    /**
     * @dev Override transfer functions to enforce trading restrictions
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0) && to != address(0)) { // Skip minting and burning
            require(!isTradingRestricted(tokenId), "Token trading is restricted");
        }
    }

    /**
     * @dev Add an operator address
     */
    function addOperator(address operator) external onlyOwner {
        require(operator != address(0), "Invalid operator address");
        require(_operators.add(operator), "Operator already exists");
        emit OperatorAdded(operator);
    }

    /**
     * @dev Remove an operator address
     */
    function removeOperator(address operator) external onlyOwner {
        require(_operators.remove(operator), "Operator not found");
        emit OperatorRemoved(operator);
    }

    /**
     * @dev Check if an address is an operator
     */
    function isOperator(address operator) external view returns (bool) {
        return _operators.contains(operator);
    }

    /**
     * @dev EIP-2981 royalty standard implementation
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address receiver, uint256 royaltyAmount)
    {
        require(_exists(tokenId), "Nonexistent token");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        if (royalty.recipient == address(0) || royalty.basisPoints == 0) {
            return (address(0), 0);
        }
        royaltyAmount = (salePrice * royalty.basisPoints) / 10000;
        return (royalty.recipient, royaltyAmount);
    }
}
```
