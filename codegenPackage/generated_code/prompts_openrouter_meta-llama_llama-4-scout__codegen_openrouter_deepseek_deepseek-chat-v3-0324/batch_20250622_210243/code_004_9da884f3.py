"""
Generated Code Metadata:
========================
Original URL: https://neotokyo-85y.pages.dev
Prompt: Design a smart contract to manage the minting and uploading of digital assets in the Neo Tokyo ecosystem.
Generated: DETERMINISTIC_9da884f3f7219178
Batch ID: 20250622_210243
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
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract NeoTokyoDigitalAsset is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    struct DigitalAsset {
        string metadataURI;
        address creator;
        uint256 creationTimestamp;
    }

    mapping(uint256 => DigitalAsset) private _digitalAssets;
    mapping(address => bool) private _approvedMinters;

    event AssetMinted(
        uint256 indexed tokenId,
        address indexed creator,
        string metadataURI,
        uint256 timestamp
    );

    event MinterApprovalChanged(
        address indexed minter,
        bool approved
    );

    constructor() ERC721("Neo Tokyo Digital Asset", "NTDA") {}

    modifier onlyApprovedMinter() {
        require(
            _approvedMinters[msg.sender] || msg.sender == owner(),
            "Not approved minter"
        );
        _;
    }

    function approveMinter(address minter, bool approved) external onlyOwner {
        _approvedMinters[minter] = approved;
        emit MinterApprovalChanged(minter, approved);
    }

    function isApprovedMinter(address minter) external view returns (bool) {
        return _approvedMinters[minter];
    }

    function mintDigitalAsset(
        address recipient,
        string memory metadataURI
    ) external onlyApprovedMinter nonReentrant returns (uint256) {
        require(bytes(metadataURI).length > 0, "Empty metadata URI");

        _tokenIdCounter.increment();
        uint256 newTokenId = _tokenIdCounter.current();

        _safeMint(recipient, newTokenId);
        
        _digitalAssets[newTokenId] = DigitalAsset({
            metadataURI: metadataURI,
            creator: msg.sender,
            creationTimestamp: block.timestamp
        });

        emit AssetMinted(
            newTokenId,
            msg.sender,
            metadataURI,
            block.timestamp
        );

        return newTokenId;
    }

    function getDigitalAsset(uint256 tokenId) external view returns (
        string memory metadataURI,
        address creator,
        uint256 creationTimestamp
    ) {
        require(_exists(tokenId), "Token does not exist");
        DigitalAsset memory asset = _digitalAssets[tokenId];
        return (asset.metadataURI, asset.creator, asset.creationTimestamp);
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _digitalAssets[tokenId].metadataURI;
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function supportsInterface(bytes4 interfaceId) public view override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
