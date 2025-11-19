"""
Generated Code Metadata:
========================
Original URL: https://rexas-ae.web.app
Prompt: Write a smart contract in Solidity that enables tokenization of real-world assets like real estate or art, similar to the functionality described in the Rexas Finance ecosystem.
Generated: DETERMINISTIC_72d4a609ec3b533d
Batch ID: 20250612_145242
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AssetTokenization is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    struct Asset {
        uint256 tokenId;
        address owner;
        string assetType;
        uint256 valuation;
        string valuationReportHash;
        bool isFractionalized;
        uint256 totalFractions;
        uint256 fractionPrice;
        bool isActive;
    }

    mapping(uint256 => Asset) private _assets;
    mapping(uint256 => mapping(address => uint256)) private _fractionBalances;
    mapping(uint256 => address[]) private _fractionHolders;

    event AssetRegistered(
        uint256 indexed tokenId,
        address indexed owner,
        string assetType,
        uint256 valuation
    );
    event AssetFractionalized(
        uint256 indexed tokenId,
        uint256 totalFractions,
        uint256 fractionPrice
    );
    event FractionPurchased(
        uint256 indexed tokenId,
        address indexed buyer,
        uint256 fractionAmount
    );
    event AssetRedeemed(
        uint256 indexed tokenId,
        address indexed redeemer
    );

    constructor() ERC721("AssetTokenization", "AST") {}

    function registerAsset(
        string memory assetType,
        uint256 valuation,
        string memory valuationReportHash,
        string memory tokenURI
    ) external returns (uint256) {
        require(bytes(assetType).length > 0, "Asset type cannot be empty");
        require(valuation > 0, "Valuation must be greater than zero");
        require(bytes(valuationReportHash).length > 0, "Valuation report hash cannot be empty");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        _assets[tokenId] = Asset({
            tokenId: tokenId,
            owner: msg.sender,
            assetType: assetType,
            valuation: valuation,
            valuationReportHash: valuationReportHash,
            isFractionalized: false,
            totalFractions: 0,
            fractionPrice: 0,
            isActive: true
        });

        emit AssetRegistered(tokenId, msg.sender, assetType, valuation);
        return tokenId;
    }

    function fractionalizeAsset(
        uint256 tokenId,
        uint256 totalFractions,
        uint256 fractionPrice
    ) external {
        require(_exists(tokenId), "Asset does not exist");
        require(ownerOf(tokenId) == msg.sender, "Only asset owner can fractionalize");
        require(!_assets[tokenId].isFractionalized, "Asset already fractionalized");
        require(totalFractions > 0, "Total fractions must be greater than zero");
        require(fractionPrice > 0, "Fraction price must be greater than zero");

        _assets[tokenId].isFractionalized = true;
        _assets[tokenId].totalFractions = totalFractions;
        _assets[tokenId].fractionPrice = fractionPrice;

        // Reserve all fractions for the owner initially
        _fractionBalances[tokenId][msg.sender] = totalFractions;
        _fractionHolders[tokenId].push(msg.sender);

        emit AssetFractionalized(tokenId, totalFractions, fractionPrice);
    }

    function purchaseFraction(
        uint256 tokenId,
        uint256 fractionAmount
    ) external payable nonReentrant {
        require(_exists(tokenId), "Asset does not exist");
        require(_assets[tokenId].isFractionalized, "Asset not fractionalized");
        require(_assets[tokenId].isActive, "Asset not active");
        require(fractionAmount > 0, "Fraction amount must be greater than zero");
        require(
            _fractionBalances[tokenId][_assets[tokenId].owner] >= fractionAmount,
            "Not enough fractions available"
        );
        require(
            msg.value >= fractionAmount.mul(_assets[tokenId].fractionPrice),
            "Insufficient payment"
        );

        // Transfer fractions from owner to buyer
        _fractionBalances[tokenId][_assets[tokenId].owner] = _fractionBalances[tokenId][_assets[tokenId].owner].sub(fractionAmount);
        _fractionBalances[tokenId][msg.sender] = _fractionBalances[tokenId][msg.sender].add(fractionAmount);

        // Add buyer to fraction holders if not already present
        bool isHolder = false;
        for (uint i = 0; i < _fractionHolders[tokenId].length; i++) {
            if (_fractionHolders[tokenId][i] == msg.sender) {
                isHolder = true;
                break;
            }
        }
        if (!isHolder) {
            _fractionHolders[tokenId].push(msg.sender);
        }

        // Transfer payment to asset owner
        payable(_assets[tokenId].owner).transfer(msg.value);

        emit FractionPurchased(tokenId, msg.sender, fractionAmount);
    }

    function redeemAsset(uint256 tokenId) external nonReentrant {
        require(_exists(tokenId), "Asset does not exist");
        require(_assets[tokenId].isFractionalized, "Asset not fractionalized");
        require(_assets[tokenId].isActive, "Asset not active");

        // Check if redeemer owns all fractions
        require(
            _fractionBalances[tokenId][msg.sender] == _assets[tokenId].totalFractions,
            "Must own all fractions to redeem"
        );

        // Transfer ownership of the NFT
        _transfer(_assets[tokenId].owner, msg.sender, tokenId);

        // Update asset ownership
        _assets[tokenId].owner = msg.sender;
        _assets[tokenId].isFractionalized = false;
        _assets[tokenId].isActive = false;

        emit AssetRedeemed(tokenId, msg.sender);
    }

    function getAssetDetails(uint256 tokenId) external view returns (
        address owner,
        string memory assetType,
        uint256 valuation,
        string memory valuationReportHash,
        bool isFractionalized,
        uint256 totalFractions,
        uint256 fractionPrice,
        bool isActive
    ) {
        require(_exists(tokenId), "Asset does not exist");
        Asset memory asset = _assets[tokenId];
        return (
            asset.owner,
            asset.assetType,
            asset.valuation,
            asset.valuationReportHash,
            asset.isFractionalized,
            asset.totalFractions,
            asset.fractionPrice,
            asset.isActive
        );
    }

    function getFractionBalance(uint256 tokenId, address holder) external view returns (uint256) {
        require(_exists(tokenId), "Asset does not exist");
        return _fractionBalances[tokenId][holder];
    }

    function getFractionHolders(uint256 tokenId) external view returns (address[] memory) {
        require(_exists(tokenId), "Asset does not exist");
        return _fractionHolders[tokenId];
    }

    // The following functions are overrides required by Solidity.
    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
